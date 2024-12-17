
from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology",
            "website": "https://www.nissan-global.com/"
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology",
            "website": "https://www.mercedes-benz.com/"
        },
        {    "name": "Audi",
             "description": "Great cars. German technology",
             "website": "https://www.audi.com/"
        },
        {    "name": "Kia",
             "description": "Great cars. Korean technology",
             "website": "https://www.kia.com/"
        },
        {    "name": "Toyota",
             "description": "Great cars. Japanese technology",
             "website": "https://www.toyota-global.com/"
        },
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'],
            description=data['description'],
            website=data['website']
        ))

    car_model_data = [
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "dealer_id": 1,
            "seating_capacity": 7,
            "number_of_doors": 5,
            "transmission": "automatic",
            "fuel": "Petrol",
            "mileage": 10000, 
            "engine_size": 3000
        },
        {
            "name": "Qashqai",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "dealer_id": 1,
            "seating_capacity": 5,
            "number_of_doors": 5,
            "transmission": "manual",
            "fuel": "Diesel", 
            "mileage": 20000,
            "engine_size": 2000
        },
        {
            "name": "XTRAIL",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "dealer_id": 1,
            "seating_capacity": 7,
            "number_of_doors": 5,
            "transmission": "automatic",
            "fuel": "Hybrid/Petrol",
            "mileage": 15000, 
            "engine_size": 2500
        },
        {
            "name": "A-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
            "dealer_id": 2,
            "seating_capacity": 5,
            "number_of_doors": 5,
            "transmission": "automatic",
            "fuel": "Petrol", 
            "mileage": 12000, 
            "engine_size": 2000
        },
        {
            "name": "C-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
            "dealer_id": 2,
            "seating_capacity": 5,
            "number_of_doors": 5,
            "transmission": "manual",
            "fuel": "Diesel",
            "mileage": 25000,
            "engine_size": 2200
        },
        {
            "name": "E-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
            "dealer_id": 2,
            "seating_capacity": 5,
            "number_of_doors": 5,
            "transmission": "automatic",
            "fuel": "Hybrid/Diesel",
            "mileage": 18000,
            "engine_size": 3000
        },
        {
            "name": "C-300",
            "type": "Coupe", 
            "year": 2023,
            "car_make": car_make_instances[1],
            "dealer_id": 2,
            "seating_capacity": 4,
            "number_of_doors": 2,
            "transmission": "manual",
            "fuel": "Petrol",
            "mileage": 35000,
            "engine_size": 1991
        },
        {
            "name": "A4",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
            "dealer_id": 3,
            "seating_capacity": 5,
            "number_of_doors": 5,
            "transmission": "automatic",
            "fuel": "Petrol",
            "mileage": 13000,
            "engine_size": 1800
        },
        {
            "name": "A5",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
            "dealer_id": 3,
            "seating_capacity": 5,
            "number_of_doors": 5,
            "transmission": "manual",
            "fuel": "Diesel",
            "mileage": 22000,
            "engine_size": 2000
        },
        {
            "name": "A6",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
            "dealer_id": 3,
            "seating_capacity": 5,
            "number_of_doors": 5,
            "transmission": "automatic",
            "fuel": "Hybrid/Petrol",
            "mileage": 16000,
            "engine_size": 2400
        },
        {
            "name": "A7",
            "type": "Hybrid",
            "year": 2023,
            "car_make": car_make_instances[2],
            "dealer_id": 3,
            "seating_capacity": 5,
            "number_of_doors": 5,
            "transmission": "automatic",
            "fuel": "Hybrid/Diesel", 
            "mileage": 35000, 
            "engine_size": 1984
        },
        {
            "name": "Sorrento", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": car_make_instances[3], 
            "dealer_id": 4, 
            "seating_capacity": 7, 
            "number_of_doors": 5, 
            "transmission": "automatic", 
            "fuel": "Petrol", 
            "mileage": 14000, 
            "engine_size": 3300
        },
        {
            "name": "Picanto", 
            "type": "Hatchback", 
            "year": 2022, 
            "car_make": car_make_instances[3], 
            "dealer_id": 4, 
            "seating_capacity": 5, 
            "number_of_doors": 5, 
            "transmission": "automatic", 
            "fuel": "Petrol", 
            "mileage": 12000, 
            "engine_size": 1000
        },
        {
            "name": "Carnival", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": car_make_instances[3], 
            "dealer_id": 4, 
            "seating_capacity": 7, 
            "number_of_doors": 5, 
            "transmission": "manual", 
            "fuel": "Diesel", 
            "mileage": 16000, 
            "engine_size": 2200
        },
        {
            "name": "Cerato", 
            "type": "Sedan", 
            "year": 2023, 
            "car_make": car_make_instances[3], 
            "dealer_id": 4, 
            "seating_capacity": 5, 
            "number_of_doors": 4, 
            "transmission": "automatic", 
            "fuel": "Hybrid/Petrol", 
            "mileage": 10000, 
            "engine_size": 1800
        },
        {
            "name": "Corolla", 
            "type": "Sedan", 
            "year": 2023, 
            "car_make": car_make_instances[4], 
            "dealer_id": 5, 
            "seating_capacity": 5, 
            "number_of_doors": 4, 
            "transmission": "manual", 
            "fuel": "Petrol", 
            "mileage": 15000, 
            "engine_size": 1800
        },
        {
            "name": "Camry", 
            "type": "Sedan", 
            "year": 2023, 
            "car_make": car_make_instances[4], 
            "dealer_id": 5, 
            "seating_capacity": 5, 
            "number_of_doors": 4, 
            "transmission": "automatic", 
            "fuel": "Diesel", 
            "mileage": 20000, 
            "engine_size": 2200
        },
        {
            "name": "Kluger", 
            "type": "SUV", 
            "year": 2023, 
            "car_make": car_make_instances[4], 
            "dealer_id": 5, 
            "seating_capacity": 7, 
            "number_of_doors": 5, 
            "transmission": "automatic", 
            "fuel": "Hybrid/Diesel", 
            "mileage": 18000, 
            "engine_size": 2500
        },
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            dealer_id=data['dealer_id'],
            seating_capacity=data['seating_capacity'],
            number_of_doors=data['number_of_doors'],
            transmission=data['transmission'],
            fuel=data['fuel'],
            mileage=data['mileage'],
            engine_size=data['engine_size']
        )
        # Print statement
        print(f"Created CarModel: {data['name']} of type {data['type']}")
