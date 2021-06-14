if __name__ == "__main__":
    grid_string = input()
    grid = grid_string.split("\n")

    slopes = [[1, 1],
              [3, 1],
              [5, 1],
              [7, 1],
              [1, 2]]

    width = len(grid[0])

    tree = '#'
    tree_count = []
    for slope in slopes:
        di = slope[1]
        dj = slope[0]

        i = 0
        j = 0
        tree_cnt = 0

        while i < len(grid):
            if grid[i][j] == tree:
                tree_cnt += 1

            i += di
            j += dj
            j %= width

        tree_count.append(tree_cnt)

    print("Tree count\n", tree_count)
    product = 1
    for count in tree_count:
        product *= count
    print("The product is %d" % product)