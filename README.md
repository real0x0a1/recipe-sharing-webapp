# **Recipe Book API**

A simple recipe book API built with FastAPI, allowing users to create, read, update, and delete recipes.

## **Getting Started**

### Installation

1. Clone the repository: `git clone https://github.com/real0x0a1/recipe-sharing-webapp.git`
2. Install the dependencies: `pip3 install -r requirements.txt`
3. Run the application: `uvicorn main:app --reload`

### Usage

The API is accessible at `http://localhost:8000`. You can use a tool like `curl` or a web browser to interact with the API.

### Endpoints

- `GET /`: Returns the homepage
- `GET /recipes/`: Returns a list of all recipes
- `GET /recipes/{recipe_id}`: Returns a single recipe by ID
- `POST /addrecipe/`: Creates a new recipe
- `POST /editrecipe/{recipe_id}`: Updates a single recipe by ID
- `POST /deleterecipe/{recipe_id}`: Deletes a single recipe by ID

## **Contributing**

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## **Acknowledgments**

This project was built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## **Author**

- Ali (Real0x0a1)

---
