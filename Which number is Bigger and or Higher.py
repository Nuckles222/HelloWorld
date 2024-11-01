# take in two numbers, tell which one is the highest. 
# first one is inputting via code lines


#first_number = 50
#Second_number = 40 
#if first_number>Second_number: 
#    print (first_number)
#else:
#    print (Second_number)

#second one to be put in via user inputs below
running = True
while running: 
    print("Please Input Numbers to see which one is Higher/Bigger in Count/Amount")
    first_number = input("Please put in your First Number > ")
    second_number = input("Please put in Your Second Number > ")
    if first_number>second_number:
        print(first_number + " < is the highest number")
    elif second_number == first_number: 
        print(first_number + " < is the same for Both inputs")
    else:
        print(second_number + " < is the highest number")
    keep_going = input("would you like to try Again? (Yes/No)")
    if keep_going  !='Yes' and keep_going !='YES' and keep_going !='yes' and keep_going !='yEs' and keep_going !='yeS' and keep_going !='Y' and keep_going !='y':
        running=False

#print("Please input numbers to see which one is higher in count")
#first_number = input("Please put in your First Number > ")
#second_number = input("Please put in Your Second Number > ")
#if first_number>second_number:
#    print(first_number)
#else: 
#    print(second_number)
