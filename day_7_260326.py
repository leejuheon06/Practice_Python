## LeetCode >> Explore >> Arrays 101

# In-Place Operations
""" 1.
Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
"""
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])     # 오른쪽 전체 중 최대값을 현재 인덱스 값으로 할당

        arr[-1] = -1
        return arr

# 위 코드는 매번 오른쪽 전체 인덱스를 확인하기 때문에 속도가 느린 문제점 있음
# 아래 <참고> 처럼 역순으로 한 번에 계산을 끝내는 방식 권장
# <참고>
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -1      # 초기 최댓값 지정

        for i in range(len(arr)-1, -1, -1): # 역순으로 진행
            current_id = arr[i]             # 비교를 위해 현재값 백업
            arr[i] = max_value              # 현재 위치 오른쪽 최댓값 할당
            if current_id > max_value:
                max_value = current_id      # 최댓값 업데이트

        return arr
    

""" 2.
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_point = 0   # 0이 아닌 값 입력 위치
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[current_point] = nums[current_point], nums[i]
                current_point += 1

""" 3.
Sort Array By Parity

Given an integer array nums, move all the even integers 
at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
"""
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        current_point = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[current_point] = nums[current_point], nums[i]
                current_point += 1
                
        return nums
    
# 이전 문제와 같이 투 포인터 방식

