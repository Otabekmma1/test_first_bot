# class User:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#

# from collections import namedtuple
#
# User = namedtuple('User', 'id, name, lastname, age, email')
#
# users = [
# (1, 'Toxir', 'Toxirov', 28, 'toxir@gmail.com'),
# (2, 'Sobir', 'Sobirov', 12, 'sobir@gmail.com'),
# (3, 'Jalil', 'Jalilov', 34, 'jalil@gmail.com'),
# ]
#
# for user in users:
#     us = User(*user)
#     print(*us)



from collections import namedtuple

Cars = namedtuple('Cars', 'model_name colour speed price count')

cars = [
    ('Malibu', 'Red', '300 km/h', 20000, 4),
    ('Lacetti', 'White', '220 km/h', 10000, 4),
    ('Nexia 3', 'Balck', '220 km/h', 150000, 4),
]

for car in cars:
    us = Cars(*car)
    print(*us)

