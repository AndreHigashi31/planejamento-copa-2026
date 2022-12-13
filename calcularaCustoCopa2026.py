dolar = 5.32
voo_canada = voo_eua = voo_mexico = 4000
ingressos = [2500, 800, 1000, 1700, 3500, 4000]
hospedagem_eua = 2000
hospedagem_mexico = 1000
hospedagem_canada = 1000
alimentacao_diaria = 100 * dolar
total_viagem = total_alimentacao = gasto_total = 0


def investimento(gasto_total):
    aporte_mensais = gasto_total * 0.01 / ((1.01**36) - 1)
    print(f'\nSe começarmos a planejar nossa viagem para a Copa 2026, precisaremos aportar mensalmente R$ {aporte_mensais:.2f}')


print('=' * 100)
print(' '* 40 + 'RUMO A COPA 2026')
print('=' * 100)

print('\nA Copa Mundo está acabando e que tal começar a nos planejar para acompanhar a proxima Copa do Mundo?\n')
print('-' * 100)
print('\nA Copa do Mundo 2026 será disputa em 3 paises: Canadá, Estados Unidos e México!\n'
      '\nAs sedes no Canadá serão:'
      '\n- Vancouver;'
      '\n- Toronto;\n'
      '\nNos EUA:'
      '\n- Seattle;'
      '\n- São Francisco;'
      '\n- Los Angeles;'
      '\n- Kansas City;'
      '\n- Dallas;'
      '\n- Atlanta;'
      '\n- Houston;'
      '\n- Boston;'
      '\n- Nova Iorque;'
      '\n- Filadelfia;'
      '\n- Miami;\n'
      '\nE no México as sedes serão:'
      '\n- Guadalajara;'
      '\n- Cidade do México;'
      '\n- Monterrey.')
print('-' * 100)
destino = int(input('Em qual desses paises você gostaria de ver os Jogos da Copa 2026:'
                             '\n[1] - Canadá;'
                             '\n[2] - EUA;'
                             '\n[3] - México '
                             '\nDigite o número correspondente ao país que deseja viajar:'))
print('-' * 100)
dias_de_viagem = int(input('\nQuantos dias gostaria de acompanhar os jogos da copa? '))
print('-' * 100)
acompanhantes = int(input('\nPretende viajar sozinho ou acompanhado?'
                           '\n[1] - Sozinho;'
                           '\n[2] - Acompanhado.'
                           '\nDigite o número correspondente: '))
if acompanhantes == 2:
    print('-' * 100)
    total_acompanhantes = int(input('Quantas pessoas vão a Copa com você: '))
    total_passageiros = total_acompanhantes + 1
else:
    total_passageiros = 1

print('-' * 100)
fase_jogos = int(input('\nQual jogo gostaria de assistir:'
                       '\n[0] - Abertura'
                       '\n[1] - Fase de Grupos'
                       '\n[2] - Oitavas de final'
                       '\n[3] - Quartas de final'
                       '\n[4] - Semi Final'
                       '\n[5] - Final'
                       '\nDigite o número correspondente ao jogo que gostaria de assistir: '))

print('-' * 100)
if destino == 1:
    print(f'Para {total_passageiros} pessoa(s) teremos o custo de:')
    total_passagens = (voo_canada * 2) * total_passageiros
    print(f'\nCom passagens aereas (ida e volta) teremos o custo de R$ {total_passagens:.2f}')
    total_hospedagem = hospedagem_canada * dias_de_viagem
    print(f'\nCom hospedagem para {dias_de_viagem} dias, teremos o custo de R$ {total_hospedagem:.2f}')
    total_alimentacao = (dias_de_viagem * (100 * total_passageiros)) * dolar
    print(f'\nPara os {dias_de_viagem} dias, gastaremos R$ {total_alimentacao:.2f} com alimentação')
    total_ingressos = ingressos[fase_jogos] * total_passageiros
    print(f'\nPara o jogos que você quer assisitir, o preço do ingresso é de R$ {ingressos[fase_jogos]:.2f}')
    gasto_total = total_alimentacao + total_hospedagem + total_passagens + total_ingressos
    print(f'\nPara acompanhar nossa Seleção, teremos um custo de R$ {gasto_total:.2f}!')
    investimento(gasto_total)

elif destino == 2:
    print(f'Para {total_passageiros} pessoa(s) teremos o custo de:')
    total_passagens = (voo_eua * 2) * total_passageiros
    print(f'\nCom passagens aereas (ida e volta) teremos o custo de R$ {total_passagens:.2f}')
    total_hospedagem = hospedagem_eua * dias_de_viagem
    print(f'\nCom hospedagem para {dias_de_viagem} dias, teremos o custo de R$ {total_hospedagem:.2f}')
    total_alimentacao = (dias_de_viagem * (100 * total_passageiros)) * dolar
    print(f'\nPara os {dias_de_viagem} dias, gastaremos R$ {total_alimentacao:.2f} com alimentação')
    total_ingressos = ingressos[fase_jogos] * total_passageiros
    print(f'\nPara o jogos que você quer assisitir, o preço do ingresso é de R$ {ingressos[fase_jogos]:.2f}')
    gasto_total = total_alimentacao + total_hospedagem + total_passagens + total_ingressos
    print(f'\nPara acompanhar nossa Seleção, teremos um custo de R$ {gasto_total:.2f}!')
    investimento(gasto_total)

else:
    print(f'Para {total_passageiros} pessoa(s) teremos o custo de:')
    total_passagens = (voo_mexico * 2) * total_passageiros
    print(f'\nCom passagens aereas (ida e volta) teremos o custo de R$ {total_passagens:.2f}')
    total_hospedagem = hospedagem_mexico * dias_de_viagem
    print(f'\nCom hospedagem para {dias_de_viagem} dias, teremos o custo de R$ {total_hospedagem:.2f}')
    total_alimentacao = (dias_de_viagem * (100 * total_passageiros)) * dolar
    print(f'\nPara os {dias_de_viagem} dias, gastaremos R$ {total_alimentacao:.2f} com alimentação')
    total_ingressos = ingressos[fase_jogos] * total_passageiros
    print(f'\nPara o jogos que você quer assisitir, o preço do ingresso é de R$ {ingressos[fase_jogos]:.2f}')
    gasto_total = total_alimentacao + total_hospedagem + total_passagens + total_ingressos
    print(f'\nPara acompanhar nossa Seleção, teremos um custo de R$ {gasto_total:.2f}!')
    investimento(gasto_total)
