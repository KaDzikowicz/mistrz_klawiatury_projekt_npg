import random
import time
import os

class MistrzKlawiatury:
    def __init__(self):
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
        print("Wybierz tryb: nauka, wyzwanie")
        tryb = input().lower()  # wybór trybu
        os.system('cls')  # czyszczenie konsoli

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