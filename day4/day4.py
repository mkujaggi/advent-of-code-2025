rolls_list = []
try:
    with open("day4/input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            rolls_list.append(line.strip())
except FileNotFoundError:
    print("Error: 'input.txt' not found.")
rolls_matrix = []
rolls_matrix.append(list('.'*(len(rolls_list[0])+2)))
for roll in rolls_list:
    rolls_matrix.append(list('.'+roll+'.'))

rolls_matrix.append(list('.'*(len(rolls_list[0])+2)))
# print(len(rolls_matrix))
# print(len(rolls_matrix[1][0]))

paper_extract = 0
paper_extracted = 1
while paper_extracted>0:
    paper_extracted = 0
    for i in range(0,len(rolls_matrix)-1):
        
        for j in range(1,len(rolls_matrix[i])-1):
            if rolls_matrix[i][j] != '@':
                continue
            # print(rolls_m/atrix)
            count_at = 0
            # print(i,j)
            if rolls_matrix[i-1][j-1] == '@':
                count_at += 1
            if rolls_matrix[i-1][j] == '@':
                count_at += 1
            if rolls_matrix[i-1][j+1] == '@':
                count_at += 1
            if rolls_matrix[i][j-1] == '@':
                count_at += 1
            if rolls_matrix[i][j+1] == '@':
                count_at += 1
            if rolls_matrix[i+1][j-1] == '@':
                count_at += 1
            if rolls_matrix[i+1][j] == '@':
                count_at += 1
            if rolls_matrix[i+1][j+1] == '@':
                count_at += 1
            if count_at < 4:
                paper_extract += 1
                paper_extracted += 1
                rolls_matrix[i][j] = '.'
            
print(paper_extract)