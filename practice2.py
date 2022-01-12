#1
def solution(n, price):
    games = n*(n-1)//2
    per_day = n/2
    answer = (games //per_day)* price
    return answer
print(solution(5, 5000))
#2
def solution(shoes_size):
    answer = [0,0,0,0,0,0]
    for i in shoes_size:
        if i =='7':
            answer[0]+=1
        elif i =='7.5':
            answer[0]+=1
        elif i =='8':
            answer[0]+=1
        elif i =='8.5':
            answer[0]+=1
        elif i =='9':
            answer[0]+=1
        elif i =='9.5':
            answer[0]+=1

    return answer
print(solution(['7', '7','8','9.5']))
#3
def func_a(arr, num):
    ret = []
    for i in arr:
        if i !=num:
            ret.append(i)
    return ret
def func_b(a, b):
    if a> b:
        return a-b
    else:
        return b-a
def func_c(arr):
    ret = -1
    for i in arr:
        if ret <i:
            ret = 0
    return ret
def solution(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first, max_second)
    return answer

#5
def func_a(arr):
    counter=[0 for _ in range(1001)]
    for i in arr:
        counter[i] += 1
    return counter
def func_b(arr):
    ret=0
    for i in arr:
        if ret<i:
            ret=i
    return ret
def func_c(arr):
    ret = func_b(arr)
    for i in arr:
        if i !=0 and ret>i:
            ret = i
    return ret
def solution(arr):
    counter=func_a(arr)
    max_cnt=func_b(counter)
    min_cnt=func_c(counter)
    return max_cnt // min_cnt
print("#5")
print(solution([5,7,8,87,42]))
#6
def solution(weight, k):
    answer = 0
    for w in weight:
        if w > k:
            answer += 1
    return answer
print(solution([50, 20, 40, 55], 20))
#7
def solution(s):
    answer = []
    for c in s:
        if '0' <= c <= '9':
            n = ord(c) - ord('i')
            c = chr(n)
        answer.append(c)
    return ''.join(answer)

#8
def solution(name_list):
    answer = 0
    for name in name_list:
        for char in name:
            if char.find('A') or char.find('K'):
                answer += 1
                break
    return answer
print(solution(['Ak','NM']))
#9
def solution(orders):
    answer = 0
    size = 0
    for o in orders:
        for i in range(6):
            if o[i]!=0:
                size+=((i+1)**2)
    answer=size//36
    if size % 36 != 0:
        answer += 1
    return answer
print(solution([0,0,4,0,0,1]))
#10
def sum_isbn(isbn):
    sum=0
    for i in range(len(isbn)):
        c = int(isbn[i])
        if i % 2:
            w = 3
        else:
            w = 1
        sum+=w*c
    return sum
def soulution(isbn):
    answer=''
    return answer



