from chatterbot import ChatBot, constants
from chatterbot.trainers import ListTrainer
from chatterbot.languages import ENG
from spacy.cli import download

# Baixa o modelo SpaCy (se já tiver, pode comentar)
download("en_core_web_sm")

# Cria a classe customizada
class ENGSM(ENG):
    ISO_639_1 = 'en'

# Força o mapeamento do modelo SpaCy correto
constants.DEFAULT_LANGUAGE_TO_SPACY_MODEL_MAP[ENGSM] = "en_core_web_sm"

# Usa a classe no ChatBot
chatbot = ChatBot("BotAlex", tagger_language=ENGSM)

consversa = [
    "Coe",
    "e ai tranquilo",
    "Tranquilo",
    "Qual a boa de hoje",
    "a hashtag tá ensinando python e até chatbot",
    "Caraca que doidera",
    "Maneiro né",
    "Irado"
]

trainer = ListTrainer(chatbot)
trainer.train(consversa)

while True:
    mensagem = input("Mande uma mensagem para o chatbot:")
    if mensagem == "parar":
        break
    
    resposta = chatbot.get_response(mensagem)
    print(resposta)

#comando para apagar o banco de dados
#chatbot.storage.drop()
