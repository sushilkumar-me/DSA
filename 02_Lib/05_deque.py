from collections import deque 

dq = deque([1,2,3])
dq.appendleft(0)
dq.append(4)
print(dq)
dq.pop()       # remove from right
dq.popleft()   # remove from left
print(dq)

## What it is: A double-ended queue, where you can add/remove from both ends.