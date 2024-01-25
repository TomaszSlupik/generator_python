# Generator zwraca wartość i nie zapycha pamięci
# Prosty generator
import locale
import datetime


def my_generator():
    yield 1
    yield 8
    yield 13


my_number = [item for item in my_generator()]

print(my_number)
print('---')

numbers = my_generator()

print(next(numbers))
print(next(numbers))

print('---')

# Kolejny generator


def genFive(x):

    while x < 4:
        yield x
        x += 1


for x in genFive(1):
    print(x)

print('---')
# generator o nazwie file_gen(), który z otrzymanej listy z nazwami plików,
# wybierze tylko te z rozszerzeniem .txt.
fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']


def file_gen(fnames):
    yield from (item for item in fnames if item.endswith('txt'))


gen = file_gen(fnames)
for item in gen:
    print(item)

print('---')

# Stworzenie generatora enum, który dla podanej listy poda Klucze
program = ['java', 'c++', 'python']


def enum(program):
    for key, value in enumerate(program):
        yield (f"Klucz: {key}, Wartość {value}")


my_enum = enum(program)

for test_program in my_enum:
    print(test_program)

print('---')

# Generator, który sprawdza czy liczba jest parzyste z przedziału
def even_numbers(n):
    for i in range(n - 1):
        if i % 2 == 0:
            yield i


for number in even_numbers(10):
    print(number, end=',')

print()

for number in even_numbers(30):
    print(number, end=',')
print()

print('---')

# Generator, który liczy ciąg geometryczny 
def geometric_sequence(a, q, n):
    for i in range(n):
        result = a * (q ** i)
        yield result

for num in geometric_sequence(1, 2, 10):
    print(num, end=',')

print()

for num in geometric_sequence(1, 4, 10):
    print(num, end=',')

print()

for num in geometric_sequence(1, 0.5, 5):
    print(num, end=',')    

print()

print('---')

"""
Generator generuje kolejne numery zamówień z podanym prefiksem i zakresem numerów:
prefix - prefiks do numeru zamówienia
start - dolny zakres numerów zamówień (dolny zakres jest włączony do rozwiązania)
end - górny zakres numerów zamówień (górny zakres jest wyłączony z rozwiązania)
Numer w zamówieniu powinien być odpowiednio sformatowany -  dopełniony wiodącymi zerami do sześciu cyfr. 
"""
def order_number_generator(prefix, start, end):
    for i in range(start, end):
        result = f'{prefix}-{i:06}'
        yield result

for order_num in order_number_generator('ORD', 100, 110):
    print(order_num) 

print()

for order_num in order_number_generator('#111', 10, 20):
    print(order_num)        

print()

print('---')