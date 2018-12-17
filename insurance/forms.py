from django import forms

from insurance.models import Employee, Family, Relation, FileInsurance


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


class FileInsuranceForm(forms.ModelForm):

    class Meta:
        model = FileInsurance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FileInsuranceForm, self).__init__(*args, **kwargs)

        self.fields['delivery_date'].widget.attrs.update({'class': 'datepicker', 'onkeydown': 'return false'})
        self.fields['filing_date'].widget.attrs.update({'class': 'datepicker', 'onkeydown': 'return false'})
        self.fields['Repayment_date'].widget.attrs.update({'class': 'datepicker', 'onkeydown': 'return false'})

        self.fields['stat'].widget.attrs.update({'class': 'form-control'})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'datepicker form-control', 'onkeydown': 'return false'})

