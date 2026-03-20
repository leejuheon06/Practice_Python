## LeetCode >> Explore >> Arrays 101
""" 1.
Max Consecutive Ones

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
"""

class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0       
        max_count = 0   # 숫자 1 반복 횟수 초기화

        for i in nums:
            if i == 1:
                count += 1  # 숫자 1을 발견하면 +1
            else:
                max_count = max(count, max_count)   # 1이 반복되는 횟수를 max_count 에 저장
                count = 0   # count 초기화
            
        return max(count, max_count)

""" 2.
Find Numbers with Even Number of Digits

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            # 숫자를 문자열로 변환한 후, 전체 길이가 2로 나누어 떨어지는지 확인
            if len(str(num)) % 2 == 0:
                count += 1  # 나누어 떨어지면 +1
        return count
        