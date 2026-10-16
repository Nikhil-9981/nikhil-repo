# input1 = input("Enter you name: ")
# input2 = input("Enter your age: ")
# intput3 = input("Enter your city: ")
# sums = int(input1) + int(input2) + int(intput3)

# print(sums)
print("Hello\rWorld")

user_list = input("Enter your list: ").split()



# max_value = max(user_list)
# print(max_value)
max_val = 0
for val in user_list:
    if int(val) > int(max_val):
        max_val = val
print(max_val)



product1 = input("enter first number")
product2 = input("Enter second number")
product3 = input("Enter third number")


sum = int(product1) + int(product2) + int(product3)

avg_price = sum/3

print(sum)

print(avg_price)


input1 = input("Enter first number: ")

print("You entered: " + input1)

    




