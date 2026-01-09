![logo diginamic](./img/logo-diginamic.png)

<br>

# **Scénario cours-api**

Cette doc n'avais pas pour finalité de servir de cours, mais plutot de la documentation annexe pour les apprenants. Cette doc se base sur la doc officielle de FastAPI et SQLModel, ainsi que sur des ressources internes pour compléter les notions.

<br>

## <u>**Sommaire**</u>

- **I. Introduction et concepts d'une API**
    - [01-definition-api](./I.%20Introduction%20et%20concepts%20d'une%20API/01-definition-api.md)
    - [02-types-api](./I.%20Introduction%20et%20concepts%20d'une%20API/02-types-api.md)
    - [03-format-de-donnees](./I.%20Introduction%20et%20concepts%20d'une%20API/03-format-de-donnees.md)
    - [04-codes-retour-http](./I.%20Introduction%20et%20concepts%20d'une%20API/04-codes-retour-http.md)
    - [05-methodes-http](./I.%20Introduction%20et%20concepts%20d'une%20API/05-methodes-http.md)
- **III. Création d'une api REST avec FastAPI**
    - [07-organisation-projet](./III.%20Création%20d'une%20api%20REST%20avec%20FastAPI/07-organisation-projet.md)
        - uniquement jusque `Structure recommandée`
    - [01-introduction-fastapi](./III.%20Création%20d'une%20api%20REST%20avec%20FastAPI/01-introduction-fastapi.md)
    - [02-definition-endpoints](./III.%20Création%20d'une%20api%20REST%20avec%20FastAPI/02-definition-endpoints.md)
    - [03-schema](./III.%20Création%20d'une%20api%20REST%20avec%20FastAPI/03-schema.md)
    - [04-swagger](./III.%20Création%20d'une%20api%20REST%20avec%20FastAPI/04-swagger.md)
- **II. Modélisation et manipulation de la bdd avec SQLModel**
    - 00-installation-et-introduction-cursor
        - [01-Installation-configuration-mariaDB-Dbeaver](./II.%20Modélisation%20et%20manipulation%20de%20la%20bdd%20avec%20SQLModel/00-installation-et-introduction-cursor/01-Installation-configuration-mariaDB-Dbeaver.md) _(OPTIONNEL)_
        - [02-Connexion-requetage-bdd](./II.%20Modélisation%20et%20manipulation%20de%20la%20bdd%20avec%20SQLModel/00-installation-et-introduction-cursor/02-Connexion-requetage-bdd.md) _(OPTIONNEL)_
    - [01-introduction-sqlmodel](./II.%20Modélisation%20et%20manipulation%20de%20la%20bdd%20avec%20SQLModel/01-introduction-sqlmodel.md)
    - [02-creer-des-tables](./II.%20Modélisation%20et%20manipulation%20de%20la%20bdd%20avec%20SQLModel/02-creer-des-tables.md)
    - [03-mise-en-place-bdd](./II.%20Modélisation%20et%20manipulation%20de%20la%20bdd%20avec%20SQLModel/03-mise-en-place-bdd.md)
    - [04-requetage-simple](./II.%20Modélisation%20et%20manipulation%20de%20la%20bdd%20avec%20SQLModel/04-requetage-simple.md)
- **III. Création d'une api REST avec FastAPI**
    - [05-dependances-injection](./III.%20Création%20d'une%20api%20REST%20avec%20FastAPI/05-dependances-injection.md) (+adaptation au sqlmodel mis en place)
    - [06-gestion-erreurs](./III.%20Création%20d'une%20api%20REST%20avec%20FastAPI/06-gestion-erreurs.md)
    - [07-organisation-projet](./III.%20Création%20d'une%20api%20REST%20avec%20FastAPI/07-organisation-projet.md)
        - uniquement après `Structure recommandée`
- **II. Modélisation et manipulation de la bdd avec SQLModel**
    - [05-requetage-one-to-many](./II.%20Modélisation%20et%20manipulation%20de%20la%20bdd%20avec%20SQLModel/05-requetage-one-to-many.md)
    - [06-requetage-many-to-many](./II.%20Modélisation%20et%20manipulation%20de%20la%20bdd%20avec%20SQLModel/06-requetage-many-to-many.md)

<div style="page-break-after: always;"></div>

## <u>**Aller plus loin**</u>

Dans cet doc, il y a aussi les notions de tests automatisés, de déploiement, etc. qui ne seront pas abordé pendant ce cours. Vous pouvez les consulter si vous le souhaitez.
Sachant qu'il vous sera demandé de faire des tests unitaires dans le projet final, il est conseillé de lire au moins la partie sur Pytest.

- **IV. Tests automatisés avec Pytest**
    - [01_pourquoi_tester](./IV.%20Tests%20automatis%C3%A9s%20avec%20Pytest/01_pourquoi_tester.md)
    - [02_types_de_tests](./IV.%20Tests%20automatis%C3%A9s%20avec%20Pytest/02_types_de_tests.md)
    - [03_introduction_pytest](./IV.%20Tests%20automatis%C3%A9s%20avec%20Pytest/03_introduction_pytest.md)
    - [04_httpx_et_client_test](./IV.%20Tests%20automatis%C3%A9s%20avec%20Pytest/04_httpx_et_client_test.md)
    - [05_fixtures](./IV.%20Tests%20automatis%C3%A9s%20avec%20Pytest/05_fixtures.md)
    - [06_couverture_code_ci](./IV.%20Tests%20automatis%C3%A9s%20avec%20Pytest/06_couverture_code_ci.md)
- **V. Environnement de développement et de déploiement avec Docker**
    - [01-pourquoi-docker](./V.%20Environnement%20de%20développement%20et%20de%20déploiement%20avec%20Docker/01-pourquoi-docker.md)
    - [02-concepts-docker](./V.%20Environnement%20de%20développement%20et%20de%20déploiement%20avec%20Docker/02-concepts-docker.md)
    - [03-creation-image-personnalisee-avec-Dockerfile](./V.%20Environnement%20de%20développement%20et%20de%20déploiement%20avec%20Docker/03-creation-image-personnalisee-avec-Dockerfile.md)
    - [04-orchestration-avec-docker-compose](./V.%20Environnement%20de%20développement%20et%20de%20déploiement%20avec%20Docker/04-orchestration-avec-docker-compose.md)
    - [05-executer-et-tester-avec-dockers](./V.%20Environnement%20de%20développement%20et%20de%20déploiement%20avec%20Docker/05-executer-et-tester-avec-dockers.md)
    - [06-bonnes-pratiques-docker](./V.%20Environnement%20de%20développement%20et%20de%20déploiement%20avec%20Docker/06-bonnes-pratiques-docker.md)


> Pour avoir un retour au plus tot, à la fin du projet dédié, on vous fournira le dossier : `VI. Exemple projet FastAPI SQLModel` qui contiendra un exemple complet d'une API REST avec FastAPI et SQLModel mais uniquement avec 1 seule entité (pour simplifier).