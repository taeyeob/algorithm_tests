# 18258
import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([])
for i in range(n):
    s = sys.stdin.readline().split()

    if s[0] == 'push':
        q.append(s[1])

    elif s[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    elif s[0] == 'size':
        print(len(q))

    elif s[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif s[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif s[0] == 'back':
        if(len(q)) == 0:
            print(-1)
        else:
            print(q[-1])

# 2164
from collections import deque

n = int(input())
deq = deque([i for i in range(1, n+1)])

while len(deq) > 1:
    deq.popleft()
    move_n = deq.popleft()
    deq.append(move_n)

print(deq[0])

# 11866
from collections import deque
n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
answer = []

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")

# 1966
test_cases = int(input())

for _ in range(test_cases):
    n, m = list(map(int, input().split()))
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'

order = 0

while True:
    if imp[0] == max(imp):
        order += 1
        if idx[0] == 'target':
            print(order)
            break
        else:
            del imp[0]
            del idx[0]
    else:
        imp.append(imp[0])
        del imp[0]
        idx.append(idx[0])
        del idx[0]
    
# 10866
from collections import deque
import sys

n = int(sys.stdin.readline())
deq = deque([])

for i in range(n):
    s = sys.stdin.readline().split()
    
    if s[0] == 'push_front':
        deq.appendleft(s[1])
    
    elif s[0] == 'push_back':
        deq.append(s[1])
    
    elif s[0] == 'pop_front':
        if len(deq) > 0:
            print(deq[0])
            deq.popleft()
        else:
            print(-1)
    
    elif s[0] == 'pop_back':
        if len(deq) > 0:
            print(deq[-1])
            deq.pop()
        else:
            print(-1)
    
    elif s[0] == 'size':
        print(len(deq))
    
    elif s[0] == 'empty':
        if len(deq) > 0:
            print(0)
        else:
            print(1)
    
    elif s[0] == 'front':
        if len(deq) > 0:
            print(deq[0])
        else:
            print(-1)
    
    elif s[0] == 'back':
        if len(deq) > 0:
            print(deq[-1])
        else:
            print(-1)

# 1021
from collections import deque

n, m = map(int, input().split())
num_list = deque(i for i in range(1, n+1))
positions = list(map(int, input().split()))
answer = 0

for position in positions:
    while True:
        if num_list[0] == position:
            num_list.popleft()
            break
        else:
            if num_list.index(position) < len(num_list) / 2:
                while num_list[0] != position:
                    num_list.append(num_list.popleft())
                    answer += 1
            else:
                while num_list[0] != position:
                    num_list.appendleft(num_list.pop())
                    answer += 1

print(answer)

# 5430
from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())

    # 덱에 리스트 그대로 넣기
    line = sys.stdin.readline()[1:-2].split(',')
    deq = deque()
    for l in line:
        if l != '':
            deq.append(l)
    
    error_flag = 0
    reverse = 0

    for i in p:
        if i == 'R': # reverse(flag) 바꿔주기
            if reverse == 0:
                reverse = 1
            else:
                reverse = 0
        else: # D면 reverse 여부에 따라 앞이나 뒤에서 빼기
            if deq and deq[0] != '':
                if reverse == 0:
                    deq.popleft()
                else:
                    deq.pop()
            else:
                error_flag = 1
                break
    
    if error_flag == 1: # 에러 출력
        print('error')
    else:
        if reverse == 1: # reverse 1이면 뒤집어서 출력
            deq.reverse()
        print('[', end = '')
        for i in range(len(deq)):
            if i == len(deq) - 1:
                print(str(deq[i]), end = '')
            else:
                print(deq[i], end=',')
        print(']')
