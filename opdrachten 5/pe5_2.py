
def  convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit
def table():
    print('{:10} {:10}'.format('F', 'C'))
    for temp in range(-30, 50, 10):
        print('{:5} {:7}'.format(convert(temp), temp))
table()

