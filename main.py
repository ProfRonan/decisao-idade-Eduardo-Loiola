Idade = int(input("Digite uma Idade: "))
if Idade < 0:
    print("Impossível!")
elif Idade < 18:
    print("Não precisa se alistar.")
elif Idade >= 18 and Idade <= 65:
    print("Não esqueça de votar na próxima eleição.")
elif Idade > 65:
    print("Vá descansar.")
else:
    print("Eita!")