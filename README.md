# AlmanaxHelper
## Application d'aide pour la réalisation de stock d'Almanax sur Dofus

Almanax Helper permet de faciliter la réalisation des stocks d'offrande pour la quête Almanax sur Dofus. Plusieurs fonctionnalité :

- Ajoute au presse-papier l'offrande à acheter
- Application au premier plan pour éviter de devoir faire des ALT+TAB régulier
- Tri les offrandes par type d'offrande (*ressource, consommable, équipement*) ce qui permet de minimiser les aller-retours entre les différents HDV.
- Les objets non-achetables (cf. objets de quêtes, objets à recette secrète, etc) sont regroupés dans le type *autre*.

L'application crée un fichier data_almanax.csv contenant les futures offrandes jusqu'à un an maximum. Ce fichier est généré en scrappant le site du Krosmoz http://www.krosmoz.com/fr/almanax et en utilisant les fichiers **equipements_dofus.txt**, **ressources_dofus.txt**, **consommables_dofus.txt** et **armes_dofus.txt**, nécessaires à la catégorisation des offrandes.

## Installation et lancement
Téléchargez `almanax_helper_0.4.py` ainsi les quatre fichiers `equipements_dofus.txt`, `ressources_dofus.txt`, `consommables_dofus.txt` et `armes_dofus.txt`. Veillez à ce qu'ils soient tous présents dans le même dossier que le fichier Python. 

Eéxécutez ensuite `almanax_helper_0.4.py`.

NB: En cas de dépendances manquantes, installez-les simplement dans un Terminal avec :
> pip install NomDeLaDépendance 

## Utilisation
Une console s'ouvre. Indiquez sur combien de jour vous voulez réaliser votre stock. 

![alt text](https://i.imgur.com/KqKKJXe.png)

La fênetre d'Almanax Helper s'ouvre et vous n'avez plus qu'à *"coller"* le nom de la ressource dans l'HDV. Il n'y a pas besoin de *"copier"* le nom de la ressource. L'offrande se retrouve directement dans le presse-papier chaque fois que vous cliquez sur le bouton "Jour suivant".

![](https://i.imgur.com/OhvhTvS.png)

Les offrandes sont présentées dans cet ordre : **ressources > armes & équipements > consommables > autre**. Une couleur différente est associée à chacun des types d'offrande de façon à mieux percevoir quand il est nécessaire de changer d'HDV. 
