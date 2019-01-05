from django.contrib import messages
from django.contrib.auth import logout, authenticate, login,\
    update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, AdminPasswordChangeForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from accounts.decorators import admin_required
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserChangeAdminForm
from accounts.models import CustomUser


def logout_user(request):
    logout(request)
    form = CustomUserCreationForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'accounts/login.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('insurance:list-employee')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('insurance:list-employee')
            else:
                return render(request, 'accounts/login.html',
                              {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/login.html',
                          {'error_message': 'Invalid login or invalid password'})
    return render(request, 'accounts/login.html')


@login_required
@admin_required
def register(request):
    print(request.POST)
    if "cancel" in request.POST:
        return redirect('accounts:list_user')
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            if user is not None:
                return redirect('accounts:list_user')

        else:
            messages.error(request, 'Please correct the error below.')
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)


@login_required
def update_my_profile(request):
    print(request.POST)
    if "cancel" in request.POST:
        return redirect('insurance:list-employee')
    user = get_object_or_404(CustomUser, pk=request.user.id)
    print(user.password)
    form = CustomUserChangeForm(request.POST or None, request.FILES or None, instance=user)
    form.fields['username'].widget.attrs['readonly'] = True
    # form.fields['is_admin'].widget.attrs['disabled'] = True
    # form.fields['is_admin'].widget.attrs['checked'] = True
    if request.method == 'POST':
        print(request.POST['username'])
        if form.is_valid():
            user.save()
            return redirect('insurance:list-employee')
        else:
            messages.error(request, 'Please correct the error below.')
    password_form = AdminPasswordChangeForm(request.user)
    return render(request, 'accounts/update_my_profile.html', {'form': form, 'password_form': password_form})


@login_required
@admin_required
def list_user(request):
    user_list = CustomUser.objects.all().exclude(id=request.user.id)
    form = AdminPasswordChangeForm(request.user)

    return render(request, 'accounts/user_list.html', {
        'users': user_list,
        'form': form
    })


@login_required
@admin_required
def update_user(request, pk):
    if "cancel" in request.POST:
        return redirect('accounts:list_user')

    user = get_object_or_404(CustomUser, pk=pk)
    form = CustomUserChangeAdminForm(request.POST or None, request.FILES or None,
                                     instance=user)
    if request.method == 'POST':
        if form.is_valid():
            user.save()
            return redirect('accounts:list_user')
        else:
            return render(request, 'accounts/register.html', {'form': form, })
    else:
        form = CustomUserChangeAdminForm(instance=user)
    return render(request, 'accounts/register.html', {'form': form, })


@login_required
@admin_required
def delete_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    data = dict()

    if request.method == 'POST':
        user.delete()
        data['form_is_valid'] = True
        users = CustomUser.objects.all().exclude(id=request.user.id)
        data['html_user_list'] = render_to_string('accounts/partial_user_list.html', {
            'users': users
        })
    else:
        context = {'user': user, }
        data['html_form'] = render_to_string('accounts/partial_user_delete.html', context, request=request, )

    return JsonResponse(data)


@login_required
def change_password(request):
    if "cancel" in request.POST:
        return redirect('accounts:update_my_profile')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:update_my_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


@login_required
@admin_required
def admin_change_password(request, pk):
    if "cancel" in request.POST:
        return redirect('accounts:list_user')
    user_change = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = AdminPasswordChangeForm(user_change, request.POST)
        if form.is_valid():
            messages.success(request, ' password was successfully updated!')
            return redirect('accounts:list_user')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('accounts:list_user')
    else:
        form = AdminPasswordChangeForm(user_change)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
