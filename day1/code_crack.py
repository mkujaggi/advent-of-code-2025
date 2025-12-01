rotation_list = []
current_rotation = 50
min_rotation = 0
max_rotation = 99
zero_counter = 0
zero_clicks = 0
try:
    with open("day1/input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            rotation_list.append((line.strip()))
except FileNotFoundError:
    print("Error: 'input.txt' not found.")

for code in rotation_list:
    for i in range(int(code[1:])):
        if code[0] == "R":        
            current_rotation = (current_rotation + 1) % 100
        elif code[0] == "L":
            current_rotation = (current_rotation - 1) % 100
        if current_rotation == 0:
            zero_counter += 1

print(zero_counter)
