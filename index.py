# -*- coding: utf-8 -*-    
from src.logger import logger, loggerMapClicked
from src.images import load_images
from src.usuario import deslogar, selecionaContas
from src.libTelegram import enviarMensagemTelegram
from random import randint
from random import random
#from pyclick import HumanClicker

import numpy as np
import mss
import pyautogui
import time
import sys
import yaml
import telegram
import os
import pygetwindow

# PROCESSO DO BOT =========================
# 1 - Deslogar de conta atual
# 2 - Coletar contas para fazer o loop
# 3 - Conectar na conta
# 4 - Colocar todos os personagens para trabalhar
# 5 - A cada 1 minutos ir reposionar os bonecos
# 6 - completando 10 minutos tirar print da tela e enviar via telegram
# 7 - Deslogar da conta atual
# 8 - Ir para a proxima conta do loop
# 9 - CTRL + F5


# CONFIGURAÇÂO 
pyautogui.PAUSE = 2 # Intervalo de tempo entre movimentos
pyautogui.FAILSAFE = False
#hc = HumanClicker() # LIB de click's
pyautogui.MINIMUM_DURATION = 0.1
pyautogui.MINIMUM_SLEEP = 0.1
pyautogui.PAUSE = 2
saldo_atual = 0.0

print('Configurado.')

# CARREGANDO RECURSOS
images = load_images()



def main():

    while True:
        
        contas = selecionaContas()
        ##enviarMensagemTelegram( '🔌 Bot inicializado em %d Contas. \n 💰 É hora de faturar alguns BCoins!!!' % len(contas))
      
        for conta in contas:
           
            for window in pygetwindow.getWindowsWithTitle('Bombcrypto'):
                if window.title.count('Bombcrypto - Mozilla Firefox') >= 1:
                    window.activate()
                   ##     if not window.isMaximized:
                   ##         window.maximize()
                        
                   
                    time.sleep(5)                    
                    deslogar(images)
                    time.sleep(5)              
           

main()