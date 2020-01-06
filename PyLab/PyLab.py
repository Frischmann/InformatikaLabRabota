import random
import string
import re

def naborsup(i):
    try:
        sstr = input("Введите " + (str(i + 1)) + "ю пятибуквенную строку (строчными буквами): \n")
        if (sstr.isalpha() == False):
            print("\nСтрока должна содержать только буквы! Повторите ввод")
            return None
        elif (sstr.islower() == False):
            print("\nСтрока должна содержать только строчные буквы! Повторите ввод")
            return None
        elif (len(sstr) != 5):
            print("\nСтрока должна содержать только пять букв! Повторите ввод")
            return None
        elif re.search(r'[^a-zA-Z]', sstr):
            print("\nСтрока должна содержать только буквы латинского алфавита! Повторите ввод")
            return None
        else:
            return sstr
    except KeyboardInterrupt:
        print("\nВы нажали на Ctrl-C\n")
        return None
    except EOFError:
        print("\nВы пытались ввести Ctrl+любая буква\n")
        return None
    except:
       return None

def randstr(length):
    letters = string.ascii_lowercase 
    return ''.join(random.choice(letters) for i in range(length))

def inarr(a):
    k = 0
    arr = [ [0]*5 for i in range(5) ]

    tstr = ''.join(sorted(''.join(a)))  

    while k < len(tstr):
        for i in range(5):
            for j in range(5):
                arr[i][j] = tstr[k]
                k += 1

    print("\nРезультат сортировки: ")

    for i in range(5):
        for j in range(5):
            print("Элемент " + str((i+1)) + "x" + str((j+1)) + " = " + str(ord(arr[i][j])))
    input()

def nabor():
    a = [None, None, None, None, None]
    for i in range(5):
        while a[i] == None:
            a[i] = naborsup(i)
    inarr(a)
        
def rand():
    a = [0]*5
    for i in range(5):
        a[i] = randstr(5)
    inarr(a)

def choice():
    try:
        a = input("Введите способ ввода строк: \n1. Ввести строки вручную \n2. Сгенерировать случайные строки\n")

        if (a.isdigit() == False):
            print ("\nВы ввели не цифры! Введите номер способа заново!")
            choice()
        elif (int(a) == 1):
            nabor()
        elif (int(a) == 2):
            rand()
        else:
            print ("\nСпособ не найден! Введите номер способа заново!")
            choice()
    except KeyboardInterrupt:
        print("\nВы нажали на Ctrl-C\n")
        choice()
    except EOFError:
        print("\nВы пытались ввести Ctrl+любая буква\n")
        choice()
    except:
        choice()

print("Задание варианта: имеется массив из пяти пятибуквенных строк, составленных из букв английского алфавита.\nСтроки могут как вводиться пользователем, так и генерироваться случайным образом.\nНеобходимо из исходного массива сформировать матрицу размера 5 на 5,\nв которой каждый элемент - это код соответствующей буквы соответствующего слова.\nНапример, по индексам[1, 1] в требуемой матрице должен лежать код первой буквы первого слова.\nДалее требуется упорядочить строки полученной матрицы по убыванию.\nРезультаты работы вывести на экран.\n")
choice()