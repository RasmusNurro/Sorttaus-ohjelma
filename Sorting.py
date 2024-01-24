import json # Saadaan json tiedostosta paatteet.

with open("file_endings.json", encoding='utf8') as read_file: #otetaan tiedostosta mahdolliset paatteet
    data = json.load(read_file) #laitetaan ne funktioon 
    
print(len(data['Paatteet'][0]['Paate'])) #Varmistetaan että on oikea määrä ei ole
