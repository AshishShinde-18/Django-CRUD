from django.contrib import admin
from .models import UserModel
# Register your models here.
# admin.site.register(UserModel)


@admin.register(UserModel)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'gender', 'date_created']