## LeetCode >> Explore >> Arrays 101

# Searching for items in an Array
""" 1.
Check If N and Its Double Exist

iven an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
"""
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                # i와 j가 다르고, 한 쪽이 다른 쪽의 2배
                if i != j and arr[i] == 2 * arr[j]:
                    return True
                            
        return False
    
## 참고 Hash Set 사용
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for num in arr:
            # 현재 숫자의 2배가 이미 있거나, 
            # 현재 숫자가 짝수이면서 그 절반이 이미 있는지 확인
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # 확인 후 현재 숫자를 셋에 추가
            seen.add(num)
        return False
    
# 지나온 숫자를 기억해두고 비교
# 메모리를 상대적 더 많이 사용하지만 속도는 훨씬 빠름

""" 2.
Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        # 최소 3개 이상의 요소
        if n < 3:
            return False
        
        i = 0
        # 다음 숫자가 더 클 때까지만 이동
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
            
        # 정상이 시작점(i=0)이거나 끝점(i=n-1)이면 산이 아님
        if i == 0 or i == n - 1:
            return False
            
        # 다음 숫자가 더 작을 때까지만 이동
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
            
        # 끝까지 도달했다면 True, 중간에 멈췄거나 평지가 있었다면 False
        return i == n - 1
