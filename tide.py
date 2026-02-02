
def area_cal(x, y):
    reg_cal = x * y
    tri_cal = (1/2) * x * y
    return (reg_cal, tri_cal)


reg, tri = area_cal(6, 4)
print(f'หาสี่เหลี่ยม {reg}')
print(f'หาสามเหลี่ยม {tri}')