with open('input.txt') as f:
    lines = f.readlines()
draw = lines[0].split(",")

matrices = list(filter(lambda line: len(line)==15, lines))
#parse lines into list of rows for matrix
def create_matrix(matrices):
    matrix_rows = []
    for row in matrices:
        matrix_rows.append(row.split())
    return matrix_rows
#recursive procedure to generate 5x5 matrix and append as alist element 
def separate_matrices(rows):
    if len(rows) == 0:
        return rows
    else:
        return[rows[:5]] + separate_matrices(rows[5:])

#for each iterative subset of the numbers drawn, how many numbers in a given row are represented  
def count_rows(row, drawn):
    count = 0
    for cell in row:
        if cell in drawn: count += 1
    return count
            
def count_cols(col, drawn):
    pass
    count = 0
    for cell in col:
        if cell in drawn: count +=1
    return count

#return row for given row index in matrix
def matrix_row(matrix, row_index):
    row = []
    for cell in matrix[row_index]: row.append(cell)
    return row

#return column for given column index in matrix
def matrix_col(matrix, col_index):
    col = []
    for row in matrix:
        col.append(row[col_index])
    return col

#check each matrix for winning draw, and if there is one returns the draw and the row or column
def tic_tac_toe(matrix, drawn):
    min_win = float('inf')
    match = None
    for i in range(len(drawn)):
        for index in range(5):
            row, col = matrix_row(matrix, index), matrix_col(matrix, index)
            if count_rows(row, drawn[:i]) == 5:
                if i < min_win: min_win, match = i. 'Row'

            if count_cols(col, drawn[:i]) == 5:
                if i < min_win: min_win, i, 'Col
    return{"Draw": min_win, "Match": match, "Index": index}

#calculate winning draw for each board, return minimum along with winning draw
def check_matrices(matrices, drawn):
    win = {"Matrix": None, "Draw":float('inf'), "Match": None, "Index": None}
    for matrix in matrices:
        new_draw, new_match, new_index = tic_tac_toe(matrix, drawn)["Draw"]-1, tic_tac_toe(matrix, drawn)["Match"], tic_tac_toe(matrix, drawn)["Index"]
        if new_draw < win["Draw"]:
            win["Draw"] = new_draw
            win["Matrix"] = matrix
            win["Match"] = new_match
            win["Index"] = new_index
    return win
#take winning matrix, sum all unmatched numbers at subset draw and multiply by kast number drawn
def calc_total(winning_matrix, winning_draw, drawn):
    not_drawn = 0
    for row in winning_matrix:
        for num in row:
            if num not in drawn[:winning_draw+1]: not_drawn += int(num)
    return(not_drawn*int(drawn[winning_draw]))

# 4.2 Find largest minimum match in a matrix
def check_loss(matrices, drawn):
    win = {"Matrix": None, "Draw":float(0), "Match": None, "Index": None}
    for matrix in matrices:
        new_draw, new_match, new_index = tic_tac_toe(matrix, drawn)["Draw"]-1, tic_tac_toe(matrix, drawn)["Match"], tic_tac_toe(matrix, drawn)["Index"]
        if new_draw > win["Draw"]:
            win["Draw"] = new_draw
            win["Matrix"] = matrix
            win["Match"] = new_match
            win["Index"] = new_index
    return win
                
matrix_rows = create_matrix(matrices)
boards = separate_matrices(matrix_rows)
winning_matrix = check_matrices(boards, draw)
losing_matrix = check_loss(boards, draw)

print(winning_matrix)
print(losing_matrix)
print(calc_total(winning_matrix['Matrix'], winning_matrix['Draw'], draw))
print(calc_total(losing_matrix['Matrix'], losing_matrix['Draw'], draw))




