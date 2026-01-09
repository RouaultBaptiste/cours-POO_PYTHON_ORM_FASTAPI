![logo-diginamic](../img/logo-diginamic.png)

<br>

# **🚢 Pourquoi utiliser Docker ?**

<br>

## **<u>Sommaire</u>**

* [Problèmes classiques sans Docker](#problèmes-classiques-sans-docker)
* [Pourquoi Docker ?](#pourquoi-docker)
* [✅ Avantages](#✅-avantages)

<div style="page-break-after: always;"></div>

## **<u>Problèmes classiques sans Docker</u>**

* **Ça marche chez moi mais pas chez toi**
* Environnements différents entre développeurs :
  * Version de Python
  * Bibliothèques installées
  * Système d’exploitation (Linux, Windows, macOS)
* Difficulté à reproduire les bugs
* Déploiement non standardisé

<br>

## **<u>Pourquoi Docker ?</u>**

Docker permet de **containeriser** une application avec **tout son environnement** (code, bibliothèques, configuration système).
Cela garantit qu’elle fonctionne de manière **identique partout** : local, cloud, CI/CD...

<br>

## **<u>✅ Avantages</u>**

* **Portabilité** : le même container fonctionne sur n’importe quelle machine
* **Reproductibilité** : même version des dépendances pour toute l’équipe
* **Isolation** : chaque service (API, base de données, etc.) tourne dans son propre container
* **Déploiement simplifié** : en cloud, sur serveur distant, ou intégré à une chaîne CI/CD
