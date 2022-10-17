Cinema=[]

def listar(Cinema):
    print("Os filmes em exibição são:")
    for sala in Cinema:
        print(sala[2])
    return

def disponivel(Cinema, filmep, lugar):
    res=False
    for sala in Cinema:
        lugares, vendidos, filme= sala
        if filmep==filme and lugar not in vendidos and lugar<lugares:
            res=True
    return res

def vendebilhete(Cinema, filmep, lugar):
    if disponivel(Cinema, filmep, lugar):
        for sala in Cinema:
            filme=sala[2]
            if filmep==filme:
                sala[1].append(lugar)
                sala[1].sort
        print("O bilhete foi vendido.")
    else:
        print("O lugar não se encontra disponível.")
    return cinema

def listardisponibilidade(Cinema):
    for sala in Cinema:
        lugares, vendidos, filme= sala
        print("---------------------")
        print("Filme:", filme)
        print("Lugares disponíveis:", lugares-len(vendidos))

def inserirSala(Cinema, sala):
    if sala not in Cinema:
        Cinema.append(sala)
    return cinema

def menu():
    print('''
    Menu:
    1 : Listar filmes em exibição;
    2 : Verificar disponibilidade de um lugar;
    3 : Vender bilhete;
    4 : Listar número de lugares disponíveis por filme;
    5 : Inserir sala;
    0 : Sair.''')

menu()
option=int(input("Selecione uma opção:"))

while option!=0:
    if option==1:
        listar(Cinema)
    if option==2:
        filmep=str(input("Insira o filme:"))
        lugar=int(input("Insira o lugar:"))
        if disponivel(Cinema,filmep,lugar):
            print("O lugar encontra-se disponível")
        else:
            print("O lugar não se encontra disponível")

    if option==3:
        filmep=str(input("Insira o filme:"))
        lugar=int(input("Insira o lugar:"))
        cinema=vendebilhete(Cinema, filmep, lugar)
    if option==4:
        listardisponibilidade(Cinema)
    if option==5:
        sala=[]
        sala.append(int(input("Insira o número de lugares da sala:")))
        sala.append([])
        sala.append(str(input("Insira o nome do filme em exebição:")))
        cinema=inserirSala(Cinema, sala)
    menu()
    option=int(input("Selecione uma opção:"))

