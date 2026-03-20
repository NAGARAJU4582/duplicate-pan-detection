# duplicate-pan-detection


## 📌 Objective
This project identifies duplicate PAN numbers from a dataset of application records.

---

## 🧠 Problem
Duplicate records can affect data validation and model evaluation.  
The goal is to detect applications that share the same PAN number.

---

## 🛠️ Approach
- Clean PAN values by removing extra spaces  
- Group records based on PAN numbers  
- Identify PANs that appear more than once  
- Collect corresponding application IDs  

---

## 📥 Input
A list of application records containing:
- Application ID  
- PAN number  

---

## 📤 Output
A list of application IDs that have duplicate PAN numbers.

---

## ⚙️ Methodology
- Use a dictionary to group PAN values  
- Check for duplicate occurrences  
- Maintain original order of records  
- Return application IDs with duplicate PANs  

---

## ✅ Additional Checks
- Validate PAN format  
- Convert PAN to uppercase  
- Handle missing or null values  
- Ensure uniqueness of application IDs  

---

## 🚀 Usage
Run the script using Python to detect duplicate PAN records.

---
