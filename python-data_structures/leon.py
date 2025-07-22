# C = [39.2, 36.5, 37.3, 38, 37.8]
# F = list(map(lambda x: (float(9)/5)*x + 32, C))
# print(F)
# def fahrenheit(T):
#     return ((float(9)/5)*T + 32)
# def celsius(T):
#     return (float(5)/9)*(T-32)
# temperatures = (36.5, 37, 37.5, 38, 39)
# F = map(fahrenheit, temperatures)
# C = map(celsius, F)
# temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
# temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
# print(temperatures_in_Fahrenheit)
# print(temperatures_in_Celsius)
# from functools import reduce
# print(reduce((lambda x, y: x+y), range(1, 6)))
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()