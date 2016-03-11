from app.models.car import Car

def save_car(car):
    try:
        with open('app/data/cars.data', 'a') as cars_data_file:
            text_to_save = "|".join([car.id,
                                     car.brand,
                                     car.model,
                                     car.year,
                                     car.license_plate,
                                     car.owner_id,
                                     ]) + '|\n'
            cars_data_file.write(text_to_save)
    except IOError as io_err:
        # Display error message [TODO]
        print(str(io_err))


def find_car_by_id(car_id):
    try:
        with open('app/data/cars.data') as cars_data_file:
            content = cars_data_file.readlines()[1:]
            cars_info = None
            for car_dump in content:
                car_info = car_dump.strip().split('|')
                if car_id == car_info[0]:
                    break
                else:
                    pass #continue
            else:
                # No matches
                return None
            
            return Car(car_info[1], car_info[2], car_info[3],
                       car_info[4], car_info[0])
    except IOError as io_err:
        # Display error message [TODO]
        print(str(io_err))
