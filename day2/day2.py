prod_ids = []
invalid_ids = 0
try:
    with open("day2/input.txt", "r") as file:
        id_seq = file.read().split(",")
        for ids in id_seq:
            prod_ids.append((ids.strip()))
except FileNotFoundError:
    print("Error: 'input.txt' not found.")
for id_ranges in prod_ids:
    id_ranges = id_ranges.split("-")
    for id in range(int(id_ranges[0]), int(id_ranges[1]) + 1):
        id_str = str(id)   
        id_length = len(id_str)
        is_valid = True
        for p_len in range(1, id_length//2+1):
            if id_length % p_len == 0:
                seq = id_str[:p_len]
                reps = id_length // p_len
                if reps >=2:
                    if id_str == seq * reps:
                        is_valid = False
                        break
        if is_valid== False:
            invalid_ids += id
       
        # if id_length%2 == 0:
        #     if id_str[:int(id_length/2)] == id_str[int(id_length/2):]:
        #         print("Invalid ID: ", id)
        #         invalid_ids += id
print(invalid_ids)