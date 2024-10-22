def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        if x % 2 == 0:
            print(f'Сложное')
        else:
            print(f'Простое')
        return x
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
