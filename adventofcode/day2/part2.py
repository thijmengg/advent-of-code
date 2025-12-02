# Still in construction

def isRepeated(sub, string):
    for i in range(0, len(string), len(sub)):
        # print(string[i:len(sub)+i], sub)
        if string[i:len(sub)+i] != sub:
            return False
    return True

def isValid(number):
    string_number = str(number)
    for i in range(len(string_number) -1):
        sub = string_number[0:i+1]
        # print(sub, string_number)
        subIsRepeated = isRepeated(sub, string_number)
        if subIsRepeated:
            return False
    return True


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
            if not isValid(j):
                invalid_id.append(j)
                final_sum += j

    print(final_sum)

