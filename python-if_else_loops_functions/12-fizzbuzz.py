#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        fizz = num % 3
        buzz = num % 5
        if fizz and buzz:
            print("{}".format('FizzBuzz'), end=' ')
        elif fizz:
            print("{}".format('Fizz'), end=' ')
        elif buzz:
            print("{}".format('Buzz'), end=' ')
