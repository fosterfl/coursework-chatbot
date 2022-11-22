from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# to train the chatterbot in french
frenchBot = ChatBot('TchatBot', storage_adapter='chatterbot.storage.SQLStorageAdapter', trainer = 'chatterbot.trainers.ListTrainer')
trainer = ChatterBotCorpusTrainer(frenchBot)
trainer.train("chatterbot.corpus.french")
