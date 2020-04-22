#Harus menginstal libary numpy
import numpy as np
import perhitungan

#Invers Matriks
def inv_m22(x):
    det = np.linalg.det(x).astype(int)
    if(det != 0):
        print("\nInvers Matriks :")
        print("[", x[1][1],"/",det,"    ", -x[0][1],"/",det, "]")
        print("[", -x[1][0],"/",det,"    ", x[0][0],"/",det, "]")
    else:
        print("\nTidak memiliki Invers")

def inv_m33(x):
    det = np.linalg.det(x)
    if(det != 0):
        z = np.linalg.inv(x)
        print("\nInvers Matriks :\n", z)
    else:
        print("\nTidak memiliki Invers")

#Error
def error():
    print("\nMasukan SALAH !!!")

print("Tugas Modul 4 Kelompok 45")
print("- Syahrul Ramadhan / 21120119120011")
print("- Timothy Bagaskara / 21120119130088")
print("---PROGRAM KALKULATOR MATRIKS---\n")
print("Ukuran Matriks")
print("1. Matriks 2x2")
print("2. Matriks 3x3")
print("-" * 14)
pil = int(input(">> "))
if(pil == 1):
    v = 2
    print(" ")
    mtx = [[int(input("Masukan elemen[{},{}] : ".format(r + 1, c + 1))) for c in range(v)] for r in range(v)]
    print("Matriks :")
    for s in mtx:
        print(s)
    print("\nPilih Operasi :")
    print("1. Determinan Matriks")
    print("2. Invers Matriks")
    print("3. Penjumlahan/Pengurangan 2 Matriks")
    print("4. Perkalian 2 Matriks")
    print("-" * 22)
    pil1 = int(input(">> "))
    if(pil1 == 1):
        matriks = perhitungan.operasi(mtx)
    elif(pil1 == 2):
        inv_m22(mtx)
    elif(pil1 == 3):
        matriks = perhitungan.operasi(0)
        matriks.plusminus(mtx, v)
    elif(pil1 == 4):
        matriks = perhitungan.operasi(0)
        matriks.kali(mtx, v)
    else :
        error()

elif(pil == 2):
    v = 3
    print(" ")
    mtx = [[int(input("Masukan elemen[{},{}] : ".format(r + 1, c + 1))) for c in range(v)] for r in range(v)]
    print("Matriks :")
    for t in mtx:
        print(t)
    print("\nPilih Operasi :")
    print("1. Determinan Matriks")
    print("2. Invers Matriks")
    print("3. Penjumlahan/Pengurangan 2 Matriks")
    print("4. Perkalian 2 Matriks")
    print("-" * 22)
    pil1 = int(input(">> "))
    if(pil1 == 1):
        matriks = perhitungan.operasi(mtx)
    elif(pil1 == 2):
        inv_m33(mtx)
    elif(pil1 == 3):
        matriks = perhitungan.operasi(0)
        matriks.plusminus(mtx, v)
    elif(pil1 == 4):
        matriks = perhitungan.operasi(0)
        matriks.kali(mtx, v)
    else :
        error()

else:
    error()