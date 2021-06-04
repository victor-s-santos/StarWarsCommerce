import django.contrib.auth
User = django.contrib.auth.get_user_model()

list_names = [
    {'username': 'darthvader', 'first_name': 'Darth', 'last_name': 'Vader',
     'email': 'darth_vader@email.com', 'password': 'senhasecreta', 'is_staff': False},

    {'username': 'obiwan', 'first_name': 'Obi-Wan', 'last_name': 'Kenobi',
     'email': 'obi_wan@email.com', 'password': 'senhasecreta', 'is_staff': False},

    {'username': 'skywalker', 'first_name': 'Luke', 'last_name': 'Skywalker',
     'email': 'skywalker@email.com', 'password': 'senhasecreta', 'is_staff': False},

    {'username': 'palpatine', 'first_name': 'Imperador', 'last_name': 'Palpatine',
     'email': 'imperador_palpatine@email.com','password': 'senhasecreta', 'is_staff': False},

    {'username': 'hansolo', 'first_name': 'Han', 'last_name': 'Solo',
     'email': 'han_solo@email.com', 'password': 'senhasecreta', 'is_staff': False}
]
for i in list_names:
    u = User.objects.create_user(username=i['username'], first_name=i['first_name'], last_name=i['last_name'], 
    email=i['email'], password=i['password'], is_staff=i['is_staff'])
    u.save()
    print(f'{i["username"]} has been registered!')
