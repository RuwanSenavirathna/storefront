from django.contrib import admin
from django.contrib.admin.decorators import register
from . models import Customer, Register

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'tp_number', 'profile_pic')

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'date')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Register, RegisterAdmin)