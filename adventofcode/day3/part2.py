

def highest_joltage(line):
    joltage_list = list(map(int, list(line)))
    final_nr = ""

    #O (1) -> O(n)
    for i in range(12):
        subList = joltage_list[0:len(joltage_list)+(i-11)]
        #O(n)
        max_nr = max(subList)
        final_nr += str(max_nr)
        #O(n)
        the_index = joltage_list.index(max_nr)
        joltage_list = joltage_list[the_index+1::]
    return int(final_nr)


with open('./adventofcode/day3/part1.txt', 'r') as f:
    sum = 0
    # Let state nr of lines = d
    # O(d)
    for line in f.readlines():
        joltage_line = line.strip() 
        #O(n)
        sum += highest_joltage(str(joltage_line))
    #Final complexity: O(n x d)
    
    print(sum)