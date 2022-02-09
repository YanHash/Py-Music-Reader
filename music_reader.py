def READER ():
    """
    Lit des fichiers audio entrés en input 
    """
    from pygame import mixer 
    mixer.init()
    
    musique = input("un titre:")
    
    mixer.music.load(musique)
    mixer.music.set_volume(0.7)
    mixer.music.play(0)

    while True:
        print("'P' pour pause, 'R' pour reprendre")
        print("'Q' pour quitter")
        res = input('>>> ')
    
        if res == 'P':
            mixer.music.pause()
        elif res == 'R':
            mixer.music.unpause()
        elif res == 'Q':
            mixer.music.stop()
        break
    
READER()