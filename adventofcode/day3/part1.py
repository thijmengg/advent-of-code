

def highest_joltage(line):
    joltage_list = list(map(int, list(line)))
    highest_number = max(joltage_list[0:len(joltage_list)-11])
    highest_nr_index = joltage_list.index(highest_number)
    lowest_nr = max(joltage_list[highest_nr_index+1::])
    lowest_nr_index = joltage_list.index(lowest_nr)
    final_nr = int(str(line[highest_nr_index]) + str(line[lowest_nr_index]))
    # print(final_nr)
    return final_nr


with open('./adventofcode/day3/part1.txt', 'r') as f:
    sum = 0
    for line in f.readlines():
        joltage_line = line.strip() 
        sum += highest_joltage(str(joltage_line))
    
    print(sum)