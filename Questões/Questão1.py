def Questao1(i):
    listed = list(i)
    for index in range(0, len(i), 1):
        if listed.count(listed[index]) == 1:
            break
    return i[index]


Questao1("teste")
Questao1("engenharia de dados")
