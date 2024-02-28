import random

valeurs_cartes = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As'}
val_sym = ['coeur', 'trefle', 'carreau', 'pique']

class Carte(object):
    def __init__(self, val='Null', coul='Null'):
        self._valeur = val
        self._couleur = coul

    def get_valeur(self):
        return self._valeur
    
    def set_valeur(self, n):
        self._valeur = n

    def get_couleur(self):
        return self._couleur
    
    def set_couleur(self, sym):
        self._couleur = sym

    def __str__(self):
        return f"{self._valeur} de {self._couleur}"

class Joueur(object):
    def __init__(self, nom='sans nom'):
        self.nom = nom
        self.deck = []
        self.score = 0
        self.defausse =[]

    def get_score(self):
        return self.score
    
    def set_score(self, score):
        self.score = score

    #permet de pioche une carte dans le deck
    def piocher(self):
        if len(self.deck) == 0:
            return None
        return self.deck[-1] 
    
    #ajouter la carte gagner dans la defausse 
    def ajouter_carte(self, carte):
        self.defausse.insert(0, carte) 
    

class Partie(object):
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.deck=[]

    #creation d'un deck avec tout les cartes dedans 
    def creation_deck(self):
        for symbole in val_sym:
            for valeur in valeurs_cartes.values():
                carte = Carte(valeur, symbole)
                self.deck.append(carte)

    #distribution du deck crée juste avant pour le distribuer en deux deck avec le meme nombres de cartes dedans 
    def distribuer(self):
        random.shuffle(self.deck)
        moitie = len(self.deck) // 2
        self.joueur1.deck = self.deck[:moitie]
        self.joueur2.deck = self.deck[moitie:]
        print(f"{len(self.joueur1.deck)}/{len(self.joueur2.deck)}")

    #crée les fonction ci-dessus 
    def jouer(self):
        self.creation_deck()
        self.distribuer()
        self.jouer_recursive()

    # fonction qui permet le deroulement du jeu en comparant chaque carte des joueurs, il y a ausi une partie du code qui gere les batailles
    def jouer_recursive(self):
        while self.joueur1.deck + self.joueur1.defausse and self.joueur2.deck + self.joueur2.defausse: #boucle qui verifier si le joueur 1 ou le jouer 2 a encore des cartes
            print("------------------------")
            """mélanger la defausse pour le mettre dans le deck si il est vide """
            if self.joueur1.piocher() == None:
                random.shuffle(self.joueur1.defausse)
                self.joueur1.deck = self.joueur1.defausse
                self.joueur1.defausse=[]
                print(f"{len(self.joueur1.deck)}")
            if self.joueur2.piocher()== None :
                random.shuffle(self.joueur2.defausse)  
                self.joueur2.deck = self.joueur2.defausse 
                self.joueur2.defausse=[]
                print(f"{len(self.joueur2.deck)}")
            carte1 = self.joueur1.piocher()
            carte2 = self.joueur2.piocher()
            print(f"{carte1} vs {carte2}")
            """comparer les cartes entre elles """
            if carte1.get_valeur() > carte2.get_valeur():
                self.joueur2.deck.pop()
                self.joueur1.ajouter_carte(carte2)
                self.joueur1.score += 1
                print(f"-> Gagnant : {self.joueur1.nom} {len(self.joueur1.deck)+len(self.joueur1.defausse)}/{len(self.joueur2.deck)+len(self.joueur2.defausse)}")
            elif carte1.get_valeur() < carte2.get_valeur():
                self.joueur1.deck.pop()
                self.joueur2.ajouter_carte(carte1)
                self.joueur2.score += 1
                print(f"-> Gagnant : {self.joueur2.nom} {len(self.joueur1.deck)+len(self.joueur1.defausse)}/{len(self.joueur2.deck)+len(self.joueur2.defausse)}")
            else:
                self.joueur1.deck.pop()
                self.joueur2.deck.pop()
                if self.joueur1.piocher() == None:
                    if self.joueur1.defausse==[]:
                        self.terminer_partie()
                        break
                    else :    
                        random.shuffle(self.joueur1.defausse)
                        self.joueur1.deck = self.joueur1.defausse
                        self.joueur1.defausse=[]
                if self.joueur2.piocher()== None :
                    if self.joueur2.defausse==[]:
                        self.terminer_partie()
                        break
                    else :       
                        random.shuffle(self.joueur2.defausse)  
                        self.joueur2.deck = self.joueur2.defausse 
                        self.joueur2.defausse=[]
                print("-> Bataille")
                carte3 = self.joueur1.piocher()
                carte4 = self.joueur2.piocher()
                print(f"[cartes cachée]: {carte3} vs {carte4}")
                self.joueur1.deck.pop()
                self.joueur2.deck.pop()
                """mélanger la defausse pour le mettre dans le deck si il est vide et verifier que la partie n'est pas terminer  """
                if self.joueur1.piocher() == None:
                    if self.joueur1.defausse ==[]: #cas ou le jouer un n'a plus de carte même dans sa defausse 
                        self.terminer_partie()
                        break
                    else :    
                        random.shuffle(self.joueur1.defausse)
                        self.joueur1.deck = self.joueur1.defausse
                        self.joueur1.defausse=[]
                if self.joueur2.piocher()== None :
                    if self.joueur2.defausse==[]:
                        self.terminer_partie()
                        break
                    else :       
                        random.shuffle(self.joueur2.defausse)  
                        self.joueur2.deck = self.joueur2.defausse 
                        self.joueur2.defausse=[]
                carte5 = self.joueur1.piocher()
                carte6 = self.joueur2.piocher()
                print(f"[bataille] : {carte5} vs {carte6}")
                self.joueur1.deck.pop()
                self.joueur2.deck.pop()
                if  carte5.get_valeur()> carte6.get_valeur(): #gagnant de la bataille recupere les 6 cartes dont 3 de l'autre joueur
                    self.joueur1.ajouter_carte(carte1)
                    self.joueur1.ajouter_carte(carte3)
                    self.joueur1.ajouter_carte(carte5)
                    self.joueur1.ajouter_carte(carte2)
                    self.joueur1.ajouter_carte(carte4)
                    self.joueur1.ajouter_carte(carte6)
                    self.joueur1.score += 1
                    print(f"-> Gagnant : {self.joueur1.nom} {len(self.joueur1.deck)+len(self.joueur1.defausse)}/{len(self.joueur2.deck)+len(self.joueur2.defausse)}")
                else:    
                    self.joueur2.ajouter_carte(carte2)
                    self.joueur2.ajouter_carte(carte4)
                    self.joueur2.ajouter_carte(carte6)
                    self.joueur2.ajouter_carte(carte1)
                    self.joueur2.ajouter_carte(carte3)
                    self.joueur2.ajouter_carte(carte5)
                    self.joueur2.score += 1
                    print(f"-> Gagnant : {self.joueur2.nom} {len(self.joueur1.deck)+len(self.joueur1.defausse)}/{len(self.joueur2.deck)+len(self.joueur2.defausse)}")
        self.terminer_partie()

    #renvoie le gagnant du jeu 
    def terminer_partie(self):
        if self.joueur1.score > self.joueur2.score:
            print(f"---> Gagnant final: {self.joueur1.nom}")
        elif self.joueur1.score < self.joueur2.score:
            print(f"---> Gagnant final: {self.joueur2.nom}")
       

    