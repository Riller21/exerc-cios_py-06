pergunta_1 = input("Telefonou para a vítima?(sim ou não) ")
pergunta_2 = input("Esteve no local do crime?(sim ou não)")
pergunta_3 = input("Mora perto da vítima?(sim ou não)")
pergunta_4 = input("Devia para a vítima?(sim ou não)")
pergunta_5 = input("Já trabalhou com a vítima?(sim ou não)")


respostas = [pergunta_1, pergunta_2,pergunta_3,pergunta_4,pergunta_5]


#função .count para encontrar quantas vezes foi respondido sim na lista com as respostas.
if respostas.count("sim") == 2:
    print("Suspeito")
elif respostas.count("sim") == 3 or respostas.count("sim") == 4:
    print("Cúmplice")
elif respostas.count("sim") == 5 :
    print("Culpado")
else:
    print("Inocente")
