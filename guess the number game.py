import random

number = random.randint(1, 100)

guesses = 0

print("Я загадал число от 1 до 100. Попробуйте угадать его.")

while True:
    guess = int(input("Введите ваше предположение: "))
    guesses += 1

    if guess < number:
        print("Мое число больше.")
    elif guess > number:
        print("Мое число меньше.")
    else:
        print(f"Поздравляю! Вы угадали число за {guesses} попыток!")
        break