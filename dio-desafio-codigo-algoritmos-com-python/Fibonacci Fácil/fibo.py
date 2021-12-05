n = int(input("Digite no numero: "))

fib_list = [0, 1]

for i in range(0, n):

    fib_list.append(fib_list[i] + fib_list[i + 1])
    fib_string = fib_list[i]
    print(fib_string, end=' ')
