![logo-digi](../../img/logo-diginamic.png)

<br>

# **Installation & configuration de MariaDB / DBeaver**

<br>

## **<u>Sommaire</u>**

- [**Installation \& configuration de MariaDB / DBeaver**](#installation--configuration-de-mariadb--dbeaver)
  - [**Sommaire**](#sommaire)
  - [**Installation de MariaDB**](#installation-de-mariadb)
    - [**Linux / MacOS**](#linux--macos)
  - [**Créer la base de donnée**](#créer-la-base-de-donnée)
  - [**DBeaver**](#dbeaver)
    - [**Installation**](#installation)
    - [**Connexion à une BDD**](#connexion-à-une-bdd)

<div style="page-break-after: always;"></div>

## **<u>Installation de MariaDB</u>**

[Installer MariaDB](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.1.3&os=windows&cpu=x86_64&pkg=msi&m=icam)

Après avoir choisis votre mot_de_passe, exemple : `root` ou encore `password`
cochez `Use UTF8 as default derver's character set`

> **mot de passe**  
> 
> vous allez devoir choisir un mot de passe pour votre administrateur `root`.
> même si ce n'est pas très sécurisé, ne mettez pas quelques chose de trop long et embétant.
> vous pourrez le changer à tout moment avec les requetes adéquats.

### **Linux / MacOS**

```bash
sudo apt update
sudo apt install mariadb-server
sudo mysql_secure_installation
```

<br>

## **<u>Créer la base de donnée</u>**

`votre_utilisateur` et `chemin/vers/votre/script/` sont à remplacer avec votre configuration.

- depuis un terminal

    ```bash
    mysql -u votre_utilisateur -p < chemin/vers/votre/script/librairie.sql
    ```

  > **Chemin script sql**  
  > 
  > Si vous vous deplacez avec votre terminal dans le dossier de votre script, alors il n'y aura pas de chemin à renseigner.
  >
  > Vous pourrez faire uniquement `mysql -u votre_utilisateur -p < librairie.sql`

- depuis le terminal mariaDB

    ```bash
    source chemin\librairie.sql
    ```

<div style="page-break-after: always;"></div>

## **<u>DBeaver</u>**

### **Installation**

[Téléchager dbeaver](https://dbeaver.io/download/)

Lancer l'installation en tant qu'administrateur

- Composant à installer (par défaut) : suivant

<br>

### **Connexion à une BDD**

Lancer DBeaver en tant qu'administrateur

- Ajouter connexion (le '+' en haut à gauche)  
- Chosir MariaDB  
- Remplissez correctement les champs pour : `database`, `nom d'utilisateur` et `mot de passe`  
- Test de la connexion, puis télécharger les pilotes si besoin.
- Après, cliquez sur OK
