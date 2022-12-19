import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import json

x= np.array([10,20,30,40,50,60])
y= np.array([12,7,9,5,5,10])


plt.title("Jumlah Mahasiswa Pada Mata Kuliah Pilihan")
plt.xlabel("Nilai")
plt.ylabel("Banyak Mahasiswa")
plt.axis([0,70,0,13])
plt.plot(x,y, marker="o", color="green")
plt.grid()
plt.show()