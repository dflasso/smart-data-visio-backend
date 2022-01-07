from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from Security.models.user import User
from Security.models.profile import Profile
from Security.models.resources import Resources

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'doc_identification', 'first_name', 'last_name')
    list_filter = ("is_active", "is_superuser")


admin.site.register(Profile)
admin.site.register(Resources)
admin.site.register(User, UserAdmin)