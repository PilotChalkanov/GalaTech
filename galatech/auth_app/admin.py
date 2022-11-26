from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib.auth.admin import UserAdmin

from galatech.auth_app.forms import UserRegistrationForm

UserModel = get_user_model()



# @admin.register(UserModel)
# class PetstagramUserAdmin(UserAdmin):
#     list_display = ('email', 'is_staff')
#     list_filter = ('is_staff', 'is_superuser', 'groups')
#     ordering = ('email',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {
#             'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     readonly_fields = ('date_joined',)