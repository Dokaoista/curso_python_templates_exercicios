from os import system

lista_normal = list()
desfazer_lista = list()
refazer_lista = list()

while True:
    print("Comandos: listar, desfazer, refazer")
    opcao = input("Digite uma tarefa ou comando: ")
    if opcao == "listar":
        print(lista_normal)
    elif opcao == "desfazer":
        try:
            ultimo_item = lista_normal.pop()
            desfazer_lista.append(ultimo_item)
        except:
            pass
    elif opcao == "refazer":
        try:
            item_retirado = desfazer_lista.pop()
            refazer_lista.append(item_retirado) 
            if refazer_lista is not None:
                lista_normal.append(refazer_lista[-1])
        except:
            pass
    elif opcao == "clear":
        system("cls")
    else:
        lista_normal.append(opcao)