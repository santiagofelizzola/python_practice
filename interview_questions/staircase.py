def staircase(n):
    for i in range(1, n + 1):
        spaces = ""
        hashes = ""
        for j in range(1, n - i + 1):
            spaces += " "
        for k in range(1, i + 1):
            hashes += "#"
        print(spaces + hashes)

staircase(5)