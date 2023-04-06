def calcular_fatorial(num):
    if num == 0:
         return 1
    else:
        return num * calcular_fatorial(num-1)
    
num = 5
fatorial = calcular_fatorial(num)
print('o fatorial de', num, 'é', fatorial)
