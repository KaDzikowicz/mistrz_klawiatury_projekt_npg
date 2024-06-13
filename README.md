# mistrz_klawiatury_projekt_npg
Gra polega na jak najszybszym napisaniu wyrazów pojawiających się na ekranie.

interfejs użytkownika - TUI

Funkcjonalności:
====================
1. Baza haseł z poziomami łatwy, średni, trudny co najmniej 25 w każdym.
2. Tryb nauki i wyzwania.
3. Implementacja zasad gry.
4. Statystyka wygranych.
5. Zapis/odczyt stanu gry.
6. Jedna zaproponowane przez grupę.
====================

Implementacja:
====================
- funkcja errorhandler: obsługa błędów, wyświetlanie komunikatów o błędach
- Klasa **MistrzKLawiatury**: przechowuje bazę haseł dla poziomów trudności, wybrany poziom, liczbę podjętych gier/prób, liczbę wygranych gier/prób
- funkcja _wybierz_poziom_: przydziela poziom w zależności od wyboru gracza
- funkcja _wylosuj_haslo_: potrzebna do poziomu wyzwania, losuje hasło z bazy haseł
- funkcja _graj_: podaje graczowi hasła i weryfikuje poprawność wpisanego przez gracza słowa
- funkcja _statystyki_: zwraca liczbę podjętych oraz wygranych gier/prób
- funkcja on_press: obsługuje naciśnięcia klawiszy
- funkcja reset_timer: resetuje licznik czasu
- funkcja timer_now: zwraca czas jaki nastąpił od momentu uruchomienia timera
- funkcja ask_questions: zastępuje standardową funckję 'input()'
- Klasa **Zapis_Gry**: przechowuje postępy w grze
- funkcja zapis: zapisuje stan gry do pliku zapis.txt
- funkcja odczyt: odczytuje stan gry z pliku zapis.txt
====================

Znane Problemy:
====================
- Aby zapis do pliku działał poprawnie wyłączenie antywirusa, w szczególności "automatycznej izolacji" może być konieczny 
