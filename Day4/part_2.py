def get_total_X_MAS_count(file_name):
    with open(file_name) as file :
        text = file.read()

    text_matrix = text.split()
    row_count = len(text_matrix)
    col_count = len(text_matrix[0])

    total_X_MAS_count = 0

    for col_nb in range(col_count - 2) :
        for row_nb in range(row_count - 2) :
            direct_diag = text_matrix[row_nb][col_nb] + text_matrix[row_nb + 1][col_nb + 1] + text_matrix[row_nb + 2][col_nb + 2]
            anti_diag = text_matrix[row_nb + 2][col_nb] + text_matrix[row_nb + 1][col_nb + 1] + text_matrix[row_nb][col_nb + 2]
            
            if (direct_diag == 'MAS' or direct_diag == 'SAM') and (anti_diag == 'MAS' or anti_diag == 'SAM') :
                total_X_MAS_count += 1

    return total_X_MAS_count

    
print(get_total_X_MAS_count('input.txt'))