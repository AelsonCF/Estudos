'''
[ Feito ] - Criar uma lista de curiosidades que deverá ser pronunciada pela IA ao ser escolhida a opção de curiosidades;
[ Feito ] - Após a IA pronunciar algumas palavras é realizado uma pesquisa no google. retire a pesquisa automática, essa funcionalidade deverá ser realizada somente quanto solicitada pelo usuário;
[ Feito ] -  Adicionar boa tarde e boa noite ao trecho de perguntas e respostas;
[ Feito linux ] - Adicionar 5 programas do Windows que deverão ser inicializados pela IA;
[ Feito ] - Retirar as duplicidades da pesquisa ao realizar qualquer tarefa;
[ Feito ] - Adicionar uma função para desligar o assistente virtual, o assistente deverá enviar uma mensagem de despedida;
[ Feito ] - Ao iniciar o código, o assistente deverá se apresentar ao usuário;
[ Feito ] - A instalação das bibliotecas utilizadas no código é parte da avaliação;
[ Feito ] - Adicione a possibilidade do usuário escolher uma música do youtube para ser executada. Use a biblioteca 
'''
'''
1 - Pesquisar no wikipedia "oque deseja pesquisar"
2 - pesquisar no google "oque deseja pesquisar"
3 - toque "nome da musica"
4 - abre "nome do programa"
5 - oi
6 - qual é o seu nome
7 - bom dia, boa tarde, boa noite
8 - curiosidades
9 - desligar

'''

import speech_recognition as sr
import pyttsx3
import datetime
import random
import os
import wikipedia
import pywhatkit
import webbrowser


# Configurações gerais
comando = ''
ligado = 1
audio = sr.Recognizer()
Assistente = pyttsx3.init()

# Funções da assistente

def falar(audio):
    
    Assistente.say(audio)
    Assistente.runAndWait()   

def usuario(C):
    comand = C
    
    if comand == 'qual o seu nome':
        falar('Meu nome é assistente. muito prazer')

    elif comand == 'bom dia':
        falar('bom dia')
        print('bom dia')

    elif comand == 'boa tarde':
        falar('boa tarde')
    
    elif comand == 'boa noite':
        falar('boa noite')

    elif comand == 'oi':
        falar('oi')

    # Abrir softwares ----------------------------------

    elif comand == 'abrir vs code':
        os.startfile('C:\Users\Aelson Carvalho\AppData\Local\Programs\Microsoft VS Code\Code.exe')
    
    elif comand == 'abrir libreoffice':
        os.startfile('C:\Program Files\LibreOffice\program\soffice.exe')

    elif comand == 'abrir intellij':
        os.startfile('C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2022.1.4\bin\idea64.exe')

    elif comand == 'abrir steam':
        os.startfile('C:\Program Files (x86)\Steam\Steam.exe')
    
    elif comand == 'abrir edge':
        os.startfile('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

    # --------------------------------------------------

    # Pesquisas

    elif comand == 'curiosidades' or comand == 'curiosidade':
        curiosidade = ['Passar  álcool  na  pele  dá  uma  sensação  momentânea  de  frio', 'Colocar  gelo  em  cima  do  machucado  ajuda  na  recuperação', 'Sentimos  mais  frio  quando  estamos  com  febre', 'Ao  passar  por  uma  cirurgia  no  dente,  os  dentistas  recomendam  ingerir  bebidas/comidas  frias', 'Quando  o  dia  amanhece  frio,  o  carro  que  foi  abastecido  com  álcool  pode  demorar  a  ligar']
        falar(curiosidade[random.randint(0, 4)])

    elif 'pesquisar no wikipedia' in comand:
        pesquisar = comand.replace('pesquisar no wikipedia', '')
        wikipedia.set_lang('pt')
        procurar = wikipedia.summary(pesquisar, 2)
        falar(procurar)
    
    elif 'toque' in comand:
        pesquisar = comand.replace('toque', '')
        procurar = pywhatkit.playonyt(pesquisar)
        falar('tocando {}'.format(pesquisar))
    
    elif 'pesquisar no google' in comand:
        pesquisar = comand.replace('pesquisar no google', '')
        webbrowser.open(f'https://www.google.com/search?q={pesquisar}')
# --------------------------------------------------------------------------------------

# Controle que mantem o assistente ligado
while ligado == 1:

    usuario('google chrome')
    try:
        with sr.Microphone() as source:
            print('Ouvindo ...')
            fala = audio.listen(source)
            comando = audio.recognize_google(fala, language='pt-BR')
            comando = comando.lower()

            if comando == 'desligar':
                falar('desligando  assistente. até  depois')
                ligado = 0
            
            usuario('pesquisar no wikipedia carros')

    except:
        falar('Não  consigo  escutar  o  seu  microfone!!')
        break