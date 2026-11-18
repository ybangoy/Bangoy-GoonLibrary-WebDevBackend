from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    productList: str
    productName: str
    productDescription: str
    price: int
    chapters: int
    status: str
    priceInfo: str
    source: str
    genre: str
