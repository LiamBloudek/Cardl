import customtkinter as customtkinter
from PIL import Image 
import random


CARD_NUMBER = 5
FONT = 'Press Start 2P'
NUM_OF_GUESSES = 5

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.guessed = False
        self.suit_guessed = False
        self.number_guessed = False
    def show_card(self):
        return f'{self.number} of {self.suit}'

class Card_image:
    def __init__(self, Card, number_color='gray', suit_color='gray'):
        self.number = Card.number
        self.suit = Card.suit

        self.card_image = Image.open("cardle/images/card_default.png")
        self.suit_image = Image.open(f'cardle/images/suit_{self.suit}.png')
        self.number_image = Image.open(f'cardle/images/number_{self.number}.png').convert('RGBA')
        self.corner_image = Image.open(f'cardle/images/corner_{self.number}.png').convert('RGBA')

        if number_color == 'green':
            self.pixels = self.number_image.load()
            for x in range(self.number_image.width):
                for y in range(self.number_image.height):
                    r, g, b, a = self.pixels[x, y]
                    if (r, g, b) != (255, 255, 255):
                        self.pixels[x, y] = (0, 255, 0, a)
            self.pixels = self.corner_image.load()
            for x in range(self.corner_image.width):
                for y in range(self.corner_image.height):
                    r, g, b, a = self.pixels[x, y]
                    if (r, g, b) != (255, 255, 255):
                        self.pixels[x, y] = (0, 255, 0, a)

        if number_color == 'yellow':
            self.pixels = self.number_image.load()
            for x in range(self.number_image.width):
                for y in range(self.number_image.height):
                    r, g, b, a = self.pixels[x, y]
                    if (r, g, b) != (255, 255, 255):
                        self.pixels[x, y] = (255, 255, 0, a)
            self.pixels = self.corner_image.load()
            for x in range(self.corner_image.width):
                for y in range(self.corner_image.height):
                    r, g, b, a = self.pixels[x, y]
                    if (r, g, b) != (255, 255, 255):
                        self.pixels[x, y] = (255, 255, 0, a)

        if suit_color == 'green':
            self.pixels = self.suit_image.load()
            for x in range(self.suit_image.width):
                for y in range(self.suit_image.height):
                    r, g, b, a = self.pixels[x, y]
                    if r != 255 and g != 255 and b != 255:
                        self.pixels[x, y] = (0, 255, 0, a)

        if suit_color == 'yellow':
            self.pixels = self.suit_image.load()
            for x in range(self.suit_image.width):
                for y in range(self.suit_image.height):
                    r, g, b, a = self.pixels[x, y]
                    if r != 255 and g != 255 and b != 255:
                        self.pixels[x, y] = (255, 255, 0, a)

        self.card_image.paste(self.suit_image, (10, 10))
        if self.number == ('Jack') or self.number == 'Queen' or self.number == 'King':
            print('Done')
            self.card_image.paste(self.number_image, (10, 35))
        else:
            print(self.number)
            self.card_image.paste(self.number_image, (40, 50))
        self.card_image.paste(self.suit_image, (77, 110))
        self.card_image.paste(self.corner_image, (77, 10))
        self.card_image.save('result.png')

        self.card_image = customtkinter.CTkImage(light_image=Image.open('result.png'), dark_image=Image.open('result.png'), size=(200,200))

class Spinbox(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.master = master
        self.title = title
        self.width = 100
        self.height = 32
        self.command = None
        self.step_size=1
        self.img_list = []

        self.grid_columnconfigure(1, weight=3)

        self.title = customtkinter.CTkLabel(self, text=self.title, font= (FONT, 12), fg_color="White", border_color='black', corner_radius=0, border_width=3, )
        self.title.grid(row=0, column=0, sticky="ew", columnspan=3)
        for i in [1, 2]:

            if i == 1:
                self.entry_1 = customtkinter.CTkEntry(self, width=self.width-(2*self.height), font= (FONT, 10), border_color='black', corner_radius=0, border_width=3, height=self.height-6)
                self.entry_1.grid(row=i, column=1, columnspan=1, padx=1, pady=1, sticky="ew")                            
                self.entry_1.insert(0, 'X')

                self.subtract_button = customtkinter.CTkButton(self, text="<", font= (FONT, 9), fg_color='white', text_color='black', border_color='black', corner_radius=0, border_width=3, width=self.height-6, height=self.height-6,
                                                       command=self.down_button_1)
                self.subtract_button.grid(row=i, column=0, padx=(3, 0), pady=3)

                self.add_button = customtkinter.CTkButton(self, text=">", font= (FONT, 9), fg_color='white', text_color='black', border_color='black', corner_radius=0, border_width=3, width=self.height-6, height=self.height-6,
                                                  command= self.up_button_1)
                self.add_button.grid(row=i, column=2, padx=(0, 3), pady=3)

            else:
                self.entry_2 = customtkinter.CTkEntry(self, width=self.width-(2*self.height), font= (FONT, 9), border_color='black', border_width=3, corner_radius=0,height=self.height-6)
                self.entry_2.grid(row=i, column=1, columnspan=1, padx=1, pady=1, sticky="ew")
                self.entry_2.insert(0, 'X')

                self.subtract_button = customtkinter.CTkButton(self, text="<", font= (FONT, 9), fg_color='white', text_color='black', border_color='black', corner_radius=0, border_width=3, width=self.height-6, height=self.height-6,
                                                       command=self.down_button_2)
                self.subtract_button.grid(row=i, column=0, padx=(3, 0), pady=3)

                self.add_button = customtkinter.CTkButton(self, text=">", font= (FONT, 9), fg_color='white', text_color='black', border_color='black', corner_radius=0, border_width=3, width=self.height-6, height=self.height-6,
                                                  command=self.up_button_2)
                self.add_button.grid(row=i, column=2, padx=(0, 3), pady=3)

    def up_button_1(self):
        iterate_list = ['X','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        value = iterate_list.index(self.entry_1.get())
        self.entry_1.delete(0,'end')
        if value >= len(iterate_list)-1:
            value = -1
        elif value < 0:
            value = len(iterate_list)-1
        self.entry_1.insert(0, iterate_list[value+1])
        self.new_card_im()

    def down_button_1(self):
        iterate_list = ['X','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        value = iterate_list.index(self.entry_1.get())
        self.entry_1.delete(0,'end')
        if value >= len(iterate_list)-1:
            value = -1
        elif value < 0:
            value = len(iterate_list)-1
        self.entry_1.insert(0, iterate_list[value-1])
        self.new_card_im()

    def up_button_2(self):
        iterate_list = ['X','Clubs', 'Spades', 'Diamonds', 'Hearts']
        value = iterate_list.index(self.entry_2.get())
        self.entry_2.delete(0,'end')
        if value >= len(iterate_list)-1:
            value = -1
        elif value < 0:
            value = len(iterate_list)-1
        self.entry_2.insert(0, iterate_list[value+1])
        self.new_card_im()

    def down_button_2(self):
        iterate_list = ['X','Clubs', 'Spades', 'Diamonds', 'Hearts']
        value = iterate_list.index(self.entry_2.get())
        self.entry_2.delete(0,'end')
        if value >= len(iterate_list)-1:
            value = -1
        elif value < 0:
            value = len(iterate_list)-1
        self.entry_2.insert(0, iterate_list[value-1])
        self.new_card_im()

    def get(self):
        entries = []
        entries.append(self.entry_1.get())
        entries.append(self.entry_2.get())
        return entries

    def new_card_im(self):
        for i in range(len(self.img_list)):
            card_im = Card_image(Card(self.entry_1.get(), self.entry_2.get()))
            for j in range(len(self.img_list[i])):
                    #card_im = Card_image(Card(self.entry_1.get(), self.entry_2.get()))
                    self.img_list[i][j].configure(image=card_im.card_image)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.spinboxes = []
        self.img_list=[]
        self.placed_images = []
        self.restart()
        self.title('Cardl')
        self.guesses = 0
        self.textbox = 0
        self.geometry('800x600')
        self.grid_columnconfigure((tuple(range(CARD_NUMBER))), weight=1)
        self.grid_rowconfigure((2, 3, 4), weight = 4)

        self.button_guess = customtkinter.CTkButton(self, text="Make Guess", font=('Press Start 2P', 12), text_color = 'black', fg_color='white', border_color='black', border_width=5, corner_radius=0, command=self.guess)
        self.button_guess.grid(row=NUM_OF_GUESSES+3, column=0, padx=10, pady=10, sticky="ew", columnspan=CARD_NUMBER)

        self.button_restart = customtkinter.CTkButton(self, text="Restart", font=('Press Start 2P', 12), text_color = 'black', fg_color='white', border_color='black', border_width=5, corner_radius=0, command=self.restart)
        self.button_restart.grid(row=NUM_OF_GUESSES+4, column=0, padx=10, pady=10, sticky="ew", columnspan=CARD_NUMBER)

    def guess(self):
        guess = []
        card_guess = []
        self.guesses += 1

        if self.textbox != 0:
            return
        
        for i in range(CARD_NUMBER):
            print(f"Card {i+1} guess:", self.spinboxes[i].get())
            guess.append(self.spinboxes[i].get())
            card_guess.append(Card(self.spinboxes[i].get()[0], self.spinboxes[i].get()[1]))


        result_numbers = ['gray'] * len(guess)
        remaining = {}

        for i in range(CARD_NUMBER):
            if guess[i][0] == self.draw[i].number:
                result_numbers[i] = "green"
            else:
                remaining[self.draw[i].number] = remaining.get(self.draw[i].number, 0) + 1

        for i in range(len(guess)):
            if result_numbers[i] == "green":
                continue

            if remaining.get(guess[i][0], 0) > 0:
                result_numbers[i] = "yellow"
                remaining[guess[i][0]] -= 1

        print(result_numbers)

        result_suits = ['gray'] * len(guess)
        remaining = {}

        for i in range(CARD_NUMBER):
            if guess[i][1] == self.draw[i].suit:
                result_suits[i] = "green"
            else:
                remaining[self.draw[i].suit] = remaining.get(self.draw[i].suit, 0) + 1

        for i in range(len(guess)):
            if result_suits[i] == "green":
                continue

            if remaining.get(guess[i][1], 0) > 0:
                result_suits[i] = "yellow"
                remaining[guess[i][1]] -= 1

        print(result_suits)
        img_list = []
        for i, card in enumerate(card_guess):
                img_list = []
                #for j in range(CARD_NUMBER):
                    #card_im = Card_image(card, result_numbers[i], result_suits[i])
                    #card_label = customtkinter.CTkLabel(self, image=card_im.card_image, text='')
                card_im_2 = Card_image(card, result_numbers[i], result_suits[i])
                card_label_2 = customtkinter.CTkLabel(self, image=card_im_2.card_image, text='')
                img_list.append(card_label_2)
                self.spinboxes[i].img_list.append(img_list)

        for i, spinbox in enumerate(self.spinboxes):
            for j, img_list in enumerate(spinbox.img_list):
                for k in img_list:

                    new_image = customtkinter.CTkLabel(self,image=k.cget("image"), text="")
                    new_image.place(x=45+(self.guesses*12) + (i * 307),y=290 + 34 * self.guesses)        
                    self.placed_images.append(new_image)

        print('Done!')

        if result_numbers == (['green']*CARD_NUMBER) and result_suits == (['green']*CARD_NUMBER):
            self.remove_textbox()
            self.textbox = customtkinter.CTkLabel(self,width=500,height=150, text = 'You Win!\n Press restart to play again', border_color='black', border_width=5, font=(FONT, 15))
            self.textbox.place(relx=0.5, rely=0.5, anchor="center")

        elif self.guesses > NUM_OF_GUESSES and result_numbers != (['green']*CARD_NUMBER) and result_suits != (['green']*CARD_NUMBER):
            self.remove_textbox()
            self.textbox = customtkinter.CTkLabel(self,width=500,height=150, text = 'You Loose!\n Press restart to play again', border_color='black', border_width=5, font=(FONT, 15))
            self.textbox.place(relx=0.5, rely=0.5, anchor="center")
            return

    def restart(self):
        self.spinboxes = []
        self.img_list = []
        self.deck = []
        self.guesses = 0
        self.remove_textbox()
        self.textbox = 0

        for i in self.placed_images:
            i.destroy()
        self.placed_images = []

        for i in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
            self.deck.append(Card(i, 'Clubs'))
            self.deck.append(Card(i, 'Spades'))
            self.deck.append(Card(i, 'Diamonds'))
            self.deck.append(Card(i, 'Hearts'))    

        self.draw = []
        for j in range(NUM_OF_GUESSES+2):
            for i in self.grid_slaves(row=j+1):
                i.destroy()

        for i in range(CARD_NUMBER):
            card_number = random.randint(0, len(self.deck)-1)
            self.draw.append(self.deck[card_number])
            self.deck.pop(card_number)

        for i in self.draw:
            print(i.show_card())

        for i in range(CARD_NUMBER):
            #for j in range(CARD_NUMBER):
                img_list = []
                card_im = Card_image(Card('X', 'X'))
                card_label = customtkinter.CTkLabel(self, image=card_im.card_image, text='')
                card_label.grid(row=2, column=i, padx=0, pady=20, sticky='n')
                img_list.append(card_label)
                spinbox = Spinbox(self, f'Card {i+1}')
                spinbox.grid(row=0, column=i, padx=5, pady=5, sticky='nsew', columnspan=1)
                self.spinboxes.append(spinbox)
                self.spinboxes[i].img_list.append(img_list)

        self.number_amounts = []
        self.suit_amounts = []

        for i, card in enumerate(self.draw):
            self.suit_amounts.append(card.suit)
            self.number_amounts.append(card.number)

    def remove_textbox(self):
        try:
            self.textbox.destroy()
        except:
            return

app = App()
app.mainloop()