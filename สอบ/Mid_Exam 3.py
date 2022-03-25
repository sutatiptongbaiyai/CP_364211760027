"""
Name: {นางสาวสุธาทิพย์ ทองใบใหญ่}
SID: {364211760027}
Group: {MIT211}
"""

"""
Question 3:
จงเขียนโปรแกรมจาก dictionary ที่กำหนดให้
(10 คะแนน)
"""

mydict = {'brand':'toyota','model':'cross','year':'2021'}

# แสดงข้อมูลทั้งหมดใน dicionary mydict
print('Data in dictionary: ', mydict)
# แสดงชนิดข้อมูลตัวแปร mydict
print(mydict)
# แสดงชนิดข้อมูลค่า value ทุกตัวใน mydict
for x in mydict.values():
    print(x)
# เพิ่มข้อมูล 'color':['white','black'] ใน mydict
mydict['color'] = 'white','black'
print(mydict)
# เพิ่มข้อมูล 'hp': 150 ใน mydict
mydict.update({'hp': 150})
print(mydict)
# แสดงข้อมูลเฉพาะ keys ใน mydict
print(mydict.keys())
# แสดงข้อมูลเฉพาะ values ใน mydict
print(mydict.values())
# คัดแยกข้อมูล keys จาก mydict มาเก็บไว้ใรตัวแปรชนิด list ชื่อ mykeys และแสดงข้อมูลทางหน้าจอ
mykeys = mydict.keys()
print("mykeys=", mykeys)
# คัดแยกข้อมูล values จาก mydict มาเก็บไว้ใรตัวแปรชนิด list ชื่อ myvalues และแสดงข้อมูลทางหน้าจอ
myvalues = mydict.values()
print("myvalues =", myvalues)
# ลบข้อมูล key: 'hp'
del mydict['hp']
print(mydict)
# เปลี่ยนแปลงข้อมูลจากเดิม 'color': ['white','black'] เป็น 'Red'
mydict.update({'color': 'Red'})
print(mydict)
# แสดงข้อมูล mylist ทางหน้าจอภาพ
print(mydict)
