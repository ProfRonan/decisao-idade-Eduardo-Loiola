Idade = int(input("Digite uma Idade: "))
if Idade < 0:
    print("impossível!")
elif Idade < 18:
    print("não precisa se alistar.")
elif Idade >= 18 and Idade <= 65:
    print("Não esqueça de votar na próxima eleição.")
elif Idade > 65:
    print("Vá descansar.")
else:
    print("eita!")