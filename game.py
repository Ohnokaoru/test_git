import random


start = 1
end = 50
x = random.randint(start, end)

for i in range(5):

    guess = eval(input(f"請猜數字{start}-{end}:"))
    print(f"機會一共5次，已猜第{i+1}次")
    if guess == x:
        print("答對")
        break

    else:
        print(f"猜錯了")

        if guess > x:
            if end > guess:
                print(f"猜低一點")
                end = guess - 1

            else:
                print("數字區間錯誤")

        else:
            if start < guess:
                print(f"猜高一點")
                start = guess + 1

            else:
                print("數字區間錯誤")

print()
print(f"答案:{x}")

print("測試回當下sha-1，新增分支並add與commit後，切回master，再merge 要合併的分支")
