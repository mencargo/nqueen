# N Queens problem solver in Python 3

## Queen solver:
### Using recursion, checking for queens each position
```
$ python3 queen_solver.py [max_size] [min_size] [log_level]
 max_size  : Board maximum size, default = 10
 min_size  : Board initial size, default = 1
 log_level : Output detail shown in the process, default = 0
             Recommended only whith min_size = max_size
             0 Only show statistics
             1 Display all solutions with boards
             2 Display all steps in the process
```

## Attack solver:
### Using recursion, creating an attack map board for each move
```
$ python3 attack_solver.py [max_size] [min_size] [log_level]
 max_size  : Board maximum size, default = 10
 min_size  : Board initial size, default = 1
 log_level : Output detail shown in the process, default = 0
             Recommended only whith min_size = max_size
             0 Only show statistics
             1 Display all solutions with boards
             2 Display all steps in the process showing queen maps
             3 Display all steps in the process showing attack maps
```