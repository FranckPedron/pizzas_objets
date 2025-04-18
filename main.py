class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = "- Vegetarienne"
        print(f"PIZZA {self.nom} : {self.prix}€ {veg_str}")
        print(", ".join(self.ingredients))
        print()

    def filtrer(self):
        pass


class PizzaPersonalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0

    def __init__(self):
        PizzaPersonalisee.dernier_numero += 1
        self.numero = PizzaPersonalisee.dernier_numero
        super().__init__("Personnalisée " + str(self.numero), 0, [])
        self.demander_ingredients_utilisateur()
        self.calculer_prix()

    def demander_ingredients_utilisateur(self):

        print(f"Ingrédients pour la pizza personnalisée n° {self.numero}")
        while True:
            ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingredients: {', '.join(self.ingredients)}")

    def calculer_prix(self):
        self.prix = self.PRIX_DE_BASE + (len(self.ingredients) * self.PRIX_PAR_INGREDIENT)


pizzas = [
    Pizza("4 fromages", 8.5, ("Bleu", "Emmental", "Comté", "Parmesan"), True),
    Pizza("Hawai", 7.5, ("Tomate", "Ananas", "Oignons"), True),
    Pizza("Océane", 11.5, ("Fruits de mer", "Emmental", "Tomate", "Parmesan"), False),
    Pizza("Texane", 9.5, ("Steak haché", "Emmental", "Tomate", "Parmesan"), False),
    Pizza("Poulet", 10.5, ("Crème", "Emmental", "Champignons"), False),
    PizzaPersonalisee(),
    PizzaPersonalisee()
]

for pizza in pizzas:
    pizza.afficher()
