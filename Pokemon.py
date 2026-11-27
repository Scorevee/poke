import tkinter as tk
from api_login import *
app = "Pokemon3v3"
pokemonj1 = []
pokemonj2 = []

### hola xavi

torn = 1
a=0

def sortir():
    finestra_mare.destroy()

finestra_mare = tk.Tk()
finestra_mare.title("Pokemon")
finestra_mare.geometry("1300x800")

def obrir_instruccions():
    # Creem la finestra secundària vinculada a la mare
    finestra_inst = tk.Toplevel(finestra_mare)
    finestra_inst.title("Instruccions")
    finestra_inst.geometry("800x350")
    finestra_inst.config(bg="black")
    # Contingut de la nova finestra
    msg = tk.Label(finestra_inst, text="Cada jugador podrà triar entre 9 pokémons\n diferents per a elegir els seus 3,\n 3 de foc, 3 d'aigua i 3 de planta.\n A cada moment només hi ha un Pokémon\n per jugador al camp. Guanya qui deixa\n l'altre jugador sense Pokémon vius.", font=("Arial", 20, "bold"), bg="black", fg="white")
    msg.pack(pady=40, padx=20)
   
    boto_tancar = tk.Button(finestra_inst, text="Tancar", command=finestra_inst.destroy)
    boto_tancar.pack()
    
def obrir_seleccio():
    global torn, foto_ty, foto_fl, foto_to, foto_mi, foto_va, foto_fo, foto_se, foto_le, foto_sc, label_torn, label_equips
    # Creem la finestra secundària vinculada a la mare
    finestra_selec = tk.Frame(finestra_mare, bg="orange")
    finestra_selec.place(x=0, y=0, width=1300, height=800)
    # Contingut de la nova finestra
    #Label que indica el turno del jugador
    label_torn = tk.Label(finestra_selec, text=("J",torn), font=("Arial", 30, "bold"), bg="orange", fg="black")
    label_torn.place(x=800, y=600)
    label_equips = tk.Label(finestra_selec, text=(f"Jugador 1: {pokemonj1} | Jugador 2: {pokemonj2}"), font=("Arial", 15, "bold"), bg="orange", fg="black")
    label_equips.place(x=100, y=700)

    global boto_ty
    boto_ty = tk.Button(
        finestra_selec,
        text="Typhlosion",
        font=("Arial", 30, "bold"),
        bg="red",
        fg="white",
        disabledforeground="gray",     # color de la letra cuando está desactivado
        command=lambda: typhlosion(boto_ty)
    )
    
    boto_ty.pack()
    boto_ty.place(x=50, y=100)


    global boto_fl
    boto_fl = tk.Button(
        finestra_selec,
        text="Flaereon",
        font=("Arial", 30, "bold"),
        bg="red",
        fg="white",
        disabledforeground="gray",     # color de la letra cuando está desactivado
        command=lambda: flareon(boto_fl)
    )

    boto_fl.pack()
    boto_fl.place(x=350, y=100)


    global boto_to
    boto_to = tk.Button(
        finestra_selec,
        text="Torkoal",
        font=("Arial", 30, "bold"),
        bg="red",
        fg="white",
        disabledforeground="gray",     # color de la letra cuando está desactivado
        command=lambda: torkoal(boto_to)
    )

    boto_to.pack()
    boto_to.place(x=600, y=100)


    global boto_mi
    boto_mi = tk.Button(
        finestra_selec,
        text="Milotic",
        font=("Arial", 30, "bold"),
        bg="blue",
        fg="white",
        disabledforeground="gray",     # color de la letra cuando está desactivado
        command=lambda: Milotic(boto_mi)
    )

    boto_mi.pack()
    boto_mi.place(x=100, y=250)

    global boto_va
    boto_va = tk.Button(
        finestra_selec,
        text="Vaporeon",
        font=("Arial", 30, "bold"),
        bg="blue",
        fg="white",
        disabledforeground="gray",     # color de la letra cuando está desactivado
        command=lambda: Vaporeon(boto_va)
    )

    boto_va.pack()
    boto_va.place(x=335, y=250)

    global boto_fo
    boto_fo = tk.Button(
        finestra_selec,
        text="Floatzel",
        font=("Arial", 30, "bold"),
        bg="blue",
        fg="white",
        disabledforeground="gray",     # color de la letra cuando está desactivado
        command=lambda: Floatzel(boto_fo)
    )

    boto_fo.pack()
    boto_fo.place(x=600, y=250)

    global boto_se
    boto_se = tk.Button(
        finestra_selec,
        text="Serperior",
        font=("Arial", 30, "bold"),
        bg="green",
        fg="white",
        disabledforeground="gray",     # color de la letra cuando está desactivado
        command=lambda: Serperior(boto_se)
    )

    boto_se.pack()
    boto_se.place(x=75, y=400)
    
    global boto_le
    boto_le = tk.Button(
        finestra_selec,
        text="Leafeon",
        font=("Arial", 30, "bold"),
        bg="green",
        fg="white",
        disabledforeground="gray",     # color de la letra cuando está desactivado
        command=lambda: Leafeon(boto_le)
    )

    boto_le.pack()
    boto_le.place(x=350, y=400)

    global boto_sc
    boto_sc = tk.Button(
        finestra_selec,
        text="Sceptile",
        font=("Arial", 30, "bold"),
        bg="green",
        fg="white",
        disabledforeground="gray",     # color de la letra cuando está desactivado
        command=lambda: Sceptile(boto_sc)
    )
    boto_sc.pack()
    boto_sc.place(x=600, y=400)


#FOTOS
    #Typholsion
    foto_ty = tk.PhotoImage(file="pokemon/157.png")
    etiqueta_ty = tk.Label(finestra_selec, image=foto_ty, bg="orange")
    def mostrar(event):
        etiqueta_ty.place(x=800, y=25)

    def amagar(event):
        etiqueta_ty.place_forget()

    boto_ty.bind("<Enter>", mostrar)
    boto_ty.bind("<Leave>", amagar)


    #Flareon
    foto_fl = tk.PhotoImage(file="pokemon/136.png")
    etiqueta_fl = tk.Label(finestra_selec, image=foto_fl, bg="orange")
    def mostrar(event):
        etiqueta_fl.place(x=800, y=0)

    def amagar(event):
        etiqueta_fl.place_forget()

    boto_fl.bind("<Enter>", mostrar)
    boto_fl.bind("<Leave>", amagar)


    #Torkoal
    foto_to = tk.PhotoImage(file="pokemon/324.png")
    etiqueta_to = tk.Label(finestra_selec, image=foto_to, bg="orange")
    def mostrar(event):
        etiqueta_to.place(x=800, y=0)

    def amagar(event):
        etiqueta_to.place_forget()

    boto_to.bind("<Enter>", mostrar)
    boto_to.bind("<Leave>", amagar)

    #Milotic
    foto_mi = tk.PhotoImage(file="pokemon/VhJnxCo.png")
    etiqueta_mi = tk.Label(finestra_selec, image=foto_mi, bg="orange")
    def mostrar(event):
        etiqueta_mi.place(x=800, y=0)

    def amagar(event):
        etiqueta_mi.place_forget()

    boto_mi.bind("<Enter>", mostrar)
    boto_mi.bind("<Leave>", amagar)

    #Vaporeon
    foto_va = tk.PhotoImage(file="pokemon/134.png")
    etiqueta_va = tk.Label(finestra_selec, image=foto_va, bg="orange")
    def mostrar(event):
        etiqueta_va.place(x=800, y=0)

    def amagar(event):
        etiqueta_va.place_forget()

    boto_va.bind("<Enter>", mostrar)
    boto_va.bind("<Leave>", amagar)

    #Floatzel
    foto_fo = tk.PhotoImage(file="pokemon/419.png")
    etiqueta_fo = tk.Label(finestra_selec, image=foto_fo, bg="orange")
    def mostrar(event):
        etiqueta_fo.place(x=800, y=0)

    def amagar(event):
        etiqueta_fo.place_forget()

    boto_fo.bind("<Enter>", mostrar)
    boto_fo.bind("<Leave>", amagar)

    #Serpior
    foto_se = tk.PhotoImage(file="pokemon/800px-Serperior.png").subsample(2, 2)
    etiqueta_se = tk.Label(finestra_selec, image=foto_se, bg="orange")
    def mostrar(event):
        etiqueta_se.place(x=850, y=50)

    def amagar(event):
        etiqueta_se.place_forget()

    boto_se.bind("<Enter>", mostrar)
    boto_se.bind("<Leave>", amagar)

    #Leafeon
    foto_le = tk.PhotoImage(file="pokemon/470.png")
    etiqueta_le = tk.Label(finestra_selec, image=foto_le, bg="orange")
    def mostrar(event):
        etiqueta_le.place(x=850, y=0)

    def amagar(event):
        etiqueta_le.place_forget()

    boto_le.bind("<Enter>", mostrar)
    boto_le.bind("<Leave>", amagar)

    #Sceptile
    foto_sc = tk.PhotoImage(file="pokemon/254.png")
    etiqueta_sc = tk.Label(finestra_selec, image=foto_sc, bg="orange")
    def mostrar(event):
        etiqueta_sc.place(x=850, y=0)

    def amagar(event):
        etiqueta_sc.place_forget()

    boto_sc.bind("<Enter>", mostrar)
    boto_sc.bind("<Leave>", amagar)

def actualitzar_torn():
    label_torn.config(text="J " + str(torn))
    label_equips.config(text=(f"Jugador 1: {pokemonj1} | Jugador 2: {pokemonj2}"))

def typhlosion(boto_ty):
    global torn
    if torn == 1:
        pokemonj1.append("Typhlosion")
        torn = 2
    elif torn == 2:
        pokemonj2.append("Typhlosion")
        torn = 1
    boto_ty.config(state="disabled", bg="gray", disabledforeground="white")
    actualitzar_torn()
    print("Jugador 1:", pokemonj1)
    print("Jugador 2:", pokemonj2)

def flareon(boto_fl):
    global torn
    if torn == 1:
        pokemonj1.append("Flareon")
        torn = 2
    elif torn == 2:
        pokemonj2.append("Flareon")
        torn = 1
    boto_fl.config(state="disabled", bg="gray", disabledforeground="white")
    actualitzar_torn()
    print("Jugador 1:", pokemonj1)
    print("Jugador 2:", pokemonj2)
    
def torkoal(boto_to):
    global torn
    if torn == 1:
        pokemonj1.append("Torkoal")
        torn = 2
    elif torn == 2:
        pokemonj2.append("Torkoal")
        torn = 1
    boto_to.config(state="disabled", bg="gray", disabledforeground="white")
    actualitzar_torn()
    print("Jugador 1:", pokemonj1)
    print("Jugador 2:", pokemonj2)

def Milotic(boto_mi):
    global torn
    if torn == 1:
        pokemonj1.append("Milotic")
        torn = 2
    elif torn == 2:
        pokemonj2.append("Milotic")
        torn = 1
    boto_mi.config(state="disabled", bg="gray", disabledforeground="white")
    actualitzar_torn()
    print("Jugador 1:", pokemonj1)
    print("Jugador 2:", pokemonj2)

def Vaporeon(boto_va):
    global torn
    if torn == 1:
        pokemonj1.append("Vaporeon")
        torn = 2
    elif torn == 2:
        pokemonj2.append("Vaporeon")
        torn = 1
    boto_va.config(state="disabled", bg="gray", disabledforeground="white")
    actualitzar_torn()
    print("Jugador 1:", pokemonj1)
    print("Jugador 2:", pokemonj2)
    
def Floatzel(boto_fo):
    global torn
    if torn == 1:
        pokemonj1.append("Floatzel")
        torn = 2
    elif torn == 2:
        pokemonj2.append("Floatzel")
        torn = 1
    boto_fo.config(state="disabled", bg="gray", disabledforeground="white")
    actualitzar_torn()
    print("Jugador 1:", pokemonj1)
    print("Jugador 2:", pokemonj2)
    
def Serperior(boto_se):
    global torn
    if torn == 1:
        pokemonj1.append("Serperior")
        torn = 2
    elif torn == 2:
        pokemonj2.append("Serperior")
        torn = 1
    boto_se.config(state="disabled", bg="gray", disabledforeground="white")
    actualitzar_torn()
    print("Jugador 1:", pokemonj1)
    print("Jugador 2:", pokemonj2)
    
def Leafeon(boto_le):
    global torn
    if torn == 1:
        pokemonj1.append("Leafeon")
        torn = 2
    elif torn == 2:
        pokemonj2.append("Leafeon")
        torn = 1
    boto_le.config(state="disabled", bg="gray", disabledforeground="white")
    actualitzar_torn()
    print("Jugador 1:", pokemonj1)
    print("Jugador 2:", pokemonj2)

def Sceptile(boto_sc):
    global torn
    if torn == 1:
        pokemonj1.append("Sceptile")
        torn = 2
    elif torn == 2:
        pokemonj2.append("Sceptile")
        torn = 1
    boto_sc.config(state="disabled", bg="gray", disabledforeground="white")
    actualitzar_torn()
    print("Jugador 1:", pokemonj1)
    print("Jugador 2:", pokemonj2)

# Evitem que la finestra es pugui redimensionar si la imatge té una mida fixa

finestra_mare.resizable(False, False)

# 3. Creem un Canvas que ocupi tota la finestra
canvas = tk.Canvas(finestra_mare, width=1300, height=800, bg="darkblue")
canvas.pack(fill="both", expand=True)

foto = tk.PhotoImage(file="pokemon/Togedemaru.png")
canvas.create_image(450, 400, image=foto)


boto_com = tk.Button(
    finestra_mare,
    text="Començar",
    font=("Arial", 40, "bold"),
    bg="DarkBlue",
    fg="yellow",
    command=obrir_seleccio
)

canvas.create_window(1000, 250, window=boto_com)

boto_ins = tk.Button(
    finestra_mare,
    text="Instruccions",
    font=("Arial", 40, "bold"),
    bg="DarkBlue",
    fg="yellow",
    command=obrir_instruccions
)  

canvas.create_window(1000, 400, window=boto_ins)

boto_sort = tk.Button(
    finestra_mare,
    text="Sortir",
    font=("Arial", 40, "bold"),
    bg="DarkBlue",
    fg="yellow",
    command=sortir
)

canvas.create_window(1000, 550, window=boto_sort)

nom_jugador = ""

def registrar():
    nom = entrada_usuari.get()
    contra = entrada_contra.get()
    if nom == "" or contra == "":
        label_missatge.config(text="Omple tots els camps", fg="red")
        return
    try:
        if api_register(app, nom, contra):
            label_missatge.config(text="Usuari creat! Ara pots entrar", fg="lightgreen")
        else:
            label_missatge.config(text="No s'ha pogut crear (potser ja existeix)", fg="red")
    except Exception:
        label_missatge.config(text="Error de connexió", fg="red")

def entrar():
    global nom_jugador
    nom = entrada_usuari.get()
    contra = entrada_contra.get()
    try:
        if api_login(app, nom, contra):
            nom_jugador = nom
            frame_login.destroy()
            mostrar_usuari()
        else:
            label_missatge.config(text="Usuari o contrasenya incorrectes", fg="red")
    except Exception:
        label_missatge.config(text="Error de connexió", fg="red")
def mostrar_usuari():
    global nom_jugador
    label_user.config(text=nom_jugador)

# Pantalla de login (tapa el menú)
frame_login = tk.Frame(finestra_mare, bg="darkblue")
frame_login.place(x=0, y=0, width=1300, height=800)

tk.Label(frame_login, text="Inicia sessió", font=("Arial", 40, "bold"), bg="darkblue", fg="yellow").place(x=450, y=120)

tk.Label(frame_login, text="Usuari:", font=("Arial", 25), bg="darkblue", fg="white").place(x=350, y=270)
entrada_usuari = tk.Entry(frame_login, font=("Arial", 25))
entrada_usuari.place(x=550, y=270)

tk.Label(frame_login, text="Contrasenya:", font=("Arial", 25), bg="darkblue", fg="white").place(x=290, y=350)
entrada_contra = tk.Entry(frame_login, font=("Arial", 25), show="*")
entrada_contra.place(x=550, y=350)

tk.Button(frame_login, text="Entrar", font=("Arial", 25, "bold"), command=entrar).place(x=450, y=450)
tk.Button(frame_login, text="Registrar", font=("Arial", 25, "bold"), command=registrar).place(x=600, y=450)

label_missatge = tk.Label(frame_login, text="", font=("Arial", 20, "bold"), bg="darkblue")
label_missatge.place(x=450, y=550)

label_user = tk.Label(finestra_mare, text=(nom_jugador), font=("Arial", 30, "bold"), bg="darkblue", fg="yellow")
label_user.place(x=900, y=100)

finestra_mare.mainloop()