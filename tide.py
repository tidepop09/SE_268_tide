
import math

def area_cal(x, y, r):
    reg_cal = x * y                
    tri_cal = 0.5 * x * y           
    cir_cal = math.pi * r * r
    sem_cal = 1/2 * math.pi * r * r
    
    return reg_cal, tri_cal, cir_cal, sem_cal


reg, tri, cir, sem = area_cal(6, 4, 3)

print(f'หาสี่เหลี่ยม = {reg}')
print(f'หาสามเหลี่ยม = {tri}')
print(f'วงกลม = {cir}')
print(f'ครึ่งวงกลม = {sem}')