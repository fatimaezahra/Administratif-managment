from django import forms

from insurance.models import Employee, Family, Relation, FileInsurance


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        self.fields['service_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['employee_image'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['function'].widget.attrs.update({'class': 'form-control'})
        self.fields['hiring_date'].widget.attrs.update({'class': 'datepicker form-control', 'onkeydown': 'return false'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['birth_date'].widget.attrs.update({'class': 'datepicker form-control', 'onkeydown': 'return false'})
        self.fields['sex'].widget.attrs.update({'class': 'form-control'})



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

        self.fields['delivery_date'].widget.attrs.update({'class': 'datepicker form-control', 'onkeydown': 'return false'})
        self.fields['filing_date'].widget.attrs.update({'class': 'datepicker form-control', 'onkeydown': 'return false'})
        self.fields['Repayment_date'].widget.attrs.update({'class': 'datepicker form-control', 'onkeydown': 'return false'})
        self.fields['Patient'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['stat'].widget.attrs.update({'class': 'form-control'})
        self.fields['file_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount_reimbursed'].widget.attrs.update({'class': 'form-control'})
        self.fields['collaborator'].widget.attrs.update({'class': 'form-control'})
        self.fields['regulation_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['method_settlement'].widget.attrs.update({'class': 'form-control'})





