![logo-diginamic](../img/logo-diginamic.png)

<br>

# **Gestion des erreurs dans FastAPI**

<br>

## <u>**Sommaire**</u>

- [**Gestion des erreurs dans FastAPI**](#gestion-des-erreurs-dans-fastapi)
  - [**Sommaire**](#sommaire)
  - [**Pourquoi gérer les erreurs ?**](#pourquoi-gérer-les-erreurs-)
  - [**Les codes d'erreur HTTP**](#les-codes-derreur-http)
  - [**Lever une erreur avec `HTTPException`**](#lever-une-erreur-avec-httpexception)
  - [**Personnaliser le contenu de l'erreur**](#personnaliser-le-contenu-de-lerreur)
  - [**Ajouter des en-têtes personnalisés**](#ajouter-des-en-têtes-personnalisés)
  - [**Créer ses propres exceptions**](#créer-ses-propres-exceptions)
  - [**Surcharge des gestionnaires d’erreurs FastAPI**](#surcharge-des-gestionnaires-derreurs-fastapi)
  - [**Résumé**](#résumé)

<div style="page-break-after: always;"></div>

## **<u>Pourquoi gérer les erreurs ?</u>**

Une API ne doit pas seulement fonctionner quand tout va bien. Elle doit aussi savoir :

* Répondre clairement en cas de mauvaise requête (client).
* Éviter de renvoyer des erreurs techniques (tracebacks) en production.
* Renvoyer des erreurs compréhensibles pour les développeurs clients.

<br>

## **<u>Les codes d'erreur HTTP</u>**

FastAPI repose sur les **codes HTTP** pour signaler le succès ou l’échec d’une requête.

**Principaux codes :**

* `200 OK` → Tout s’est bien passé.
* `400 Bad Request` → Mauvaise requête (souvent données invalides).
* `401 Unauthorized` / `403 Forbidden` → Accès interdit.
* `404 Not Found` → Ressource inexistante.
* `422 Unprocessable Entity` → Données mal formées (validation automatique).

> Plus de détails sur le cours chapitre 1 partie 4 de ce cursus.

<br>

## **<u>Lever une erreur avec `HTTPException`</u>**

La classe `HTTPException` est utilisée pour retourner une erreur HTTP proprement.

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"pen": "A blue pen"}

@app.get("/items/{item_id}")
async def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}
```

Si l'utilisateur demande un `item_id` inexistant, FastAPI renverra automatiquement :

```json
{
  "detail": "Item not found"
}
```

<div style="page-break-after: always;"></div>

## **<u>Personnaliser le contenu de l'erreur</u>**

Tu peux envoyer plus d’informations dans le champ `detail`, comme un dictionnaire ou une liste.

```python
raise HTTPException(
    status_code=403,
    detail={"error": "forbidden", "reason": "Not enough privileges"}
)
```

FastAPI se charge de convertir le `detail` en JSON.

<br>

## **<u>Ajouter des en-têtes personnalisés</u>**

Tu peux également ajouter des en-têtes HTTP si besoin :

```python
raise HTTPException(
    status_code=404,
    detail="Item not found",
    headers={"X-Error": "ItemMissing"}
)
```

Cela peut être utile pour transmettre des métadonnées à un client frontend ou un service externe.

<div style="page-break-after: always;"></div>

## **<u>Créer ses propres exceptions</u>**

Tu peux définir des exceptions personnalisées pour des erreurs métier.

```python
class AccessDeniedException(Exception):
    def __init__(self, user: str):
        self.user = user
```

Puis tu peux créer un gestionnaire global :

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(AccessDeniedException)
async def access_denied_handler(request: Request, exc: AccessDeniedException):
    return JSONResponse(
        status_code=403,
        content={"message": f"User {exc.user} is not allowed to access this resource."}
    )
```

Et l’utiliser :

```python
@app.get("/secure")
def secure_endpoint(user: str):
    if user != "admin":
        raise AccessDeniedException(user)
    return {"message": "Welcome, admin"}
```

<div style="page-break-after: always;"></div>

## **<u>Surcharge des gestionnaires d’erreurs FastAPI</u>**

FastAPI utilise déjà des gestionnaires d’erreurs internes, notamment pour :

* `HTTPException`
* `RequestValidationError` (erreur dans les données d’entrée)

Tu peux les surcharger pour unifier les messages d’erreurs.

```python
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import PlainTextResponse

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse("Mauvaise donnée envoyée", status_code=400)
```

<br>

## **<u>Résumé</u>**

* `raise HTTPException(...)` permet de signaler une erreur propre.
* Tu peux personnaliser le message (`detail`) et les en-têtes (`headers`).
* Pour les cas spécifiques, tu peux créer tes propres exceptions.
* FastAPI permet de surcharger les gestionnaires globaux pour unifier ou simplifier les retours d’erreur.
