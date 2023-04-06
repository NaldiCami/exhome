def verificar_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True 
    

num = 53
if verificar_primo(num):
    print(num, 'é primo.')
else:
    print(num, 'não é primo.')
    