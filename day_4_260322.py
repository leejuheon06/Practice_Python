## LeetCode >> Explore >> Arrays 101
""" 3.
Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            answer.append(i**2)
        answer.sort()
        return answer

""" 4.
Duplicate Zeros

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. 
Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, 
the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, 
the input array is modified to: [1,2,3]
"""

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0) # 0 삽입
                arr.pop()        # 마지막 요소 제거 (길이 유지)
                i += 1           # 복제된 0을 건너뛰기 위해 추가 이동
            i += 1

""" 5.
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. 
The 0 is only there to ensure the merge result can fit in nums1.
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1      # nums1의 숫자 끝
        j = n - 1      # nums2의 숫자 끝
        k = m + n - 1  # nums1의 진짜 맨 마지막 칸
        
        # 뒤부터 채우기
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# 과거 내역 commit 수정 연습
# git rebase -i HEAD~5
# git add <파일명>
# git commit --amend -m "TEXT"
# git rebase --continue
# git push origin main --force



    