from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Oracle")
trainer = ListTrainer(chatbot)

while True:
    first_choice = input("Type '1' to chat with the bot\n     '2' to train the bot\n     '3' to exit\n     type 'corpus' to view training data\nChoice: ")
    
    match first_choice:
        case '2':
            print("You MUST print phrase per phrase, and press ENTER after each phrase.")
            print("Type 'exit' to close this panel.")
            while True:
                text = input("Type your phrase: ")
                if text == 'exit':
                    break
                with open("corpus.txt", "a", encoding="utf-8") as corpus:   
                    corpus.write(text + '\n')
        
        case '1':
            trainer = ListTrainer(chatbot)
            try:
                with open("corpus.txt", 'r', encoding="utf-8") as corpus:
                    data = corpus.read().splitlines()
                trainer.train(data)
                
                while True:
                    prompt = input("Me: ")
                    if prompt.lower() == 'exit':
                        break
                    response = chatbot.get_response(prompt)
                    print(f"Oracle: {response}")
            except FileNotFoundError:
                print("No training data found. Please train the bot first.")
        
        case 'corpus':
            try:
                with open("corpus.txt", 'r', encoding="utf-8") as corpus:
                    data = corpus.read()
                    if data.strip():
                        print("\n--- Your Corpus ---")
                        print(data)
                        print("--- End of Corpus ---\n")
                    else:
                        print("Your corpus is empty. Train the bot first.")
            except FileNotFoundError:
                print("No corpus file found. Train the bot first to create one.")
        
        case '3':
            print("Goodbye!")
            break
        
        case _:
            print("Not an option, try again.")