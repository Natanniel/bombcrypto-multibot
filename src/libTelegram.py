import telegram

bot = telegram.Bot('5016590609:AAHAomWfXhshG5Wg4y1dri-EV83mT8qiPNM')
    
def enviarMensagemTelegram(mensagem):
    global bot    
    tchat = '782375549'
    bot.send_message(chat_id=tchat, text=mensagem)
