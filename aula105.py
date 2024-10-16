def decorator(func):
    print("Decorator 1")
    def aninhada(*args, **kwargs):
        print("Aninhada 1")
        result = func(*args, **kwargs)
        return result
    return aninhada

@decorator
def soma(x, y):
    return x + y

soma = soma(2, 5)

print(soma)