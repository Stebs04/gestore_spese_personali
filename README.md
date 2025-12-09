# 💰 Gestore Spese Personali

Un'applicazione CLI (Command Line Interface) scritta in Python per gestire le proprie spese quotidiane in modo semplice e veloce.
Questo progetto è stato realizzato per esercitarsi con la logica di programmazione, la manipolazione di liste/dizionari e il salvataggio dati su file JSON.

## 🚀 Funzionalità

* **Aggiungi Spesa:** Inserisci importo, descrizione e data.
* **Visualizza Spese:** Guarda l'elenco completo delle spese salvate.
* **Calcola Totale:** Somma automatica di tutte le spese registrate.
* **Ricerca:** Trova le spese effettuate in una data specifica.
* **Elimina:** Rimuovi una spesa non più necessaria.
* **Salvataggio Automatico:** I dati vengono salvati su un file `spese.json` per non perderli alla chiusura.

## 🛠️ Requisiti

* Python 3.x installato.

## ▶️ Come usare il programma

1.  Scarica la cartella del progetto.
2.  Apri il terminale nella cartella.
3.  Esegui il comando:
    ```bash
    python main.py
    ```
4.  Segui le istruzioni a schermo navigando nel menu numerico.

## 📂 Struttura del Progetto

* `main.py`: Il punto di ingresso del programma, gestisce il menu utente.
* `logica.py`: Contiene le funzioni principali (creazione, calcoli, ricerca).
* `gestione_files.py`: Gestisce il salvataggio e il caricamento dal file JSON.
* `spese.json`: Il database dove vengono archiviati i dati.

## ✍️ Autore

Stefano Bellan