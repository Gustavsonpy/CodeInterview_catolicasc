candidates_list = [2, 3, 4, 6, 7]
target = 8
answer_list = []

# Output = [[2, 2, 3], [7]]

for index, _ in enumerate(candidates_list):
    temp_list = []
    sum = 0
    while sum < target:
        sum = sum + candidates_list[index]

    if sum == target:
        j = 0
        while j != (target / candidates_list[index]):
            temp_list.append(candidates_list[index])
            j += 1
            
    if temp_list != []:
        answer_list.append(temp_list)

    # Different numbers
    temp_list = []
    sum = 0
    while sum < target:
        sum = sum + candidates_list[index]
        rest = target - sum
        for candidate in candidates_list:
            if candidate == rest:
                temp_list.append(candidate)
        if temp_list != []: answer_list.append(temp_list)



print(answer_list)