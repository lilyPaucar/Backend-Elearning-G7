numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
m_tres=0
m_cinco=0
for i in numeros:
    if i%3==0 and i%5==0:
        continue
    elif i%3==0:
        m_tres+=1
    elif i%5==0:
        m_cinco+=1
print("los multiplos de 3 son: {} y los multiplos de 5 son: {}" .format(m_tres,m_cinco))