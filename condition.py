x=int(input("what is x?"))
y=int(input("what is y?"))

#however we can improve the above code 
#logically elif x == y is not a necessary evaluation to run beause if x<y and x>y its automatically x will be equal to y
x=int(input("what is x?"))
y=int(input("what is y?"))

if x<y:
    print("x is less than y")

elif x>y:
    print("x is greater than y")

else:
    print("x is equal to y")

