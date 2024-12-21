from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import psycopg2

app = FastAPI()

#@app.get("/")

#def read_root():
    #return {"hello akram" : "World"}

#@app.get("/souaad")
#def read_root2():
    #return {"hello lolam" : "World"}
# # Define a data model
# class Item(BaseModel):
#     name: str
#     price: float
#     in_stock: bool

# @app.post("/items/")
# def create_item(item: Item):
#     return {"message": "Item created successfully", "item": item}

# @app.get("/users/{id}")
# def read_root2(id: str):
#     return {f"hello {id}" : "World"}

#class Item(BaseModel):
       # name:str
       # description:str | None
       # price:float
       # ismember: bool                                                  #CRUD 

#@app.get("items/{id}")
#def read_item(id:int,q: Union[str,None] = None):
   # print(id)
#    return {"item_id":id, "q": q}

#@app.put("items/{id}")
#async def update_item(id:int ,item:Item):
     #return {"item_id":id. item.model_dump()}


try:
    connection = psycopg2.connect(
        database="Training camp DB",     # Nom de la base de données
        user="postgres",         # Nom d'utilisateur PostgreSQL
        password="",     # Remplacez par votre mot de passe PostgreSQL
        host="localhost",        # Adresse du serveur PostgreSQL
        port="5432"              # Port PostgreSQL (5432 par défaut)
    )
    print("Connexion établie avec succès !")
except psycopg.Error as e:
    print("Erreur lors de la connexion à la base de données :", e)

# Définir un modèle Pydantic pour la validation des données d'entrée
class Item(BaseModel):
    name: str
    description: Union[str, None] = None

# Exemple d'endpoint FastAPI pour tester la connexion
@app.get("/")
def read_root():

    return {"message": "Connexion à la base de données réussie"}

     #lifespan ytexecuta khtra fel bedya t3 l app

