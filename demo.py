# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
	print ("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)
    print(f"It is {arg1} and {arg2} Juice")


Arg1 = input("Enter arg here  ")
Arg2 = input("Enter arg2 here  ")
myFun(Arg1, Arg2)
