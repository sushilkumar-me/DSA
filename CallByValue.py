# Pass By Value
def DoSomething(num):
    print(num)
    num += 5
    print(num)
    num += 5
    print(num)

num = 10 
DoSomething(num)
print(num)