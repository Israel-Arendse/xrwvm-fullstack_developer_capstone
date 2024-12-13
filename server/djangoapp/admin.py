from django.contrib import admin
from .models import CarMake, CarModel


# Register your models class here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id', 'seating_capacity', 'number_of_doors', 'transmission', 'fuel', 'mileage', 'engine_size')
    list_filter = ('car_make', 'type', 'year', 'fuel')
    search_fields = ('name', 'car_make__name', 'type', 'transmission', 'fuel')

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'website')
    search_fields = ('name', 'description')

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)