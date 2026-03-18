try:
    begin, end = map(int, input().split())
except ValueError:
    print("")
    exit()

otvet = [] 

def get_fibonacci_range(start, stop):
    a, b = 0, 1
    result = []
    
    while a <= stop:
        if a >= start:
            result.append(str(a)) 
        a, b = b, a + b 
    
    return result


numbers = get_fibonacci_range(begin, end)

if numbers:
    print(" ".join(numbers))
else:
    print("В заданном диапазоне нет чисел Фибоначчи")  