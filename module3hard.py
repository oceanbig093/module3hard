data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data):
    total_sum = 0
    if isinstance(data, (int, float)):
        total_sum += data
    elif isinstance(data, str):
        total_sum += len(data)
    elif isinstance(data, dict):
        for key in data.items():
            total_sum += calculate_structure_sum(key)
    elif isinstance(data, (tuple, list, set)):
        for element in data:
            total_sum += calculate_structure_sum(element)
    return total_sum

result = calculate_structure_sum(data_structure)
print(result)