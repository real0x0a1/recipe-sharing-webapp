import json
import os

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

RECIPES_FILE ='recipes.json'

class Recipe(BaseModel):
    id: int
    title: str
    description: str
    ingredients: str
    instructions: str

def load_recipes():
    if os.path.exists(RECIPES_FILE):
        with open(RECIPES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_recipes(recipes):
    with open(RECIPES_FILE, 'w') as f:
        json.dump(recipes, f, indent=4)

recipes = load_recipes()

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/recipes/", response_class=HTMLResponse)
async def read_recipes(request: Request):
    return templates.TemplateResponse("recipes.html", {"request": request, "recipes": recipes})

@app.get("/recipes/{recipe_id}", response_class=HTMLResponse)
async def read_recipe(request: Request, recipe_id: int):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return templates.TemplateResponse("recipe.html", {"request": request, "recipe": recipe})
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.get("/addrecipe/", response_class=HTMLResponse)
async def add_recipe(request: Request):
    return templates.TemplateResponse("addrecipe.html", {"request": request})

@app.post("/addrecipe/")
async def create_recipe(title: str = Form(...), description: str = Form(...), ingredients: str = Form(...), instructions: str = Form(...)):
    new_recipe = {"id": len(recipes) + 1, "title": title, "description": description, "ingredients": ingredients, "instructions": instructions}
    recipes.append(new_recipe)
    save_recipes(recipes)
    return Response(status_code=302, headers={"Location": "/recipes/"})

@app.get("/editrecipe/{recipe_id}", response_class=HTMLResponse)
async def edit_recipe(request: Request, recipe_id: int):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return templates.TemplateResponse("editrecipe.html", {"request": request, "recipe": recipe})
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.post("/editrecipe/{recipe_id}")
async def update_recipe(recipe_id: int, title: str, description: str, ingredients: str, instructions: str):
    for i, recipe in enumerate(recipes):
        if recipe["id"] == recipe_id:
            recipe["title"] = title
            recipe["description"] = description
            recipe["ingredients"] = ingredients
            recipe["instructions"] = instructions
            save_recipes(recipes)
            return Response(status_code=302, headers={"Location": "/recipes/"})
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.get("/deleterecipe/", response_class=HTMLResponse)
async def delete_page(request: Request):
    return templates.TemplateResponse("deleterecipe.html", {"request": request})

@app.post("/deleterecipe/{recipe_id}")
async def delete_recipe(recipe_id: int):
    global recipes
    recipes = [recipe for recipe in recipes if recipe["id"]!= recipe_id]
    save_recipes(recipes)
    return Response(status_code=302, headers={"Location": "/recipes/"})