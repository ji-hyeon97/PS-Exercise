import numpy as np

def to_num(x, y, columns):
    return y * columns + x

def index_list(x1, y1, x2, y2, columns):
    y1, x1, y2, x2 = x1-1, y1-1, x2-1, y2-1
    return [to_num(x, y1, columns) for x in range(x1, x2 + 1)] + [to_num(x2, y, columns) for y in range(y1+1, y2+1)] + [to_num(x, y2, columns) for x in range(x2-1, x1-1, -1)] + [to_num(x1, y, columns) for y in range(y2-1, y1, -1)]

# def to_list(l, indices, nums)

def print_array(array, rows, columns):
    for row in range(rows):
        print(array[row * columns : (row + 1) *columns])

def solution(rows, columns, queries):
    answer = []
    
    array = np.array([i for i in range(1, rows*columns+1)])
    
    # print_array(array, rows, columns)
    
    for query in queries:
        
        x1, y1, x2, y2 = query
        
        indices = index_list(x1, y1, x2, y2, columns)
        
        # print(indices)
        
        num = array[indices]
        
        replace_num = num[:-1]
        replace_num = np.append([num[-1]], replace_num)
        
        i = 0
        for idx in indices:
            array[idx] = replace_num[i]
            i += 1
        
        # print_array(array, rows, columns)
        
        answer.append(int(np.min(num)))
        
        # print(f'answer\n{answer}')
        
    return answer