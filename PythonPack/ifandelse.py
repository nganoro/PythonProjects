secret_number = 9
count = 1

while count <= 3:
    guessNumber = int(input('Guess number '))
    count += 1
    if guessNumber == int(secret_number):
        print('Correct')
        break
    elif guessNumber != int(secret_number) and count < 4:
        print('Try Again')
else:
    print('Maybe Next time')