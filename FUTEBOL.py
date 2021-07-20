import random

from time import sleep

times = ['BRASIL','ARGENTINA','FRANÇA','MEXICO','ALEMANHA','RUSSIA','ESTADOS UNIDOS','INGLATERRA','PORTUGAL']
print(times)

pc_escolha = random.choice(times)
print(' ')
print(f'Time escolhido pelo Computador: {pc_escolha}')
print(' ')


while True:

    m1 = random.randrange(1, 5)
    p1 = random.randrange(1, 5)

    m2 = random.randrange(1, 6)
    p2 = random.randrange(1, 6)

    var = random.randrange(1,10)

    escolha_do_time = input('Escolha seu time: ').upper().strip()
    if escolha_do_time in times:
        print(f'{escolha_do_time} boa escolha.')
    elif escolha_do_time not in times:
        print('Opção de time não é valida. Tente novamente!')
        continue
    else:
        break

    while True:
        sleep(2)
        print('')
        print('**** Menu ****')
        print('(Jogar) - Iniciar o primeiro tempo')
        print('(Voltar) - Retornar para escolha dos times ')
        print('')
        escolha = input('Escolha uma opção para continuar: ').upper().strip()

        if escolha == 'VOLTAR':
            sleep(2)
            print('Defina um novo time.')
            break
        elif escolha == 'JOGAR':
            print('Inicio do 1 Tempo. ')
            sleep(2)
            print(f'Jogo segue acirrada entre as equipes do {escolha_do_time} e {pc_escolha}.')
            print(f'Placar já está {p1} e {m1}')
            sleep(2)
            print('Estamos nos encaminhando para o 2 tempo')
            print('Opa tivemos um lance próximo da área será que foi penalti? Estamos aguardando a valiação do var!')
            sleep(5)
            print('Var verificando...')

            if var >= 7:
                print(f'Penalti para {escolha_do_time}')
                sleep(2)
                print(f'O Atacante da seleção {escolha_do_time} se prepara para bater ....')
                sleep(5)
                print('Jogador corre para bola para bater ....')
                sleep(3)
                print('GOOOOOOOOOOOOOOOOOOOOOOOL, Ta laah! No fundo da rede. ')
                print('Bola em campo para o final do 1 tempo')
                p1 += 1
                print('')
                print(f'Com esse gol o {escolha_do_time} amplia o placar para {p1}')

            elif var <= 5:
                print(f'Penaliti para {pc_escolha}')
                sleep(2)
                print(f'O Atacante da seleção {pc_escolha} se prepara para bater ....')
                sleep(5)
                print('Jogador corre para bola para bater ....')
                sleep(3)
                print('GOOOOOOOOOOOOOOOOOOOOOOOL, Ta laah! No fundo da rede. ')
                print('Bola em campo para o final do 1 tempo')
                m1 += 1
                print(f'Com esse gol o {pc_escolha} amplia o placar para {m1}')
                print('')
            else:
                print(f'Var achou que o lance foi normal e segue o jogo, e já nos encaminhamos para o final do 1 tempo com {p1} e {m1} no placar')
                sleep(2)

            print('Fim do primeiro tempo')
            print('')
            print('Inicio do 2 Tempo')
            print('bola rolando ...')
            sleep(5)
            print('')

            resultado_p = p1 + p2
            resultado_m = m1 + m2

            print(f'Chegamos ao final do 2 tempo com o resultado de {pc_escolha} {resultado_m} x {resultado_p} {escolha_do_time}')
            if resultado_p > resultado_m:
                print("Parabéns, você ganhou!")
                print("       ___________      ")
                print("      '._==_==_=_.'     ")
                print("      .-\.:     /-.    ")
                print("     | (|:.     |) |    ")
                print("      '-|:.     |-'     ")
                print("        \.\::.  /      ")
                print("         '::. .'        ")
                print("           ) (          ")
                print("         _.' '._        ")
                print("        '-------'       ")
                break
            elif resultado_m > resultado_p:
                print("Puxa, você é um perdedor. Tenta na proxima!")
                print("    _______________         ")
                print("   /               \       ")
                print("  /                 \      ")
                print("//                   \/\  ")
                print("\|   XXXX     XXXX   | /   ")
                print(" |   XXXX     XXXX   |/     ")
                print(" |   XXX       XXX   |      ")
                print(" |                   |      ")
                print(" \__      XXX      __/     ")
                print("   |\     XXX     /|       ")
                print("   | |           | |        ")
                print("   | I I I I I I I |        ")
                print("   |  I I I I I I  |        ")
                print("   \_             _/       ")
                print("     \_         _/         ")
                print("       \_______/           ")

                break
            else:
                print('Empate, bora para 2 jogo!')



