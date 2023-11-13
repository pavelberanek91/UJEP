# NoSQL databázové systémy

## Cvičení 8 - Objektově-dokumentové mapování v MongoDB

Cílem tohoto cvičení je napsat webovou aplikaci, která využívá OOP paradigmatu pro práci s dokumentovou databází, tedy techniku objektově-dokumentového mapování. Hlavním tutoriálem bude tato stránka: [ZDE](https://medium.com/@gurramakhileshwar333/get-your-beanies-a-beginners-guide-to-beanie-mongodb-odm-for-python-b715c3f59a92). Seznámíte se s jiným webovým frameworkem než je Flask a to s frameworkem FastAPI, který slouží pouze pro API operace.

### Zadání
Pojedete podle zmíněného tutoriálu. Proveďte z něj postupně následující kroky u kterých vypisuji kód pro snažší orientaci vůči původnímu tutoriálu:
1. Vytvořte si virtuální prostředí a nainstalujte závislosti (fastapi, beanine, uvicorn).
2. Vytvořte jednoduchou aplikaci, která vrací řetězec na nějaký GET požadavek.
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Root"])
async def index() -> dict:
    return {"message": "Welcome to your books app!"}
```
3. Vytvořte modely pro databázové schéma z tutoriálu.
```
from beanie import Document
from pydantic import BaseModel
from typing import List, Optional


class Review(Document):
    review: str


class Book(Document):
    title: str
    author: str
    published_year: int
    reviews: List[str] = []

    class Settings:
        name = "books"

    class Config:
        schema_extra = {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "published_year": 1925,
                "review": "Excellent course!",
            }
        }


class UpdateBook(BaseModel):
    title: Optional[str]
    author: Optional[str]
    published_year: Optional[int]
```
4. Spusťte si MongoDB přes Docker a připravte si k němu připojení podle vašeho nastavení v compose souboru nebo Dockerfilu.
```
from beanie import init_beanie
import motor.motor_asyncio

from server.models.book import Book


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017"
    )

    #client = motor.motor_asyncio.AsyncIOMotorClient(
    #    "mongodb+srv://<username>:<password>@cluster0.zlhkso0.mongodb.net/?retryWrites=true&w=majority"
    #)

    await init_beanie(database=client.db_name, document_models=[Book])
```
5. Navažte spojení s databází pomocí vaší FastAPI aplikace.
```
from fastapi import FastAPI
from server.database import init_db

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
```
6. 
7. 
8. 
9. 
10. 
