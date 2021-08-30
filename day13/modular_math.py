def solve_mod_system(a, b):
    b_curr = b[0]
    a_curr = a[0]
    for i in range(1, len(a)):
        diff = (b[i] - b_curr) % a[i]

        j = 0
        while (a_curr * j) % a[i] != diff:
            j += 1

        b_curr = b_curr + j * a_curr
        a_curr = a_curr * a[i]

    x = b_curr % a_curr

    return x

if __name__ == '__main__':
    a = [3, 5, 11]
    b = [2, 3, 7]

    x = solve_mod_system(a, b)

