""" 1.
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

입출력 예
  s	  return
"abcde"	"c"
"qwer"	"we"
"""

def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]

print(solution("abcde"))
print(solution("qwee"))

""" 2.
문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

입출력 예
arr	        divisor	return
[5, 9, 7, 10]	5	[5, 10]
[2, 36, 1, 3]	1	[1, 2, 3, 36]
[3,2,6]	        10	[-1]
"""

def solution(arr, division):
    answer = [i for i in arr if i % division ==0]

    if not answer:
        return [-1]
    
    answer.sort()
    return answer

print(solution([5,9,7,10], 5))
print(solution([2,36,1,3], 1))
print(solution([3,2,6], 10))

""" 3.
문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

입출력 예
n	return
3	"수박수"
4	"수박수박"
"""

def solution(n):
    answer = ""
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer
print(solution(3))
print(solution(4))

""" 4.
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

입출력 예
N	answer
123	6
987	24
"""

def solution(n):
    return sum(int(i) for i in str(n))

print(solution("123"))
print(solution("987"))

""" 5.
문제 설명
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

예시
입력 
5 3
출력
*****
*****
*****
"""

a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

""" 6.
문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

입출력 예
a	b	return
3	5	12
3	3	3
5	3	12
"""

def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a, b+1):
            answer += i
    else:
        for i in range(b, a+1):
            answer += i
    return answer

print(solution(3,5))
print(solution(3,3))
print(solution(5,3))