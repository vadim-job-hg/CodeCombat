# http://codecombat.com/play/level/gridmancer-eppstein-polygon
# !/usr/bin/env python
#
# Copyright 2014 Arn-O. See the LICENSE file at the top-level directory of this
# distribution and at
# https://github.com/Arn-O/py-gridmancer/blob/master/LICENSE.

'''
A codecombat gridmancer solver in Python.
Take the challenge by yourself on the following link:
    http://codecombat.com/play/level/gridmancer
'''

import argparse

# grid[i][j] ... i = height, j = length

GRID_SIMPLE = [
    [-1, -1, 0, -1],
    [0, -1, -1, -1],
    [0, -1, -1, 0],
    [-1, -1, 0, 0]
]

GRID_SIMPLE2 = [
    [-1, -1, -1, -1, -1, -1, -1],
    [0, 0, 0, -1, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

GRID_SIMPLE3 = [
    [-1, -1, -1, -1],
    [-1, -1, -1, 0],
    [-1, -1, -1, -1],
    [-1, -1, 0, -1]
]

GRID_4T1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, -1, -1, -1, -1, 0, -1, -1, -1, -1, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

GRID_4T2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, -1, -1, -1, -1, 0, -1, -1, -1, -1, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
GRID_CODECOMBAT = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, -1, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0],
    [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, 0],
    [0, 0, -1, 0, 0, 0, 0, -1, -1, -1, 0, 0, -1, -1, -1, 0, 0, -1, -1, 0],
    [0, 0, -1, 0, 0, 0, 0, -1, -1, -1, 0, 0, -1, -1, -1, 0, 0, -1, -1, 0],
    [0, -1, -1, 0, 0, 0, 0, -1, -1, -1, 0, 0, -1, -1, -1, 0, 0, -1, -1, 0],
    [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0],
    [-1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0],
    [-1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, -1, -1, -1, -1, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0],
    [0, 0, 0, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0],
    [0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0],
    [0, 0, 0, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0],
    [-1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, 0, 0, 0],
    [-1, -1, -1, -1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
    [-1, -1, -1, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

interactif = False


def get_args():
    '''Hangle program parameters'''
    grids = {
        's1': GRID_SIMPLE,
        's2': GRID_SIMPLE2,
        's3': GRID_SIMPLE3,
        '4t1': GRID_4T1,
        '4t2': GRID_4T2,
        'cc': GRID_CODECOMBAT
    }
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-g",
        "--grid",
        default='s1',
        choices=grids.keys(),
        help='test grid name'
    )
    parser.add_argument(
        "-i",
        "--interactif",
        action="store_true",
        help='trigger interactive mode'
    )
    args = parser.parse_args()
    global interactif
    interactif = args.interactif
    return grids[args.grid]


def pretty_print(grid, pos):
    '''Nice display of a grid'''
    print
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == pos:
                disp = 'X'
            else:
                if grid[i][j] == -1:
                    disp = '.'
                else:
                    disp = str(grid[i][j])
            print '%2s ' % disp,
        print
    print


def copy_grid(grid):
    '''Copy a grid to a new grid (for code readability)'''
    return [list(row) for row in grid]


def is_grid_full(grid):
    '''Check if the free space is a rectangle'''
    for row in grid:
        if -1 in row:
            return False
    return True


def get_start_pos(grid):
    '''Find the upper free cell'''
    for i, row in enumerate(grid):
        if -1 in row:
            return i, row.index(-1)


def get_free_right(grid, pos):
    '''Return the number of free cells on the right'''
    (i, j) = pos
    ret = 0
    for cell in grid[i][(j + 1):]:
        if cell == -1:
            ret = ret + 1
        else:
            break
    return ret


def get_free_bellow(grid, pos):
    '''Return the number of free cells bellow'''
    (i, j) = pos
    ret = 0
    for row in grid[(i + 1):]:
        if row[j] == -1:
            ret = ret + 1
        else:
            break
    return ret


def add_rec(grid, pos, rec, number_tag):
    '''Add a new rectangle on the grid and return a new one'''
    (i, j) = pos
    (length, height) = rec
    grid_ret = copy_grid(grid)
    for row in grid_ret[i:(i + height)]:
        for pos in range(j, (j + length)):
            if row[pos] <> -1:
                return
            else:
                row[pos] = number_tag
    return grid_ret


def get_all_recs(grid, pos):
    '''Return all possible rectangle for a given position'''
    cell_free_bellow = get_free_bellow(grid, pos)
    cell_free_right = get_free_right(grid, pos)
    recs = []
    for i in reversed(range(cell_free_right + 1)):
        for j in reversed(range(cell_free_bellow + 1)):
            rec = (i + 1, j + 1)
            grid_next = add_rec(grid, pos, rec, 99)
            if grid_next:
                recs.append(rec)
    return recs


def sieve_recs(recs):
    '''Remove suboptimal rectangles'''
    cur_length = None
    cur_height = None
    recs_ret = []
    for rec in recs:
        if rec[0] == cur_length:
            continue
        cur_length = rec[0]
        if rec[1] == cur_height:
            continue
        cur_height = rec[1]
        recs_ret.append(rec)
    return recs_ret


def get_rectangles(grid, pos):
    '''Return only relevant rectangles for a give position'''
    all_recs = get_all_recs(grid, pos)
    recs = sieve_recs(all_recs)
    return recs


def rec_gridmancer(grid, rec_nb, rec_nb_min):
    '''New recursive tree explorer'''
    start_pos = get_start_pos(grid)
    if not start_pos:
        rec_nb_min = rec_nb
        print 'New minimal solution found for %i' % rec_nb_min
        pretty_print(grid, start_pos)
        return rec_nb_min
    rec_nb += 1
    if rec_nb >= rec_nb_min:
        return rec_nb_min
    recs = get_rectangles(grid, start_pos)
    for rec in recs:
        grid_next = add_rec(grid, start_pos, rec, rec_nb)
        if interactif:
            pretty_print(grid_next, start_pos)
            key = raw_input('Hit enter')
        rec_nb_min = rec_gridmancer(grid_next, rec_nb, rec_nb_min)
    return rec_nb_min


def main():
    '''Where everything starts'''
    grid_start = get_args()
    big_max = len(grid_start) * len(grid_start[0])
    rec_gridmancer(grid_start, 0, big_max)


if __name__ == '__main__':
    main()
