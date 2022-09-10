# from collections import Counter
#
# phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11", "iPhone 12",
#             "iPhone 12", "Xiaomi Mi11"]
# countPhones = Counter(phones)
# countPhones
#
# ephem module
import ephem

mars = ephem.Jupiter('1997/07/05')
contellation_07051197 = ephem.constellation(mars)
print(contellation_07051197)
