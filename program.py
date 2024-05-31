#import keyboard
from pynput.keyboard import Key, Listener, Controller
import random
import time
import sys 
import os

REFRESH_RATE = 0.05 #predkosc odswiezania

class MistrzKlawiatury:
    def __init__(self):
        self.user_input = "" #łańcuch znaków wpisanych przez uzytkownika
        self.key_pressed = None
        self.cleanInput = False #czyszczenie wejscia, jesli uzywasz funkcji input() ta zmienna MUSI byc false

        self.baza_hasel = {
            'debug': ["jabłka", "orzechy"],  # tryb testowy
            'łatwy': ['pies', 'kot', 'dom', 'auto', 'drzewo', 'jabłko', 'słońce', 'krzesło', 'telefon', 'chleb',
                      'woda', 'kawa', 'książka', 'kwiat', 'kawałek', 'ręka', 'noga', 'okno', 'telewizor', 'lampa',
                      'telefon', 'klawiatura', 'myszka', 'gra', 'film', 'muzyka', 'radio', 'piosenka', 'serce'],
            'średni': ['komputer', 'programowanie', 'telewizja', 'książka', 'muzyka', 'universum', 'planeta',
                       'galaktyka', 'kosmos', 'orbita', 'satelita', 'promień', 'neutron', 'elektron', 'proton',
                       'jupiter', 'mars', 'wenus', 'saturn', 'uran', 'neptun', 'pluton', 'galaktyka', 'gwiazda',
                       'teleskop', 'obserwatorium', 'teoria', 'przestrzeń', 'gwiazdozbiór'],
            'trudny': ['elektroencefalograf', 'hippopotomonstrosesquippedaliophobia', 'antykonstytucyjny',
                       'konstantynopolitańczykowianeczka', 'autostrada', 'hipopotam', 'elektrownia',
                       'parametryzacja', 'podstawowonarodowoska', 'krzyżówka', 'pseudokibic', 'psychofizjologia',
                       'przedstawicielstwo', 'przedstawicielski', 'psychoanalityk', 'sztucznojądrowy',
                       'zainteresowaniom', 'niezawodnościowo', 'krzyżóweczka', 'bezwzględność', 'odporonośrodek',
                       'pszenżytożercy', 'elektroenergetyczny', 'przedstawicielskie', 'słowiańszczyzna',
                       'wytrzymałościowym', 'paradoksalizm', 'zastanawiający', 'przeanalizowanie']
        }
        self.poziom = None

    def wybierz_poziom(self):
        os.system('cls')                        # czyszczenie konsoli
        print("Wybierz tryb: nauka, wyzwanie")
        tryb = input().lower()                  # wybór trybu
        os.system('cls')

        if tryb == 'nauka':
            print("Wybrano tryb nauka!")
            print("Wybierz poziom trudności: łatwy, średni, trudny")
            self.poziom = input().lower()

            while self.poziom not in ['debug', 'łatwy', 'średni', 'trudny']:
                print("Niepoprawny poziom. Spróbuj ponownie.")
                self.poziom = input().lower()

        elif tryb == 'wyzwanie':
            print("Wybrano tryb wyzwanie!\n")
            self.poziom = 'wyzwanie'
        else:
            os.system('cls')
            print("Niepoprawny tryb.")
            self.wybierz_poziom()

        if self.poziom == 'wyzwanie':
            print("Tryb wyzwania został wybrany. Musisz napisać 10 haseł.")
            self.baza_hasel['wyzwanie'] = random.sample(self.baza_hasel['łatwy'] + self.baza_hasel['średni'] + self.baza_hasel['trudny'], 10)
            self.start_time = time.time()

    def wylosuj_haslo(self):
        if self.poziom == 'wyzwanie':
            return random.choice(self.baza_hasel['wyzwanie'])
        else:
            return random.choice(self.baza_hasel[self.poziom])
        
    def on_press(self, key) -> None:        #funkcja wykonuje sie po wcisnieciu klawisza, zwraca literke po wcisnieciu literki lub lancuch znakow Key.<nazwa klawisza> dla znaków specjalnych (np "Key.enter")
        key = str(key)
        if(len(key) == 3):
            self.key_pressed = key[1]
            
            if self.cleanInput:
                keyboard = Controller()
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)

        elif(key == "Key.backspace"):       #zapobieganie rekurencji
            pass
        else:
            self.key_pressed = key

        
    
    

    def ask_question(self, question : str, with_timer : bool = True) -> str:
        """Funkcja jest alternatywa funkcji input()

        :param str question: lancuch znakow z pytaniem dla uzytkownika
        :param bool with_timer: zmienna decydujaca czy wyswietlac czas
        :return: wejscie uzytkownika
        """
        
        self.cleanInput = True          #bez tego wyskakuje blad na koniec programu
        self.start_time = time.time()
        self.key_pressed = None         #potrzebne żeby przypadkiem nie wczytało entera z poprzedniej funkcji
        while(self.key_pressed != "Key.enter"):
            
            self.displayed_time = time.time() - self.start_time

            if self.key_pressed != None:
                if len(self.key_pressed) == 1:
                    self.user_input += self.key_pressed
                    self.key_pressed = None

            #wyswietlanie
            os.system('cls')
            sys.stdout.write(question + "\n")
            if with_timer:
                sys.stdout.write("Twój czas: {0:.1f}\n".format(self.displayed_time))
            sys.stdout.write(self.user_input)
            sys.stdout.flush() 

            listener.join(REFRESH_RATE)

        self.cleanInput = False
        return self.user_input



    #TODO: Funkcja graj:
    def graj(self):
        #placeholder

        self.wybierz_poziom()

        #przykładowe użycie funkcji ask question:
        tekst = self.ask_question(self.wylosuj_haslo())
        print("\nwpisany tekst: " + tekst)
        

        




if __name__ == "__main__":

    # Collect events until released
    gra = MistrzKlawiatury()

    listener = Listener(on_press=gra.on_press)
    listener.start()
    gra.graj()
    listener.stop()
