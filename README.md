Este repositorio contiene utilidades para el tratamiento de fotos.

El fichero setDateTimeOriginal.py actúa sobre un directorio de fotos las cuáles han perdido los datos exif (como por ejemplo al ser enviado por whatsapp). 

Sobre los ficheros que no tienen exif intenta deducir el campo DateTimeOriginal a partir del nombre del fichero. Actualmente son capturados 4 tipos de formato:

IMG-20150129-WA0003

IMG_20190103_121449977

2014-05-26 19.34.36

20150820_182144


Sobre los ficheros que tienen exif pero no tienen el campo DateTimeOriginal también actúa, pero en este caso SOBREESCRIBE la información exif al completo. Mucha atención con esto.


Se recomienda hacer una copia de las fotos antes.


Requisitos:

Python 3

pip install Pillow

pip install piexif



Uso:

python setDateTimeOriginal.py


files: 8837

files_video: 121

files_image: 0

exif_empty: 6056

exif_setted: 2259

exif_date_not_found: 401

match_regular_exp1: 6184

match_regular_exp2: 1

match_regular_exp3: 5

match_regular_exp4: 1

saved: 6191

cannot_setted_date: 266
