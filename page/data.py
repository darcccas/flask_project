from dataclasses import dataclass


@dataclass
class Book:
    date: str
    author: str
    title: str
    text: str
    age: int


data = [
    Book(
        date="datta",
        author="gerg",
        title="namas",
        text="dsfsbfg",
        age=23,
    ),
    Book(
        date="data",
        author="cxv",
        title="gfhgfgfhjhjgf",
        text="dssfdgfdgdf",
        age=18,
    ),
    Book(
        date="<NAME>",
        author="<NAME>",
        title="<NAME>",
        text="<NAME>",
        age=18,
    ),
    Book("asdasd", "sdad", "sdaad", "sdasd", 25),
]

