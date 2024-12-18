from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# CarModel model
class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE
    )  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('HYBRID', 'Hybrid'),
    ]
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SUV'
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )
    dealer_id = models.IntegerField(default=1)
    seating_capacity = models.IntegerField(default=4)
    number_of_doors = models.IntegerField(default=4)
    transmission = models.CharField(max_length=9, default='manual')

    FUEL_TYPES = [
        ('PETROL', 'Petrol'),
        ('DIESEL', 'Diesel'),
        ('HYBRID/PETROL', 'Hybrid/Petrol'),
        ('HYBRID/DIESEL', 'Hybrid/Diesel'),
        ('GAS', 'Gas'),
        ('ELECTRIC', 'Electric'),
    ]
    fuel = models.CharField(
        max_length=13,
        choices=FUEL_TYPES,
        default='Petrol'
    )
    mileage = models.IntegerField(
        default=60000,
        validators=[
            MaxValueValidator(3999999),
            MinValueValidator(0)
        ]
    )
    engine_size = models.IntegerField(
        default=2000,
        validators=[
            MaxValueValidator(8000),
            MinValueValidator(500)
        ]
    )
    # Use 'now' for default value
    created_at = models.DateTimeField(default=now)
    # Automatically update timestamp
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
