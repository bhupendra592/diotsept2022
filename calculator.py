def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Division by zero not allowed")
res_add = add(10,20)
print(res_add)
res_sub = sub(20,10)
print(res_sub)
res_mul = mul(20,10)
print(res_mul)
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
res_div = div(num1,num2)
print(f"{num1} / {num2} = {res_div}")
