from sqlmodel import Session

from database import create_db_and_tables, engine
from models import Book


def main():
    create_db_and_tables()

    book1 = Book(
        productList='Web Novel',
        productName='Dual Cultivation',
        productDescription='Imprisoned for scheming against the high heavens, legendary cultivator Su Yang gets a new life with his memories intact, trying to reclaim his power and reunite with his past lovers through dual cultivation.',
        price=0,
        chapters=1148,
        status='Ongoing',
        priceInfo='Free (unlock with stones, or pay with coins after 100 chapters)',
        source='WebNovel',
        genre='Xianxia'
    )
    book2 = Book(
        productList='Web Novel',
        productName='Profane Prince of Domination',
        productDescription='Struck down by divine lightning, Earth's most infamous man, Konrad, is reborn as a half-incubus servant with just three hours to conquer his first target or lose everything.',
        price=0,
        chapters=584,
        status='Complete',
        priceInfo='Free',
        source='WebNovel',
        genre='Fantasy'
    )
    book3 = Book(
        productList='Novel',
        productName='Fifty Shades of Grey',
        productDescription='Anastasia interviews young billionaire Christian Grey, and their attraction pulls her into his secret world of dominance and dark desires.',
        price=8,
        chapters=26,
        status='Complete',
        priceInfo='$7.99 USD (Kindle Edition)',
        source='Amazon',
        genre='Dark Romance'
    )

    with Session(engine) as session:
        session.add(book1)
        session.add(book2)
        session.add(book3)
        session.commit()


if __name__ == "__main__":
    main()
