# -*- coding: utf-8 -*-
import math
from math import acos
from math import sqrt, acos
#Yeu cau nguoi dung nhap input toa do
Ax = eval(input('Ax: '))
Ay = eval(input('Ay: '))
Bx = eval(input('Bx: '))
By = eval(input('By: '))
Cx = eval(input('Cx: '))
Cy = eval(input('Cy: '))

#Kiem tra cac toa do co phai tam giac khong
def kiemtra_tamgiac(Ax, Ay, Bx, By, Cx, Cy):
    a = [Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By)]
    if a == 0:
        print('Flase')
    else:
        print('True')

#Tinh do dai cac canh cua mot tam giac va cac goc yeu cau nguoi dung nhap A, B, C
def goccanh_tamgiac(Ax, Ay, Bx, By, Cx, Cy):
    AB = math.sqrt(((Bx - Ax)**2 + (By - Ay)**2))
    AC = math.sqrt(((Cx - Ax)**2 + (Cy - Ay)**2))
    BC = math.sqrt(((Cx - Bx)**2 + (Cy - By)**2))
    print("AB: " +str(AB))
    print("AC: " +str(AC))
    print("BC: " +str(BC))
    



#Xet tam giac can, tam deu, vuong can hay nhon
def  xet_tamgiac(Ax, Ay, Bx, By, Cx, Cy):
    AB = math.sqrt(((Bx - Ax)**2 + (By - Ay)**2))
    AC = math.sqrt(((Cx - Ax)**2 + (Cy - Ay)**2))
    BC = math.sqrt(((Cx - Bx)**2 + (Cy - By)**2))
    angleNeededA = input('Xin hay nhap A ').upper()
    angleNeededB = input('Xin hay Nhap B ').upper()
    angleNeededC = input('Xin hay Nhap C ').upper()
    sumOfSquares = {'A':AB*AB + AC*AC, 'B':BC*BC + AB*AB, 'C': AC*AC + BC*BC}
    sqOfOppSide = {'A':BC*BC, 'B':AC*AC, 'C':AB*AB}
    denominator = {'A': 2*AB*AC, 'B': 2*BC*AB, 'C': 2*AC*BC}
    fractionA = (sumOfSquares[angleNeededA] - sqOfOppSide[angleNeededA])/denominator[angleNeededA]
    fractionB = (sumOfSquares[angleNeededB] - sqOfOppSide[angleNeededB])/denominator[angleNeededB]
    fractionC = (sumOfSquares[angleNeededC] - sqOfOppSide[angleNeededC])/denominator[angleNeededC]
    angleA = math.degrees(math.acos(fractionA))
    print('Angle %s = %.1f degrees' %(angleNeededA, angleA))
    angleB = math.degrees(math.acos(fractionB))
    print('Angle %s = %.1f degrees' %(angleNeededB, angleB))
    angleC = math.degrees(math.acos(fractionC))
    print('Angle %s = %.1f degrees' %(angleNeededC, angleC))
    AB = math.sqrt(((Bx - Ax)**2 + (By - Ay)**2))
    AC = math.sqrt(((Cx - Ax)**2 + (Cy - Ay)**2))
    BC = math.sqrt(((Cx - Bx)**2 + (Cy - By)**2))
    if AC==BC and AB==AC:
        print('Tam giac deu.')
    
    elif (angleA or angleB or angleC == 90.0) and (AB==AC or AB==BC or AC==BC) :
        print("vuong can")  
    elif AB==AC or AB==BC or AC==BC:
        print('Tam giac can.')
    else:
        print('Tam giac nhon')
        

#Tinh dien tich tam giac
def dientich_tamgiac(Ax, Ay, Bx, By, Cx, Cy):
  area = abs(0.5*((Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))))
  print("Dien tich tam giac:" + str(area))

#Tinh duong cao cua tam giac  
   
def duongcao_tamgiac(Ax, Ay, Bx, By, Cx, Cy):
    AB = math.sqrt(((Bx - Ax)**2 + (By - Ay)**2))
    AC = math.sqrt(((Cx - Ax)**2 + (Cy - Ay)**2))
    BC = math.sqrt(((Cx - Bx)**2 + (Cy - By)**2))
    x = (AB + AC + BC) / 2
    p = round(x, 2) 
    height = 2 * (math.sqrt(p(p - AC)(p - BC)(p - AB))) / BC
    print(height)
    

#Driver code
if __name__=='__main__':
    kiemtra_tamgiac(Ax, Ay, Bx, By, Cx, Cy)
    goccanh_tamgiac(Ax, Ay, Bx, By, Cx, Cy)
    dientich_tamgiac(Ax, Ay, Bx, By, Cx, Cy)
    xet_tamgiac(Ax, Ay, Bx, By, Cx, Cy)
    duongcao_tamgiac(Ax, Ay, Bx, By, Cx, Cy)
    