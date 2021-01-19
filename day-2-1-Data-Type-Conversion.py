# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# find out the data type of the input received

print(type(two_digit_number)) #string

#Convert the string data type to intergers
first_digit = int(two_digit_number[0])
last_digit = int(two_digit_number[1])

# Find the data type, checks if conversion was successful
print(type(first_digit)) #data type is interger
print(type(last_digit))

# Print the sum
print("The sum of the two-digit-number is:\n")
sum = first_digit + last_digit
print(sum)







