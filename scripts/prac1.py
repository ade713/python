def comma_code(words):
    str = ''
    for i in range(len(words)):
        if i == len(words) - 1:
            str += 'and ' + words[i]
            break
        str += words[i] + ', '

    return str

pic_grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def picture_grid(grid):
    for j in range(len(grid[0])):
        row = ''
        for i in range(len(grid)):
            row += grid[i][j]
        print(row + '\n')
        

picture_grid(pic_grid)