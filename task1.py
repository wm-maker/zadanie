# begin, end  = map(int, input().split())
# otvet = ""
# if begin < 1 or begin == 0:
#   otvet += "0"
#   otvet += " 1"
# def fibonachi(begin, end, otvet):
#    a = 0
#    b = 1    
#    while b < end:
#     x = b
#     b += a
#     a = x
#     if b > begin:
#         otvet += " " + b
# print(otvet)
        
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
    print("В выбранном диапазоне нет чисел Фибоначчи.")  