# import the following libraries 
# will convert the image to text string 
import pytesseract	 

# adds image processing capabilities 
from PIL import Image	 

# converts the text to speech 
import pyttsx3		 
from skimage import io as skio
#translates into the mentioned language 
from googletrans import Translator	 

# opening an image from the source path 
img = Image.open('text1.png')	 
img = skio.imread('https://store-images.s-microsoft.com/image/apps.54739.14266069062940839.0386a7c7-7a53-4e48-b184-3c1b8af04617.60917b6c-f77d-4aef-baf4-b8aa891c5889?mode=scale&q=90&h=720&w=1280')
# describes image format in the output 
print(img)						 
# path where the tesseract module is installed 
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable 
result = pytesseract.image_to_string(img) 
# write text in a text file and save it to source path 
with open('abc.txt',mode ='w') as file:	 
	
				file.write(result) 
				print(result) 
				
p = Translator()					 
# translates the text into german language 
k = p.translate(result,dest='german')	 
print(k) 
engine = pyttsx3.init() 

# an audio will be played which speaks the test if pyttsx3 recognizes it 
engine.say(k)							 
engine.runAndWait() 

import mymodule
help('modules')
