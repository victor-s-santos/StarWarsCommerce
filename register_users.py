from django.contrib.auth.models import User

u = User(username='darthvader', first_name='Darth', last_name='Vader', email='darth_vader@email.com', is_staff=False)
u.save()
print('Darth Vader has been registered!')

u = User(username='obiwan', first_name='Obi-Wan', last_name='Kenobi', email='obi_wan@email.com', is_staff=False)
u.save()
print('Obi-Wan Kenobi has been registered!')

u = User(username='skywalker', first_name='Luke', last_name='Skywalker', email='skywalker@email.com', is_staff=False)
u.save()
print('Luke Skywalker has been registered!')

u = User(username='palpatine', first_name='Imperador', last_name='Palpatine', email='imperador_palpatine@email.com', is_staff=False)
u.save()
print('Imperador Palpatine has been registered!')

u = User(username='hansolo', first_name='Han', last_name='Solo', email='han_solo@email.com', is_staff=False)
u.save()
print('Darth Vader has been registered!')
