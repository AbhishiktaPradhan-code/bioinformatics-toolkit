#to define a function in python we use the def keyword
#defining a function Hello
def hello(to="World"):
	print("Hello,", to)

def main():
	name = input("What's your name? ")
	hello(name)

main()