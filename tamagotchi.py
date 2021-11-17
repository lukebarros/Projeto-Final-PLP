from time import sleep

class tamagotchi: #Classe Tamagotchi
    
    def __init__(self,nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def __str__(self):
        return f'\nNome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade} anos\n'


tama = {} # Criação de dicionário para o objeto baseado no input
def criar(): # Função para criar o tamagotchi
    print('Criação do Tamagotchi\n\n')
    nome = input('Nome: ')
    fome = input('Fome: ')
    saude = input('Saúde: ')
    idade = int(input('Idade: '))
    tama[nome] = tamagotchi(nome,fome,saude,idade)


while True: # Loop para realização das tarefas
    i = int(input('O que deseja fazer?\n\n[1] Criar novo tamagotchi\n[2] Mostrar dados\n[3] Alterar Dados\n[4] Sair\n\n'))
    if i == 1: 
        criar()
        tamakeys = list(tama) # Criação de lista baseada no dict "tama" para mostrar as opções disponiveis
    elif i == 2:
        k = input(f'Tamagotchi Disponíveis: {tamakeys[0]}, {tamakeys[len(tamakeys)-1]}\n')
        k = tama[k]
        op = int(input('Dados:\n[1] Nome\n[2] Fome\n[3] Saúde\n[4] Idade\n[5] Todos\n\n'))
        if op == 1:
            print(k.nome)
            sleep(1)
        elif op == 2: 
            print(k.fome)
            sleep(1)
        elif op == 3: 
            print(k.saude)
            sleep(1)
        elif op == 4: 
            print(k.idade)
            sleep(1)
        else:
            print(k)
            sleep(2)
    elif i == 3:
        n = input(f'Tamagotchi Disponíveis: {tamakeys[0]}, {tamakeys[len(tamakeys)-1]}\n')
        j = int(input('Selecione o atributo para alteração:\n[1] Nome\n[2] Fome\n[3] Saúde\n[4] Idade\n[5] Voltar\n\n'))
        if j == 1:
            novonome = input('Digite o novo nome do tamagotchi: ')
            tama[n].nome = novonome
        elif j == 2:
            novafome = input('Digite o novo status de fome: ')
            tama[n].fome = novafome
        elif j == 3:
            novasaude = input('Digite o novo status de saúde: ')
            tama[n].saude = novasaude
        elif j == 4: 
            novaidade = int(input('Digite a nova idade: '))
            tama[n].idade = novaidade
        else: 
            True
    else:
        break