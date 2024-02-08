import random
import os

class Hangman():

    def __init__(self):

        self.words = []
        self.load_words()

        self.current_word = ''
        self.user_gueses = []
        self.words_guessed = 0

        self.art_stage = 0
        self.art = [  
'''+---+
    |
    |
    |
   ===''', '''
+---+
O   |
    |
    |
   ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']
        
    def load_words(self):
        try:
            with open('words.txt', 'r') as words_file:
                self.words = list(map(lambda x: x.replace('\n', ''), words_file.readlines()))
        except Exception:
            print(Exception)

    def load_word_strings(self):

        output = ''

        for i in self.current_word:
            if i in self.user_gueses:
                output += f'{i} '
            else:
                output += '_ '

        return f'{output}\n'
    
    def check_user_guessed_word(self):
        
        letters = sorted(list(set([a for a in self.current_word])))
        user_inputs = sorted(self.user_gueses)
        print(letters, user_inputs)
        
        return letters == user_inputs

    def main(self):
        self.current_word = self.words[random.randint(0,len(self.words)-1)]

        print(self.current_word)

        while True:
            if self.art_stage < 6:
                print(f'{self.art[self.art_stage]}')
                print(self.load_word_strings())
                guess = input(':> ')

                if len(guess) == 1:
                    if guess in self.current_word and guess not in self.user_gueses:
                        self.user_gueses.append(guess)
                        if self.check_user_guessed_word():
                            print(f'{self.art[self.art_stage]}')
                            print(self.load_word_strings())
                            self.user_gueses = []
                            self.words_guessed += 1
                            self.art_stage = 0
                            user_choice = input(f'Good, see the word is {self.current_word}, would you like to continue?> ')
                        
                            if user_choice in ['y', 'Y', 'YES', 'yes', 'Yes', '1', 'ok', 'go', 'leego']:
                                self.main()

                            elif user_choice in ['n', 'N', 'NO', 'no', 'No', '0', 'stop']:
                                print(f'Ok, your score is {self.words_guessed}, have a good one.\nP.S.: bet even my granny can beat those numbers:((')
                                break
                    else:
                        self.art_stage += 1
                        print(f'Nope')
                else:
                    if guess == self.current_word:
                        self.user_gueses = []
                        self.words_guessed += 1
                        self.art_stage = 0
                        choice = input('Well done, this is the word, took you long enough:(, would you like to continue?\n:> ')

                        if choice in ['y', 'Y', 'YES', 'yes', 'Yes', '1', 'ok', 'go', 'leego']:
                            self.main()
                        elif choice in ['n', 'N', 'NO', 'no', 'No', '0', 'stop']:
                            print(f'Ok, your score is {self.words_guessed}, have a good one.\nP.S.: bet even my granny can beat those numbers:((')
                            break
                    else:
                        self.art_stage += 1
                        print(f'Nope')
            else:
                print(f'{self.art[self.art_stage]}')
                print(self.load_word_strings())
                print(f'You have no tries left and been hanged! BTW, the word was {self.current_word}')
                break
        
        
if __name__ == '__main__':
    hangman = Hangman()
    hangman.main()