def DoSomething(num): 
    print(num)
    num[0] += 5 
    print(num)
    num[0] += 5
    print(num)

num = [10] 
DoSomething(num)
print(num)

'''
Instead, Python's model is:

"Variables are names bound to objects. Arguments are passed by object reference."

So what does that mean?
Immutable types like int, float, str, tuple: Even though the reference is passed, you can't change the original because these types create a new object on modification.

Mutable types like list, dict, set, class objects: You can modify them in-place, and the changes will reflect outside the function.
'''