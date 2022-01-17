import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

if __name__ == '__main__':
    f = open('my_slice.txt')
    slice_text = f.read()
    f.close()

    lines = slice_text.split('\n')

    space = np.array([[1 if x == '#' else 0 for x in lines[i]] for i in range(len(lines))])
    space = np.expand_dims(space, axis=[2, 3])

    for cycle in range(6):
        space = np.pad(space, ((1, 1), (1, 1), (1, 1), (1, 1)))
        space_padded_twice = np.pad(space, ((1, 1), (1, 1), (1, 1), (1, 1)))

        sliding_window = sliding_window_view(space_padded_twice, window_shape=(3, 3, 3, 3))

        neighbour_counts = np.einsum('ijklpqmn->ijkl', sliding_window) - space

        for i in range(space.shape[0]):
            for j in range(space.shape[1]):
                for k in range(space.shape[2]):
                    for l in range(space.shape[3]):
                        if not (space[i, j, k, l] == 1 and neighbour_counts[i, j, k, l] in [2, 3]):
                            space[i, j, k, l] = 0

                        if space[i, j, k, l] == 0 and neighbour_counts[i, j, k, l] == 3:
                            space[i, j, k, l] = 1



    print('Number of active cubes = {:d}'.format(np.sum(space)))