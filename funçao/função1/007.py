def anobi(ano):
    if ano%4 != 0:
        return False 
    elif ano %100 !=0:
        return True
    elif ano %400 !=0:
        return False 
    else:
        return True 


## anos para comparação

dados = [1900,2000,2016,1987,2020]


## resultado

result = [False,True,True,False,True]

##checar 

for i in range(len(dados)):
    yr = dados[i]
    print(yr,'->', end = '')
    resultado = anobi(yr)
    if resultado == result[i]:
        print('ok')
    else:
        print('falha')