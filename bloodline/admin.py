from django.contrib import admin
from .models import BloodlineUser, BloodlineBank, BloodlineBlood

class BloodlineUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile', 'blood_type', 'verified')
    list_filter = ['blood_type']
    search_fields = ['username']

class BloodlineBankAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ['name']

class BloodlineBloodAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank', 'blood_status')
    list_filter = ['blood_status']
    search_fields = ['user']

admin.site.register(BloodlineUser, BloodlineUserAdmin)
admin.site.register(BloodlineBank, BloodlineBankAdmin)
admin.site.register(BloodlineBlood, BloodlineBloodAdmin)