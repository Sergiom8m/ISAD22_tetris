from playsound import playsound
import pygame
import os

class Soinuak():
    def __init__(self):
        super(Soinuak, self).__init__()

    def play_rotate(self):
        path= os.path.join("/soinuak", "rotate.wav")
        playsound(os.getcwd() + path, False)  # "False" asinkronoa egiteko eta programa ez gelditzeko

    def play_fall(self):
        path = os.path.join("/soinuak", "encajar.wav")
        playsound(os.getcwd() + path, False)  # "False" asinkronoa egiteko eta programa ez gelditzeko

    def play_crash(self):
        path = os.path.join("/soinuak", "crash.wav")
        playsound(os.getcwd() + path, False)  # "False" asinkronoa egiteko eta programa ez gelditzeko

    def play_music(self, musika):
        pygame.quit()
        pygame.init()
        pygame.mixer.init()
        if musika != "ez":
            if musika == "original":
                path = os.path.join("/soinuak/musika", "Original_Tetris_Theme.wav")
            elif musika == "99":
                path = os.path.join("/soinuak/musika", "Tetris_99_Main_Theme.wav")
            elif musika == "orchestra":
                path = os.path.join("/soinuak/musika", "Tetris_Orchestra.wav")
            elif musika == "piano":
                path = os.path.join("/soinuak/musika", "Tetris_Piano_Version.wav")
            abestia = pygame.mixer.Sound(os.getcwd() + path)
            pygame.mixer.Sound.play(abestia, -1)

    def quit_music(self):
        pygame.quit()
