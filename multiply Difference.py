import random
import time


def NormalMultiplication(number1, number2):
    number1 = str(number1)[::-1]  # reverse
    number2 = str(number2)[::-1]
    lst_result = []

    if len(number1) == 1 and len(number2) == 1:
        return int(number1) * int(number2)

    for j in range(len(number2)):
        result = 0
        plus = 0
        for i in range(len(number1) + 1):
            try:
                num = str(int(number1[i]) * int(number2[j]) + int(plus))
                plus = 0
            except:
                if int(plus) == 0:
                    break
                num = plus
                plus = 0

            if len(num) == 2:
                plus = num[0]
                num = num[1]
            pw = (10 ** i)
            result += int(num) * pw
        lst_result.append(result * (10 ** j))

    return sum(lst_result)


def KaratsubaMultiplication(x, y):
    if len(str(x)) == 1:
        return x * y
    else:
        n = int(len(str(x))) // 2
        a = x // 10 ** n
        b = x % 10 ** n
        c = y // 10 ** n
        d = y % 10 ** n

        ac = KaratsubaMultiplication(a, c)
        bd = KaratsubaMultiplication(b, d)
        z = KaratsubaMultiplication((a + b), (c + d))

        return (ac * 10 ** (2 * n)) + ((z - ac - bd) * 10 ** n) + bd


def GenerateNumber(len_of_number):
    Min = int("1" + (len_of_number - 1) * "0")

    Max = int(len_of_number * "9")
    number = random.randint(Min, Max)
    return number


def show_the_difference():
    num1 = GenerateNumber(1500)  # You can change the number in parentheses and write your desired number.
    num2 = GenerateNumber(1500)  # You can change the number in parentheses and write your desired number.
    print("number1:", num1)
    print("number2 :", num2)
    print("please wait for multiply !!!")

    t1_start = time.time()
    NormalMultiplication(num1, num2)
    t1_stop = time.time()

    t2_start = time.time()
    KaratsubaMultiplication(num1, num2)
    t2_stop = time.time()

    # print(f'CPU time took {t1_stop - t1_start} seconds with the first algorithm, but with the second algorithm the CPU time changed to {t2_stop - t2_start}!')


show_the_difference()

