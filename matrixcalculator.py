import numpy as np
print("---MATRIX CALCULATOR---")

def create_matrix():
    while True:
       try:
          row = int(input("Enter no. of rows of matrix: "))
          col = int(input("Enter no. of columns of matrix: "))
          elements = input(f"Enter {row*col} elements (space seperated): ")
          elements_list = [float(x) for x in elements.split()]
          if (len(elements_list) != (row*col)):
              print(f"You must enter excatly {row*col} elements")
              continue
          else:
              matrix = np.matrix(elements_list).reshape(row,col)
              return matrix
       except Exception as e:
          print("Error creating matrix:" , e)
          continue

while True:
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. SCALAR MULTIPLICATION")
    print("4. DOT PRODUCT")
    print("5. TRANSPOSE")
    print("6. DETERMINANT")
    print("7. INVERSE")
    print("8. RANK")
    print("9. TRACE")
    print("10. POWER")
    print("11. EIGENVALUE & EIGENVECTOR")
    print("12. TO CHECK SYMMETRIC & SKEW SYMETRIC")
    print("13. TO CHECK ORTHOGONAL MATRIX")
    print("14. EXIT")

    user_choice = int(input("Enter your choice: "))

    if (user_choice==1):
        try:
           print("Creating First matrix")
           a1 = create_matrix()
           print("Creating Second matrix")
           b1 = create_matrix()
           if a1.shape != b1.shape:
               print("Please ensure that order of both matrices should be same.")
           else:
               print(np.add(a1,b1))
        except Exception as e:
            print("Error: " ,e)

    elif (user_choice==2):
        try:
           print("Creating First matrix")
           a2 = create_matrix()
           print("Creating Second matrix")
           b2 = create_matrix()
           if a1.shape != b1.shape:
               print("Please ensure that order of both matrices should be same.")
           else:
               print(np.subtract(a2,b2))
        except Exception as e:
            print("Error" , e)

    elif (user_choice==3):
        try:
            a3 = create_matrix()
            scalar = float(input("Enter scalar you want to multiply: "))
            print(scalar*a3)
        except Exception as e:
            print(e)

    elif (user_choice==4):
        try:
            print("Creating First matrix")
            a4 = create_matrix()
            print("Creating Second matrix")
            b4 = create_matrix()
            if (a4.shape[1] != b4.shape[0]):
                print("Please follow mulitplication rules of matrix")
            else:
                print(np.dot(a4 , b4))
        except Exception as e:
            print("Error" , e)

    elif (user_choice==5):
        try:
            a5 = create_matrix()
            print(a5.T)
        except Exception as e:
            print(e)

    elif (user_choice==6):
        try:
            a6 = create_matrix()
            print("Determinant of given matrix is: " , np.linalg.det(a6))
        except (np.linalg.LinAlgError,ValueError):
            print("Matrix must be square for determinant")

    elif (user_choice==7):
        try:
            a7 = create_matrix()
            print(np.linalg.inv(a7))
        except (np.linalg.LinAlgError,ValueError):
            print("Matrix must be non-singular for inverse")

    elif (user_choice==8):
        try:
            a8 = create_matrix()
            print("Rank of the give matrix is: " , np.linalg.matrix_rank(a8))
        except Exception as e:
            print(e)

    elif (user_choice==9):
        try:
            a9 = create_matrix()
            print("Trace of the given matrix is: " , np.linalg.trace(a9))
        except Exception as e:
            print(e)

    elif (user_choice==10):
        try:
            a10 = create_matrix()
            power = int(input("Enter power: "))
            result = np.linalg.matrix_power(a10 , power)
            print(result)
        except Exception as e:
            print(e)

    elif (user_choice==11):
        try:
            a11 = create_matrix()
            eigenvalue , eigenvector = np.linalg.eig(a11)
            print("Eigenvalue is: " , eigenvalue)
            print("Eigenvector is: " , eigenvector)
        except (np.linalg.LinAlgError,ValueError):
            print("Matrix must be square to calculate eigenvalue/eigenvector")

    elif (user_choice==12):
        try:
            a12 = create_matrix()
            is_symmetric = np.allclose( a12 , a12.T)
            is_skew_symmetric = np.allclose(a12.T , -a12)
            if (is_symmetric==True):
                print("Result: Given matrix is Symmetric")
            elif (is_skew_symmetric==True):
                print("Result: Given matrix is Skew Symmetric")
            else:
                print("Matrix is neither symmetric nor skew symmetric")
        except Exception as e:
            print(e)
            
    elif (user_choice==13):
        try:
            a13 = create_matrix()
            if a13.shape[0] != a13.shape[1]:
                print("Matrix must be square to check orthogonality")
            else:
                d13 = np.eye(a13.shape[0])
                is_orthogonal = np.allclose(a13 @ a13.T , d13) and np.allclose(a13.T @ a13 , d13)
                if (is_orthogonal==True):
                    print("Result: Given matrix is orthogonal")
                else:
                    print("Result: Given matrix is not orthogonal")
        except Exception as e:
            print(e)

    elif (user_choice == 14):
        print("Program Exited... ")
        break

    else:
        print("You chose wrong input")