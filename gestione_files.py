#importo la libreria json per gestire i file json
import json

#Funzione che salva i dati sul file
def salva_dati(lista_spese, nome_file="spese.json"):
    with open(nome_file, "w") as f: #Apro il file in scrittura, se il file non c'è lo crea, se c'è lo sovvrascrive
        json.dump(lista_spese, f, indent=4)
        #indent=4 serve per rendere leggibile il file se aperto con il blocco note
#Funzione per caricare i dati dal file (Lettura)
def carica_dati(nome_file = "spese.json"):
#Se il file non esiste (è la prima volta che usi il programma),
# Python darebbe errore. Noi gestiamo l'errore restituendo una lista vuota.
  try:
     with open(nome_file, "r") as f:
        dati_caricati = json.load(f)
        return dati_caricati
  except (FileNotFoundError, json.JSONDecodeError):
     return [] #Se il file non esiste ritorno una stringa vuota
     
