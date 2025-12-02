
# Part 1
with open('./adventofcode/day2/part1.txt', 'r') as f:
    line = f.readline()
    all_ranges = line.split(",")    
    final_sum = 0  
    invalid_id = []
    for i in range(len(all_ranges)):
        temp = all_ranges[i].split("-")
        start = temp[0]
        end = temp[1]

        for j in range(int(start), int(end)+1):
            if len(str(j)) % 2 == 0:
                half_index = len(str(j)) //2
                left = str(j)[0:half_index]
                right = str(j)[half_index::]
                if left == right:
                    invalid_id.append(j)
                    final_sum += j


    print(final_sum)