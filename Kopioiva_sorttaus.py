import os
import shutil
import tkinter as tk
from tkinter import filedialog

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

        # Kopioidaan tiedosto sitä vastaavaan kansioon
        shutil.copy2(polun_lahde, destination_path)

        print(f"Moved {filename} to {kansio}")


def browse_source():
    lahde_kansio = filedialog.askdirectory()
    source_var.set(lahde_kansio)

def browse_target():
    kohde_kansio = filedialog.askdirectory()
    target_var.set(kohde_kansio)

def sort_files():
    lahde_kansio = source_var.get()
    kohde_kansio = target_var.get()
    organize_files(lahde_kansio, kohde_kansio)

# Luodaan pää ikkuna
root = tk.Tk()
root.title("File Sorter")

# Variabelit tallettakseen lahde ja kohde kansiot
source_var = tk.StringVar()
target_var = tk.StringVar()

# UI komponentit
tk.Label(root, text="Source Directory:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=source_var).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_source).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Target Directory:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=target_var).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_target).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Sort Files", command=sort_files).grid(row=2, column=1, pady=20)

# Suorittaa loopin
root.mainloop()
