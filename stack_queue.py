# 0828
import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    word = sys.stdin.readline().split() # split하여 입력받기
    order = word[0] # 명령어 받기

    # order가 push일 경우
    if order == 'push':
        stack.append(word[1])
    
    # order가 pop일 경우
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    # order가 size일 경우
    elif order == 'size':
        print(len(stack))
    
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

# 10773
import sys

# 값 입력
k = int(sys.stdin.readline())
stack = []
answer = 0

for _ in range(k):
    num = int(sys.stdin.readline())

    if num > 0:
        stack.append(num)
    
    elif num == 0:
        if len(stack) > 0:
            stack.pop(-1) # 0을 외칠 경우 가장 최근의 숫자 제거

if len(stack) > 0:
    for i in range(len(stack)):
        answer += stack[i] # stack에 수가 있을 경우 그 안의 값을 더하고, 없을 경우 0 출력

print(answer)

# 9012
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    open = []
    close = []
    par = sys.stdin.readline()
    for i in par:
        if i == '(':
            open.append(i) # 괄호열기는 open
        elif i == ')':
            close.append(i) # 괄호닫기는 close
            if len(close) > len(open): # 열리지 않은 괄호를 닫는 부호가 먼저 나오는 경우 중단
                break
    
    if len(open) == len(close):
        print('YES')
    else:
        print('NO')

# 4949
while True:
    s = input()

    if s == '.':
        break
    stack = []
    temp = True

    for i in s:
        if i == '(' or i=='[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack:
        print('yes')
    else:
        print('no')

# 17298
n = int(input())
a = list(map(int, input().split()))
stack = []
answer = [-1] * n

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        answer[stack.pop()] = a[i]
    stack.append(i)

print(*answer)