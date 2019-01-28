from random import randint

numbers = []
tries = 0
i = 0
strike = 0
ball = 0
guesses = []

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
while len(numbers) < 3:
    new_number = randint(0, 9)

    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)

    tries += 1
    print("세 수를 하나씩 차례대로 입력하세요.")
    if guesses[i] == numbers[i]:
        strike += 1
    elif guesses[i] in numbers:
        ball += 1
