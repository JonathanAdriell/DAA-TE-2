import random

def input_generator(n):
    values = list(range(1, n + 1))
    total_values = sum(values)

    if total_values % 2 != 0:
        values[-1] += 1
    random.shuffle(values)
    
    return values

print(f"Dataset with 10 elements:\n{input_generator(10)}\n")
print(f"Dataset with 40 elements:\n{input_generator(40)}\n")
print(f"Dataset with 80 elements:\n{input_generator(80)}\n")

# Dataset with 10 elements:
# [3, 8, 5, 11, 9, 4, 7, 2, 6, 1]

# Dataset with 40 elements:
# [33, 3, 23, 10, 31, 38, 4, 24, 16, 29, 27, 28, 1, 11, 40, 19, 32, 9, 26, 20, 36, 30, 8, 34, 21, 35, 13, 18, 37, 7, 5, 15, 12, 25, 2, 17, 22, 14, 39, 6]

# Dataset with 80 elements:
# [76, 62, 22, 23, 56, 27, 26, 51, 59, 57, 20, 44, 29, 80, 1, 68, 63, 34, 19, 39, 4, 53, 46, 2, 70, 43, 17, 36, 5, 60, 7, 40, 24, 6, 49, 42, 54, 11, 69, 3, 78, 79, 33, 25, 10, 18, 61, 13, 38, 47, 9, 35, 55, 66, 74, 12, 8, 50, 58, 41, 31, 14, 16, 15, 37, 72, 65, 73, 45, 75, 67, 30, 32, 28, 21, 71, 48, 77, 52, 64]