"""
Name: {นางสาวสุธาทิพย์ ทองใบใหญ่}
SID: {364211760027}
Group: {MIT211}
"""

"""
Question 2:
จงเขียนโปรแกรมจาก tuple ที่กำหนดให้
(10 คะแนน)
"""

myTuple = (100,200,300,400,500)  

# แสดงผลข้อมูลใน myTuple ทั้งหมด
print(myTuple)
# แสดงผลข้อมูล 200 จาก myTuple
print(myTuple[1])
# แสดงผลข้อมูล 500 จาก myTuple
print(myTuple[4])
# แสดงผลข้อมูล 500 จาก myTuple โดยใช้ negative index
print(myTuple[-1])

# แสดงผลข้อมูล (200,300,400) โดยใช้ range index
print(myTuple[1:4])
# แสดงผลข้อมูล (400,500) โดยใช้ range index
print(myTuple[3:])
# แสดงผลข้อมูล (100,200) โดยใช้ range negative index
print(myTuple[:2])

# แสดงผลข้อมูลใน myTuple ทั้งหมด โดยการใช้ for loop
for x in myTuple:
    print(x)

# Tuples ไม่สามารถเพิ่มหรือลบข้อมูลได้ แต่สามารถเปลี่ยน Tuples เป็น List เพื่อเพื่อหรือลบข้อมูล
# เปลี่ยน myTuple เป็น List ชื่อ myList
myList = list(myTuple)
print(myList, type(myList), len(myList))
# เพิ่มข้อมูล 10,20,30 ใน myList
myList[5:] = [10, 20, 30]
print(myList)
# เพิ่มข้อมูล 40 ใน myList ในตำแหน่งที่ 0
myList.insert(0, 40)
print(myList)
# เพิ่มข้อมูล 50 ใน myList ในตำแหน่งที่ 3
myList.insert(3, 50)
print(myList)
# แสดงผลข้อมูลใน myList ทั้งหมด 
print(myList)

# ลบข้อมูล 10
myList.remove(10)
print(myList)
# ลบข้อมูล 100
myList.remove(100)
print(myList)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# ลบข้อมูลตำแหน่งสุดท้ายใน myList
myList.pop()
print(myList)
# แสดงผลข้อมูลใน myList ทั้งหมด 
print(myList)

# เรียงข้อมูล myList จาก น้อย-มาก
myList.sort()
print(f'Sort Low to High: {myList}')
# แสดงผลข้อมูลใน myList ทั้งหมด 
print(myList)

# นำข้อมูลใน myList ทั้งหมดบวกรวมกัน และเก็บไว้ในตัวแปร total จากนั้นแสดงตัวแปร total หน้าจอ output
total = sum(myList)
print(f'total = {total}')
# เปลี่ยน myList เป็น Tuple ในชื่อ myTuple
myTuple = tuple(myList)
print(myTuple)
# แสดงผลข้อมูลทั้งหมดใน myTuple
print(myTuple)
