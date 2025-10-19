import heapq
import math

def a_star(graphe, coordonnees, depart, arrivee):

    def h(noeud1, noeud2):
        (x1, y1) = coordonnees[noeud1]
        (x2, y2) = coordonnees[noeud2]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    g_score = {noeud: float('inf') for noeud in graphe}
    g_score[depart] = 0

    f_score = {noeud: float('inf') for noeud in graphe}
    f_score[depart] = h(depart, arrivee)

    predecesseurs = {}
    visites = set()

    # File de priorité avec min-heap
    file_priorite = [(f_score[depart], depart)]

    while file_priorite:
        f_actuel, noeud_actuel = heapq.heappop(file_priorite)

        # Ignore si déjà visité
        if noeud_actuel in visites:
            continue

        visites.add(noeud_actuel)

        # On atteint la destination alors on reconstruit le chemin
        if noeud_actuel == arrivee:
            chemin = reconstruire_chemin(predecesseurs, depart, arrivee)
            return chemin, g_score[arrivee]

        # Explore les voisins
        for voisin, poids in graphe[noeud_actuel]:
            if voisin in visites:
                continue

            # Calcule le nouveau g_score
            tentative_g_score = g_score[noeud_actuel] + poids

            # Si ce nouveau chemin est meilleur
            if tentative_g_score < g_score[voisin]:
                predecesseurs[voisin] = noeud_actuel
                g_score[voisin] = tentative_g_score
                f_score[voisin] = g_score[voisin] + h(voisin, arrivee)

                # Ajouter dans la file de priorité
                heapq.heappush(file_priorite, (f_score[voisin], voisin))

    # Aucun chemin trouvé
    return None, float('inf')

def reconstruire_chemin(predecesseurs, depart, arrivee):
    """
    Reconstruit le chemin trouvé par A* en suivant les prédécesseurs.
    """
    if arrivee not in predecesseurs and arrivee != depart:
        return None

    chemin = []
    noeud = arrivee
    while noeud != depart:
        chemin.append(noeud)
        noeud = predecesseurs.get(noeud)
        if noeud is None:
            return None
    chemin.append(depart)
    chemin.reverse()
    return chemin


#Exemple
if __name__ == "__main__":
    graphe = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 5), ("D", 10)],
        "C": [("E", 3)],
        "D": [("F", 11)],
        "E": [("D", 4)],
        "F": []
    }

    # Coordonnées fictives pour la fonction heuristique
    coordonnees = {
        "A": (0, 0),
        "B": (4, 0),
        "C": (2, 2),
        "D": (8, 3),
        "E": (4, 4),
        "F": (10, 5)
    }

    depart, arrivee = "A", "F"
    chemin, cout = a_star(graphe, coordonnees, depart, arrivee)

    if chemin is None:
        print(f"Aucun chemin trouvé entre {depart} et {arrivee}.")
    else:
        print(f"Chemin trouvé par A* : {' -> '.join(chemin)}")
        print(f"Coût total : {cout}")
