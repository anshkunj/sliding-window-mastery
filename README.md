<p align="center">
  <img src="https://github.com/anshkunj/sliding-window-mastery/blob/d3badf525b12edb39096c559542ef67f912597aa/1768559036081.jpg" alt="Sliding Window Mastery" width="1200">
</p>

<h1 align="center">Sliding Window Mastery</h1>
<p align="center">Curated sliding window algorithm problems with optimized Python solutions and pattern insights 🌊🐍</p>

# 🚀 Sliding Window mastery

A curated collection of **sliding window algorithm problems** covering fixed, variable, and conditional windows. Each solution is optimized, explained with diagrams, and mapped to real-world scenarios like substring processing, analytics, and streaming data.

---

## 🧠 Features
- Well-structured Python solutions  
- Optimized O(n) algorithms (no brute force)  
- Clear explanation of window logic  
- ASCII diagrams showing expansion/shrinking  
- JSON-friendly examples where applicable  

---

## 📂 Repo Structure
```
sliding-window-mastery/  
├── main.py          # FastAPI app & routes  
├── logic.py         # Core algorithm implementations  
├── models.py        # Pydantic request models  
├── .gitignore  
├── requirements.txt  
├── render.yaml  
├── README.md        # Project Overview  
└── LICENSE         # License file (MIT)  
```
---

## 🏗️ How This Repo Works
- logic.py contain logic of all problems  
- Sliding window logic is explained  
- Key patterns highlighted for **real-world applications**  
- Focus on **maximum length / sum / frequency** using efficient O(n) techniques  

---

## 📌 Problem Patterns Covered
- Fixed-length window (max sum, max product)  
- Variable-length window (longest substring/array with constraints)  
- At most K changes / flips / distinct elements  
- Prefix-sum + window combination  
- Handling negative numbers and large inputs  

---

## ⚙️ Installation & Run

1) Clone the repository  
git clone https://github.com/anshkunj/sliding-window-mastery.git  
cd sliding-window-mastery  

2) Install dependencies  
pip install -r requirements.txt  

3) Run the server  
uvicorn main:app --reload  

---

## 🌐 API Documentation

Swagger UI: http://127.0.0.1:8000/docs  

ReDoc: http://127.0.0.1:8000/redoc  

---

## 🌐 Live API

Base URL: https://sliding-window-mastery.onrender.com  
Docs: https://sliding-window-mastery.onrender.com/docs

---

## 🔗 Endpoints – Sliding Window Mastery

This section documents conceptual API-style endpoints mapped directly to the functions
implemented in logic.py using the Sliding Window technique.
Each endpoint includes example input and expected output.

### 1️⃣ Longest Substring Without Repeating Characters
Endpoint: /sliding-window/longest-substring-without-repeating

Input:
s = "abcabcbb"

Output:
length = 3

### 2️⃣ Minimum Size Subarray Sum
Endpoint: /sliding-window/min-size-subarray-sum

Input:
target = 7
nums = [2,3,1,2,4,3]

Output:
minLength = 2

### 3️⃣ Longest Substring with At Most K Distinct Characters
Endpoint: /sliding-window/longest-substring-k-distinct

Input:
s = "eceba"
k = 2

Output:
length = 3

### 4️⃣ Longest Repeating Character Replacement
Endpoint: /sliding-window/character-replacement

Input:
s = "AABABBA"
k = 1

Output:
length = 4

### 5️⃣ Max Consecutive Ones II
Endpoint: /sliding-window/max-consecutive-ones-ii

Input:
nums = [1,0,1,1,0]

Output:
maxLength = 4

### 6️⃣ Contiguous Array
Endpoint: /prefix-sliding/contiguous-array

Input:
nums = [0,1,0,1]

Output:
maxLength = 4

### 7️⃣ Subarray Sum Equals K
Endpoint: /prefix-sliding/subarray-sum-k

Input:
nums = [1,2,3]
k = 3

Output:
count = 2

### 8️⃣ Fruit Into Baskets
Endpoint: /sliding-window/fruit-into-baskets

Input:
fruits = [1,2,1]

Output:
maxFruits = 3

### 9️⃣ Max Consecutive Ones III
Endpoint: /sliding-window/max-consecutive-ones-iii

Input:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

Output:
maxLength = 6

### 1️⃣0️⃣ Subarrays With K Different Integers
Endpoint: /sliding-window/subarrays-with-k-distinct

Input:
nums = [1,2,1,2,3]
k = 2

Output:
count = 7

### 1️⃣1️⃣ Shortest Subarray With Sum At Least K
Endpoint: /sliding-window/shortest-subarray-at-least-k

Input:
nums = [2,-1,2]
k = 3

Output:
length = 3

### 1️⃣2️⃣ Binary Subarrays With Sum
Endpoint: /prefix-sliding/binary-subarrays-with-sum

Input:
nums = [1,0,1,0,1]
goal = 2

Output:
count = 4

---

## 🚧 Edge Cases Handled
- Empty arrays / strings  
- Large input sizes (up to 10^5)  
- Negative numbers  
- Exact vs at most K changes  

---

## 🛠️ Tech Stack
- Python 3.x  
- Standard libraries (`collections`, `itertools`)  
- Optional: Jupyter Notebook for visualization  

---

## 📄 Licence
MIT Licence  

---

## 🤝 Contributing
Contributors are welcome!  
• Add new sliding window problems  
• Improve explanations  
• Optimise exists code  

---

## 👤 Author
**anshkunj**  
GitHub: https://github.com/anshkunj  
Fiverr: https://www.fiverr.com/s/xX9mNXB  
LinkedIn: https://linkedin.com/in/anshkunj 

---

## ⭐ Support
If you find this repo helpful, give it a star ⭐  
It motivates me to create more real-world algorithm projects 🚀  

---

## 🔹 Note
This repo is regularly updated with new sliding window problems and explanations.
