meme_dict = {
            "pneumonoultramicroscopicsilicovolcanoconiosis": "enfermedad pulmonar crónica e irreversible",
            "hipopotomonstrosesquipedaliofobia": "el miedo irracional, intenso y persistente a leer o pronunciar palabras largas o complejas", "Nefelibata": "Se refiere a una persona soñadora, que anda por las nubes", "Eunoya": "Pensamiento bondadoso o belleza en la mente.", "FNAF": "Abrebiacion De Five Nights AT freddys, Juego popular credo por scott cawthon en 2014", "Meme":"unidad de información cultural (idea, comportamiento, imagen o vídeo) que se replica y difunde masivamente de persona a persona, generalmente a través de internet"}
word = input("Escribe una palabra que no entiendas: ")
if word in meme_dict.keys():
  print( meme_dict[word])
else:
    Print("No encontre la palabra, lo siento mucho")
