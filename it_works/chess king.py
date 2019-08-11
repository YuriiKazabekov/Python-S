print ('Введіть номер колонки на початку ходу')
a = int(input())
print ('Введіть номер рядка на початку ходу' )
b = int(input())
print ('Введіть номер колонки в кінці ходу')
c = int(input())
print ('Введіть номер рядка в кінці ходу' )
d = int(input())
x= a-c
y= b-d
if 1 >= x >= -1 and 1 >= y >= -1:
    print("YES")
else:
    print("NO")