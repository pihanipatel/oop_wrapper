# 📘 Employee Management System (Python OOP)

## 🚀 Overview
This project is a simple **Employee Management System** built using **Object-Oriented Programming (OOP)** concepts in Python.

It demonstrates:
- Classes & Objects
- Inheritance
- Encapsulation
- Method Overriding
- Basic CLI interaction

---

## 🧩 Classes Included

- 👤 Person  
- 🧑‍💼 Employee  
- 👨‍💻 Developer (inherits Employee)  
- 🧑‍💼 Manager (inherits Employee)

---

## 🔄 Flowchart

```mermaid
flowchart TD
    A[Start] --> B[User Chooses Option]
    B -->|1| C[Create Person]
    B -->|2| D[Create Employee]
    B -->|3| E[Create Manager]
    B -->|4| F[Show Details]
    B -->|5| G[Update Salary & ID]
    B -->|6| H[Delete Employee]
    B -->|7| I[Create Developer]
    B -->|8| J[Exit]

    C --> B
    D --> B
    E --> B
    F --> B
    G --> B
    H --> B
    I --> B
    J --> K[End]
```

---

## 📸 Screenshot

_(Attach your screenshot here)_  

Example:
![App Screenshot](screenshot.png)

---

## 💻 How to Run

1. Make sure Python is installed  
2. Run the script:
```bash
python OOP_Wrapper.py
```

---

## ✨ Features

- Interactive menu system 🎯  
- Multiple roles (Employee, Manager, Developer) 👥  
- Data display and updates 🔄  
- Object lifecycle demonstration (constructor & destructor) ⚙️  

---

## 📌 Notes

- This is a learning project for understanding OOP concepts  
- Some parts can be improved (validation, structure, storage)

---

## ❤️ Made for Learning
Keep exploring Python and OOP!
