def Questao1(i):
    listed = list(i)
    for index in range(0, len(i), 1):
        if listed.count(listed[index]) == 1:
            break
    return i[index]

print(Questao1("teste"))
print(Questao1("engenharia de dados"))
