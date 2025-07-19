with open('input.txt', 'r') as infile:
    for i, line in enumerate(infile, start=1):  # 1-based line numbers
        if i % 2 == 0:
            print(line.strip())  # .strip() removes the newline at the end