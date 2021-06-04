import os
from commerce.models import Product

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
list_products = [

    {'product_name': 'Millenium Falcon', 'unit_price': 550000.0, 'multiple': 1, 
        'image': os.path.join(BASE_DIR, 'product_images/millenium_falcon.png')},
    {'product_name': 'X-Wing', 'unit_price': 60000.0, 'multiple': 2, 
        'image': os.path.join(BASE_DIR, 'product_images/millenium_falcon.png')},
    {'product_name': 'Super​ ​Star​ ​Destroyer', 'unit_price': 4570000.0, 'multiple': 1, 
        'image': os.path.join(BASE_DIR, 'product_images/super_star_destroyer.png')},
    {'product_name': 'TIE Fighter', 'unit_price': 75000.0, 'multiple': 2, 
        'image': os.path.join(BASE_DIR, 'product_images/tie_fighter.jpeg')},
    {'product_name': 'Lightsaber', 'unit_price': 6000.0, 'multiple': 5, 
        'image': os.path.join(BASE_DIR, 'product_images/lightsaber.png')},
    {'product_name': 'DLT-19 Heavy Blaster Rifle', 'unit_price': 5800.0, 'multiple': 1, 
        'image': os.path.join(BASE_DIR, 'product_images/DLT-19.png')},
    {'product_name': 'DL-44 Heavy Blaster Pistol', 'unit_price': 1500.0, 'multiple': 10, 
        'image': os.path.join(BASE_DIR, 'product_images/DL-44.jpg')}
]

for i in list_products:
    p = Product(product_name=i['product_name'], unit_price=i['unit_price'],
        multiple=i['multiple'], image=i['image']) 
    p.save()
    print(f'{i["product_name"]} has been registered!')

"""
as imagens não serão hospedadas no cloudinary, infelizmente não foi possível encontrar 
uma maneira de fazê-lo por linha de comando. Ao importar as dependências do cloudinary e as
credenciais através do .env, é retornado erro. 
"""