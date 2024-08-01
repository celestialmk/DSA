print(0)
print(1)
count = 2

def fibonacci(prev1, prev0):
    global count
    if count <= 19:
        new_fib = prev0 + prev1
        print(new_fib)
        prev0 = prev1
        prev1 = new_fib
        count += 1
        fibonacci(prev1, prev0)
    else:
        return

fibonacci(1, 0)