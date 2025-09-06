# Matrix Calculator (Python + NumPy)

A command-line **Matrix Calculator** built with **Python** and **NumPy** that allows users to perform various matrix operations such as addition, subtraction, multiplication, determinant, inverse, eigenvalues, symmetry checks, and more.

---

## 🚀 Features
This calculator supports the following operations:

1. **Addition** ➝ Adds two matrices of the same order.  
2. **Subtraction** ➝ Subtracts two matrices of the same order.  
3. **Scalar Multiplication** ➝ Multiplies a matrix by a scalar value.  
4. **Dot Product** ➝ Performs matrix multiplication (rules of multiplication apply).  
5. **Transpose** ➝ Returns the transpose of a matrix.  
6. **Determinant** ➝ Computes determinant (only for square matrices).  
7. **Inverse** ➝ Finds the inverse of a non-singular square matrix.  
8. **Rank** ➝ Calculates the rank of a matrix.  
9. **Trace** ➝ Computes the sum of diagonal elements (square matrices).  
10. **Power** ➝ Raises a square matrix to an integer power.  
11. **Eigenvalues & Eigenvectors** ➝ Finds eigenvalues and eigenvectors (square matrices).  
12. **Symmetric & Skew-Symmetric Check** ➝ Identifies whether the matrix is symmetric, skew-symmetric, or neither.  
13. **Orthogonal Matrix Check** ➝ Verifies if a square matrix is orthogonal.  
14. **Exit** ➝ Terminates the program.  

---

## 🛠️ Requirements
- Python 3.x  
- NumPy library  

Install NumPy if not already installed:
```bash
pip install numpy
```

---

## ▶️ How to Run
1. Clone or download this repository.  
2. Save the code in a file, e.g., `matrix_calculator.py`.  
3. Run the program in your terminal:
```bash
python matrix_calculator.py
```
4. Follow the on-screen menu to choose an operation.  

---

## 📖 Usage Examples

### 1️⃣ Matrix Addition
```
Enter your choice: 1
Creating First matrix
Enter no. of rows of matrix: 2
Enter no. of columns of matrix: 2
Enter 4 values (space seperated): 1 2 3 4
Creating Second matrix
Enter no. of rows of matrix: 2
Enter no. of columns of matrix: 2
Enter 4 values (space seperated): 5 6 7 8

[[ 6.  8.]
 [10. 12.]]
```

### 2️⃣ Determinant
```
Enter your choice: 6
Enter no. of rows of matrix: 2
Enter no. of columns of matrix: 2
Enter 4 values (space seperated): 1 2 3 4

Determinant of given matrix is: -2.0000000000000004
```

### 3️⃣ Eigenvalues & Eigenvectors
```
Enter your choice: 11
Enter no. of rows of matrix: 2
Enter no. of columns of matrix: 2
Enter 4 values (space seperated): 2 0 0 3

Eigenvalue is:  [2. 3.]
Eigenvector is:  
[[1. 0.]
 [0. 1.]]
```

### 4️⃣ Symmetric / Skew-Symmetric Check
```
Enter your choice: 12
Enter no. of rows of matrix: 2
Enter no. of columns of matrix: 2
Enter 4 values (space seperated): 1 7 7 4

Result: Given matrix is Symmetric
```

### 5️⃣ Orthogonal Check
```
Enter your choice: 13
Enter no. of rows of matrix: 2
Enter no. of columns of matrix: 2
Enter 4 values (space seperated): 0 1 -1 0

Result: Given matrix is orthogonal
```

---

## ⚠️ Error Handling
- Addition/Subtraction requires matrices of the **same order**.  
- Determinant/Inverse/Eigenvalue/Eigenvector require a **square matrix**.  
- Inverse requires the matrix to be **non-singular**.  
- Dot product requires **columns of first = rows of second**.  
- Orthogonality check requires a **square matrix**.  
- Program prevents invalid inputs with proper error messages.  

---

## 📌 Future Improvements
- Add support for complex matrices.  
- GUI version using Tkinter or PyQt.  
- Save matrices to file and reload them.  

---

## 👨‍💻 Author
Developed as a Python + NumPy project for learning matrix operations.  
Feel free to fork and improve! 🚀
