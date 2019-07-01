print ('Введіть кількість школярів')
n = float(input())
print ('Введіть кількість яблук' )
k = float(input())
print(k // n)
print(k % n)
v = k // n
w = k % n
print("Кожен учень отримає " + str(v) + " яблук(а)")
print(str(w) + " яблук(а) залишиться в корзині")