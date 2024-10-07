import numpy as np

def nominal_dissimilarity(a, b):
    if a == b:
        return 0
    else:
        return 1

def numeric_dissimilarity(a, b):
    return abs(a - b)

def mixed_dissimilarity(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return nominal_dissimilarity(a, b)
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return numeric_dissimilarity(a, b)
    else:
        return 1  
def dissimilarity_matrix(attributes):
    num_attributes = len(attributes)
    dissimilarity_matrix = np.zeros((num_attributes, num_attributes))
    
    for i in range(num_attributes):
        for j in range(i, num_attributes):
            if i == j:
                dissimilarity_matrix[i, j] = 0
            else:
                dissimilarity = 0
                for k in range(len(attributes[0])):
                    a = attributes[i][k]
                    b = attributes[j][k]
                    dissimilarity += mixed_dissimilarity(a, b)
                dissimilarity_matrix[i, j] = dissimilarity
                dissimilarity_matrix[j, i] = dissimilarity
    
    return dissimilarity_matrix


attributes = [
    ["red", "blue", "green"],
    [10, 20, 30],
    ["small", "medium", "large"],
    [40, 50, 60]
]

dissimilarity_matrix = dissimilarity_matrix(attributes)
print(dissimilarity_matrix)