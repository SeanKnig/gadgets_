from copy import deepcopy
import numpy as np
import string,random

class Wordle_Board():
    def __init__(self):
        #5x6
        self.matrix = []
        self.alphabet = string.ascii_lowercase
        self.inword = []
        self.select = [True,False]
        self.match = ['','','','','']
        self.init_guess = ['t','o','k','e','n']
        self.test_dictionary_apple = ['stars','tople','north','jugle','yodle','apple']

    def place_char(self, c, i):
        self.match[i] = c
    def is_word(self, guess):
        if guess not in self.test_dictionary_apple:
            return False
        else:
            return True
    def guess(self, i):
        guess = ''
        row = []
        options = self.inword
        for j,char in enumerate(self.match):
            if char != '':
                row.append([char, True, True])
            else:
                random_char = random.choices(self.alphabet)[0]
                if i==0:
                    #[char, matched index, inword]
                    row.append([self.init_guess[j], False, False])
                else:
                    #backtrack to match a word
                    #inword placing mechanism
                    #randomize char placement
                    if random.choices(self.select)[0] and len(options) > 0:
                        referenced_guess = random.choices(options)[0]
                        options = self.clean_list(options,referenced_guess)
                        row.append([referenced_guess, False, False])
                    else:
                        row.append([random.choices(self.alphabet)[0], False,False])
        for char,b,bb in row:
            guess+=char
        print(f'word guess: {guess}')
        return [guess, row]
    def check_match(self,word):
        for i,char in enumerate(word):
            if self.match[i] != char:
                self.match[i] = ''
            elif self.match[i] == char:
                pass
    def clean_list(self,subject,obj):
        bet = []
        for letter in subject:
            if letter == obj:
                pass
            else:
                bet.append(letter)

        subject=bet
        return subject

    def engine(self):
        #5x6
        self.matrix = []
        g = []
        #wut
        word=['p','h','o','n','y']
        #test
        count = 0

        for i in range(1200):
            count+=1
            guess = ''
            row = []
            options = self.inword
            for j,char in enumerate(self.match):
                if char != '':
                    row.append([char, True, True])
                else:
                    random_char = random.choices(self.alphabet)[0]
                    if i==0:
                        #[char, matched index, inword]
                        row.append([self.init_guess[j], False, False])
                    else:
                        #backtrack to match a word
                        #inword placing mechanism
                        #randomize char placement
                        if random.choices(self.select)[0] and len(options) > 0:
                            referenced_guess = random.choices(options)[0]
                            options = self.clean_list(options,referenced_guess)
                            row.append([referenced_guess, False, False])
                        else:
                            row.append([random.choices(self.alphabet)[0], False,False])
            for char,b,bb in row:
                guess+=char
            print(f'word guess: {guess}')
            self.matrix.append(row)
            #count = 0
            #bad complexity
            for i,c in enumerate(row):
                subject = c[0][0]
                cplace = word[i]
                print(c[0][0], word[i])
                if subject == cplace:
                    c[1] == True
                    self.place_char(subject, i)
                elif subject in word and subject != cplace:
                    #[char, attempted, [pos_history']]
                    #this is cheating?
                    self.clean_list(self.alphabet, subject)
                    if subject not in self.inword:
                        self.inword.append(subject)
                    c[2] == True

            print(f'match:   {self.match}')
            print(f'inword:   {self.inword}')
            if '' not in self.match:
                print(f'found in {count} attempts')
                exit(0)
        #print(self.inword)
        #self.inword = list(set(self.inword))


if __name__ == "__main__":
    bd = Wordle_Board()
    bd.engine()
