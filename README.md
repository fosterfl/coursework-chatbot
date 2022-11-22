![tchatbot-header](https://user-images.githubusercontent.com/17324902/203384349-885c00ad-3797-4139-8b07-2dca224edf6a.png)


# coursework-chatbot
A Chatbot I built for a class. I created the little mascot, seen above, and trained it in french. 

# Class prompt
Installer et me rendre accessible un serveur sur votre réseau privé ou bien trouver un endroit où votre FAI indique que c’est impossible du fait du NAT. Le serveur n’a pas besoin d’être compliqué : il doit accepter une connexion, y lire le message Bonjour, répondre avec Bonsoir et c’est tout.

# Sources
- I used this excellent example from Edureka for the base of making a chatbot using Python (https://www.edureka.co/blog/how-to-make-a-chatbot-in-python/)
- Training the chatterbot in french (https://github.com/gunthercox/chatterbot-corpus)

# Description of construction (en français)
- Pour faire le chatbot lui-même, j’ai commencé avec les imports normales pour la manipulation des url et des querys. Je declare le port specifique, 8080. Je declare Handler, et une liste vide. Je declare un class en ce qui je vais faire tout le travail. Je commence avec le fonction do_GET et continue avec le chargement des HTML, CSS, et des fichiers graphiques.
- Maintenant, la partie la plus interessante: les choix de Tchat. J’ai mise en place un chatbot qui vous aide avec une liste. On peut "ajoute", "supprime", "affiche" des choses sur la liste, ou demande "aide" pour rappeller les commandes.
- Avec la notice original, j’ai mis la réponse specifique “Bonsoir” si donné "Bonjour".
- Le dernier choix de la logique est de tourner vers chatterbot pour un peu de conversation. J’ai mis "read_only =True" après l’entrainment pour améliorer le temps de réponse.
- Pour bien utilise chatter-bot, il faut "entrainer" le bot. Donc, j’ai fait train-Bot.py pour charger sa base de données avec le "corpus" français de chatterbot https://github.com/gunthercox/chatterbot-corpus.
- On commence l’entrainement. Dans le terminal, j’ai mis python3 trainBot.py pour démarrer.
- Je lance mon bot avec python3 chatBot.py. Je vois que des fichiers sont chargés.
- Je navigue le navigateur vers localhost:8080 pour accès le port 8080, ou je trouve Tchat avec les mots de bienvenue voir dans le HTML.


# Finished interactions

<img alt="chatbot-2" src="https://user-images.githubusercontent.com/17324902/203381023-2d1aedb0-cd1b-4206-879e-9742fb3b303c.png">


![chatbot-3](https://user-images.githubusercontent.com/17324902/203377956-9bc1b979-8f4c-4c0b-bdf5-6f4c80db20eb.png)
