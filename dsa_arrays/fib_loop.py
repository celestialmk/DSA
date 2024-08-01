prev1 = 1
prev0 = 0
print(prev0)
print(prev1)
for i in range(18):
    new_fibo = prev0 + prev1
    print(new_fibo)
    prev0 = prev1
    prev1 = new_fibo