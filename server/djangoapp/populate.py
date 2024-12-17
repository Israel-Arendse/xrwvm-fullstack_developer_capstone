from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology", "website":"https://www.nissan-global.com/"},
        {"name":"Mercedes", "description":"Great cars. German technology", "website":"https://www.mercedes-benz.com/"},
        {"name":"Audi", "description":"Great cars. German technology", "website":"https://www.audi.com/"},
        {"name":"Kia", "description":"Great cars. Korean technology", "website":"https://www.kia.com/"},
        {"name":"Toyota", "description":"Great cars. Japanese technology", "website":"https://www.toyota-global.com/"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description'], website=data['website']))

    car_model_data = [
        {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id":1, "seating_capacity":7, "number_of_doors":5, "transmission":"automatic", "fuel":"Petrol", "mileage":12000, "engine_size":3.5},
        {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id":1, "seating_capacity":5, "number_of_doors":5, "transmission":"manual", "fuel":"Diesel", "mileage":20000, "engine_size":2.0},
        {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id":1, "seating_capacity":7, "number_of_doors":5, "transmission":"automatic", "fuel":"Hybrid/Petrol", "mileage":15000, "engine_size":2.5},
        {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id":2, "seating_capacity":5, "number_of_doors":5, "transmission":"automatic", "fuel":"Petrol", "mileage":13000, "engine_size":2.0},
        {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id":2, "seating_capacity":5, "number_of_doors":5, "transmission":"manual", "fuel":"Diesel", "mileage":22000, "engine_size":2.2},
        {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id":2, "seating_capacity":5, "number_of_doors":5, "transmission":"automatic", "fuel":"Hybrid/Diesel", "mileage":14000, "engine_size":3.0},
        {"name":"C-300", "type":"Coupe", "year": 2023, "car_make":car_make_instances[1], "dealer_id":2, "seating_capacity":4, "number_of_doors":2, "transmission":"manual", "fuel":"Petrol", "mileage":30000, "engine_size":3.0},
        {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id":3, "seating_capacity":5, "number_of_doors":5, "transmission":"automatic", "fuel":"Petrol", "mileage":13000, "engine_size":2.0},
        {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id":3, "seating_capacity":5, "number_of_doors":5, "transmission":"manual", "fuel":"Diesel", "mileage":22000, "engine_size":2.2},
        {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id":3, "seating_capacity":5, "number_of_doors":5, "transmission":"automatic", "fuel":"Hybrid/Petrol", "mileage":15000, "engine_size":2.5},
        {"name":"A7", "type":"Hybrid", "year": 2023, "car_make":car_make_instances[2], "dealer_id":3, "seating_capacity":5, "number_of_doors":5, "transmission":"automatic", "fuel":"Hybrid/Diesel", "mileage":17000, "engine_size":3.0},
        {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id":4, "seating_capacity":7, "number_of_doors":5, "transmission":"automatic", "fuel":"Petrol", "mileage":12000, "engine_size":3.5},
        {"name":"Picanto", "type":"Hatchback", "year": 2022, "car_make":car_make_instances[3], "dealer_id":4, "seating_capacity":5, "number_of_doors":5, "transmission":"automatic", "fuel":"Petrol", "mileage":8000, "engine_size":1.2},
        {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id":4, "seating_capacity":7, "number_of_doors":5, "transmission":"manual", "fuel":"Diesel", "mileage":20000, "engine_size":2.2},
        {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "dealer_id":4, "seating_capacity":5, "number_of_doors":4, "transmission":"automatic", "fuel":"Hybrid/Petrol", "mileage":14000, "engine_size":2.0},
        {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id":5, "seating_capacity":5, "number_of_doors":4, "transmission":"manual", "fuel":"Petrol", "mileage":11000, "engine_size":1.8},
        {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id":5, "seating_capacity":5, "number_of_doors":4, "transmission":"automatic", "fuel":"Diesel", "mileage":13000, "engine_size":2.5},
        {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id":5, "seating_capacity":7, "number_of_doors":5, "transmission":"automatic", "fuel":"Hybrid/Diesel", "mileage":15000, "engine_size":2.5},
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
