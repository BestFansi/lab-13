def task1():
    numbers = [12, 24, 36, 48, 109, 187]

    '''задача A'''
    def multiply1(x):
       return x * 27
    result1 = list(map(multiply1, numbers))
    print(result1)

    '''задача B'''
    multiply2 = lambda x: x * 27
    result2 = list(map(multiply2, numbers))
    print(result2)

def task2():
    tele1 = '89147165538'
    tele2 = '89695231074'
    my_number = list(map(int, tele1))
    tele_number = list(map(int, tele2))

    new_list = list(map(lambda x, y: x * y, my_number, tele_number))
    print(new_list)

def task3():
    telenum = '89147165538'
    numlist = list(map(int, telenum))
    mult_list = list(map(lambda x: x * 20, numlist))
    even_num = list(filter(lambda x: x % 2 == 0, mult_list))
    odd_num = list(filter(lambda x: x % 2 == 1, mult_list))
    print(f"even numbers: {even_num}")
    print(f"odd numbers: {odd_num}")

def task4():
    telenum = '89147165538'
    numlist = list(map(int, telenum))
    div_1 = list(map(lambda x: int(x) // 20, numlist))
    div_2 = list(map(lambda x: int(x) / 20, numlist))
    print(f"целочисленное деление: {div_1}")
    print(f"дробное деление: {div_2}")


task = int(input("Задание "))
if task == 1:
    task1()
elif task == 2:
    task2()
elif task == 3:
    task3()
elif task == 4:
    task4()
elif task == 5:
    task5()
elif task == 6:
    task6()