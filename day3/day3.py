battery_list = []
jolt_list = []
try:
    with open("day3/input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            battery_list.append(line.strip())
except FileNotFoundError:
    print("Error: 'input.txt' not found.")

def find_largest_joltage(battery, num_digits=12):

    n = len(battery)
    
    result = []
    start_index = 0
    
    for pos in range(num_digits):
        print("pos: ", pos)
        remaining_positions = num_digits - pos - 1
        print("remaining_positions: ", remaining_positions)
        end_index = n - remaining_positions
        print("end_index: ", end_index)
        max_digit = '0'
        max_index = start_index
        print("start_index: ", start_index)
        
        for i in range(start_index, end_index):
            if battery[i] > max_digit:
                max_digit = battery[i]
                max_index = i
                print("max_digit: ", max_digit)
        
        result.append(max_digit)
        print(result)
        start_index = max_index + 1
    
    return ''.join(result)

for bat in battery_list:
    largest_joltage = find_largest_joltage(bat, num_digits=12)
    jolt_list.append(largest_joltage)

int_jolts = [int(jolt) for jolt in jolt_list]
sum_jolts = sum(int_jolts)
print("Total output joltage: ", sum_jolts)