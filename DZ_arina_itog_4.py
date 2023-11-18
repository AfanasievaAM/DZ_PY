# Задание №3: Кэширование для ускорения вычислений

def decor(function):
    cache = {}

    def brain(*arg):
        if arg in cache:
            return cache[arg]

        res = function(*arg)
        cache[arg] = res
        return res

    return brain

@decor
def fibonachi(a):
    if a<=0:
        return 0
    elif a == 1:
        return 1

    else:
        return fibonachi(a-1)+fibonachi(a-2)

print(fibonachi(7))
