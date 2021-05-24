from flask import Flask, render_template, request

"""from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Friend') #create the bot

bot.set_trainer(ListTrainer) # Teacher

#bot.train(conv) # teacher train the bot

for knowledeg in os.listdir('base'):
	BotMemory = open('base/'+ knowledeg, 'r').readlines()
	bot.train(BotMemory)"""
from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path='C:/Users\Priti\Desktop\chatterbot_corpus\data\english/'
for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

while True:
    message = input('You:')
    print(message)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        print('ChatBot:', reply)



app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('qwerty.html')


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
	user_input=request.form['user_input']
	
	a=open("Vanalyse.txt","a")
	#a.write(user_input)
	if (user_input=="Bye"):
		a.close()
	else:
		a.write(user_input+"\n")
	bot_response=bot.get_response(user_input)
	bot_response=str(bot_response)
	if(user_input =="Bye"):
		bot_response="Bye"
		print(bot_response)
		os.system('python chatbotsenti.py')
	else:
		print("Chatbot: "+bot_response)
	
	return render_template('index.html',user_input=user_input,
		bot_response=bot_response
		)


if __name__=='__main__':
	app.run(debug=True,port=5000)
       # app.run()

