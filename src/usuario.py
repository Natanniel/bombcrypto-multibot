from tkinter.tix import Tree
import pyautogui
from src.logger import logger
from src.helper import clickbtn , movetowithrandomness
import time

def selecionaContas():
    return [
        ['Conta 1', 'Bla bla bla',0],
        ['Conta 2', 'Ble ble ble',0]
        ]

def deslogar(images):
    global login_attempts
    logger('😿 Deslogando da conta atual')
    print('teste')
    if clickbtn(images['metamask-taskbar'], timeout=10, threshold= 0.7, deslogar = True):
        logger('🎉 Botão de conexão metamask encontrado e deslogado')
        time.sleep(10)
      
       
