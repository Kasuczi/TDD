"""
Napisz program, który wyświetla liczby od 1 do N.
Dla liczb podzielnych przez 3 niech program wyświetli „Fizz”;
dla liczb podzielnych przez 5 niech wyświetli ‚Buzz’;
a dla liczb podzielnych przez 15 niech wyświetli ‚FizzBuzz’.
"""

def fizzbuzz(i):
        if  i % 15 == 0:
            i =  'FizzBuzz'
        elif i % 5 == 0:
            i = 'Buzz'
        elif  i % 3 == 0:
            i = 'Fizz'

        return i


def main():
    n = int(input("Provide number: "))
    print(fizzbuzz(n))


main()
