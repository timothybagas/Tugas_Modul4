#Harus menginstal libary numpy
import numpy as np

class operasi :
    #Operasi Matriks
    def __init__(self, x):
        if(x != 0):    
            self.det = np.linalg.det(x).astype(int)
            print("\nDeterminan : ", self.det)
        else :
            print(" ")

    def plusminus(self, x, v):
        print("a) Penjumlahan")
        print("b) Pengurangan")
        pil2 = input("Pilih(a/b) : ")
        print("\nElemen matriks ke-2")
        mtx2 = [[int(input("Masukan elemen[{},{}] : ".format(m + 1, n + 1))) for n in range(v)] for m in range(v)]
        hsl = [[0 for n in range(v)] for m in range(v)]
        for i in range(v):
            for j in range(v):
                if(pil2 == "a"):
                    hsl[i][j] = x[i][j] + mtx2[i][j]
                elif(pil2 == "b"):
                    hsl[i][j] = x[i][j] - mtx2[i][j]
        print("\nHasil :")
        for r in hsl:
            print(r)
        
    def kali(self, x, v):
            print("Elemen matriks ke-2")
            mtxmult = [[int(input("Masukan elemen[{},{}] : ".format(m + 1, n + 1))) for n in range(v)] for m in range(v)]
            mult = [[0 for n in range(v)] for m in range(v)]
            for i in range(len(x)):
                for j in range(len(mtxmult[0])):
                    for k in range(len(mtxmult)):
                        mult[i][j] += x[i][k] * mtxmult[k][j]
            print("\nHasil :")
            for r in mult:
                print(r)