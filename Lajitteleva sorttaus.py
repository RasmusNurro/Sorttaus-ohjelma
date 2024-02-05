import os
import shutil

def organize_files():
    # Saadaan selville mistä otetaan tiedostot
    lahde = input("Enter the path of the source directory: ")
    
    # Varmistetaan että on oikea lähde
    if not os.path.exists(lahde):
        print(f"Error: Source directory '{lahde}' does not exist.")
        return

    # Selvitetään mihin kansioon tiedostot viedään
    kohde_kansio = input("Enter the path of the target directory: ")

    # Luodaan polku jos ei ennudestaan ole olemassa
    if not os.path.exists(kohde_kansio):
        os.makedirs(kohde_kansio)

    # Lajittelee tiedostot lähde kansiosta
    for filename in os.listdir(lahde):
        polun_lahde = os.path.join(lahde, filename)

        # Skippaa kansiot
        if os.path.isdir(polun_lahde):
            continue

        # Saadaan tiedostojen päätteet
        _, tiedosto_paatteet = os.path.splitext(filename)
        tiedosto_paatteet = tiedosto_paatteet.lower()

        # Luokitellaan tiedostot mihin eri tyyppiset tiedostot menevät
        folders = {
            '.txt': 'TextFiles',
            '.pdf': 'PDFs',
            '.jpg': 'Images',
            '.png': 'Images',
            '.mp3': 'Audio',
            '.mp4': 'Videos',
            '.py': 'PythonFiles',
            #'.pääte' : 'KansioNimi', <- Tuolla tavalla
            # Tarpeitten mukaan voi lisätä lisää lajiteltavia
        }

        # Määritetään kohdekansio tiedostopäätteen avulla
        kansio = folders.get(tiedosto_paatteet, 'OtherFiles')
        kansio_path = os.path.join(kohde_kansio, kansio)

        # Luodaan kohdekansio, jos sitä ei ole
        if not os.path.exists(kansio_path):
            os.makedirs(kansio_path)

        # Muodostetaan tiedoston kohdepolku
        destination_path = os.path.join(kansio_path, filename)

        # Siirretään tiedosto sitä vastaavaan kansioon
        shutil.move(polun_lahde, destination_path)

        print(f"Moved {filename} to {kansio}")

# Aloita organisaatioprosessi funktio toiminnolla
organize_files()
