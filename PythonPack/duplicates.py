numbers = [2,6,3,4,1];
for index, num in numbers:
    numbers.remove(num)
    if num in numbers:
        print("dupplicate found")
        break