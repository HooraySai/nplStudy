#
# a = {
#         "sai": {
#             'A': 1,
#             'B': 2
#         },
#
#         "wang": {
#             'A': 1,
#             "C": 2
#         }
# }
#
# import pandas as pd
#
# mypd = pd.DataFrame.from_dict(dict(a))
# print(mypd)

a = [1, 2, 3, 4]
b = [2, 3, 4]
c = [i for i in a if i in b]
print(c)