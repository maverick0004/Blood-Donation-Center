from django.contrib import admin
from .models import Patient,Donor,BloodBank

admin.site.site_header = 'Blood Donation Admin'
admin.site.site_title = 'Blood Donation Admin'
admin.site.index_title = 'Blood Donation Admin'

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'dob','blood_group',
        'disease','contact_no',
        'address'
    ]

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'dob','blood_group',
        'blood_bank',
        'contact_no',
        'address'
    ]

@admin.register(BloodBank)
class BloodBankAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'contact_no',
        'address'
    ]

# @admin.register(BloodBank)
# class BloodBankAdmin(admin.ModelAdmin):
#     list_display = [
#         'name',
#         'contact_no',
#         'address',
#         'get_donor'
#     ]