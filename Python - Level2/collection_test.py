


from collections import deque
d = deque('ssafy')
d.appendleft('welcome to')
d.popleft()

d.rotate(1)
print(d)