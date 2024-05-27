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
