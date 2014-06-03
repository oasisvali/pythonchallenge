from itertools import izip, combinations
from operator import mul
from pprint import pprint

FILE = 'up.txt'

DIMENSIONS_TAG = '# Dimensions'
HORIZONTAL_TAG = '# Horizontal'
VERTICAL_TAG = '# Vertical'

def load_config():
  DIM_X = 0
  DIM_Y = 0

  SOL_HOR = ()
  SOL_VER = ()

  with open(FILE, 'r') as f:
    txt = f.readlines()

  region = ''
  for line in txt:
    if DIMENSIONS_TAG in line:
      region = 'DIM'
      continue
    elif HORIZONTAL_TAG in line:
      region = 'HOR'
      continue
    elif VERTICAL_TAG in line:
      region = 'VER'
      continue

    dat = line.strip().split()

    if region == 'DIM':
      if len(dat) == 2:
        DIM_X = int(dat[0])
        DIM_Y = int(dat[1])
        continue
    elif region == 'HOR':
      if len(dat) == 0:
        continue
      row = ()
      for num in dat:
        row += (int(num),)
      assert row != ()
      assert sum(row) <= DIM_Y
      SOL_HOR += (row,)
      continue
    elif region == 'VER':
      if len(dat) == 0:
        continue
      row = ()
      for num in dat:
        row += (int(num),)
      assert row != ()
      assert sum(row) <= DIM_X
      SOL_VER += (row,)

  assert DIM_X == len(SOL_VER)
  assert DIM_Y == len(SOL_HOR)

  print DIM_X, DIM_Y

  return DIM_X, DIM_Y, SOL_HOR, SOL_VER


DIM_X, DIM_Y, SOL_HOR, SOL_VER = load_config()


# see how many 100% blanks and 100% fills we can determine
def build_row_leftmost_blocks(sol):
  row = []
  for block in sol:
    row.extend([True]*block)
    if len(row) == DIM_X:
      break
    row.append[False]
  row.extend([False]*(DIM_X - len(row)))
  return row


def update_constraints(i, filled, empty, overlap_constraints, column = False):



def calc_intersection(leftmost_row, rightmost_row):



def calculate_overlap_constraints():
  overlap_constraints = empty_sketch()

  # for each row, put blocks on leftmost, put blocks on rightmost and their intersection gives 100% positions
  for i, sol in enumerate(SOL_HOR):
    row_blocks_leftmost = build_row_leftmost_blocks(sol)
    row_blocks_rightmost = row_blocks_leftmost[::-1]
    filled, empty = calc_intersection(row_blocks_leftmost, row_blocks_rightmost)
    update_constraints(i, filled, empty, overlap_constraints)

  # for each column, put blocks on topmost, put blocks on bottommost, and their intersection gives 100% positions
  for i, sol in enumerate(SOL_VER):
    col_blocks_topmost = build_row_leftmost_blocks(sol)
    col_blocks_bottommost = col_blocks_topmost[::-1]
    filled, empty = calc_intersection(col_blocks_topmost, col_blocks_bottommost)
    update_constraints(i, filled, empty, overlap_constraints, column = True)

  # print out how many (out of 32*32) positions we were able to determine 100%
  positions = 0
  for row in overlap_constraints:
    for pos in row:
      if pos is not None:
        positions += 1
  print 'Constrained', positions, 'out of', DIM_X*DIM_Y, 'positions'

OVERLAP_CONSTRAINTS = calculate_overlap_constraints()

def analyze_row(row):
  res = ()
  cum = 0
  for val in row:
    if val:
      cum+=1
    else:
      if cum > 0:
        res += (cum,)
        cum = 0
  if cum > 0:
    res += (cum,)
  return res

def is_solution(mat):
  for row, sol in izip(mat,SOL_HOR):
    if analyze_row(row) != sol:
      return False
  for col, sol in izip(izip(*mat),SOL_VER):
    if analyze_row(col) != sol:
      return False

  return True

def print_sketch(mat):
  print '','_'*(DIM_X*2+1)

  for row in mat:
    buf = []
    for cell in row:
      if cell:
        buf.append(unichr(0x2588))
      else:
        buf.append(' ')
    print '|', ' '.join(buf), '|'
  print '', unichr(0x203E)*(DIM_X*2+1)

def ON(mat, x, y):
  mat[x][y] = True

def OFF(mat, x, y):
  mat[x][y] = False

def new_sketch():
  return [[False]*DIM_X for j in xrange(DIM_Y)]


def empty_sketch():
  return [[None]*DIM_X for j in xrange(DIM_Y)]


def apply_combination(combination):
  mat = new_sketch()
  for position in combination:
    ON(mat, position/DIM_X, position%DIM_X)

  return mat


def build_matrices(mat, possibilities, combinations):
  assert len(mat) == (DIM_Y-len(possibilities))

  if len(possibilities) == 0:
    combinations.append(mat)
    return

  for possibility in possibilities[0]:
    if len(possibilities) == DIM_Y:
      mat = [possibility]
    else:
      mat.append(possibility)
    build_matrices(list(mat), possibilities[1:], combinations)
    mat.pop()

  return

def get_combinations(possibilities):
  print 'Fetching combinations for ', reduce(mul, list(len(x) for x in possibilities), 1), 'possibilities'
  print
  print 'Do you want to continue?'
  raw_input()
  combinations = []

  build_matrices([], possibilities, combinations)

  print 'Found', len(combinations), 'combinations'
  return combinations


def build_row(possibility, sol):
  assert len(possibility) == len(sol)
  row = [False] * DIM_X
  offset = 0
  for index, num in izip(possibility, sol):
    row[(offset+index):(index+offset+num)] = [True]*num
    offset += (num-1)

  return row


# check if given row meets the constraints calculated earlier
def satisfies_overlap_constraints(row, i):
  for j,pos in enumerate(row):
    if OVERLAP_CONSTRAINTS[i][j] != None:
      if OVERLAP_CONSTRAINTS[i][j] != pos:
        return False
  return True


def get_possibilities():

  possibilities = [[] for _ in xrange(DIM_Y)]
  for i, sol in enumerate(SOL_HOR):
    print 'calculating possibilities for row', i+1

    # combinations optimization
    p = DIM_X - sum(sol) + len(sol)
    r = len(sol)

    row_possibilities = combinations(xrange(p),r)
    #see which possibilities conform with the solution
    for possibility in row_possibilities:
      row = build_row(possibility, sol)
      if analyze_row(row) == sol:
        if satisfies_overlap_constraints(row, i):
          possibilities[i].append(row)

    print 'found ', len(possibilities[i]), 'possibilities'

  return possibilities


def find_solution(possibilities):
  for combination in get_combinations(possibilities):
    # assert len(combination) == 55
    # mat = apply_combination(combination)
    mat = combination
    if is_solution(mat):
      print 'Solution found:'
      print
      print_sketch(mat)
      break
  else:
    print 'No Solutions found'


if __name__ == '__main__':

  # first find all the valid row-by-row configs
  possibilities = get_possibilities()

  # print possibilities

  find_solution(possibilities)




