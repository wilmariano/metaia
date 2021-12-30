from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Substitua o Friday pelo nome que quiser
chatbot = ChatBot("Friday")

# Coloque o caminho do Chromedriver e o link do chatbot vítima
navegador = webdriver.Chrome("C:/chromedriver.exe")
navegador.get("http://127.0.0.1:5000/")

# Configuração da variável de aprendizagem
trainer = ChatterBotCorpusTrainer(chatbot)
# Ensinando um pouco de português e importando um yml como insumo de IA
#trainer.train('chatterbot.corpus.portuguese')
#trainer.train(
#   "games"
#)

# Iniciando a conversa com o robô 'digitando' um 'oi' e enviando mensagem
navegador.find_element_by_xpath('//*[@id="textInput"]').send_keys("oi")
navegador.find_element_by_xpath('//*[@id="textInput"]').send_keys(u'\ue007')
# contador de mensagens para saber a qual mensagem capturar para aprender e responder
contador = 3
# Loop infinito para escutar mensagem e responder em seguida
while(1):
    time.sleep(1)
    user_input = navegador.find_element_by_xpath('//*[@id="chatbox"]/p['+str(contador)+']/span')
    bot_response = chatbot.get_response(user_input.text)
    navegador.find_element_by_xpath('//*[@id="textInput"]').send_keys(bot_response.text)
    navegador.find_element_by_xpath('//*[@id="textInput"]').send_keys(u'\ue007')
    contador =+1
