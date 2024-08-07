##Note: the 'main' file name refers to main as inside of the caroop project, nothing outside.
from car import Car

car_1 = Car('Chevy', 'Corvette', 2021, 'blue')
car_2 = Car('Ford', 'Mustang', 2022, 'red')

car_1.wheels = 2

print(car_1.wheels)
print(Car.wheels)