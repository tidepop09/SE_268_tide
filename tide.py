
import math

def area_cal(x, y, r):
    reg_cal = x * y                
    tri_cal = 0.5 * x * y           
    cir_cal = math.pi * r * r      
    return reg_cal, tri_cal, cir_cal


reg, tri, cir = area_cal(6, 4, 3)

print(f'หาสี่เหลี่ยม = {reg}')
print(f'หาสามเหลี่ยม = {tri}')
print(f'วงกลม = {cir}')