def fizz_buzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return "FizzBuzz"
    elif numero % 2 == 0:
        return "fizz"
    elif numero % 5 == 0:
        return "buzz"
    else:
        return numero

fizz_buzz = fizz_buzz(15)
print(fizz_buzz)