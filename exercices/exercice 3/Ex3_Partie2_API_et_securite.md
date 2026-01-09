
#  Exercice 3 – Développement de l’API REST avec FastAPI  
## Partie 2 – API et sécurité des données

---

##  Risques si l’API accède directement aux tables de la base de données

- Couplage fort entre l’API et la base de données
- Difficulté de maintenance et d’évolution du schéma
- Absence de validation des règles métier
- Risque de suppression ou modification accidentelle des données
- Exposition involontaire de données sensibles

---

##  Risques si l’API exécute des requêtes SQL construites à partir des données client

- Vulnérabilité aux injections SQL
- Accès non autorisé aux données
- Altération ou suppression de données en base
- Perte d’intégrité des données
- Failles de sécurité critiques exploitables

---

##  Bonnes pratiques recommandées

- Utiliser un ORM (SQLModel) pour sécuriser l’accès à la base
- Valider toutes les données reçues par l’API
- Séparer clairement :
  - la couche API
  - la logique métier
  - l’accès aux données
- Ne jamais construire de requêtes SQL dynamiques à partir d’entrées utilisateur

---

 Ces pratiques garantissent une API plus sûre, maintenable et évolutive.
