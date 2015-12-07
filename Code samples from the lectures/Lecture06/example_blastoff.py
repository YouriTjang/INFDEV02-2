import time

def rec_countdown(n):
    if n <= 0:
        print("Blast off")
    else:
        print(n)
        time.sleep(0.3)
        rec_countdown(n - 1)
# rec_countdown(10)

def it_countdown(n):
    for i in range(n, -1, -1):
        if i == 0:
            print("Blast off!")
        else:
            print(i)

it_countdown(10)