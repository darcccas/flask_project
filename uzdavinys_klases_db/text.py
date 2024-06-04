from uzdavinys_klases_db.database import PandaDB


class Text(PandaDB):
    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def find_words_with_fragments(self, fragment: str) -> list:
        words = [word for word in self.text.split() if fragment in word.lower()]
        self.create_dataframe(words)
        self.create_table_in_DB(f"find_words_with_fragments( {fragment} )")
        return words

    def find_five_longest_words(self) -> list:
        list_of_five = self.text.split()
        list_of_five.sort(reverse=True, key=lambda x: len(x))
        self.create_dataframe(list_of_five[:5])
        self.create_table_in_DB("find_five_longest_words")
        return list_of_five[:5]

    def delete_fragment(self, fragment: str) -> str:
        text_without_fragment = self.text.replace(fragment, "")
        self.create_dataframe(text_without_fragment.split())
        self.create_table_in_DB(f"delete_fragment_from_words( {fragment} )")
        return self.text.lower().replace(fragment, "")


random_text = (
    "Sunlight drifted through the ancient trees, casting shimmering"
    " patterns on the forest floor, where vibrant flowers bloomed beside"
    " a babbling brook, serenading the peaceful glade with its melodic"
    " whispers"
)

if __name__ == "__main__":
    text = Text(random_text)
    print(text.find_words_with_fragments("a"))
    print(text.find_five_longest_words())
    print(text.delete_fragment("a"))
