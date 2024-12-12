# Capstone Project For Israel Arendse - 2024


## Module-1: Static Pages

**Home Page:**
![homepage](https://github.com/user-attachments/assets/06315162-1cd5-40a4-ae09-ffc3a11cb226)

**About Us page:**
![about_us](https://github.com/user-attachments/assets/1b03d496-48b2-432a-9348-a10f6c7848b4)

**Contact Us:**
![contact_us](https://github.com/user-attachments/assets/cbbc8458-fe12-44df-b48e-64784a4a89db)


(profile images provided freepik.com)


## Module-2: User Management

**Login Page:**
![Login](https://github.com/user-attachments/assets/e7d64ced-e780-4fa7-a2ea-78249bba1047)

**Logout Page:**
![logout](https://github.com/user-attachments/assets/b0201008-55a2-423f-ab44-b0ad19065518)

**Sign-up Page:**
![sign-up](https://github.com/user-attachments/assets/00434229-e72f-4321-8c4b-02020e0d34bf)


## Module-3: Back-End Services

### Implement API endpoints using Express-Mongo

**Fetch Dealer by ID**
![dealer_details](https://github.com/user-attachments/assets/1028bf70-80a5-42ae-910e-877c7ea2f947)

**Fetch Reviews by dealer ID**
![dealer_review](https://github.com/user-attachments/assets/741e7626-8499-4ff2-8e89-9be20f6b5745)

** Fetch all Dealers **
![dealerships](https://github.com/user-attachments/assets/5838e850-9a10-479d-b086-4adaaacc0a65)

** Fetch Dealers by location **
![kansasDealers](https://github.com/user-attachments/assets/efda8b58-b4bc-4040-9cca-ba5631778af9)

### Django Models and Proxy Services

** CarMake and CarModel **

As the project allowed me to add additional fields to the Django models 'CarMake' and 'CarModel', here is what I created.

In the 'CarMake' model, the new field created is 

```
website = models.URLFiedl(blank=True, null=True)
```

For the 'CarModel' model, the CAR_TYPES field has been updated with the following choices:

```
        # Add more choices, as required
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('HYBRID', 'Hybrid'),
```

There are other fields created in the 'CarModel' including:

```
       # Other fields as needed
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
        fuel = models.CharField(max_length=13, choices=FUEL_TYPES, default='Petrol')
        mileage = models.IntegerField(default=60000,
            validators=[
                MaxValueValidator(3999999),
                MinValueValidator(0)
            ])
        engine_size = models.IntegerField(default=2000,
            validators=[
                MaxValueValidator(8000),
                MinValueValidator(500)
            ])
```
