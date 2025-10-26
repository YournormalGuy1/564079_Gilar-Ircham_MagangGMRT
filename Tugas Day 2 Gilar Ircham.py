# File untuk menghitung Forward kinematics
# Gilar Ircham Wibisana


import math as cm
import matplotlib.pyplot as ml

# Tentukan nilai
s1 = cm.radians(40)           # 40 Derajat
s2 = cm.radians(30)           # 30 Derajat 
gab = s1 + s2                 # Nilai derajat gabungan

re1 = 79                      # Panjang dari femur
re2 = 22                      # Panjang dari Tibia

x1 = re1 * cm.cos(s1)         # Mencari masing masing koordinat yg garis lurus (koordinat pertama)
y1 = re1 * cm.sin(s1)         # Mencari masing masing koordinat yg garis lurus (koordinat pertama)

x2 = re1 * cm.cos(s1) + re2 * cm.cos(gab)          # ini mencari endpoint dimana si tangnan tersebut meanaikkan ke x berapa dan y berapa
y2 = re1 * cm.sin(s1) + re2 * cm.sin(gab)          # ini mencari endpoint dimana si tangnan tersebut meanaikkan ke x berapa dan y berapa

faktor =  cm.sqrt(x2**2 + y2**2)                   # Mencari panjang vektor seperti biasa

#nilai x dan y awal
x0 = 0
y0 = 0

list_x = [x0,x1, x2]         # Memasukkan masing masing ke list agar bisa didata              
list_y = [y0,y1, y2]         # Memasukkan masing masing ke list agar bisa didata

print(f"x2 adalah = {x2:.2f}\nY2 adalah = {y2:.2f}\nDan faktornya adalah {faktor:.2f}" )            # menunjukkan output perhitungan tadi

ml.figure                                                        # canvas kosong
ml.plot(list_x, list_y, '-o', linewidth=4, markersize=9)         # Untuk menampilkan di matplotlibnya, '-o' berartti kasih line dan o disetiap x dan y nya
ml.axis('equal')
ml.xlabel("X")
ml.ylabel("Y")

ml.show()
