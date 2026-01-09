
#  Exercice 3 – Développement de l’API REST avec FastAPI  
## Partie 1 – Analyse des données

###  Payload utilisateur de référence

```json
{
  "email": "user@test.com",
  "full_name": "John Doe",
  "age": 32,
  "is_active": true
}
```

---

## 1️ Champs à stocker en base de données

- `id`
- `email`
- `full_name`
- `age`
- `is_active`

---

## 2️ Détail des champs

###  id
- **Type SQLModel** : `int`
- **Clé primaire** : oui
- **Contraintes** :
  - auto-incrémenté
  - non nullable
  - unique

###  email
- **Type SQLModel** : `str`
- **Clé primaire** : non
- **Contraintes** :
  - obligatoire
  - unique
  - non nullable

###  full_name
- **Type SQLModel** : `str`
- **Clé primaire** : non
- **Contraintes** :
  - obligatoire
  - non nullable

###  age
- **Type SQLModel** : `int`
- **Clé primaire** : non
- **Contraintes** :
  - valeur positive (> 0)
  - peut être optionnel selon le besoin métier

###  is_active
- **Type SQLModel** : `bool`
- **Clé primaire** : non
- **Contraintes** :
  - obligatoire
  - valeur par défaut possible : `true`

---

 Ces champs représentent les informations essentielles pour la gestion des utilisateurs dans l’API.
