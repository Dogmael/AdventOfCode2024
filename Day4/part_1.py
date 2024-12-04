def get_XMAS_count_in_string(string) :
    XMAS_count = 0

    for i in range(0,len(string)) :
        if string[i:i+4] == 'XMAS' or string[i:i+4] == 'SAMX' :
            XMAS_count += 1

    return XMAS_count

def get_count_in_rows(text) :
    count_in_rows = 0

    for row in text.split() :
        count_in_rows += get_XMAS_count_in_string(row)

    return count_in_rows

def get_count_in_cols(text) :
    count_in_cols = 0

    for col_nb in range(len(text.split()[0])) :
        col = ''
        for row in text.split() :
            col += row[col_nb]
        count_in_cols += get_XMAS_count_in_string(col)

    return count_in_cols

def get_count_in_diags(text) : # ATTENTION A NE PAS OUBLIER LES 2 TYPES DE DIAGONALES
    count_in_diags = 0
    
    text_matrix = text.split()
    row_count = len(text_matrix)
    col_count = len(text_matrix[0])

    # Antidiagonales
    for diag_nb in range(row_count+col_count-1) :
        starting_row = min(diag_nb,row_count-1)
        starting_col = max(0,diag_nb - row_count + 1)

        diag = ''
        # On remonte d'une ligne tant que pas à zéro. On décale une colonne tant que pas à col_count
        for row_nb, col_nb in zip(range(starting_row,-1,-1), range(starting_col,col_count)) :
            diag += text_matrix[row_nb][col_nb]

        count_in_diags += get_XMAS_count_in_string(diag)

    # Diagonales principales
    for diag_nb in range(row_count+col_count-1) :
        starting_row = min(diag_nb,row_count-1)
        starting_col = (row_count - 1) - max(0,diag_nb - (row_count - 1))

        diag = ''
        # On remonte d'une ligne tant que pas à zéro. On diminue d'une colonne tant qu'on est pas à zéro
        for row_nb, col_nb in zip(range(starting_row,-1,-1), range(starting_col,-1,-1)) :
            diag += text_matrix[row_nb][col_nb]
        count_in_diags += get_XMAS_count_in_string(diag)

    return count_in_diags

def get_total_XMAS_count(file_name) :
    with open(file_name) as file :
        text = file.read()
    return get_count_in_rows(text) + get_count_in_cols(text) + get_count_in_diags(text)

print(get_total_XMAS_count('input.txt'))