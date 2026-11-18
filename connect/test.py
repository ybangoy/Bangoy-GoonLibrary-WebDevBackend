from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware

from models import User, Book

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)



@app.get("/")
async def root():
    return {"message": "Successful"}


@app.get("/Book/{id}")
async def read_book(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        book = session.get(Book, id)
        return {"message": book}


@app.post("/Book")
async def add_book(book  : Book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return {"message": book}


@app.post("/Register")
async def register(user: User):
    with Session(engine) as session:
        existing = session.exec(select(User).where(User.username == user.username)).first()
        if existing:
            return {"status": "failed"}
        session.add(user)
        session.commit()
        return {"status": "success"}


@app.post("/Login")
async def login(user: User):
    with Session(engine) as session:
        statement = select(User).where(User.username == user.username, User.password == user.password)
        found = session.exec(statement).first()
        if found:
            return {"status": "success"}
        return {"status": "failed"}


@app.get("/Books")
async def get_books():
    with Session(engine) as session:
        statement = select(Book)
        results = session.exec(statement)
        return results.all()
