
# Part 1
with open('./part1.txt', 'r') as f:
    dial = 50
    final_sum = 0
    for line in f.readlines():
        move = line.strip() 
        direction = move[0] 
        distance = int(move[1:])

        if direction == "L":
            dial = (dial - distance)%100
        else:
            dial = (dial + distance)%100
        
        if dial == 0:
            final_sum +=1 
    print(final_sum)
        