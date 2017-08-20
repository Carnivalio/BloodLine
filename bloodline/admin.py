from django.contrib import admin

from .models import User, Bank, Blood

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'mobile', 'blood_type', 'verified')
    list_filter = ['blood_type']
    search_fields = ['username']

class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ['name']

class BloodAdmin(admin.ModelAdmin):
    list_display = ('user', 'bank', 'blood_status')
    list_filter = ['blood_status']
    search_fields = ['user']


admin.site.register(User, UserAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Blood, BloodAdmin)