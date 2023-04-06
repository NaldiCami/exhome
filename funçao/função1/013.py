def calcular_raiz_quadrada(num, precisão = 0.0001):
    raiz = num * 2
    while abs(num - raiz ** 2) > precisão:
        raiz = (raiz + num/raiz)/2
    return raiz 
    
num = 25 
raiz = calcular_raiz_quadrada(num)
print('a raiz quadrada de', num, 'é', raiz)
print(abs(-5))