import math
from typing import Tuple, List, Set

# Perform element-wise sum and product of two tuples.
def tuple_operations(tuple_a: Tuple, tuple_b: Tuple):
    sum_result = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    product_result = tuple(map(lambda x, y: x * y, tuple_a, tuple_b))
    return sum_result, product_result

# Calculate Euclidean distance between two tuples.
def calculate_vector_length(p: Tuple[int], q: Tuple[int]) -> float:
    if len(p) != len(q):
        print("Error: Vectors must be of the same dimension.")
        return -1
    return math.sqrt(sum((p[i] - q[i])**2 for i in range(len(p))))
    

#BAG OF WORD (BoW)
def tokenize_text(text: str) -> List[str]:
    return text.split(" ")

def create_dictionary(documents: List[str]) -> Set[str]:
    vocab = set()
    for doc in documents:
        token = tokenize_text(doc)
        vocab.update(token)
    return vocab


def create_bow_vector(documents: List[str], binary: bool = False) -> List[List[int]]:
    bow_vector = []
    vocab_list = list(create_dictionary(documents)) 
    
    for doc in documents:
        token = tokenize_text(doc)
        vector = [0] * len(vocab_list)
        for word in token:
            index = vocab_list.index(word)
            if binary:
                vector[index] = 1
            else:
                vector[index] += 1
        bow_vector.append(vector)
    return bow_vector


def main():
    print("\n\t\t------Start the program------\n")
    
    print("🔹 Perform element-wise sum and product of two tuples:")
    tuple_a, tuple_b = (2, 3), (3, 6)
    sum_result, product_result = tuple_operations(tuple_a, tuple_b)
    print(f"Sum of tuples: {sum_result}")
    print(f"Product of tuples: {product_result}")
    
    distance = calculate_vector_length(tuple_a, tuple_b)
    print(f"\n🔹 Euclidean distance: {distance}")
    
    corpus = ["Tôi thích môn Toán",
              "Tôi thích AI",
              "Tôi thích âm nhạc",
              "Tôi thích AI thích Toán"]
    
    vocab = create_dictionary(corpus)
    print(f"\n🔹Vocabulary: {vocab}")
    
    print(f"\n🔹Bag-of-Words Vectors (Count-Base): ")
    bow_vectors = create_bow_vector(corpus, binary=False)
    for i, vec in enumerate(bow_vectors):
        print(f"Doc {i+1}: {vec}")
    
    print(f"\n🔹Bag-of-Words Vectors (Binary-Base): ")
    bow_vectors = create_bow_vector(corpus, binary=True)
    for i, vec in enumerate(bow_vectors):
        print(f"Doc {i+1}: {vec}")
    
    print("\n\t\t------End the program------")
    
if __name__ == "__main__":
    main()
    