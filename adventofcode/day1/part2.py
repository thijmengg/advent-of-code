
# Part 2 - puzzle input hasnt changed
with open('./part1.txt', 'r') as f:
    dial = 50
    final_sum = 0
    for line in f.readlines():
        move = line.strip() 
        direction = move[0] 
        distance = int(move[1:])
        if direction == "L":
            for _ in range(distance):
                dial = (dial - 1) % 100
                if (dial == 0):
                    final_sum += 1
        else:
           for _ in range(distance):
                dial = (dial + 1) % 100
                if (dial == 0):
                    final_sum += 1
    print(final_sum)
        