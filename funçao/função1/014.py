def verificar_palin(text):
    text = text.lower().replace('', '')
    return text == text[::-1]
    
    
text = 'socorram - me, subi no onibus em marrocos'
if verificar_palin(text):
    print(text, 'é um palindromo.')
else:
    print(text, 'não é um palindromo')