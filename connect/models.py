from sqlmodel import Field , SQLModel

class Cawfee(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    productList: str
    productName: str
    productDescription: str
    price: int 