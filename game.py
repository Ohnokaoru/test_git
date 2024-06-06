import random


x = random.randint(1, 50)
print(x)
for i in range(5):
    guess = input("猜數字:")

    if guess == str(x):
        print("答對")
        break
    else:
        print(f"猜錯了，你猜{i+1}次")
