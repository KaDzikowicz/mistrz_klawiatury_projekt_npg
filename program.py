#import keyboard
from pynput.keyboard import Key, Listener, Controller
import random
import time
import sys 
import os

REFRESH_RATE = 0.01 #predkosc odswiezania


def errorhandler(error_name):
    print("Wystapil blad:")
    print(error_name)
    print("\nwcisnij dowolny klawisz aby kontynuowac")
    kosz = input()
    quit()

#TODO: Zapis i odczyt gry
class Zapis_Gry:
    def __init__(self) ->None:
        try:                                        #utwórz plik, jeśli jeszcze go nie ma
            self.file = open("zapis.txt", "x")
            self.file.close()
        except:
            pass
        
        try:                                        #sprawdz czy się udalo
            self.file = open("zapis.txt", "r")
            self.file.close()
            self.blad = 0
        except:
            self.blad = 1

    def zapis(self, poziom, czas, tryb, trudnosc) -> None:
        self.f = open("zapis.txt", "w")
        self.f.write(str(poziom) + "\n" + str(czas) + "\n" + str(tryb) + "\n" + str(trudnosc))
        self.f.close()
    
    def odczyt(self) -> str:
        self.f = open("zapis.txt", "r")
        poziom = int(self.f.readline())
        czas = float(self.f.readline())
        tryb = self.f.readline()
        trudnosc = self.f.readline()

        self.f.close()

        return poziom, czas, tryb, trudnosc


class MistrzKlawiatury:
    def __init__(self):
        self.user_input = ""        #łańcuch znaków wpisanych przez uzytkownika
        self.key_pressed = None
        self.cleanInput = False     #czyszczenie wejscia, jesli uzywasz funkcji input() ta zmienna MUSI byc false

        self.baza_hasel = {
            'debug': ["jabłka", "orzechy"],  # tryb testowy
            'łatwy': ['pies', 'kot', 'dom', 'auto', 'drzewo', 'jabłko', 'słońce', 'krzesło', 'telefon', 'chleb',
                      'woda', 'kawa', 'książka', 'kwiat', 'kawałek', 'ręka', 'noga', 'okno', 'telewizor', 'lampa',
                      'telefon', 'klawiatura', 'myszka', 'gra', 'film', 'muzyka', 'radio', 'piosenka', 'serce'],
            'średni': ['komputer', 'programowanie', 'telewizja', 'książka', 'muzyka', 'uniwersum', 'planeta',
                       'galaktyka', 'kosmos', 'orbita', 'satelita', 'promień', 'neutron', 'elektron', 'proton',
                       'jowisz', 'szczypiorek', 'żółć', 'saturn', 'pszczoła', 'neptun', 'pluton', 'galaktyka', 'gwiazda',
                       'teleskop', 'obserwatorium', 'teoria', 'przestrzeń', 'gwiazdozbiór'],
            'trudny': ['elektroencefalograf', 'niedopowiedzenie', 'antykonstytucyjny',
                       'konstantynopolitańczykowianeczka', 'gżegżółka', 'nadprzyrodzoność', 'antydyskryminacyjny',
                       'parametryzacja', 'wielopłaszczyznowość', 'samowystarczalność', 'polipropylenowy', 'psychofizjologia',
                       'przedstawicielstwo', 'dezoksyrybonukleinowy', 'psychoanalityk', 'najnieprzyzwoitszy',
                       'zainteresowaniom', 'niezawodnościowo', 'krzyżóweczka', 'bezwzględność', 'hipopotomonstroseskwipedaliofobia',
                       'kontrrewolucjonista', 'elektroenergetyczny', 'umiędzynarodowienie', 'słowiańszczyzna',
                       'wytrzymałościowym', 'paradoksalność', 'zastanawiający', 'przeanalizowanie']
        }
        self.poziom = None

    def wybierz_poziom(self):
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
                self.cleanInput = True
                keyboard = Controller()
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                self.cleanInput = False

        elif(key == "Key.backspace"):       #zapobieganie rekurencji przy jednoczesnym zachowaniu funkcji backspace
            if(self.cleanInput == False):
                self.user_input = self.user_input[:-1]
            pass
        else:
            self.key_pressed = key

        
   

    def reset_timer(self):              #do resetowania timera :)
        self.start_time = time.time()
    
    def timer_now(self):
        return time.time() - self.start_time

    def ask_question(self, question : str) -> str:
        """Funkcja jest alternatywa funkcji input()

        :param str question: lancuch znakow z pytaniem dla uzytkownika
        :return: wejscie uzytkownika
        """
        self.user_input = ""
        self.key_pressed = None         #potrzebne żeby przypadkiem nie wczytało entera z poprzedniej funkcji
        os.system('cls')
        sys.stdout.write(question+"\n\n")
        
        while(self.key_pressed != "Key.enter"):
            
            

            if self.key_pressed != None:
                if len(self.key_pressed) == 1:
                    self.user_input += self.key_pressed
                    self.key_pressed = None

            #wyswietlanie
            sys.stdout.flush()
            
            sys.stdout.write("\033[0F\x1b[0K"+"Twój czas: {0:.1f}\n".format(self.timer_now())) #Bawienie się kursorem żeby nie było "mrugania"
            sys.stdout.write("\033[0K"+self.user_input)
            
            

            listener.join(REFRESH_RATE)

        return self.user_input



    #TODO: Funkcja graj:
    def graj(self):
        os.system('cls')
        nowagra = Zapis_Gry()

        if(nowagra.blad == 1):
            errorhandler("zapis pliku nie powiodl sie")
            
        exitflag = False

        print("Witaj w grze Mistrz Klawiatury!")
        while exitflag == False:
            if(nowagra.odczyt()[0] != 0):
                os.system('cls')
                wejscie = input("Wykryto niedokończoną grę, czy chcesz ją wczytać? (tak/nie)")
                if wejscie == "tak":
                    pass
                else:
                    self.wybierz_poziom()

            hasla = self.baza_hasel[self.poziom] if self.poziom != 'wyzwanie' else self.baza_hasel['wyzwanie']

            self.reset_timer()

            for i, haslo in enumerate(hasla):
                
                nowagra.zapis(i, self.timer_now(), 0, 0)

                slowo = self.ask_question("Twoje hasło to: " + haslo + "\nZacznij pisać:")

                while slowo != haslo:
                    slowo = self.ask_question("Niepoprawne hasło. Spróbuj ponownie.\n"+"Twoje hasło to: " + haslo+"\nZacznij pisać:")
            

            ostateczny_czas = self.timer_now()

            kontynuuj = ""
            os.system('cls')

            nowagra.zapis(0, ostateczny_czas, "nie", "nie")

            while kontynuuj != "tak": 
                print("Czy chcesz zagrać ponownie? (tak/nie)")
                kontynuuj = input().lower()
                os.system('cls')
                if kontynuuj == 'nie':
                    exitflag = True
                    break

    def statystyki(self):
        print("Liczba prób:", self.liczba_prob)
        print("Liczba wygranych gier:", self.liczba_poprawnych)


if __name__ == "__main__":
    gra = MistrzKlawiatury()
    listener = Listener(on_press=gra.on_press)
    listener.start()
    gra.graj()
    listener.stop()
