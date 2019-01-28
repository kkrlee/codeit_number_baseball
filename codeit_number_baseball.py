from random import randint

answer = []

def generate_number():
    while len(answer) < 3:
        number = randint(0, 9)
        if number in answer:
            number = randint(0, 9)
        else:
            answer.append(number)
    return answer

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("세 수를 하나씩 차례대로 입력하세요.")

answer = generate_number()

strike = 0
ball = 0
tries = 0

while strike < 3:
    guess = []
    while len(guess) < 3:
        new_number = int(input("%d번째 숫자를 입력해주세요: " % (len(guess) + 1)))
        if new_number < 0 or new_number > 9:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        elif new_number in guess:
            print("중복되는 수 입니다. 다시 입력해주세요.")
        else:
            guess.append(new_number)

    strike = 0
    ball = 0
    i = 0

    while i < 3:
        if guess[i] == answer[i]:
            strike = strike + 1
        elif guess[i] in answer:
            ball = ball + 1
        i = i + 1
    print("%dS %dB" % (strike, ball))
    tries = tries + 1

print("축하합니다. %d번만에 숫자의 값과 위치를 모두 맞추셨습니다." % (tries))
