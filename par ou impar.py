from random import randint
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
v = 0
while True:
    opcao = ' '
    while opcao not in 'pi':
        opcao = str(input('Você quer par ou ímpar? (P/I) ')).lower().strip()[0]
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = pc + jogador
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total deu {total}.', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if opcao in 'p':
        if total % 2 == 0:
            print('VOCÊ GANHOU! Vamos continuar.')
            v += 1
        else:
            print('Você perdeu!')
            break
    if opcao in 'i':
        if total % 2 == 1:
            print('VOCÊ GANHOU! Vamos continuar.')
            v += 1
        else:
            print('Você perdeu!')
            break
print(f'ACABOU! Você venceu {v} vez(es)')
