# AlmanaxHelper
Application d'aide pour la réalisation de stock d'Almanax sur Dofus

Almanax Helper permet de faciliter la réalisation des stocks d'offrande pour la quête Almanax sur Dofus. Plusieurs fonctionnalité :

- Ajoute au presse-papier l'offrande à acheter
- Application au premier plan pour éviter de devoir faire des ALT+TAB régulier
- Tri les offrandes par type d'offrande (ressource, consommable, équipement) ce qui permet de minimiser les aller-retours entre les différents HDV.
- Les objets non-achetables (cf. objets de quêtes, objets à recette secrette, etc) sont regroupés dans "autre"

L'application utilise un fichier data_almanax.csv sous cette forme : DATE,QUANTITE,OFFRANDE,TYPE contenant les futures offrandes
Ce fichier peut être généré en scrappant le site du Krosmoz http://www.krosmoz.com/fr/almanax ou en utilisant mon fichier data_almanax.csv qui contient toutes les futures offrandes jusqu'à janvier 2023.

- Utilisation
Il suffit simplement d'éxécuter la version la plus récente de almanax_helper_0.X.py. Veillez à ce que les fichiers equipements_dofus.txt, ressources_dofus.txt, consommalbes_dofus.txt, armes_dofus.txt soient présent dans le même dossier que le fichier python. 

En cas de dépendances manques, installez-les simplement avec "pip install NomDeLaDépendance" dans un Terminal



