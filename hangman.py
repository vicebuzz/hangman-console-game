import random
import os

class Hangman():

    def __init__(self):

        self.words = []
        self.load_words()

        self.current_word = ''
        self.user_gueses = []

        self.tries = 20
        self.words_guessed = 0

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
        self.art_period = 0
        self.art_stage = 0


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

        return output
    
    def check_user_guessed_word(self):
        
        if ''.join(self.user_gueses) == self.current_word:
            return True
        return False
    
    def choose_diffuculty(self):

        diff_to_tries = {
            '1':21,
            '2':14,
            '3':7,
            '4':1
        }

        diffuculty = input('Please choose a diffuculty:\n1. Easy - 21 tries\n2. Medium - 14 tries\n3. Hard - 7 tries\n:> ')

        if diffuculty in ['1','2','3']:
            self.tries = diff_to_tries[diffuculty]
            self.art_period = self.tries/7

    def play(self, tries):

        self.current_word = self.words[random.randint(0,len(self.words))]

        period_count = 0

        while True:
            print(self.art[self.art_stage])
            print(self.load_word_strings())
            guess = input(':> ')

            if len(guess) == 1:
                if guess in self.current_word:
                    self.user_gueses.append(guess)

                    if self.check_user_guessed_word():
                        user_choice = input(f'Good, see the word is {self.current_word}, would you like to continue?> ')
                        
                        if user_choice in ['y', 'Y', 'YES', 'yes', 'Yes', '1', 'ok', 'go', '12XU']:

                            self.words_guessed += 1
                            self.play()

                        elif user_choice in ['n', 'N', 'NO', 'no', 'No', '0', 'stop']:
                            
                            print(f'Ok, you have guessed {self.words_guessed} from {self.tries - tries} tries, have a good one.')
                            break
                else:
                    tries -= 1
                    period_count += 1
                    if period_count == self.art_period:
                        self.art_stage += 1
                        period_count = 0
                    print(f'Nope, you have {tries} left')
            else:
                if guess == self.current_word:
                    choice = input('Well done, this is the word, took you long enough:(, would you like to continue?\n:>')

                    if choice in ['y', 'Y', 'YES', 'yes', 'Yes', '1', 'ok', 'go', '12XU']:
                        self.words_guessed += 1
                        self.play(self.tries)

                    elif choice in ['n', 'N', 'NO', 'no', 'No', '0', 'stop']:
                        print(f'Ok, you have guessed {self.words_guessed} from {self.tries - tries} tries, have a good one.')
                        break
                else:
                    tries -= 1
                    period_count += 1
                    if period_count == self.art_period:
                        self.art_stage += 1
                        period_count = 0
                    print(f'Nope, you have {tries} left')


    def main(self):
        self.choose_diffuculty()
        tries_default = self.tries
        self.play(tries_default)
        
        
if __name__ == '__main__':
    hangman = Hangman()
    hangman.main()