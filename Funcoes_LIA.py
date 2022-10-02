import os
import datetime as dt
import wikipedia as wik
import speech_recognition as sr
import pyautogui as pg
import random
# Arquivo reservado para criação de funçõe para a IA LIA
# Desenvolvido por Matheus

# Executar algum outro arquivo


def executar_arquivo(maquina, nome):
    maquina.say('Qual deseja executar? ')
    maquina.runAndWait()
    audio1 = 'Tem certeza que escreveu corretamente?'
    audio2 = 'Arquivo inexistente no diretório de execução de scripts'
    audio3 = ('Esse arquivo não consta no meu banco de dados')
    audios = [audio1, audio2, audio3]
    pause = True
    while pause == True:
        caminho = input('Digite o nome do arquivo: ')
        arquivo = (
            'C:\Python_Projects\Programas_por_Math_Gama\IA LIA\ScriptsDeExecucao/'+caminho)
        if caminho == 'sair':
            maquina.say('Voltando a página principal')
            maquina.runAndWait()
            pause = False
        elif not os.path.exists(arquivo):
            maquina.say(random.choice(audios))
            maquina.runAndWait()
        else:
            maquina.say('Executando o arquivo '+caminho)
            maquina.runAndWait()
            os.startfile(arquivo)

            pause = False

# Dizer as horas


def saber_horas(maquina, nome):
    hora2 = dt.datetime.now().strftime('%H:%M')
    hora = dt.datetime.now().strftime('%H%M')
    teste = int(hora)
    if teste <= 1159:
        maquina.say('Bom dia ' + nome +
                    ', agora são exatamente' + hora2+' da manhã')
        maquina.runAndWait()
    elif (teste >= 1200) & (teste <= 1800):
        maquina.say('Boa tarde ' + nome +
                    ', agora são exatamente' + hora2+' da tarde')
        maquina.runAndWait()
    elif (teste >= 1900) & (teste <= 100):
        maquina.say('Boa noite ' + nome +
                    ', agora são exatamente' + hora2 + ' da noite')
        maquina.runAndWait()

# Pesquisar algo na wikipedia


def func_search(maquina, nome):
    maquina.say('Sobre quem \n ou oque deseja que eu procure?')
    maquina.runAndWait()
    pesquisa = input('Digite sobre oque deseja pesquisar: ')
    if (pesquisa == 'exit') | (pesquisa == 'sair'):
        maquina.say('Saindo do sistema \n até mais ' + nome.read())
        maquina.runAndWait()
    else:
        wik.set_lang('pt')
        resultado = wik.summary(pesquisa, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

# Comando de voz


def comando_voz(maquina, nome):
    maquina.say('Comando de voz ativado')
    maquina.runAndWait()
    audio = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            maquina.say('O microfone está OK')
            maquina.runAndWait()
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, 'pt-BR')
            comando = comando.lower()

            if 'executa um arquivo' in comando:
                executar_arquivo(maquina, nome)

            elif 'que horas' in comando:
                maquina.say('horas')
                # saber_horas(maquina, nome)

            elif 'conta uma piada' in comando:
                contar_piada(maquina)

            elif 'sair' in comando:
                maquina.say('Saindo do sistema, até mais '+nome)
                maquina.runAndWait()
    except:
        print('microfone não esta ok')

# Contar uma piada aleatória


def contar_piada(maquina):
    piada01 = 'Como juntar duas motos? \nPega as duas e Yamaha.'
    piada02 = 'Por que o homem invisível recusou uma oferta de emprego?\nPorque ele não se via trabalhando com aquilo'
    piada03 = 'Como transformar um giz em uma cobra?\nÉ só colocar na água que o giz bóia'
    piada04 = 'O que pediu o astronauta claustrofóbico?\nUm pouco de espaço'
    piada05 = 'Por que um fantasma entrou no elevador?\nPara elevar o espírito.'
    piada06 = 'Qual a diferença entre uma pizza e um judeu?\nA pizza não grita no fogo\nEssa foi pesada até mesmo pro Pericles\nTa lôuco fiquei até triste'
    piada07 = 'Ana e César foram à maternidade para o nascimento do filho\nO bebê nasceu de cesareana'
    piada08 = 'Quer ouvir duas piadas curtas e uma piada longa?\nPiada, piada, piaaaaaaaaaaaaaada'
    piada09 = 'Um homem sentou em cima de um cachorro. Qual é o nome do filme?\nSento em um dálmata'
    piada10 = 'Um rapaz viu o Thor de perto. Qual o nome dele?\nVi-thor'
    audios = ['Se liga nessa piada',    'Essa vai ser engraçada se liga',
              'Mano, essa aqui eu ri pakas', 'Olha essa']
    piadas = [piada01, piada02, piada03, piada04, piada05,
              piada06, piada07, piada08, piada09, piada10]
    maquina.say(random.choice(audios))
    maquina.say(random.choice(piadas))
    maquina.runAndWait()
