# 11047

#값 입력
n, k = map(int, input().split())
m = [int(input()) for _ in range(n)]
m.sort(reverse=True)

#코인 총 개수 입력 변수
answer = 0

# 알고리즘
# 큰 값이 있는 뒤의 인덱스부터 계산
for i in range(n):
    coin = m[i]
    if k >= coin:
        mok = k // coin
        k -= coin * mok
        answer += mok

print(answer)

# 1391
# 값 입력
n = int(input())
time = []

for _ in range(n):
    s, e = map(int, input().split())
    time.append([s, e])

time = sorted(time, key=lambda a: a[0]) # 시작시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
count = 0 # 회의 개수를 저장할 변수

for i, j in time:
    if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을 경우
        count += 1
        last = j

print(count)

# 11399
# 값 입력
n = int(input())
p = list(map(int, input().split()))
p.sort()

# 변수 설정
l = []
a = 0
b = 0

# 각자 소요되는 시간 구하기
for i in range(n):
    a += p[i]
    l.append(a)

# 합
for i in range(n):
    b += l[i]
print(b)

# 1541번
# 값 입력
a = input().split('-') # - 기호를 기준으로 나눔, + 있는것들 먼저 더한 후 빼면 최소값 출력 가능
num = []
for i in a:
    cnt = 0
    s = i.split('+') # + 기호를 기준으로 나눔
    for j in s:
        cnt += int(j) # + 기준으로 나눈 값 더하기, 즉 괄호 안의 수 더하기
    num.append(cnt) # cnt를 num에 저장

n = num[0]
for i in range(1, len(num)): # num의 첫번째 수에서 두번째 수부터 차례대로 빼기
    n -= num[i] # num의 첫 수에서 다음것들을 빼는 식

print(n)

# 13305번
# 값 입력
n = int(input())
d = list(map(int, input().split())) # 거리
p = list(map(int, input().split())) # 리터딩 가격

a = p[0] # 시작점의 리터당 기름값
answer = 0

for i in range(n-1): # len(d)
    if p[i] >= a:
        answer += d[i] * a # 이전 거점의 기름값이 더 쌀 경우 그것에 다음 거점까지의 거리를 곱하여 기름값 책정
    else:
        a = p[i]
        answer += d[i] * a # 해당 거점의 기름값이 더 쌀 경우 그것에 다음 거점까지의 거리를 곱하여 기름값 책정

print(answer)