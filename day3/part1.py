if __name__ == "__main__":
    grid_string = input()
    grid = grid_string.split("\n")

    di = 1
    dj = 3
    width = len(grid[0])

    tree = '#'

    i = 0
    j = 0
    tree_cnt = 0
    while i != len(grid):
        if grid[i][j] == tree:
            tree_cnt += 1

        i += di
        j += dj
        j %= width

    print("There are %d trees in the way" % tree_cnt)
