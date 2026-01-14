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

sliding-window-mastery/  
├── README.md                  # This file  
├── 3_longest_substring.py     # Variable window, unique chars  
├── 424_longest_repeat_char.py # Max freq, at most K replacements  
├── 487_max_consec_ones_II.py  
├── 525_contiguous_array.py  
├── 560_subarray_sum_equals_k.py  
├── 904_fruit_into_baskets.py  
├── 1004_max_consec_ones_III.py  
└── ... (add more sliding window problems)  

---

## 🏗️ How This Repo Works
- Each `.py` file contains a single problem solution  
- Sliding window logic is explained in **comments + diagrams**  
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
cd Subarray-API  

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

Base URL:  
https://sliding-window-mastery.onrender.com  
Docs:  
https://sliding-window-mastery.onrender.com/docs

---

## 🧪 Example (Longest Repeating Character Replacement)

s = "AABABBA"  
k = 1  
print(longest_repeating_char_replacement(s, k))  
# Output: 4  

- Tracks window counts  
- Shrinks window when replacements needed > k  
- Uses **stale max frequency trick** for O(n) solution  

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

## 👤 Author
**anshkunj**  
GitHub: https://github.com/anshkunj  
Fiverr: https://www.fiverr.com/s/xX9mNXB  

---

## ⭐ Support
If you find this repo helpful, give it a star ⭐  
It motivates me to create more real-world algorithm projects 🚀  

---

## 🔹 Note
This repo is regularly updated with new sliding window problems and explanations.