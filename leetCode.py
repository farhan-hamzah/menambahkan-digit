nums = int(input())
i = 0
while nums > 9:
    a = nums%10
    b = nums//10
    nums = a+b
    i += 1
print(i)