while True:
	try:
		grade = int(input("Please type your grade. "))
		if grade < 0 or grade > 100: #range of 0-100
			raise ValueError #this will send it to the print message and back to the input
		break
	except ValueError:
		print("Invalid grade. Valid grade = 0-100")

if grade >=95 and grade <=100:
	print("\"A\" is your grade. Excellent ")
elif grade >=90 and grade <=94:
	print("\"A-\" is your grade. Very Good ")
elif grade >=85 and grade <=89:
	print("\"B+\" is your grade. Well Done ")
elif grade >=80 and grade <=84:
	print("\"B\" is your grade. Good job ")
elif grade >=75 and grade <=79:
	print("\"B-\" is your grade. Nice job ")
elif grade >=70 and grade <=74:
	print("\"C+\" is your grade. Nice try ")
elif grade >=65 and grade <=69:
	print("\"C\" is your grade. ")
elif grade >=60 and grade <=64:
	print("\"C-\" is your grade. ")
elif grade >=55 and grade <=59:
	print("\"D+\" is your grade. ")
elif grade >=50 and grade <=54:
	print("\"D\" is your grade. Better next time")
elif grade >=45 and grade <=49:
	print("\"D-\" is your grade. You almost failed")
elif grade >=0 and grade <=44:
	print("\"E\" is your grade. You have failed this class")



