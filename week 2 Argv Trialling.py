import sys

arg_count = len(sys.argv)
first_arg = sys.argv[0]
print("first arg is :" + first_arg)
if arg_count > 1:
    second_arg = sys.argv[1]
    third_arg = sys.argv[2]
    print(second_arg)
    print(third_arg)
    first_number = int(second_arg)
    second_number = int(third_arg)
    result = str(first_number + second_number)
    print(result)

# first_num_ber = input("first number > ")
# first_num = int(first_num_ber)
# second_num = int(input("second number > "))
# result = str(first_num + second_num)
# print (result)



