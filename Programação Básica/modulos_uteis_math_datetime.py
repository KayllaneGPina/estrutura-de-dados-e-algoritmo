import math
import datetime

# Math
num = 81
num2 = 94.2
num3 = 5
math.e = 2
print(math.cos(120))
print(math.sqrt(num))
print(math.ceil(num2))
print(math.floor(num2))
print(math.pi)
print(math.factorial(num3))
print(math.degrees(360))
print(math.radians(360))
print(math.e)
print(math.log(32, 2))
print(math.log10(100))


# Datetime
print(datetime.date.today())
print(datetime.datetime.now())

data = datetime.date(2020, 7, 10)
print(data)
print(data.day)
print(data.month)
print(data.year)

horario = datetime.datetime(2020, 7, 10, 7, 30, 0)
print(horario)
print(horario.hour)
print(horario.minute)
print(horario.second)

dias = datetime.time(13)
print(dias)
print(dias.tzinfo)


