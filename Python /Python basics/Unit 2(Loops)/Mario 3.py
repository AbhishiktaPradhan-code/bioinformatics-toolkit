def main():
	print_square(3)

def print_square(size):
	# For each row in square
	for i in range(size):
		# For each column in square
		for j in range(size):
			print("#", end="")
		print()

main()