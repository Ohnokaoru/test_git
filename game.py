import random

start = 1
end = 50
x = random.randint(1, 50)
print(x)
for i in range(5):
    guess = eval(input(f"猜數字str{start}-{end}:"))

    if guess == x:
        print("答對")
        break
    else:
        print(f"猜錯了，你猜{i+1}次")
        if guess > x:
            print("猜低一點")
        else:
            print("猜高一點")
