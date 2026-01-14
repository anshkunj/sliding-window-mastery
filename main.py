"""
main.py
FastAPI app for Sliding Window Mastery Repo
All 12 problems exposed as API endpoints
"""

from fastapi import FastAPI
from logic import *
from models import *

app = FastAPI(title="Sliding Window Mastery API")

@app.get("/")
def root():
    return {"message": "Welcome to Sliding Window Mastery API!"}


# 1️⃣ Longest Substring Without Repeating Characters
@app.post("/longest_substring_without_repeating")
def api_longest_substring_post(input: StringKInput):
    return {"result": length_of_longest_substring(input.s)}

@app.get("/longest_substring_without_repeating")
def api_longest_substring_get(s: str):
    return {"result": length_of_longest_substring(s)}


# 2️⃣ Minimum Size Subarray Sum
@app.post("/min_size_subarray_sum")
def api_min_subarray_post(input: ArrayTargetInput):
    return {"result": min_subarray_len(input.target, input.nums)}

@app.get("/min_size_subarray_sum")
def api_min_subarray_get(nums: str, target: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": min_subarray_len(target, nums_list)}


# 3️⃣ Longest Substring With At Most K Distinct Characters
@app.post("/longest_k_distinct")
def api_longest_k_post(input: StringKInput):
    return {"result": length_of_longest_k_distinct(input.s, input.k)}

@app.get("/longest_k_distinct")
def api_longest_k_get(s: str, k: int):
    return {"result": length_of_longest_k_distinct(s, k)}


# 4️⃣ Longest Repeating Character Replacement
@app.post("/longest_repeating_char_replacement")
def api_char_replacement_post(input: StringKInput):
    return {"result": character_replacement(input.s, input.k)}

@app.get("/longest_repeating_char_replacement")
def api_char_replacement_get(s: str, k: int):
    return {"result": character_replacement(s, k)}


# 5️⃣ Max Consecutive Ones II
@app.post("/max_consecutive_ones_ii")
def api_max_ones_ii_post(input: ArrayKInput):
    return {"result": find_max_consecutive_ones(input.nums)}

@app.get("/max_consecutive_ones_ii")
def api_max_ones_ii_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": find_max_consecutive_ones(nums_list)}


# 6️⃣ Contiguous Array
@app.post("/contiguous_array")
def api_contiguous_array_post(input: ArrayKInput):
    return {"result": find_max_length(input.nums)}

@app.get("/contiguous_array")
def api_contiguous_array_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": find_max_length(nums_list)}


# 7️⃣ Subarray Sum Equals K
@app.post("/subarray_sum_equals_k")
def api_subarray_sum_post(input: ArrayTargetInput):
    return {"result": subarray_sum(input.nums, input.target)}

@app.get("/subarray_sum_equals_k")
def api_subarray_sum_get(nums: str, target: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": subarray_sum(nums_list, target)}


# 8️⃣ Fruit Into Baskets
@app.post("/fruit_into_baskets")
def api_fruit_baskets_post(input: FruitsInput):
    return {"result": total_fruit(input.fruits)}

@app.get("/fruit_into_baskets")
def api_fruit_baskets_get(fruits: str):
    fruits_list = [int(x) for x in fruits.split(",")]
    return {"result": total_fruit(fruits_list)}


# 9️⃣ Max Consecutive Ones III
@app.post("/max_consecutive_ones_iii")
def api_max_ones_iii_post(input: ArrayKInput):
    return {"result": longest_ones(input.nums, input.k)}

@app.get("/max_consecutive_ones_iii")
def api_max_ones_iii_get(nums: str, k: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": longest_ones(nums_list, k)}


# 1️⃣0️⃣ Subarrays With K Different Integers
@app.post("/subarrays_k_distinct")
def api_subarrays_k_post(input: ArrayKInput):
    return {"result": subarrays_with_k_distinct(input.nums, input.k)}

@app.get("/subarrays_k_distinct")
def api_subarrays_k_get(nums: str, k: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": subarrays_with_k_distinct(nums_list, k)}


# 1️⃣1️⃣ Shortest Subarray With Sum At Least K
@app.post("/shortest_subarray_sum_k")
def api_shortest_subarray_post(input: ArrayTargetInput):
    return {"result": shortest_subarray(input.nums, input.target)}

@app.get("/shortest_subarray_sum_k")
def api_shortest_subarray_get(nums: str, target: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": shortest_subarray(nums_list, target)}


# 1️⃣2️⃣ Binary Subarrays With Sum
@app.post("/binary_subarrays_with_sum")
def api_binary_subarrays_post(input: BinaryGoalInput):
    return {"result": num_subarrays_with_sum(input.nums, input.goal)}

@app.get("/binary_subarrays_with_sum")
def api_binary_subarrays_get(nums: str, goal: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": num_subarrays_with_sum(nums_list, goal)}