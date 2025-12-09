import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk 
import os
import utenti

# Tema scuro (nero profondo)
window = ttk.Window(themename="cyborg") 
window.title("Gestore Spese")

# Fullscreen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("375x812")

# --- CONTAINER CENTRALE ---
login_frame = ttk.Frame(window)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# --- A. LOGO ---
logo_path = "logo.png"
if os.path.exists(logo_path):
    img = Image.open(logo_path).resize((110, 110), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    logo_lbl = ttk.Label(login_frame, image=photo)
    logo_lbl.image = photo
    logo_lbl.pack(pady=(0, 20)) # Spazio sotto il logo
else:
    logo_lbl = ttk.Label(login_frame, text="Logo", font=("Arial", 14), 
                         bootstyle="secondary-inverse", width=12, anchor="center")
    logo_lbl.pack(pady=(0, 20), ipady=40) 

# --- B. TITOLO ---
titolo = ttk.Label(login_frame, 
                   text="Gestore Spese", 
                   font=("Segoe UI", 28, "bold"), # Font aumentato per bilanciare gli input grandi
                   foreground="white")
titolo.pack(pady=(0, 40)) 


# --- SETUP PROPORZIONI COMUNI ---
# Definiamo qui la larghezza comune per Entry e Bottoni
LARGHEZZA_COMUNE = 35  # Aumentato da 28 a 40 per allargare la colonna
ALTEZZA_INPUT = 8     # Altezza interna (padding)

# --- C. EMAIL ---
lbl_email = ttk.Label(login_frame, text="Email", font=("Segoe UI", 14))
# anchor="w" allinea l'etichetta a sinistra rispetto alla colonna, come nel mockup
lbl_email.pack(fill="x", pady=(0, 5)) 

entry_email = ttk.Entry(login_frame, 
                        width=LARGHEZZA_COMUNE, 
                        bootstyle="secondary", 
                        font=("Segoe UI", 12))
entry_email.pack(pady=(0, 25), ipady=ALTEZZA_INPUT) # Box alto e spaziato


# --- D. PASSWORD ---
lbl_pwd = ttk.Label(login_frame, text="Password", font=("Segoe UI", 14))
lbl_pwd.pack(fill="x", pady=(0, 5))

entry_pwd = ttk.Entry(login_frame, 
                      width=LARGHEZZA_COMUNE, 
                      show="*", 
                      bootstyle="secondary", 
                      font=("Segoe UI", 12))
entry_pwd.pack(pady=(0, 50), ipady=ALTEZZA_INPUT) # Molto spazio prima del bottone


# --- E. BOTTONE ---
def esegui_login():
    mail = entry_email.get()
    pwd = entry_pwd.get()
    risultato = utenti.login_utente(mail, pwd)
    if risultato:
        messagebox.showinfo("Login", f"Benvenuto {risultato}!")
    else:
        messagebox.showerror("Errore", "Credenziali errate")

# Il trucco per avere la STESSA larghezza visiva degli input:
# Poiché i bottoni calcolano la width diversamente dalle entry,
# spesso width=LARGHEZZA_COMUNE è sufficiente, ma a volte serve un Frame contenitore.
# Proviamo con width esplicita.
btn_accedi = ttk.Button(login_frame, 
                        text="Accedi", 
                        bootstyle="success", 
                        width=LARGHEZZA_COMUNE, # Stessa larghezza degli input!
                        command=esegui_login)
# ipady leggermente inferiore agli input perché il testo del bottone è centrato verticalmente
btn_accedi.pack(ipady=20) 


# Avvio
window.mainloop()