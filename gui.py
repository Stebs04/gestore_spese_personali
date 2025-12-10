import flet as ft
import utenti

def login(page: ft.Page):
    #1. SETUP Pagina
    page.title = "Gestore Spese - Login"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLACK
    page.window.width = 375
    page.window.height = 812
    page.window.resizable = False # Blocchiamo il ridimensionamento

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
        else:
            page.open(
                ft.SnackBar(
                content=ft.Text("Credenziali non valide!!!"),
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

ft.app(target=login, assets_dir="assets")
