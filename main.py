from dotenv import load_dotenv
from graph.graph import app
from langserve import add_routes
from fastapi import FastAPI
import uvicorn
load_dotenv()

if __name__ == "__main__":
    print("Welcome Cover Letter Assistant")
    user_input = input(">>")
    print(app.invoke(input={"question": user_input}).get("generation"))

