#Calculator project in python using if else statement.
first_num=int(input("Enter the first number.....\n"))
operator=input("Enter the operator from +,-,*,/,//,%,**.....\n")
second_num=int(input("Enter the second number.....\n"))
if operator=="+":
    print(first_num+second_num)
elif operator=="-":
    print(first_num-second_num)
elif operator=="*":
    print(first_num*second_num)
elif operator=="/":
    print(first_num/second_num)
elif operator=="//":
    print(first_num//second_num)
elif operator=="%":
    print(first_num%second_num)
elif operator=="**":
    print(first_num**second_num) 
else:
    print("you entered the wrong operator")                          

