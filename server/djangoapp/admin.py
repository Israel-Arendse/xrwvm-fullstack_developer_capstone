from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)

# CarModelInline class

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id', 'seating_capacity', 'number_of_doors', 'transmission', 'fuel', 'mileage', 'engine_size')
    list_filter = ('car_make', 'type', 'year', 'fuel')
    search_fields = ('name', 'car_make_name', 'type', 'transmission', 'fuel')

# CarMakeAdmin class with CarModelInline

# Register models here
