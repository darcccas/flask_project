from uzdavinys_klases_db.text import Text

random_text = (
    "Sunlight drifted through the ancient trees, casting shimmering"
    " patterns on the forest floor, where vibrant flowers bloomed beside"
    " a babbling brook, serenading the peaceful glade with its melodic"
    " whispers"
)

text = Text(random_text)
#
# text.create_dataframe(text.find_five_longest_words())
# text.print_info()
# # text.create_table_in_DB("find_five_longest_words", index_label="index")
# #
# # text.create_dataframe(random_text.split())
# # # text.print_info()
# # text.create_table_in_DB("text_table", "index")
#
# text.create_dataframe(text.find_words_with_fragments("a"))
# text.print_info()
# text.create_table_in_DB("find_words_with_fragments(a)")

# print(text.read_data_from_DB("text_table"))

# print(text.find_words_with_fragments("e"))
# print(text.find_five_longest_words())
# print(text.delete_fragment("i"))
#
# text.print_info()

text.find_five_longest_words()

# text.create_dataframe([])
#
# text.create_table_in_DB("belekas")