def sequence_alignment(x, y, delta):
    def char_to_index(c):
        char_map = {'A': 0, 'G': 1, 'T': 2, 'C': 3, '-': 4}
        return char_map[c]

    n = len(x)
    m = len(y)

    # Initialize the dynamic programming matrix
    matrix1 = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill in the matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x_char = x[i - 1]
            y_char = y[j - 1]

            match = matrix1[i - 1][j - 1] + delta[char_to_index(x_char)][char_to_index(y_char)]
            insert = matrix1[i][j - 1] + delta[char_to_index('-')][char_to_index(y_char)]
            delete = matrix1[i - 1][j] + delta[char_to_index(x_char)][char_to_index('-')]

            matrix1[i][j] = max(match, insert, delete)

    # Traceback to reconstruct the alignment
    aligned_x = ""
    aligned_y = ""
    i, j = n, m
    while i > 0 and j > 0:
        x_char = x[i - 1] if i > 0 else '-'
        y_char = y[j - 1] if j > 0 else '-'

        if i > 0 and j > 0 and matrix1[i][j] == matrix1[i - 1][j - 1] + delta[char_to_index(x_char)][char_to_index(y_char)]:
            aligned_x = x_char + aligned_x
            aligned_y = y_char + aligned_y
            i -= 1
            j -= 1
            print("1")
        elif j > 0 and matrix1[i][j] == matrix1[i][j - 1] + delta[char_to_index('-')][char_to_index(y_char)]:
            aligned_x = '-' + aligned_x
            aligned_y = y_char + aligned_y
            j -= 1
            print("2")
        elif i > 0 and matrix1[i][j] == matrix1[i - 1][j] + delta[char_to_index(x_char)][char_to_index('-')]:
            aligned_x = x_char + aligned_x
            aligned_y = '-' + aligned_y
            i -= 1
            print("3")
        else:
            raise ValueError("Invalid state during traceback")
            print("4")
            

    # Ensure that the entire y sequence is printed in the output
    while j > 0:
        aligned_x = '-' + aligned_x
        aligned_y = y[j - 1] + aligned_y
        j -= 1

    return aligned_x, aligned_y, matrix1[n][m]

# Example usage
x = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
y = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"
delta = [
    [1, -0.8, -0.2, -2.3, -0.6],
    [-0.8, 1, -1.1, -0.7, -1.5],
    [-0.2, -1.1, 1, -0.5, -0.9],
    [-2.3, -0.7, -0.5, 1, -1],
    [-0.6, -1.5, -0.9, -1, float('inf')]
]

aligned_x, aligned_y, z = sequence_alignment(x, y, delta)

print("Aligned X:", aligned_x)
print("Aligned Y:", aligned_y)
print(z)

