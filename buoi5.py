#sap xep theo tu be den lon roi moi den cho
victims = [('Hùng', 18, 'nam'), # 18
           ('Lan', 23, 'nữ'), # 23
           ('Lão', 65, 'nam'),
           ('Bà', 62, 'nữ'),
           ('TinTin', 8, 'chó'), # ..
           ('Cu', 6, 'nam'),
           ('Bé', 12, 'nữ')]  # 12

helps=sorted(victims,key= lambda i :i[1], reverse=0)
a=victims.__len__()
for x in range(0,a):
   if helps[x][2] =='chó':
        b=helps[x]
        helps.remove(b)
        helps.append(b)
print(helps)


