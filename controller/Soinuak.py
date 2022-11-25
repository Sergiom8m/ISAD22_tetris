from playsound import playsound
import pygame
import os

class Soinuak():
    def __init__(self):
        super(Soinuak, self).__init__()

    def play_rotate(self):
        playsound(os.getcwd() + "/soinuak/rotate.wav", False)  # "False" asinkronoa egiteko eta programa ez gelditzeko

    def play_fall(self):
        playsound(os.getcwd() + "/soinuak/encajar.wav", False)  # "False" asinkronoa egiteko eta programa ez gelditzeko

    def play_crash(self):
        playsound(os.getcwd() + "/soinuak/crash.wav", False)  # "False" asinkronoa egiteko eta programa ez gelditzeko

    def play_music(self, musika):
        pygame.quit()
        pygame.init()
        pygame.mixer.init()
        if musika != "ez":
            if musika == "original":
                abestia = pygame.mixer.Sound(os.getcwd() + "/soinuak/musika/Original_Tetris_Theme.wav")
            elif musika == "99":
                abestia = pygame.mixer.Sound(os.getcwd() + "/soinuak/musika/Tetris_99_Main_Theme.wav")
            elif musika == "orchestra":
                abestia = pygame.mixer.Sound(os.getcwd() + "/soinuak/musika/Tetris_Orchestra.wav")
            elif musika == "piano":
                abestia = pygame.mixer.Sound(os.getcwd() + "/soinuak/musika/Tetris_Piano_Version.wav")
            pygame.mixer.Sound.play(abestia, -1)

    def quit_music(self):
        pygame.quit()
