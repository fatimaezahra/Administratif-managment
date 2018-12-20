from django.db import models

STATUS_CHOICES = (
    ('in_progres','In progress'),
    ('finished','Finished'),
    ('refused', 'Refused'),
)
PAIEMENT_CHOICES = (
    ('check','Check'),
    ('devise','Devise'),

)
class Person(models.Model):
    name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    sex = models.CharField(choices=(('Female', 'female'),
                                    ('Male', 'male')), max_length=10)

    def __str__(self):
        return self.name + ' ' + self.first_name


class Employee(Person):
    service_number = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    employee_image = models.ImageField(upload_to='employee_image',
                                       null=True,
                                       blank=True)
    function = models.CharField(max_length=100)
    hiring_date = models.DateField()


class Relation(models.Model):
    parental_relation = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.parental_relation


class Family(Person):
    relation = models.ForeignKey('Relation', on_delete=models.SET_NULL, blank=True, null=True)
    employee_relation = models.ForeignKey('Employee', on_delete=models.CASCADE)

class Status(models.Model):
    status = models.CharField(max_length=220, unique=True)

class FileInsurance(models.Model):
    collaborator = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='collaborator', blank=True, null=True)
    filing_date = models.DateField(blank=True)
    amount = models.FloatField(blank=True)
    delivery_date = models.DateField(blank=True)
    status = models.ForeignKey('Status', on_delete=models.DO_NOTHING, blank=True, null=True)
    Patient = models.ForeignKey('Family', on_delete=models.CASCADE, related_name='patient', blank=True, null=True)
    file_number = models.IntegerField(default=1)
    Repayment_date = models.DateField(null=True)
    amount_reimbursed = models.IntegerField(null=True)
    regulation_number = models.IntegerField(null=True)
    method_settlement = models.CharField(choices=PAIEMENT_CHOICES, max_length=60, null=True)
    method_settlement_check = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.pk)

