#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        fizz = num % 3
        buzz = num % 5
        if fizz == 0 and buzz == 0:
            print("{}".format('FizzBuzz'), end=' ')
        elif fizz == 0:
            print("{}".format('Fizz'), end=' ')
        elif buzz == 0:
            print("{}".format('Buzz'), end=' ')
        else:
            print("{}".format(num), end=' ')
