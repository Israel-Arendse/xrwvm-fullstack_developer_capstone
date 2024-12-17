"""
This module registers the CarMake and CarModel models with the Django admin interface.
It includes custom admin classes to display and manage car makes and models.
"""

from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
# pylint: disable=too-few-public-methods
class CarModelInline(admin.TabularInline):
    """
    Inline admin descriptor for CarModel objects, to be used in the CarMakeAdmin.
    This allows CarModel objects to be edited inline within the CarMake admin page.
    """
    model = CarModel
    extra = 1  # Number of extra forms to display in the admin interface


# CarModelAdmin class
# pylint: disable=too-few-public-methods
class CarModelAdmin(admin.ModelAdmin):
    """
    Admin descriptor for CarModel objects, defining the fields to display in the list view,
    filters for easy data sorting, and search fields within the Django admin interface.
    """
    list_display = (
        'name', 'car_make', 'type', 'year', 'dealer_id', 'seating_capacity',
        'number_of_doors', 'transmission', 'fuel', 'mileage', 'engine_size'
    )
    list_filter = ('car_make', 'type', 'year', 'fuel')  # Filters for easy data sorting
    search_fields = (
        'name', 'car_make__name', 'type',
        'transmission', 'fuel'
    )  # Fields to search through in the admin interface


# CarMakeAdmin class with CarModelInline
# pylint: disable=too-few-public-methods
class CarMakeAdmin(admin.ModelAdmin):
    """
    Admin descriptors for CarMake objects, defining the fields to display in the list view,
    search fields, and inline editing of related CarModel objects within the Django admin interface.
    """
    list_display = ('name', 'description', 'website')
    search_fields = ('name', 'description')  # Fields to search through in the admin interface
    inlines = [CarModelInline]  # Allows CarModel objects to be edited inline within CarMake


# Register models here

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
