list = [3, 7, 19, 5, 13, 2]
def calc_total(list):
    total = sum(list)
    return total

total = calc_total(list)
print(total)    
def is_even(num):

    if num % 2 == 0:
        return "even"
    else:
        return "odd"


num = input("Pick any number! ")
num = int(num)
answer = is_even(num)
print(answer)
