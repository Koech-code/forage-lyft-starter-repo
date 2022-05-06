from abc import ABC

from car import Car


class octoprimeTire(Car, ABC):

    def sum(tireWearArray):
        sum=0
        for i in tireWearArray:
            sum+=i;
            if sum>=3:
                print (sum, 'service the tire')
            elif sum<3:
                print (sum, 'don\'t service the tire')
        return (sum)
        
    tireWearArray=[0,1,2,3]
    n=len(tireWearArray)
    ans=sum(tireWearArray)

    print ('The sum of array is:', ans)