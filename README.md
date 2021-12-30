# Metaia1.1 - Pytyhon 3.9
 | Chatbot (chatterbot lib) configurado como webscrapper para aprender com outros chatbot (chatterbot)

## How does it work | Como isso funciona
After downloading Chromedriver according to your Chrome version and installing Selenium, Chatterbot and Flask, configure this chatbot and enjoy | Após baixar Chromedriver de acordo com a versão do seu Chrome e instalar o Selenium, Chatterbot e Flask, configure este chatbot e divirta-se

Watch out with xpath, they are used to map where to work with the page we target as a webcrapper | Atente-se com xpath, servem para mapear onde trabalhar com a página com a qual nos direcionamos como webcrapper
```
# Iniciando a conversa com o robô 'digitando' um 'oi' e enviando mensagem
navegador.find_element_by_xpath('//*[@id="textInput"]').send_keys("oi")
navegador.find_element_by_xpath('//*[@id="textInput"]').send_keys(u'\ue007')
```

Put your own path to your Chromedriver and the victim chatbot link (I simulated my victim chatbot on my own machine) | Coloque o seu próprio caminho ao sei Chromedriver e o link do chatbot vítima (simulei meu chatbot vítima em minha própria máquina)
```
# Coloque o caminho do Chromedriver e o link do chatbot vítima
navegador = webdriver.Chrome("C:/chromedriver.exe")
navegador.get("http://127.0.0.1:5000/")
```

Follow the steps below to get a site's xpath | Siga as etapas abaixo para obter o xpath de um site
* Ctrl+Shift+c
* Clique na seta e selecione o que quer mapear (Selecionei um input text)
* Na parte de scripts selecionado do Inspecionar elemento, botão direito e copiar xpath
```
//*[@id="textInput"]
```
-----------------------------------------------
By option you can write in this field with the script (xpath to a Chatterbot with Flask) | Por opção pode escrever nesse campo com o script (xpath para um Chatterbot com Flask)
```
navegador.find_element_by_xpath('//*[@id="textInput"]').send_keys("oi")
```
-----------------------------------------------
Enter with the following script (xpath to a Chatterbot with Flask) | Dar enter com o seguinte script (xpath para um Chatterbot com Flask)
```
navegador.find_element_by_xpath('//*[@id="textInput"]').send_keys(u'\ue007')
```
Capture a text with the following script (xpath to a Chatterbot with Flask) | Capturar um texto com o seguinte script (xpath para um Chatterbot com Flask)
```
user_input = navegador.find_element_by_xpath('//*[@id="chatbox"]/p/span')
```

-----------------------------------------------
### Contributing | Contribuindo
* Contributions are welcome! Please read our guide before contributing to help this project | As contribuições são bem-vindas! Por favor, leia nosso guia antes de contribuir para ajudar este projeto.
### Referências
* Todos os scripts contém biblioteca Chatterbot e Selenium (com Chromedriver), Microframework Flask
* pip install ChatterBot
* pip install Flask
* pip install selenium
* https://chromedriver.chromium.org/downloads
