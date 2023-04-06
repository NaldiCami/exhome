def fharenheit_p_celsius(temp_t):
    temp_c = (temp_t - 32) * 5/9
    return temp_c
    
    
temp_t = 75
temp_c = fharenheit_p_celsius(temp_t)
print(temp_t, 'graus fharenheit equivalem a', temp_c, 'graus celsius.')
temp_c_arredondado = round(temp_c, 1)
print(temp_t, 'graus fahreihhjshbfdh equivalem a', temp_c_arredondado, 'graus celsios.')