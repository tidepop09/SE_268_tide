
import math

def area_cal(x, y, r, d1, d2):
    reg_cal = x * y                
    tri_cal = 0.5 * x * y           
    cir_cal = math.pi * r * r
    sem_cal = 0.5 * math.pi * r * r
    squ_cal = x * x
    rho_cal = 0.5 * d1 * d2
    pen_cal = (5 * a**2) / (4 * math.tan(math.pi / 5))
    hex_cal = (3 * math.sqrt(3) * a**2) / 2
    oct_cal = 2 * (1 + math.sqrt(2)) * a**2
    
    return reg_cal, tri_cal, cir_cal, sem_cal, squ_cal, rho_cal, pen_cal, hex_cal, oct_cal


reg, tri, cir, sem, squ, rho, pen, hex, oct = area_cal(6, 4, 3)

print(f'หาสี่เหลี่ยม = {reg}')
print(f'หาสามเหลี่ยม = {tri}')
print(f'วงกลม = {cir}')
print(f'ครึ่งวงกลม = {sem}')
print(f'หาสี่เหลี่ยมจัตุรัส = {squ}')
print(f'หาพื้นที่สี่เหลี่ยมด้านขนาน = {rho}')
print(f'หาพื้นที่รูปห้าเหลี่ยม = {pen}')
print(f'หาพื้นที่รูปหกเหลี่ยม = {hex}')
print(f'หาพื้นที่รูปแปดเหลี่ยม = {oct}')