from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from accounts.decorators import admin_required
from insurance.forms import EmployeeForm, FamilyForm, RelationForm
from insurance.models import Employee, Family, Relation


@login_required
def detail_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'insurance/detail_employee.html',
                  {'employee': employee, })


@login_required
def create_employee(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)
    if "cancel" in request.POST:
        return redirect('insurance:list-employee')

    if form.is_valid():
        employee = form.save(commit=False)
        employee.save()
        return redirect('insurance:list-employee')
    return render(request, 'insurance/create_employee.html', {"form": form, })


@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, request.FILES or None,
                        instance=employee)
    if "cancel" in request.POST:
        return redirect('insurance:list-employee')

    if request.method == 'POST':
        if form.is_valid():
            employee.save()
            return redirect('insurance:list-employee')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'insurance/update_employee.html', {'form': form, })


@login_required
def delete_employee(request, pk, page):
    employee = get_object_or_404(Employee, pk=pk)
    data = dict()
    if request.method == 'POST':
        employee.delete()
        employee_list = Employee.objects.all()

        paginator = Paginator(employee_list, 4)

        if (page-1) == paginator.num_pages:
            page = paginator.num_pages
        page_current = request.GET.get('page', page)
        try:
            employees = paginator.page(page_current)
        except PageNotAnInteger:
            employees = paginator.page(page)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        employees.number = page
        data['form_is_valid'] = True  # This is just to play along with the existing code
        data['html_employee_list'] = render_to_string('insurance/partial_employee_list.html', {
            'employees': employees
        })
    else:
        context = {'employee': employee, 'page': page}
        data['html_form'] = render_to_string('insurance/partial_employee_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


@login_required
def list_employee(request):
    employee_list = Employee.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(employee_list, 4)
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    return render(request, 'insurance/employees.html', {
        'employees': employees,
    })


def save_family_form(request, form, employee, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            family = form.save(commit=False)
            family.employee_relation = employee
            family.save()
            data['form_is_valid'] = True
            data['html_family_list'] = render_to_string('insurance/partial_family_list.html', {
                'employee': employee
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'employee': employee}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def create_family(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = FamilyForm(request.POST or None, request.FILES or None)
    else:
        form = FamilyForm()
    return save_family_form(request, form, employee, 'insurance/partial_family_create.html')


@login_required
def update_family(request, pk, pk2):
    employee = get_object_or_404(Employee, pk=pk)
    family = get_object_or_404(Family, pk=pk2)
    if request.method == 'POST':
        form = FamilyForm(request.POST or None, request.FILES or None, instance=family)
    else:
        form = FamilyForm(instance=family)
    return save_family_form(request, form, employee, 'insurance/partial_family_update.html')


@login_required
def delete_family(request, pk, pk2):
    employee = get_object_or_404(Employee, pk=pk)
    family = get_object_or_404(Family, pk=pk2)
    data = dict()
    if request.method == 'POST':
        family.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        data['html_family_list'] = render_to_string('insurance/partial_family_list.html', {
            'employee': employee
        })
    else:
        context = {'family': family, 'employee': employee}
        data['html_form'] = render_to_string('insurance/partial_family_delete.html', context, request=request, )
    return JsonResponse(data)


@login_required
@admin_required
def list_relation(request):
    relations = Relation.objects.all()
    return render(request, 'insurance/list_relation.html', {
        'relations': relations,
    })


def save_relation_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            relation = form.save(commit=False)
            relation.save()
            data['form_is_valid'] = True
            relations = Relation.objects.all()
            data['html_relation_list'] = render_to_string('insurance/partial_relation_list.html',
                                                          {'relations': relations})
        else:
            data['form_is_valid'] = False
    context = {'form': form, }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
@admin_required
def create_relation(request):
    if request.method == 'POST':
        form = RelationForm(request.POST or None, request.FILES or None)
    else:
        form = RelationForm()
    return save_relation_form(request, form, 'insurance/partial_relation_create.html')


@login_required
@admin_required
def update_relation(request, pk):
    relation = get_object_or_404(Relation, pk=pk)
    if request.method == 'POST':
        form = RelationForm(request.POST or None, request.FILES or None, instance=relation)
    else:
        form = RelationForm(instance=relation)
    return save_relation_form(request, form, 'insurance/partial_relation_update.html')


@login_required
@admin_required
def delete_relation(request, pk):
    relation = get_object_or_404(Relation, pk=pk)
    data = dict()
    if request.method == 'POST':
        relation.delete()
        data['form_is_valid'] = True
        relations = Relation.objects.all()
        data['html_relation_list'] = render_to_string('insurance/partial_relation_list.html', {
            'relations': relations
        })
    else:
        context = {'relation': relation, }
        data['html_form'] = render_to_string('insurance/partial_relation_delete.html', context, request=request, )
    return JsonResponse(data)
