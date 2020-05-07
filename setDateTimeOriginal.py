from PIL import Image
import PIL
import piexif
import os
import re


#directorio de trabajo
directory = '/home/isma/Escritorio/_limpio/'

#Expresiones regulares que deben cumplir los ficheros y que se tratarán
pattern1 = re.compile("\\D{4}\\d{8}\\D{3}\\d{4}")                                   #IMG-20150129-WA0003
pattern2 = re.compile("\\D{4}\\d{8}\\D\\d{9}")                                      #IMG_20190103_121449977
pattern3 = re.compile("\\d{4}\\D\\d{2}\\D\\d{2} \\d{2}.\\d{2}.\\d{2}")              #2014-05-26 19.34.36
pattern4 = re.compile("\\d{8}\\D\\d{6}")                                            #20150820_182144

#Comprobación de que la fecha de creación se ha creado bien
patternCheck = re.compile("\\d{4}\\D\\d{2}\\D\\d{2} \\d{2}\\D[0-5]\\d\\D[0-5]\\d")  #2015:08:20 18:21:44


#contadores de progreso
files = 0
files_video = 0
files_image = 0
exif_empty = 0
exif_setted = 0
exif_date_not_found = 0
match_regular_exp1 = 0
match_regular_exp2 = 0
match_regular_exp3 = 0
match_regular_exp4 = 0
saved = 0
cannot_setted_date = 0





#se recorre todo el directorio
for filename in os.listdir(directory):
    files = files + 1


    #omitimos los .mp4 al no saber como tratarlos por ahora
    if not filename.endswith(".mp4"): 
        files_image = 0

        img = Image.open(directory + filename)
        exif_data = img._getexif()


        #en caso de no tener información exif trataremos la imagen
        if exif_data is None or 36867 not in exif_data.keys():
            if exif_data is None:
                exif_empty = exif_empty + 1
            elif 36867 not in exif_data.keys():
                exif_date_not_found = exif_date_not_found + 1

            #COMPROBAMOS LOS DIFERENTES PATRONES CON LA FINALIDAD DE 
            #A TRAVÉS DEL NOMBRE ASIGNAR LA HORA DE CREACIÓN

            #IMG-20150129-WA0003
            if pattern1.match(filename):
                match_regular_exp1 = match_regular_exp1 + 1

                mins_secs = int(filename[15:19])
                
                mins = str(mins_secs // 60)
                if len(mins) == 1:
                    mins = "0" + mins

                secs = str(mins_secs % 60)
                if len(secs) == 1:
                    secs = "0" + secs
                
                time = filename[4:8] +  ':' + filename[8:10] +  ':' + filename[10:12] + " " + "23:" + str(mins) + ":" + str(secs)


            #IMG_20190103_121449977
            elif pattern2.match(filename):
                match_regular_exp2 = match_regular_exp2 + 1
                
                hour = str(int(filename[14:16]) % 24)
                if len(hour) == 1:
                    hour = "0" + hour

                mins = filename[16:18]
                secs = filename[18:20]

                if len(secs) == 1:
                    secs = "0" + secs
                
                time = filename[4:8] +  ':' + filename[8:10] +  ':' + filename[10:12] + " " + hour + ":" + mins + ":" + secs


            #2014-05-26 19.34.36
            elif pattern3.match(filename):
                match_regular_exp3 = match_regular_exp3 + 1

                time = filename[0:4] +  ':' + filename[5:7] +  ':' + filename[8:10] + " " + filename[11:13] + ":"+ filename[14:16] + ":"+ filename[17:19]
                


            #20150820_182144
            elif pattern4.match(filename):
                match_regular_exp4 = match_regular_exp4 + 1
                time = filename[0:4] +  ':' + filename[4:6] +  ':' + filename[6:8] + " " + filename[9:11] + ":"+ filename[11:13] + ":"+ filename[13:15]

            else: 
                cannot_setted_date = cannot_setted_date + 1
                continue


            #Al generar una nueva fecha comprobamos que tenga el formato exif
            #si lo tiene lo guardaremos
            if patternCheck.match(time):
                
                exif_ifd = {
                            piexif.ExifIFD.DateTimeOriginal: u""+time,
                        }
                exif_dict = {"Exif":exif_ifd}
                exif_bytes = piexif.dump(exif_dict)

                img.save(directory + filename, exif=exif_bytes)            

                saved = saved + 1

        else:
            exif_setted = exif_setted + 1
    else:
        files_video = files_video + 1
    

print('files: ' + str(files))
print('files_video: ' + str(files_video))
print('files_image: ' + str(files_image))
print('exif_empty: ' + str(exif_empty))
print('exif_setted: ' + str(exif_setted))
print('exif_date_not_found: ' + str(exif_date_not_found))
print('match_regular_exp1: ' + str(match_regular_exp1))
print('match_regular_exp2: ' + str(match_regular_exp2))
print('match_regular_exp3: ' + str(match_regular_exp3))
print('match_regular_exp4: ' + str(match_regular_exp4))
print('saved: ' + str(saved))
print('cannot_setted_date: ' + str(cannot_setted_date))