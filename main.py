meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "SIX SEVEN": "Meme gracioso",
            "XD": "Una reaccion",
            "CREEPY": "aterrador, siniestro",
            "tralalero tralala": "meme brainrot igual que el six seven",
            "funar": "cancelar",
            }
word = input("Escribe una palabra que no entiendas:").upper()
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print ("el significado es",meme_dict[word])
else:
     print("no e encontrado la palabra")
    # ¿Qué hacer si no se encuentra la palabra?
