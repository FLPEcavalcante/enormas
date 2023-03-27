from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DataModel


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


class DataModelAdmin(admin.ModelAdmin):
    """A ModelAdmin class for the DataModel model.

    Args:
        admin (type): The Django Admin class.
    """
    list_display = (
        'url',
        'created_at',
    )
    
    list_filter = (
        'url',
        'created_at',
    )
    
    readonly_fields = (
        'url',
        'created_at',
    )

    search_fields = (
        'url',
    )
    
admin.site.register(DataModel, DataModelAdmin)
