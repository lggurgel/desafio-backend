from django.contrib import admin
from users.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']

admin.site.register(CustomUser, CustomUserAdmin)