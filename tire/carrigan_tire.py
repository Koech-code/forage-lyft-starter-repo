from abc import ABC

from car import Car


class carriganTire(Car, ABC):
    tireWearArray=[0,1,2,3]

    for i in tireWearArray:
        if i>=0.9:
            print('service carrigan tire')
        elif i<0.9:
            print('don\'t  service carrigan tire')