from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    name = models.CharField(max_length=300,null=False)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    blood_group_choices = [('A+','A+'),('A-','A-'),('B+','B+')
        ,('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')]
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=False)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=False)
    blood_group = models.CharField(
        choices = blood_group_choices,
        max_length = 3,
        default = None,
        null = False
    )
    disease = models.CharField(
        max_length = 200,
        null = False
    )

    contact_no = models.CharField(
        max_length = 12,
        default = None
    )

    address = models.TextField(
        default = None
    )

    def __str__(self):
        return self.name

class Donor(models.Model):
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=300,null=True)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    blood_group_choices = [('A+','A+'),('A-','A-'),('B+','B+')
        ,('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')]
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    blood_group = models.CharField(
        choices = blood_group_choices,
        max_length = 3,
        default = None,
        null = True
    )

    contact_no = models.CharField(
        max_length = 12,
        default = None,
        null = True
    )

    blood_bank = models.ForeignKey('BloodBank',on_delete = models.CASCADE,null = True)

    reports = models.FileField(
        help_text = 'upload reports in PDF format',
        null = True
    )

    address = models.TextField(
        default = None,
        null = True
    )

    def __str__(self):
        return self.name

class BloodBank(models.Model):
    name = models.CharField(max_length=300,null=False)
    contact_no = models.CharField(
        max_length = 12,
        default = None
    )
    city = models.CharField(
        null =True,
        default = None,
        max_length = 200
    )
    address = models.TextField(
        default = None
    )

    def __str__(self):
        return self.name
    
    # def get_donor(self):
    #     return "\n".join([p.name for p in self.donors.all()])
