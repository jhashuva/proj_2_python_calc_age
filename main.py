# This will calculate your age

cy = 2021

by = input("Enter your birth year: ")



if by>cy  :
    print("Give correct birth year")
elif by<0 :
    print("You were not born yet")
elif type(int(by))== 'int':
    print("give number only")
else:
    print(cy-int(by))
