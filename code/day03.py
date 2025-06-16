from typing import List, Tuple

def find_none_positions(data: List[float]) -> Tuple[int, List[int]]:
    none_indices = []
    for index in range(len(data)):
        if data[index] is None:
            none_indices.append(index)
    return none_indices[0], none_indices
   
def interpolate_missing_values(data: List[float]) -> List[float]:
    data = data[:] 
    list_size = len(data)
    for index in range(list_size):
        if data[index] is None:
            left, right = index - 1, index + 1
            while left >= 0 or right < list_size:
                if left >= 0 and data[left] is not None:
                    data[index] = data[left]
                    break
                if right < list_size and data[right] is not None:
                    data[index] = data[right]
                    break
                left -= 1
                right +=1
    return data

# Matrix representation using List
def remove_odd_columns(matrix: List[List[int]]) -> List[List[int]]:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j % 2 != 0:
                del matrix[i][j]
    return matrix
                
def add_and_subtract_matrices(A: List[List[int]], B: List[List[int]]):
    if len(A) != len(B) or len(A[0]) != len(B):
        print("Matrices must have the same dimensions.")
        return None, None
    else:
        sum_matrix = []
        diff_matrix = []
        for i in range(len(A)):
            add_row = []
            subtract_row = []
            for j in range(len(A[0])):
                add_row.append(A[i][j] + B[i][j])
                subtract_row.append(A[i][j] - B[i][j])  
            sum_matrix.append(add_row)
            diff_matrix.append(subtract_row)
        return sum_matrix, diff_matrix
                
def dot_product_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    if len(A[0]) != len(B):
        print(f"Number of columns in A must match number of rows in B.")
        return None
    else:
        result = []
        for i in range(len(A)): # số dòng ma trận A
            row = []
            for j in range(len(B[0])): # số cột ma trận B
                sum_product = 0
                for k in range(len(A[0])): # số cột ma trận A = số dòng ma trận B
                    sum_product += A[i][k] * B[k][j]
                row.append(sum_product)    
            result.append(row)
        return result
# List Comprehension                  
def remove_stop_words(text: str, stop_words: List[str]) -> List[str]:                
    return [word for word in text.split() if word not in stop_words]

def main():
    print("\n\t\t------Start the program------")
    
    lst_data = [None, 1.1, None, 1.4, None, 1.5, None, 2.0]
    first, none_indices = find_none_positions(lst_data)
    print(f"\n🔹 First None position: {first}")
    print(f"\n🔹 All None positions: {none_indices}")
    
    interpolated = interpolate_missing_values(lst_data)
    print(f"\n🔹 Interpolated data: {interpolated}")
    
    lst_data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"\n🔹 Matrix after removing odd columns: {remove_odd_columns(lst_data)}")
    
    matrix_A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    matrix_B = [
        [2, 4, 6],
        [1, 3, 5],
        [1, 0, 1]
    ]
    sum_matrix, diff_matrix = add_and_subtract_matrices(matrix_A, matrix_B)
    print(f"\n🔹 Matrix Sum: {sum_matrix}")
    print(f"\n🔹 Matrix Difference: {diff_matrix}")
    
    dot_result = dot_product_matrices(matrix_A, matrix_B)
    print(f"\n🔹 Matrix Dot Product: {dot_result}")
    
    sentence  = "I love AI and listen to music"
    stop_words = ["I", "love", "and", "to"]
    filtered_words = remove_stop_words(sentence, stop_words)
    print(f"\n🔹 Filtered text: {filtered_words}")
    print("\n\t\t------End the program-----\n")
    
if __name__ == '__main__':
    main()