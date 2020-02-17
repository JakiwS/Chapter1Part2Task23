year = int(input('Введите год '))
if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

# 2-й вариант:

# if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
#     print("Обычный")
# else:
#     print("Високосный")