def generate_permutations(elements):
    if len(elements) == 1:
        return [elements]
    permutations = []
    for i in range(len(elements)):
        rest = elements[:i] + elements[i+1:]
        for p in generate_permutations(rest):
            permutations.append([elements[i]] + p)
    return permutations

def calculate(num_list, op_list, priority):
    for op in priority: 
        stack_nums = [num_list.pop(0)]  
        stack_ops = []

        while op_list:
            current_op = op_list.pop(0) 

            if current_op == op:
                next_num = num_list.pop(0)  
                if op == '+':
                    result = stack_nums.pop() + next_num
                elif op == '-':
                    result = stack_nums.pop() - next_num
                elif op == '*':
                    result = stack_nums.pop() * next_num
                stack_nums.append(result)
            else:
                stack_nums.append(num_list.pop(0))
                stack_ops.append(current_op)
                
        num_list = stack_nums
        op_list = stack_ops

    # 모든 연산이 끝난 후 최종 결과 반환
    return abs(num_list[0])


def solution(expression):
    num_list = []
    op_list = []
    current_num = ''
    
    for char in expression:
        if char in '+-*':
            num_list.append(int(current_num))
            op_list.append(char)
            current_num = ''
        else:
            current_num += char
    num_list.append(int(current_num))
    
    priorities = generate_permutations(['+', '-', '*'])
    
    max_result = 0
    for priority in priorities:
        result = calculate(num_list[:], op_list[:], priority)
        max_result = max(max_result, result)
    
    return max_result
