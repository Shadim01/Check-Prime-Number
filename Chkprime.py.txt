#Check Prime Number
user_input = int(input("Number:"))

if user_input > 1:
	for i in range(2, user_input):
		if (user_input % i) == 0:
			print(f" {user_input}, is not a prime number")
			print(f"{i} times {user_input//i} is {user_input}")
			break
	else:
			print(f"{user_input}, This is prime")
