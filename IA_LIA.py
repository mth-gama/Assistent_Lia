import pyttsx3 as ptt
from Funcoes_LIA import *

maquina = ptt.init('sapi5')
nome = 'matheus'

while True:
    print('1 - Saber as horas;')
    print('2 - Pesquisar algo na internet;')
    print('3 - Ativar comando por voz;')
    print('4 - Executar script;')
    print('5 - Contar uma piada;')
    print('0 - Sair;')
    op = int(input('Entre com a opção> '))
    if op == 1:
        saber_horas(maquina, nome)
    elif op == 2:
        func_search(maquina, nome)
    elif op == 3:
        comando_voz(maquina, nome)
    elif op == 4:
        executar_arquivo(maquina, nome)
    elif op == 5:
        contar_piada(maquina)
    elif op == 0:
        maquina.say('Saindo do sistema \n até mais ' + nome)
        maquina.runAndWait()
        break
