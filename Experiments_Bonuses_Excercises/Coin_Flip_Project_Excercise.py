while True:
    with open('coinflip.txt', 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + '\n'

    sides.append(side)

    with open('coinflip.txt', 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")