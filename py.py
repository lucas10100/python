
n = int(input("digite a sequencia ? "))
t1 = 0 
t2= 1
print('{} > {}'.format(t1,t2), end="")
cont = 3
while cont <= n:
  t3= t1 + t2
  print(' > {}'.format(t3), end="")
  t1 = t2 
  t2= t3
  cont += 1
  print("-")
if n== t1 or n==t2:
      print("faz parte ")
elif n==t3:
       print("faz parte")
else:
    print("não faz parte")
       