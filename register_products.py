import os
from commerce.models import Product

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = Product(product_name='Millenium​ ​Falcon', unit_price=550000.0, multiple=1,
            image=os.path.join(BASE_DIR, 'product_images/millenium_falcon.png'))
p.save()
print('Millenium Falcon has been registered!')

p = Product(product_name='X-Wing', unit_price=60000.0, multiple=2,
            image=os.path.join(BASE_DIR, 'product_images/xwing.jpeg'))
p.save()
print('X-Wing has been registered!')

p = Product(product_name='Super​ ​Star​ ​Destroyer', unit_price=4570000.0, multiple=1,
            image=os.path.join(BASE_DIR, 'product_images/millenium_falcon.png'))
p.save()
print('Super​ ​Star​ ​Destroyer has been registered!')

p = Product(product_name='TIE Fighter', unit_price=75000.0, multiple=2,
            image=os.path.join(BASE_DIR, 'product_images/tie_fighter.jpeg'))
p.save()
print('TIE Fighter has been registered!')

p = Product(product_name='Lightsaber', unit_price=6000.0, multiple=5,
            image=os.path.join(BASE_DIR, 'product_images/lightsaber.png'))
p.save()
print('Lightsaber has been registered!')

p = Product(product_name='DLT-19 Heavy Blaster Rifle', unit_price=5800.0, multiple=1,
            image=os.path.join(BASE_DIR, 'product_images/DLT-19.png'))
p.save()
print('DLT-19 Heavy Blaster Rifle has been registered!')

p = Product(product_name='DL-44 Heavy Blaster Pistol', unit_price=1500.0, multiple=10,
            image=os.path.join(BASE_DIR, 'product_images/DLT-19.png'))
p.save()
print('DL-44 Heavy Blaster Pistol has been registered!')

#as imagens não serão hospedadas no cloudinary, infelizmente não foi possível encontrar uma maneira de fazê-lo