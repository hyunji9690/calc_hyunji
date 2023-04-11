# get two integer parameters
# return sum
def plus(x, y):
    return x+y
def minus(x, y):
    return x-y
def multiplication(x, y):
    return x*y
def division(x, y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus")
        check = int(input())
        if check == 1:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer :")
            print("plus = ", plus(x, y))
            print("minus = ", minus(x, y))
            print("multiplication = ", multiplication(x, y))
            print("division = ", division(x, y))
        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
