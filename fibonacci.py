# Fibonacci
def fibonacci():
    number = int(input("input a number? "))


    if number <= 0:
        print("Incorrect input")

    elif number == 1:
        return 0

    elif number == 2:
        return 1
    else:
       #Fn = Fn-1 + Fn-2
        ls = [1, 1]
    for i in range(2, number):
        ls.append(ls[i - 1] + ls[i - 2])
    fib =  ls[-1]
    print(fib)

fibonacci()
