# Projet de Big Data : Page Rank
## Lancer le programme Classique
Executer la commande *python projet.py* (il faut que le fichier *path_finished.csv*
soit dans le même répertoire que le fichier executable).

## Choix de la méthode
1 : PageRank *classique*
2 : Méthode personnalisée

## Pour PageRank classique
Choix du beta ([0,1])

## Pour PageRank personnalisée :
Choix des pages : nom de pages séparées par des espaces.
Par exemple
**France Germany Africa**

## Affichage
Exemple d'affichage pour PageRank avec beta = 0.5

**PAGE**		**SCORE**
('United_States', 0.02246299133803719)
('Europe', 0.010259714320667856)
('England', 0.00926041897211565)
('United_Kingdom', 0.009215791745954322)
('Africa', 0.005840460991572599)
('World_War_II', 0.00549170135012363)
('Earth', 0.004641879964669297)
('France', 0.004334980206666213)
('Germany', 0.004116310440345009)

## Lancer le programme prenant en compte les paths paths_unfinished.
Executer la commande *python projet_path_unfinished.py* (il faut que les fichiers *paths_finished.csv* et *paths_unfinished.csv*
soient dans le même répertoire que le fichier executable).
