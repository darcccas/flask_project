from page.models import Message, db, Book, Publisher, Author, Customer, Order, Product, Offer

db.create_all()

#
# jonas = Message('Jonas', 'jonas@mail.com', 'Kažkoks labai rimtas atsiliepimas.')
# antanas = Message('Antanas', 'antanas@mail.lt', 'Antano nuomonė labai svarbi.')
# juozas = Message('Juozas', 'juozukas@friends.lt', 'Aš labai piktas, nes blogai.')
# bronius = Message('Bronius', 'bronka@yahoo.com', 'Aš tai linksmas esu, man patinka.')
#
# db.session.add_all([jonas, antanas, juozas, bronius])
# db.session.commit()

# pub1 = Publisher('Baltos Lankos')
# pub2 = Publisher('Alma Littera')
# db.session.add_all([pub1, pub2])
# db.session.commit()
# book1 = Book('Biliūnas', 'Kliudžiau', 1)
# book2 = Book('Žemaitė', 'Marti', 1)
# book3 = Book('Mažvydas', 'Katekizmas', 2)
# db.session.add_all([book1, book2, book3])
# db.session.commit()

#
# book = Book.query.get(1)
# author_1 = Author.query.get(1)
# author_2 = Author.query.get(2)
#
# book.authors.append(author_1)
# book.authors.append(author_2)
# print(author_1)
# print(author_2)
# db.session.add(book)
# db.session.commit()

# cust = Customer(name="Darius", phone_number=37012345678)
# cust_1 = Customer(name="Antanas", phone_number=37012345648)
# cust_2 = Customer(name="Rolandas", phone_number=37012344678)
# cust_3 = Customer(name="Viktoras", phone_number=37012445678)
# print(cust, cust_1)
# db.session.add_all([cust, cust_1, cust_2, cust_3])
# db.session.commit()
#
# pro_1 = Product("kebab", "Lamb, Onions, Garlic, Parsley, Salt, Pepper, Cumin, Coriander", 8.99)
# pro_2 = Product("burger", "Lamb, Onions, Garlic, Parsley, Salt, Pepper, Cumin, Coriander", 9.99)
# pro_3 = Product("potatoes", "Lamb, Onions, Garlic, Parsley, Salt, Pepper, Cumin, Coriander", 4.99)
# pro_4 = Product("lavash", "Lamb, Onions, Garlic, Parsley, Salt, Pepper, Cumin, Coriander", 6.99)
# db.session.add_all([pro_1, pro_2, pro_3, pro_4])
# db.session.commit()


# order = Order(customer_id=1,
#               product_id=3,
#               quantity=1)
# db.session.add(order)
# db.session.commit()

# order = Order.query.get(3)
# print(order)
# print(order.customer.name)
# print(order.product.name)
# print(order.product.price)
# print(order.product.quantity)
#
# # offer = Offer(3, 4, 8.00)
# db.session.add(offer)
# db.session.commit()
