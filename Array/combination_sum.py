candidates = [2, 3, 6, 7]
target = 7
answer_list = []

def backtrack(remain, stack, start_index):
    if remain == 0:
        answer_list.append(list(stack))
        return
    
    if remain < 0:
        return

    for i in range(start_index, len(candidates)):
        stack.append(candidates[i])
        
        backtrack(remain - candidates[i], stack, i)
        
        stack.pop()

backtrack(target, [], 0)
print(answer_list) 