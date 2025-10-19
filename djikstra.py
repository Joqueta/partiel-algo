import heapq

graphe = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("E", 3)],
    "D": [("F", 11)],
    "E": [("D", 4)],
    "F": []
}

def dijkstra(graphe, depart, arrivee):

    # Initialisation
    distances = {noeud: float("inf") for noeud in graphe}
    distances[depart] = 0
    predecesseurs = {}
    visites = set()
    file_priorite = [(0, depart)] 

    while file_priorite:
        dist_actuelle, noeud_actuel = heapq.heappop(file_priorite)

        # Ignorer si déjà visité
        if noeud_actuel in visites:
            continue
        visites.add(noeud_actuel)

        # Si on atteint la destination, s'arrête
        if noeud_actuel == arrivee:
            break

        # Màj des voisins
        for voisin, poids in graphe[noeud_actuel]:
            nouvelle_distance = dist_actuelle + poids

            # Si on trouve une meilleure distance
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                predecesseurs[voisin] = noeud_actuel
                heapq.heappush(file_priorite, (nouvelle_distance, voisin))

    # Reconstruction du chemin
    chemin = reconstruire_chemin(predecesseurs, depart, arrivee)

    # Retourner le chemin et la distance finale
    if chemin is None:
        return None, float("inf")
    return chemin, distances[arrivee]


def reconstruire_chemin(predecesseurs, depart, arrivee):

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


# Exemple
if __name__ == "__main__":
    depart, arrivee = "A", "F"
    chemin, distance = dijkstra(graphe, depart, arrivee)

    if chemin is None:
        print(f"Aucun chemin trouvé entre {depart} et {arrivee}.")
    else:
        print(f"Chemin le plus court de {depart} à {arrivee} : {' -> '.join(chemin)}")
        print(f"Distance totale : {distance}")
