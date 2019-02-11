import time

start_time = None
current_piece = None
delay = 0.5
delay_threshold = 0.025
mono = False
ascii = False
dropped = False
preview_pc = None
score = 0
distance_dropped = 0
drop_lists = []
LEVELS = 10
current_level = 1
num_placed = 0
lines_cleared = 0
LINES_PER_LEVEL = 10

# populate drop_lists
def insert_drop_nums(level):
    # X:  0 1 2 3 4 5 6 7 8 9
    # 1:  0        
    # 2:  0         5
    # 3:  0       4     7
    # 4:  0     3   5     8
    # 5:  0   2   4   6   8
    # 6 through 9 are the same as 5
    #10:  0 1 2 3 4 5 6 7 8 9

    l_1 = [0]
    l_2 = [0, 5]
    l_3 = [0, 4, 7]
    l_4 = [0, 3, 5, 8]
    l_5 = [0, 2, 4, 6, 8]
    l_10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = []
    # levels that share difficulty
    plateau = [5, 6, 7, 8, 9]
    if level == 1:
        l = l_1
    elif level == 2:
        l = l_2
    elif level == 3:
        l = l_3
    elif level == 4:
        l = l_4
    elif level in plateau:
        l = l_5
    else:
        l = l_10

    for n in l:
        drop_lists[level - 1].append('.' + str(n))
    #  if level == 1:
        #  buff = int(LEVELS / (level))
    #  else:
        #  buff = int(LEVELS / (level - 1))
    #  i = 0
    #  while i < LEVELS:
        #  drop_lists[level - 1].append('.' + str(i))
        #  i += buff


for i in range(LEVELS): 
    drop_lists.append([])
    insert_drop_nums(i + 1)

#  for l in drop_lists:
    #  print(l)

#  input()
