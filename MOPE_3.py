from random import randint
import math
from numpy import linalg

mas_y = []
ser_func_vid = []
mas_a = []
mas_mx = []
s =[]

x1_min = -10 + 1 # додав одиницю для того, щоб отримати ціле число для генерації масиву
x1_max = 50 - 1 # відняв одиницю для того, щоб отримати ціле число для генерації масиву

x2_min = 25
x2_max = 65

x3_min = -10
x3_max = 15

n = 4
m = 3

mas_x = [[x1_min, x2_min, x3_min],
		 [x1_min, x2_max, x3_max],
		 [x1_max, x2_min, x2_max],
		 [x1_max, x2_max, x3_min]]

# for i in range(n):
# 	print(mas_x[i])

y_min = 200 + (x1_min + x2_min + x3_min) / 3
y_max = 200 + (x1_max + x2_max + x3_max) / 3

print("Ymin = {}".format(y_min))
print("Ymax = {}".format(y_max) + "\n")

for i in range(n):
	b = []
	mas_y.append(b)
	for j in range(m):
		b.append(randint(y_min, y_max))
	mas_y.append(b)
	ser_func_vid.append(sum(b) / 3)


print("Матриця:")
for i in range(n):
	print(mas_y[i])

print("\n" + "Середні значення функції відгуку y: ")
for i in range(n):
	print(ser_func_vid[i])

print("\n" + "Середні значення функції відгуку mx: ")
mx1 = (mas_x[0][0] + mas_x[1][0] + mas_x[2][0] + mas_x[3][0]) / 4
mx2 = (mas_x[0][1] + mas_x[1][1] + mas_x[2][1] + mas_x[3][1]) / 4
mx3 = (mas_x[0][2] + mas_x[1][2] + mas_x[2][2] + mas_x[3][2]) / 4
print("mx1: {}".format(mx1))
print("mx2: {}".format(mx2))
print("mx3: {}".format(mx3) + "\n")

my = sum(ser_func_vid) / 4 
print("Середнє значення функції відгуку my: {}".format(my) + "\n")

print("Числа для знаходження коефіціентів регресійного рівняння:")

a1 = (mas_x[0][0] * ser_func_vid[0] + mas_x[1][0] * ser_func_vid[1] + mas_x[2][0] * ser_func_vid[2] + mas_x[3][0] * ser_func_vid[3]) / 4
a2 = (mas_x[0][1] * ser_func_vid[0] + mas_x[1][1] * ser_func_vid[1] + mas_x[2][1] * ser_func_vid[2] + mas_x[3][1] * ser_func_vid[3]) / 4
a3 = (mas_x[0][2] * ser_func_vid[0] + mas_x[1][2] * ser_func_vid[1] + mas_x[2][2] * ser_func_vid[2] + mas_x[3][2] * ser_func_vid[3]) / 4

print("a1: {}".format(a1))
print("a2: {}".format(a2))
print("a3: {}".format(a3))

a11 = (math.pow(mas_x[0][0], 2) + math.pow(mas_x[1][0], 2) + math.pow(mas_x[2][0], 2) + math.pow(mas_x[3][0], 2)) / 4
a22 = (math.pow(mas_x[0][1], 2) + math.pow(mas_x[1][1], 2) + math.pow(mas_x[2][1], 2) + math.pow(mas_x[3][1], 2)) / 4
a33 = (math.pow(mas_x[0][2], 2) + math.pow(mas_x[1][2], 2) + math.pow(mas_x[2][2], 2) + math.pow(mas_x[3][2], 2)) / 4

print("a11: {}".format(a11))
print("a22: {}".format(a22))
print("a33: {}".format(a33))

a12 = (mas_x[0][0]*mas_x[0][1] + mas_x[1][0]*mas_x[1][1] + mas_x[2][0]*mas_x[2][1] + mas_x[3][0]*mas_x[3][1]) / 4
a13 = (mas_x[0][0]*mas_x[0][2] + mas_x[1][0]*mas_x[1][2] + mas_x[2][0]*mas_x[2][2] + mas_x[3][0]*mas_x[3][2]) / 4
a23 = (mas_x[0][1]*mas_x[0][2] + mas_x[1][1]*mas_x[1][2] + mas_x[2][1]*mas_x[2][2] + mas_x[3][1]*mas_x[3][2]) / 4 

print("a12: {}".format(a12))
print("a23: {}".format(a23))
print("a13: {}".format(a13) + "\n")

mas_znam = [[1, mx1, mx2, mx3],
			 [mx1, a11, a12, a13],
			 [mx2, a12, a22, a23],
			 [mx3, a13, a23, a33]]

mas_chis0 = [[my, mx1, mx2, mx3],
		 	 [a1, a11, a12, a13],
		 	 [a2, a12, a22, a23],
		 	 [a3, a13, a23, a33]]

mas_chis1 = [[1, my, mx2, mx3],
		 	 [mx1, a1, a12, a13],
		 	 [mx2, a2, a22, a23],
		 	 [mx3, a3, a23, a33]]
		 
mas_chis2 = [[1, mx1, my, mx3],
		 	 [mx1, a11, a1, a13],
		 	 [mx2, a12, a2, a23],
		 	 [mx3, a13, a3, a33]]

mas_chis3 = [[1, mx1, mx2, my],
			 [mx1, a11, a12, a1],
			 [mx2, a12, a22, a2],
			 [mx3, a13, a23, a3]]

znam = linalg.det(mas_znam)
chis0 = linalg.det(mas_chis0)
chis1 = linalg.det(mas_chis1)
chis2 = linalg.det(mas_chis2)
chis3 = linalg.det(mas_chis3)

b0 = chis0 / znam
b1 = chis1 / znam
b2 = chis2 / znam
b3 = chis3 / znam

print("Коефіціенти b0, b1, b2 та b3:")
print("b0: {}".format(b0))
print("b1: {}".format(b1))
print("b2: {}".format(b2))
print("b3: {}".format(b3) + "\n")

print("Перевірка:")
y1 = b0 + b1 * mas_x[0][0] + b2 * mas_x[0][1] + b3 * mas_x[0][2]
y2 = b0 + b1 * mas_x[1][0] + b2 * mas_x[1][1] + b3 * mas_x[1][2]
y3 = b0 + b1 * mas_x[2][0] + b2 * mas_x[2][1] + b3 * mas_x[2][2]
y4 = b0 + b1 * mas_x[3][0] + b2 * mas_x[3][1] + b3 * mas_x[3][2]
print("y1: {}".format(y1))
print("y2: {}".format(y2))
print("y3: {}".format(y3))
print("y4: {}".format(y4) + "\n")

print("Перевірка одноріності за критерієм Кохрена:")
print("Дисперсії по рядках:")
s_y1 = ((mas_y[0][0] - ser_func_vid[0])**2 + (mas_y[0][1] - ser_func_vid[0])**2 + (mas_y[0][2] - ser_func_vid[0])**2) / 3
s_y2 = ((mas_y[1][0] - ser_func_vid[1])**2 + (mas_y[1][1] - ser_func_vid[1])**2 + (mas_y[1][2] - ser_func_vid[1])**2) / 3
s_y3 = ((mas_y[2][0] - ser_func_vid[2])**2 + (mas_y[2][1] - ser_func_vid[2])**2 + (mas_y[2][2] - ser_func_vid[2])**2) / 3
s_y4 = ((mas_y[3][0] - ser_func_vid[3])**2 + (mas_y[3][1] - ser_func_vid[3])**2 + (mas_y[3][2] - ser_func_vid[3])**2) / 3

s.append(s_y1)
s.append(s_y2)
s.append(s_y3)
s.append(s_y4)

print("s_y1: {}".format(s_y1))
print("s_y2: {}".format(s_y2))
print("s_y3: {}".format(s_y3))
print("s_y4: {}".format(s_y4) + "\n")

gp = max(s) / sum(s)
gt = 0.7679
print("Отримане значення Gp: {}".format(gp))

if gp < gt:
	print("Дисперсія однорідна.\n")
else:
	print("Дисперсія неоднорідна.\n")

print("Перевірка значимості коефіціентів за критерієм Стьюдента:")

s_b = sum(s) / 4
s_beta = math.sqrt(s_b / 12)

beta0 = (ser_func_vid[0] * 1 + ser_func_vid[1] * 1 + ser_func_vid[2] * 1 + ser_func_vid[3] * 1) / 4
beta1 = (ser_func_vid[0] * (-1) + ser_func_vid[1] * (-1) + ser_func_vid[2] * 1 + ser_func_vid[3] * 1) / 4
beta2 = (ser_func_vid[0] * (-1) + ser_func_vid[1] * 1 + ser_func_vid[2] * (-1) + ser_func_vid[3] * 1) / 4
beta3 = (ser_func_vid[0] * (-1) + ser_func_vid[1] * 1 + ser_func_vid[2] * 1 + ser_func_vid[3] * (-1)) / 4

print("beta0: {}".format(beta0))
print("beta1: {}".format(beta1))
print("beta2: {}".format(beta2))
print("beta3: {}".format(beta3) + "\n")

t0 = abs(beta0) / s_beta
t1 = abs(beta1) / s_beta
t2 = abs(beta2) / s_beta
t3 = abs(beta3) / s_beta

print("t0: {}".format(t0))
print("t1: {}".format(t1))
print("t2: {}".format(t2))
print("t3: {}".format(t3))
print("Коефіціенти b1, b2 та b3 є незначними, тобто вони виключаюься з рівняння.\n")

print("Перевірка критерія Фішера:")
y1k = b0
y2k = y1k
y3k = y1k
y4k = y1k

s_ad = 1.5 * ((y1k - ser_func_vid[0])**2 + (y2k - ser_func_vid[1])**2 + (y3k - ser_func_vid[2])**2 + (y4k - ser_func_vid[3]))

f = s_ad / s_b
ft = 4.1
print("Fp: {}".format(f))

if f < ft:
	print("Рівняння регресії адекватно оригіналу при рівні значимості 0.05.")
else:
	print("Рівняння регресії неадекватно оригіналу при рівні значимості 0.05")