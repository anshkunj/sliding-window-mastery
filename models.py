"""
models.py
Contains Pydantic models for API requests
"""

from pydantic import BaseModel
from typing import List

# Generic input for string + k (character replacement, k distinct, etc.)
class StringKInput(BaseModel):
    s: str
    k: int

# Generic input for integer array + k
class ArrayKInput(BaseModel):
    nums: List[int]
    k: int

# Generic input for integer array + target (sum related)
class ArrayTargetInput(BaseModel):
    nums: List[int]
    target: int

# For Fruit Basket problem
class FruitsInput(BaseModel):
    fruits: List[int]

# For Binary Array + Goal
class BinaryGoalInput(BaseModel):
    nums: List[int]
    goal: int