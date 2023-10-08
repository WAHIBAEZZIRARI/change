A = int (input("Veuillez saisir la valeur de A : "))
B = int (input("Veuillez saisir la valeur de B : "))
if A*B > 0 :
    A, B=B, A
else:
    C = A + B
    D = A* B
    A = C
    B=  D
print("La nouvelle valeur de A est: ",A)
print("La nouvelle valeur de B est: ",B)