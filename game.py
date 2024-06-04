# import os
# from pathlib import Path
#



# data = ["namas", "namelis", "nameliukas"]
#
#
# def repeating_sylbols(words: list) -> str:
#     result = ''
#     for letter in data[0]:
#         result += letter
#         if not all(word.startswith(result) for word in words):
#             result = result[:-1]
#     return result
#
#
# print(repeating_sylbols(data))

#
# new = {
#     1: 5,
#     2: 5,
#     3: 5,
#     4: 5,
# }
#
# for key in new:
#     new[key] *= 2
#
# #
# # del new[1]
# print(new)