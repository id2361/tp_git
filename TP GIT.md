---
title: Outils pour le statisticien : git
author: Rémi Pépin, Ludovic Deuneville
subject: Complément informatique
keywords: [git]
header:  ${title} - ${author} - Page ${pageNo} / ${totalPages}

---

# Outils pour le statisticien : git

## Introduction

Git est un formidable outil de versionnage de fichiers qui va vous permettre de conserver efficacement l'historique de votre code aussi bien si vous travaillez seul mais également quand vous travaillez à plusieurs.
Cet historique est conservé dans ce qu'on appelle un *dépôt git*.

Sa conception décentralisée fait qu'il est quasi impossible de perdre une donnée définitivement avec git (à noter toutefois, que, dans ce TP, nous utiliserons git en mode centralisé, l'utilisation en mode décentralisé étant plus complexe, et moins courante).
En particulier, la perte totale d'un ordinateur hébergeant votre code ne représentera qu'une perte minime de code si vous utilisez git correctement.

En outre, de nombreux outils de *CI/CD* (*Continuous Intégration / Continuous Deployment*) qui rendent possible l'automatisation de l'intégration et du déploiement de votre code s'appuient sur un *dépôt* git.

### Concepts Clés : Dépôts et Copies

Cependant, comme tout logiciel, git demande un peu d'apprentissage, et de la pratique. Pour commencer, nous aurons besoin de certains concepts essentiels pour une utilisation efficace. Par sa conception décentralisée, un dépôt git peut exister en plusieurs endroits en même temps : sur notre machine, sur chaque machine des membre du projet, ou sur un serveur hébergeant le projet.

On parlera de la *copie distante* (*remote* en anglais) du dépôt dans le cas du serveur distant. En général, une seule copie distante est utilisée, mais par sa nature décentralisée, plusieurs copies distantes sont possibles (possibilité non incluse dans ce TP).

La copie sur notre machine est la *copie locale* (*local* en anglais). Il s'agit de toutes les informations du dépôt concernant l'historique de ses fichiers, et les métadonnées du dépôt. Une distinction subtile est alors faite entre la copie locale et la *copie de travail* (*working copy* en anglais) : Nos modifications sur les fichiers du dépôt n'intégrerons la copie locale qu'à notre demande explicite. Cette intégration sera alors effectuée par l'ajout d'une entrée à l'historique du dépôt.

### Programme de ce TP

Pour utiliser git, donc pour gérer un dépôt, nous avons accès à de nombreuses commandes.
Pour ce TP de découverte vous allez utiliser seulement les commandes suivantes :

- `git add` pour ajouter un fichier présent dans la copie de travail à la copie locale
- `git commit` pour faire un point de sauvegarde (ajout à l'historique) dans la copie locale avec les modifications des fichiers de la copie de travail
- `git push` pour pousser le code depuis votre copie locale vers la copie distante (envoi de l'historique ajouté à la copie locale par rapport à la copie distante)
- `git pull` pour tirer l'historique de la copie distante vers votre copie de travail (et votre copie locale)
- `git fetch` pour tirer l'historique de la copie distante vers votre copie locale
- `git log` pour voir l'historique tel que vu par votre copie locale
- `git status` pour voir  la différence entre la copie de travail et la copie locale

> :warning: Toutes les commandes git doivent être saisies dans un terminal !

Je vous conseille de vous référer à la [cheatsheet](https://foad-moodle.ensai.fr/pluginfile.php/6195/mod_resource/content/2/github-git-cheat-sheet.pdf) git disponible sur Moodle (les commandes les plus importantes sont surlignées) pour avoir les commandes git sous les yeux.

## Travail en groupe et git 🧙‍♂️👩‍🔬🕵️‍♂️🦸‍♀️💻

### Création de compte sur gitlab et setup

Chaque étudiant doit se créer un compte sur gitlab :  https://about.gitlab.com/ > `Register`.

Récupérez le fichier `setup` disponible sur Moodle en fonction de la machine utilisée.

- Windows (VM ou pc perso windows): Fichier pour windows. Double cliquez dessus pour l'exécuter. 

- iOs / Linux : Fichier pour iOs/Linux. Ouvrez un terminal puis faites :

  ```sh
  cd ~/Download
  chmod +x setup.sh
  ./setup.sh
  ```

Rentrez les informations demandées dans la console. Le script fait toutes l'initialisation pour vous, et copie votre clef dans le presse papier (=fait un "copier" de votre clef pour que vous puissiez la coller). Récupérer également l'archive contenant le code du TP et décompressez-là. Elle contient un fichier `README.md` et un fichier python avec un simple print.

Retournez sur gitlab, et cliquez sur votre profil en haut à droite de la page puis sur `Préférences`. Ensuite cliquez sur `SSH Keys`, et copiez faite un `ctrl+V` dans le champ `Key`. Donnez un nom à la clef comme "VM ensai", supprimez la date d'expiration si vous le souhaitez, et `Add key`.

![](image tp4/gitlab_clef_ssh.png)

### Création d'un projet sur gitlab

Sur la page d'accueil de gitlab cliquez sur `New project` puis `Create blank project`. Appelez le `TP_initiation_git`, laissez-le en `private`, décochez `Initialize repository with a README` puis validez la création.

> Si pour des questions de facilité pour ce TP nous utilisons un fournisseur de dépôt git (ici : Gitlab), il est possible d'utiliser git en créant nous même un dépôt sur notre machine. Ainsi il n'est pas nécessaire d'utiliser un service comme Gitlab, Github ou Bitbucket pour utiliser git.
> Il nous faudra alors utiliser la commande `git init` pour créer ce dépôt, et initialiser la copie locale (à noter que ce dépôt n'aura alors pas de copie distante). Nous ne rentrerons pas dans les détails dans ce TP.

Sur gitlab vous avez quelques paragraphes intitulés `Commande Line Instruction`s et notamment `Push an existing folder`, c’est ce que vous allez devoir faire. En effet le code des TP est déjà dans un dossier sur votre machine.

Ouvrez le dossier du TP avec VScode, et dans le terminal saisissez les différentes commandes, sauf la première qui contient `cd existing_repo`.

Vous allez donc exécuter des commandes qui ressemblent à celles-là :

````bash
git init --initial-branch=main
git remote add origin git@github.com:id2361/tp_git.git
git add .
git commit -m "Initial commit"
git push -u origin main
````

Dans le détail :

- `git init --initial-branch=main` : initialise la copie locale. Il va créer un dossier `.git` qui va contenir l'historique du dépôt (vide pour le moment),

- `git remote add origin git@gitlab.com:username/TP_initiation_git.git` : ajoute les informations sur la copie distante, appellée `origin`, et pointant vers `git@gitlab.com:username/TP4_complement_info.git`,

- ````bash
  git add .
  git commit -m "Initial commit"
  ````

  permettent de faire notre premier commit en ajoutant d'abord tous les fichiers présents dans notre copie de travail (ils sont alors ajoutés à la zone de transit - *stagging index* en anglais - qui liste toutes les modifications de la copie travail par rapport à la copie locale) puis en réalisant le *commit* qui enregistre dans l'historique de la copie locale les modifications actuelles de la copie de travail,

- `git push -u origin main` : réalise le premier push et envoie tout l'historique de la copie locale sur la copie distante.

Si tout c'est bien passé, quand vous rafraîchissez la page web de votre projet gitlab, elle devrait avoir changé et contenir les fichiers du TP.

## ✍ Hands on 1 : Manipulations basiques avec git

* Dans le dossier git-tp, créez un fichier `voiture.py` contenant le code suivant :

  ```python
  class Voiture:
      def __init__(self, nom, couleur):
          self.couleur = couleur
          self.nom = nom
          self.vitesse = 0
  ```

* Dans le terminal VScode, exécutez les commandes suivantes : 

  1. `git status` : permet de voir les différences entre la version de travail du code et le commit le plus récent

     * Le fichier `voiture.py` apparaît dans les *Untracked files*. Cela signifie que Git a repéré ce fichier mais pour le moment il ne le versionnera pas (les fichiers non versionnés sont ignorés par `git commit`)

  2. `git add voiture.py` : permet de mettre des fichiers dans la zone de transit. Ces fichiers seront versionnés dans le prochain commit.

  3. `git status` : maintenant le fichier est reconnu par Git

  4. `git commit -m "Création classe voiture"` : permet de faire un commit = un point de sauvegarde pour git = une entrée supplémentaire à l'historique. En règle général, entre les `" "`, mettez un message court et explicite. Si vous omettez le `-m " "` Vscode va ouvrir une fenêtre pour que vous saisissiez le message de commit. Vous pouvez alors écrire le message de commit, puis fermer la fenêtre pour valider le message. Attention si vous n'écrivez rien hors de la zone de commentaire, le commit sera annulé.

  5. `git status` : affichera alors `Your branch is ahead of 'origin/main' by 1 commit`, signifiant que votre copie locale est en avance d'un commit par rapport à la copie distante.

  6. `git pull` : permet de récupérer les derniers commits disponible sur la copie distante (= la copie du projet gitlab). Actuellement il n'y en a pas, mas il faut prendre l'habitude de souvent récupérer les derniers commits.

  7. `git push` : permet de pousser vos commits sur le dépôt distant. Attention vous ne poussez que les commits (changements sur la copie locale) et pas toutes vos modifications sur votre copie de travail ! Si une modification que vous avez fait n'apparaît pas sur là copie distante, il est possible que vous n'ayez pas fait de commit avec ces modifications.

* Modifiez `voiture.py` pour qu'il ressemble à ça :

  ```python
  class Voiture:
      def __init__(self, nom, couleur):
          self.couleur = couleur
          self.nom = nom
          self.vitesse = 0
  
      def accelere(self, increment):
          if increment > 10:
              increment = 10
              self.vitesse = min(130, self.vitesse + increment)
  ```

* Dans le terminal VSCode :

  1. Faites `git status`, `git add voiture.py`, `git commit -m "Ajout méthode accelere"`, et enfin `git push`, puis vérifiez que le code sur gitlab a bien été modifié.

  2. Regardez votre historique avec un `git log --all --decorate --oneline --graph`

Pour résumer voilà ce que vous avez fait :

![Zonge git](https://nceas.github.io/sasap-training/materials/reproducible_research_in_r_fairbanks/images/git-flowchart.png)

## 🏋️‍♀️🏋️‍♂️ Exercice d'application 1

1. Créez un fichier `fibonacci.py` avec le code suivant

   ```python
   def fibonacci(n):
       if n < 2:
           return 1
       else :
           return fibonacci(n - 1) + fibonacci(n - 2)
   
   if __name__ == "__main__":
       for i in range (1, 101):
           print(fibonacci(i))
   ```

   et envoyez le sur la copie distante de votre projet gitlab

2. Créez un fichier `puissance_rec.py` avec le code suivant

   ```python
   def puissance_rec(nombre, puissance):
       if not puissance:
           return 1
       elif not puissance % 2:
           return puissance_rec(nombre, int(puissance / 2)) \
           * puissance_rec(nombre, int(puissance / 2))
       else:
           return nombre * puissance_rec(nombre, puissance - 1)
   ```

   et envoyez le sur la copie distante de votre projet gitlab

3. Afficher votre historique

## ✍ Hands on 2 : Simulation de travail en groupe

Pour cette seconde partie, vous allez cloner votre dépôt dans un autre dossier. Cela va permettre de simuler un travail à plusieurs sur le même projet. Sur la page gitlab de votre projet cliquez sur `clone` et copiez la partie `clone with SSH`. Dans VScode ouvrez une autre fenêtre et ouvrez le dossier parent du dossier actuel. Dans le terminal de VScode clonez votre projet avec la commande `git clone git@gitlab.com:username/TP_initiation_git.git` en remplaçant `git@gitlab.com:username/TP_initiation_git.git` par la partie `clone with SSH`.
Vous devrez voir apparaître un nouveau dossier avec le code disponible sut git. Ouvrez ce dossier avec VScode. Vous devez avoir 2 fenêtres VScode chacune avec le même code (mais chacune correspondant à une copie de travail distincte).

Dans une des fenêtres créez un fichier `moto.py` avec le code suivant :

```python
class Moto:
    def __init__(self, nom, couleur):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 0
        
    def accelere(self, increment):
        if increment > 15:
            increment = 15
        self.vitesse = min(150, self.vitesse + increment)
```

Puis dans le terminal de cette fenêtre faites les commandes `git add moto.py`, `git commit -m "creation classe moto"`, `git push`.

Maintenant allez dans l'autre fenêtre. Actuellement il n'y a pas le fichier `moto.py`. Il va nous falloir le récupérer.

1. Commencez par faire un `git fetch`. Cela va permettre de récupérer les modifications de la copie distante dans la copie locale, sans modifier la copie de travail (ici, `moto.py` ne va pas apparaître dans l'explorateur de fichier).

2. Ensuite faites un `git status`. Vous allez obtenir le message suivant `Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded. (use "git pull" to update your local branch)`. Cela signifie que votre copie de travail est en retard comparée à votre copie locale.

3. Faites un `git log --all --decorate --oneline --graph`. Vous devrez obtenir le résultat suivant (les valeurs des hash (les 7 caractères hexadécimaux au début) de commits peuvent être différentes :

   ```
   * aa02cb7 (origin/main) creation classe moto
   * a81a5a2 (HEAD -> main) add accelere fonction
   * 6e7c120 creation classe voiture
   * 49fdb53 Initial commit
   ```

   Actuellement le dernier commit de ma copie de travail est le commit `a81a5a` mais ma copie locale possède le commit `aa02cb7` qu'il me faut récupérer. `HEAD` permet de repérer où se trouve notre copie de travail par rapport à l'historique dans notre copie locale.

4. Faites un `git merge` maintenant. Cela va appliquer sur votre copie de travail les modifications additionnelles de votre copie locale. Par la suite nous allons remplacer les opérations `git fetch` et `git merge` par `git pull`.

   ```
   Updating a81a5a2..aa02cb7
   Fast-forward
    moto.py | 10 ++++++++++
    1 file changed, 10 insertions(+)
    create mode 100644 moto.py
   ```

5. Faites un `git log --all --decorate --oneline --graph` pour vérifier que vous avez bien récupéré la dernier version du code.

6. Créez un fichier `velo.py` et avec le même contenu que le fichier moto et faites les mêmes manipulations pour que le fichier apparaisse dans les deux fenêtres (donc dans vos deux copies de travail distinctes).

7. Maintenant créez un fichier dans chaque fenêtre VScode, dans la première vous allez faire un fichier `exo1.R` et dans l'autre vous allez créer un fichier `exo2.R` avec les codes suivants :

```R
# exo1.R
a<-c(10,5,3,2)
a[2]
a[3]
a[2:3]
```

```R
# exo2.R
b<-c(11,6,4,3)
b[2]
b[3]
b[2:3]
```

Faites un commit dans une fenêtre et poussez le code, puis faite la même chose dans l'autre fenêtre. Vous devrez recevoir ce message :

```
! [rejected]        master -> dev (fetch first)
error: failed to push some refs to 'git@gitlab.com:username/TP_initiation_git.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

Git vous signifie que votre copie locale est en retard sur la copie distante. Et comme vous êtes en retard, git ne vous permet pas de pousser vos modifications. Pour avoir le droit d'envoyer votre code sur le dépôt distant vous devez avoir en local au minimum tout l'historique de la copie distante. Récupérez ces modifications distantes avec un `git pull` puis poussez vos modifications locales.

Enfin allez récupérer ces modifications que vous venez de pousser dans l'autre fenêtre VScode. Faites un `git log --all --decorate --oneline --graph` pour voir à quoi ressemble votre historique. Vous allez constater une disjonction puis une fusion. Cette séparation correspond aux deux commits effectués en parallèle.

### Avancé

Lorsque vous maîtriserez `git pull` et la gestion de conflits (section Hands on 3 ci-dessous), vous pourrez utiliser `git pull --rebase`. Cette option permet d'éviter la disjonction / fusion inscrite dans l'historique pour n'avoir que la ligne du commit additionnel dans l'historique. L'utilisation de rebase fait partie des bonnes pratiques de git, mais son usage n'est pas nécessaire pour un débutant.

## 🏋️‍♀️🏋️‍♂️ Exercice d'application 2

- Dans une des fenêtres VScode modifiez le code de `puissance_rec.py` pour le code suivant :

  ```python
  def puissance_rec_smarter(nombre, puissance):
      if not puissance:
          return 1
      elif not puissance % 2:
          return puissance_rec(nombre, int(puissance / 2))**2
      else:
          return nombre * puissance_rec(nombre, puissance - 1)
  ```

- Dans l'autre fenêtre modifiez le code de `fibonacci.py` pour que la boucle dans la condition finale aille jusqu'à 201

- Synchronisez les deux codes.

## ✍ Hands on 3 : Un premier conflit

Pour le moment vous avez travaillé sans générer le moindre conflit. Or la gestion des conflits est un élément crucial pour utiliser correctement git. Les conflits vont apparaître quand plusieurs commits faits en parallèle sont incohérents (dans le cas de fichiers textes, ceci est le cas lorsque les modifications impactent les mêmes zones de code).

Dans la première fenêtre VScode, modifiez le fichier `voiture.py` pour qu'il ressemble à :

```python
class Voiture:
    def __init__(self, nom, couleur, marque):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 0
        self.marque = marque
        
    def accelere(self, increment):
        if increment > 10:
            increment = 10
        self.vitesse = min(130, self.vitesse + increment)
```

Dans la seconde, modifiez le fichier `voiture.py` pour qu'il ressemble à :

```python
class Voiture:
    def __init__(self, nom, couleur, vitesse_max):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 0
        self.vitesse_max = vitesse_max
        
    def accelere(self, increment):
        if increment > 10:
            increment = 10
        self.vitesse = min(self.vitesse_max, self.vitesse + increment)
```

Vous pourrez observer que ces modifications changent la ligne avec  `__init__` de manière différente.

Maintenant faites des commits dans les deux fenêtres, un `git push` dans l'un des deux et un `git pull` dans l'autre. Vous allez obtenir le message suivant :

```
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), 536 bytes | 15.00 KiB/s, done.
From https://gitlab.com/RemiPepinEnsai/tp_initiation_git
   6bee995..a57ae91  main       -> origin/main
Auto-merging voiture.py
CONFLICT (content): Merge conflict in voiture.py
Automatic merge failed; fix conflicts and then commit the result.
```

Git vous prévient que lors de la récupération (avec `git pull`), il n'est pas arrivé à fusionner les commits automatiquement. C'est cela qu'on appel un conflit. Un conflit est généré quand les mêmes lignes de fichiers sont modifiés par deux commits de manière différente. Votre code ressemble à cela désormais :

```python
class Voiture:
<<<<<<< HEAD
    def __init__(self, nom, couleur, vitesse_max):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 0
        self.vitesse_max = vitesse_max
=======
    def __init__(self, nom, couleur, marque):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 0
        self.marque = marque
>>>>>>> a57ae9120dbf97dbab78f82db81f5fc8f48f3821
        
    def accelere(self, increment):
        if increment > 10:
            increment = 10
        self.vitesse = min(self.vitesse_max, self.vitesse + increment)
```

La zone de code :

```python
<<<<<<< HEAD
...
=======
...
>>>>>>> a57ae9120dbf97dbab78f82db81f5fc8f48f3821
```

est la zone du fichier en conflit. La première partie (après `<<<<<<< HEAD` mais avant `=======`) correspond au code en que vous aviez dans votre copie de travail, la seconde au code de la copie distante. Il vous faut maintenant fusionner les deux codes comme vous le souhaitez. Vous pouvez décider de ne prendre que vos changements, que les changements distant ou faire un mix des deux. Remarquez que la ligne 19 n'est pas en conflit. Cette ligne n'a été modifiée que par un seul commit donc il n'y a pas de conflit.

Avant de faire quoi que ce soit, faite un `git status`. Vous allez voir que git vous prévient que les différents historiques ont divergé, et que le fichier `voiture.py` a été modifié par les versions. C'est donc le seul fichier en conflit.

Pour le résoudre vous allez faire un mix des deux commits. le code de votre fichier sera : 

```python
class Voiture:
    def __init__(self, nom, couleur, vitesse_max, marque):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 0
        self.vitesse_max = vitesse_max
        self.marque = marque
        
    def accelere(self, increment):
        if increment > 10:
            increment = 10
        self.vitesse = min(self.vitesse_max, self.vitesse + increment)
```

Faites maintenant un `git add voiture.py` puis un `git status`. Le message va vous dire que tout les conflits sont résolus, mais que vous être encore en train de faire une fusion. Il vous faut maintenant faire un commit pour mettre fin à la fusion. Faites un `git log --all --decorate --oneline --graph` pour voir à quoi ressemble votre historique après votre commit. Finalement, faites un `git push`, puis un `git pull` dans l'autre fenêtre de VSCode.

## 🏋️‍♀️🏋️‍♂️ Exercice d'application 3

- Dans une des fenêtres de VScode
  - Sur le constructeur de la classe `voiture` (la méthode `__init__`), mettez la valeur par défaut de couleur à `verte` : `def __init__(self, nom, vitesse_max, marque, couleur=verte)`
  - Créez un nouveau fichier `scooter.py` en copiant le contenu du fichier `voiture.py`
  - Modifiez la méthode `accelere()` de `scooter.py` pour avoir une vitesse maximale de 80

- Dans la seconde fenêtres de VScode
  -  Sur le constructeur de la classe `voiture` (la méthode `__init__`), mettez la valeur par défaut de couleur à `jaune`
  -  Créez un nouveau fichier `scooter.py` en copiant le contenu du fichier `voiture.py`
  -  Modifiez la méthode `accelere()` de `scooter.py` pour avoir une vitesse maximale de 75
  -  Créez un nouveau fichier `train.py` en copiant le contenu du fichier `voiture.py`
  -  Modifiez la méthode `accelere()` de `scooter.py` pour avoir une vitesse maximale de 350

- Synchronisez vos dépôts et résolvez les conflits.
