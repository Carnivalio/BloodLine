"""admin.py

This module modify default django administrator page into the structure that needed for a certain project
"""

from django.contrib import admin
from .models import BloodlineUser, BloodlineBank, BloodlineBlood

# Modification structure and fuction for BloodlineUser data table for administrator
class BloodlineUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile', 'blood_type', 'verified')
    list_filter = ['blood_type']
    search_fields = ['username']

# Modification structure and fuction for BloodlineBank data table for administrator
class BloodlineBankAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ['name']

# Modification structure and fuction for BloodlineBlood or blood donation data table for administrator
class BloodlineBloodAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank', 'blood_status')
    list_filter = ['blood_status']
    search_fields = ['user']

# Assign every admin model that declared above with corresponding models
admin.site.register(BloodlineUser, BloodlineUserAdmin)
admin.site.register(BloodlineBank, BloodlineBankAdmin)
admin.site.register(BloodlineBlood, BloodlineBloodAdmin)