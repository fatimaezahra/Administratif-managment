from django import forms

from insurance.models import Employee, Family, Relation


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'


class FamilyForm(forms.ModelForm):

    class Meta:
        model = Family
        fields = ['name', 'first_name', 'birth_date', 'sex', 'relation']


class RelationForm(forms.ModelForm):

    class Meta:
        model = Relation
        fields = '__all__'
