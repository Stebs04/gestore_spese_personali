import flet as ft
import utenti

def main(page: ft.Page):
    #1. SETUP Pagina
    page.title = "Gestore Spese - Login"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLACK
    page.window.width = 375
    page.window.height = 812
    page.window.resizable = False # Blocchiamo il ridimensionamento

#creazione pagina login
    def view_login(): 
        #Allineamento 
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.padding = 20
        

        #Definizione oggetti
        logo = ft.Image(src="/logo.png", height=100, width=100, fit=ft.ImageFit.CONTAIN)
        login_text = ft.Text(value="Esegui l'accesso", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)


        #Campo Email
        email_text = ft.Text(value="Email", size=15, color=ft.Colors.WHITE)
        email_field = ft.TextField(
            label="Indirizzo Email",
            hint_text="Inserisci la tua Email",
            #Abilito lo sfondo interno
            filled=True,
            bgcolor="#212121",
            #Colori quando c'è il focus su esso
            focused_bgcolor="#2C2C2C",
            focused_border_color="blue",
            cursor_color="blue",
            #Stili del testo
            text_style=ft.TextStyle(color="white"),
            hint_style=ft.TextStyle(color="grey"),
            border_radius=12, #Arrotonda gli angoli
            border_color=ft.Colors.GREY_300,
            prefix_icon=ft.Icons.MAIL_OUTLINE #icona per la UIX
        )

        #Campo Password
        pwd_text = ft.Text(value="Password", size=15, color=ft.Colors.WHITE)
        pwd_field = ft.TextField(
            label="Password",
            hint_text="Inserisci la tua Password",
            password=True, #Nasconde la password
            can_reveal_password=True, #Mostra l'occhietto per vedere la password
            filled=True,
            bgcolor="#212121",
            #Colori quando c'è il focus su esso
            focused_bgcolor="#2C2C2C",
            focused_border_color="blue",
            cursor_color="blue",
            #Stili del testo
            text_style=ft.TextStyle(color="white"),
            hint_style=ft.TextStyle(color="grey"),
            border_radius=12, #Arrotonda gli angoli
            border_color=ft.Colors.GREY_300,
            prefix_icon=ft.Icons.MAIL_OUTLINE #icona per la UIX
        )

        def login_function(e):
            email = email_field.value #Recupero l'email
            pwd = pwd_field.value #Recupero la password
            nuovo_utente = utenti.login_utente(email, pwd)
            if nuovo_utente:
                page.open(
                    ft.SnackBar(
                        content=ft.Text("Login Effettuato con successo"),
                        bgcolor="green"
                    )
                )
                view_dasboard(email)
            else:
                page.open(
                    ft.SnackBar(
                    content=ft.Text("credenziali non valide"),
                        bgcolor="red"
                    )
                )


        #Bottone per l'accesso
        submit_button = ft.ElevatedButton(
                text="Invia",
                bgcolor=ft.Colors.BLUE_ACCENT_700,
                color=ft.Colors.WHITE,
                width=375 - 40, # Per adattarsi al padding della pagina
                height=50,
                on_click=login_function
                
            )
        
        spazio_vuoto = ft.Container(height=30)

        colonna = ft.Column(
            controls= [
                ft.Container(
                    content=logo,
                    alignment=ft.alignment.center, #Centro il logo
                    margin=ft.margin.only(top=50, bottom=40)
                            ), login_text,
                            ft.Container(height=10),
                                ft.Container(
                                content=email_text,
                                alignment=ft.alignment.center_left,
                            ), email_field,
                            ft.Container(height=20), 
                            ft.Container(
                                content=pwd_text,
                                alignment=ft.alignment.center_left
                            ), 
                            pwd_field, 
                            spazio_vuoto, 
                            submit_button
                ], #Aggiunti gli oggetti appena definiti
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, #Centro gli oggetti orizzontalmente
            spacing=20 #Spazia gli oggetti
        )

        page.add(colonna)
    def view_dasboard(nome_utente):
        page.clean()
      #Allineamento 
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.padding = 20

        #Creazione topbar
        # Creazione topbar
        page.appbar = ft.AppBar(
            leading=ft.Container(
                content=ft.Image(src="/logo.png", fit=ft.ImageFit.CONTAIN),
                # padding.only(left=10) stacca il logo dal bordo sinistro dello schermo
                # padding.all(5) aggiunge un po' di aria anche sopra e sotto
                padding=ft.padding.only(left=10, top=5, bottom=5) 
            ),
            leading_width=90, 
            # Titolo
            title=ft.Text("Gestore spese", size=18, weight="bold", color="white"),
            center_title=True, # Centra il titolo rispetto alla pagina
            bgcolor="#1f1f1f"
        )

        #Barra icone in basso
        page.navigation_bar = ft.NavigationBar(
            bgcolor="#1f1f1f", #Grigio Scuro
            indicator_color="blue", #Colore selezione
            destinations=[ft.NavigationBarDestination(icon="home", label="Home"),
                        ft.NavigationBarDestination(icon="person", label="Profilo"),
                        ft.NavigationBarDestination(icon="setting", label="Impostazioni")]
        )

        #CREAZIONE DEI BOTTONI (La lista intelligente)
        # Definiamo i dati dei 6 bottoni: (Titolo, Icona)
        menu_items = [
            ("Aggiungi", ft.Icons.ADD_CIRCLE_OUTLINE),
            ("Visualizza", ft.Icons.LIST_ALT),
            ("Totale", ft.Icons.CALCULATE_OUTLINED),
            ("Elimina", ft.Icons.DELETE_OUTLINE),
            ("Cerca", ft.Icons.SEARCH),
            ("Esci", ft.Icons.EXIT_TO_APP),
        ]

        lista_bottoni_grafici = []

        for titolo, icona in menu_items:
            # Creiamo il quadrato per ogni voce
            btn = ft.Container(
                bgcolor="#1f1f1f", # Grigio scuro moderno
                border=ft.border.all(1, "white"), # Bordo sottile
                border_radius=20, # Angoli tondi
                ink=True,         # Effetto click
                on_click=lambda e: print(f"Cliccato!"), # Placeholder logica
                padding=10,
                # Cosa c'è dentro il quadrato? Icona + Testo
                content=ft.Column(
                    controls=[
                        ft.Icon(name=icona, size=40, color="white"),
                        ft.Text(titolo, color="white", weight="bold")
                    ],
                    alignment="center", # Centra verticalmente icona e testo
                    horizontal_alignment="center" # Centra orizzontalmente
                )
            )
            lista_bottoni_grafici.append(btn)

        # Testi di benvenuto
        txt_benvenuto = ft.Text(f"Benvenuto {nome_utente}", size=24, weight="bold", color="white")
        txt_istruzioni = ft.Text("Scegli un'operazione", size=16, color="grey",  weight="bold")

        # La Griglia che contiene i bottoni creati sopra
        griglia = ft.GridView(
            expand=True,        # OCCUPA TUTTO LO SPAZIO RIMASTE
            runs_count=2,       # 2 Colonne fisse
            max_extent=200,     # Larghezza massima ideale
            child_aspect_ratio=1.0, # Quadrati perfetti
            spacing=20,         # Spazio orizzontale
            run_spacing=20,     # Spazio verticale
            controls=lista_bottoni_grafici # <--- Qui mettiamo i bottoni!
        )

        # Aggiungiamo tutto alla pagina in una Colonna principale
        page.add(
            ft.Column(
                controls=[
                    ft.Container(height=10), # Spazio sotto la barra
                    txt_benvenuto,
                    txt_istruzioni,
                    ft.Container(height=10), # Spazio prima della griglia
                    griglia
                ],
                expand=True, # FONDAMENTALE: La colonna deve espandersi per far espandere la griglia
                horizontal_alignment="center"
            )
        )
        
        page.update()

    view_login()
ft.app(target=main, assets_dir="assets")
