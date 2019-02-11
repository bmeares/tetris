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
0 1 2 3 4 5 6 7 8 9
# populate drop_lists
for i in range(LEVELS): 
    drop_lists.append([])

def insert_drop_nums(level):
    low, high = 0, 9
    for i in range(level):
        mid = int((high + low) / 2)
