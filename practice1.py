def func_a(s):
     s.sort()
     return s[len(s)-1], s[0]
def func_b(s):
     ret = 0
     for i in s:
         ret +=1
     return ret
def solution(scores):
     sum = func_b(scores)
     max, min = func_a(scores)
     return sum - max - min
scores=[100, 50, 40, 30]
print(solution(scores))
#3
def solution(scores):
     count=0
     for s in scores:
         if s <= 200:
             count += 1
     return count

print(solution([20, 45, 78, 100, 300, 250]))

def solution(price, grade):
    answer = 0
    if grade =='S':
        answer = price *1.05
    elif grade =='G':
        answer = price * 1.1
    elif grade == ' V':
        answer = price *1.15


    return answer

print(solution(1000, 'S'))


def solution(number):
    count = 0
    for i in range(1, number+1):
        current = i
        while current != 0:
            unit = current % 10
            if unit == 3 or unit == 6 or unit == 9:
                count += 1
            current //=10
    return current


print(solution(34))
#6
def solution(left_rings):
    answer = 0
    for i in range(len(left_rings)):
        if left_rings[i] <= i:
            for k in range(0, i):
                if left_rings[k] > left_rings[i]:
                    answer += 1
    return answer
print(solution([1,3,45,6]))
#7
def solution(file_info):
    success = 0
    fail = 0
    for f in file_info:
        splited = f.split(",")
        if splited[0] == 'jpeg' and int(splited[2]) <=1000:
            success += 1
        else:
            fail += 1
    return success, fail

print(solution(['jpeg,all.jpg.500','jpeg,all.jpg.500']))

#8
def solution(sentence):
    filtered = []
    for s in sentence:
        if s != '' or s != '.':
            filtered.append(s)
    before = sentence
    filtered.reverse()
    after = ''.join(filtered)
    return before == after
print(solution('sat yoy tas'))

#9
def solution(characters):
    result = [characters[0]]
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:
            result.append(characters[i])
    return ''.join(result)
print(solution('aaaappppllleee'))

#10
def solution(data):
    total = 0
    for i in data:
        total += i
    cnt = 0
    average = total // len(data)
    for i in data:
        if i <= average:
            cnt+=1
    return cnt
print(solution([10, 20, 32, 26, 18, 8]))