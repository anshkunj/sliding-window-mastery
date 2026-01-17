"""
logic.py
Contains all Sliding Window Mastery problem solutions.
Each function is standalone and can be imported in main.py
"""

from collections import defaultdict
from typing import List

# 1️⃣ Longest Substring Without Repeating Characters
def length_of_longest_substring(s: str) -> int:
    char_index = {}
    l = 0
    max_len = 0
    for r, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= l:
            l = char_index[ch] + 1
        char_index[ch] = r
        max_len = max(max_len, r - l + 1)
    return max_len

# 2️⃣ Minimum Size Subarray Sum
def min_subarray_len(target: int, nums: List[int]) -> int:
    l = 0
    total = 0
    min_len = float('inf')
    for r, num in enumerate(nums):
        total += num
        while total >= target:
            min_len = min(min_len, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if min_len == float('inf') else min_len

# 3️⃣ Longest Substring with At Most K Distinct Characters
def length_of_longest_k_distinct(s: str, k: int) -> int:
    freq = defaultdict(int)
    l = 0
    max_len = 0
    for r, ch in enumerate(s):
        freq[ch] += 1
        while len(freq) > k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

# 4️⃣ Longest Repeating Character Replacement
def character_replacement(s: str, k: int) -> int:
    freq = defaultdict(int)
    l = 0
    max_len = 0
    max_freq = 0
    for r, ch in enumerate(s):
        freq[ch] += 1
        max_freq = max(max_freq, freq[ch])
        while (r - l + 1) - max_freq > k:
            freq[s[l]] -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

# 5️⃣ Max Consecutive Ones II
def find_max_consecutive_ones(nums: List[int]) -> int:
    l = 0
    k = 1  # allowed flip
    max_len = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            k -= 1
        while k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

# 6️⃣ Contiguous Array
def find_max_length(nums: List[int]) -> int:
    prefix_map = {0: -1}
    max_len = 0
    count = 0
    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if count in prefix_map:
            max_len = max(max_len, i - prefix_map[count])
        else:
            prefix_map[count] = i
    return max_len

# 7️⃣ Subarray Sum Equals K
def subarray_sum(nums: List[int], k: int) -> int:
    count = 0
    prefix = {0:1}
    total = 0
    for num in nums:
        total += num
        count += prefix.get(total - k, 0)
        prefix[total] = prefix.get(total, 0) + 1
    return count

# 8️⃣ Fruit Into Baskets
def total_fruit(fruits: List[int]) -> int:
    freq = defaultdict(int)
    l = 0
    max_len = 0
    for r, f in enumerate(fruits):
        freq[f] += 1
        while len(freq) > 2:
            freq[fruits[l]] -= 1
            if freq[fruits[l]] == 0:
                del freq[fruits[l]]
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

# 9️⃣ Max Consecutive Ones III
def longest_ones(nums: List[int], k: int) -> int:
    l = 0
    max_len = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            k -= 1
        while k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

# 1️⃣0️⃣ Subarrays with K Different Integers
def subarrays_with_k_distinct(nums: List[int], k: int) -> int:
    # Helper for at most K
    def at_most(k):
        freq = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(nums)):
            if freq[nums[r]] == 0:
                k -= 1
            freq[nums[r]] += 1
            while k < 0:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    k += 1
                l += 1
            res += r - l + 1
        return res
    return at_most(k) - at_most(k-1)

# 1️⃣1️⃣ Shortest Subarray with Sum at Least K (Sliding Window Variant)
def shortest_subarray(nums: List[int], k: int) -> int:
    from collections import deque
    n = len(nums)
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    res = n + 1
    dq = deque()
    for i, p in enumerate(prefix):
        while dq and p - prefix[dq[0]] >= k:
            res = min(res, i - dq.popleft())
        while dq and p <= prefix[dq[-1]]:
            dq.pop()
        dq.append(i)
    return res if res <= n else -1

# 1️⃣2️⃣ Binary Subarrays With Sum
def num_subarrays_with_sum(nums: List[int], goal: int) -> int:
    prefix = {0:1}
    total = 0
    count = 0
    for num in nums:
        total += num
        count += prefix.get(total - goal, 0)
        prefix[total] = prefix.get(total, 0) + 1
    return count