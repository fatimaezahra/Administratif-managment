from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50,blank=True)
    first_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    sex = models.CharField(choices=(('Female','female'),('Male','male')),max_length=10)

    def __str__(self):
        return self.name + ' ' + self.first_name


class Employee(Person):
    service_number = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    employee_image = models.ImageField(upload_to='employee_image',default='employee_image/none/default.png',blank=True)
    function = models.CharField(max_length=100)
    fattening_date = models.DateField()


class Family(Person):
    PARENTAL_RELATION = (('Daughter', 'daughter'), ('Son', 'son'))
    relation = models.CharField(choices=PARENTAL_RELATION, max_length=25)
    employee_relation = models.ForeignKey('Employee',on_delete=models.CASCADE)


class FileInsurance(models.Model):
    filing_date = models.DateField(blank=True)
    amount = models.FloatField(blank=True)
    delivery_date= models.DateField(blank=True)
    stat = models.CharField(choices=(('e','encoure'),('t','terminer')),max_length=20,blank=True)
    collaborator = models.ForeignKey('Employee',on_delete=models.CASCADE,related_name='collaborator',blank=True,null=True)
    Patient = models.ForeignKey('Family',on_delete=models.CASCADE,related_name='patient',blank=True,null=True)
    file_number = models.IntegerField(default=1)
    reimbursement_date = models.DateField(null=True)
    amount = models.BooleanField()
    regulation_number = models.IntegerField(null=True)
    method_settlement = models.CharField(max_length=60, null=True)

    def __str__(self):
        return str(self.pk)

