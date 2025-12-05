fresh_list = []
ingredient_list = []
try:
    with open("day5/sample_input.txt", "r") as file:
        lines = file.readlines()
        ingre = False
        for line in lines:
            if line.strip() == "":
                ingre = True
                continue
            if ingre:
                ingredient_list.append(line.strip())
            else:
                fresh_list.append(line.strip())
except FileNotFoundError:
    print("Error: 'input.txt' not found.")

intervals = []
for fresh in fresh_list:
    fresh_split = fresh.split('-')
    fresh_start = int(fresh_split[0])
    fresh_end = int(fresh_split[1])
    intervals.append((fresh_start, fresh_end))

intervals.sort()
# print(intervals)
merged = []
for start, end in intervals:
    if not merged:
        # print('adding', start, end)
        merged.append([start, end])
    else:
        last_start, last_end = merged[-1]

        if start <= last_end + 1:
            # print('merging', start, end)
            merged[-1][1] = max(last_end, end)
        else:

            merged.append([start, end])

total_ingre = 0
for start, end in merged:
    total_ingre += (end - start + 1)

print(total_ingre)