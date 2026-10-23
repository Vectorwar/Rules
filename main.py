#This is a transcription of the facts and rules

hechos = (
    ("mamifero", "perro"),
    ("domestico", "perro"),
    ("ladra", "perro"),
    ("convive_humanos", "perro"),
    ("sociable", "perro"),
    ("amamanta_crias", "perro"),
    ("crias_vientre_materno", "perro")
)

if ("ladra", "perro") in hechos:
    print ("El perro emite ladridos\n")

if ("mamifero", "perro") in hechos:
   print ("El perro es un mamifero\n")

if ("ladra", "perro") in hechos:
    print ("El perro emite ladridos\n")

if ("mamifero", "perro") in hechos:
    print ("El perro es un mamifero\n")


regla1 = (
    "perro",
    ("mamifero", "domestico", "ladra")
)

regla2 = (
    "perro",
    ("mamifero", "convive_humanos", "domestico")
)

reglas = [
    ("perro", ("mamifero", "domestico", "ladra")),
    ("perro", ("mamifero", "convive_humanos", "domestico"))
]

#Applying rules to the facts
animal = "perro"

for conclusion, condiciones in reglas:
    if all((condicion, animal) in hechos
           for condicion in condiciones):
        print ("Regla Cumpliada:", condiciones)
        print ("conclusion:",animal, "es un", conclusion)

#Fin del programa
