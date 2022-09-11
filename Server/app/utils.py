# from deepface import DeepFace
from PIL import Image
import pytesseract
import uuid

SpecialSym =['$', '@', '#', '%', '!', '&', '^', '-', '_', '=', '+' ]


def getDetails(path_of_img):
  im = Image.open(path_of_img)
  width, height = im.size

  left = 110
  top = 170
  right = 900
  bottom =height-180

  img = im.crop((left, top, right, bottom))
  name = "data/others/" + str(uuid.uuid4()) + ".jpg"
  img.save(name)
  img = Image.open(name,"r")
  text = pytesseract.image_to_string(name,"eng")
  text.strip()
  words=text.split("\n")
  for i in words:
    if i=='':
      words.remove("")
  details=[]
  (name,dob,gender)=(words[0],words[1],words[2])
  dobr=""
  for i in dob:
    if str(i).isnumeric() or i=='/':
      dobr+=i
  details.append(name)
  details.append(dobr)
  details.append(gender)
  return details

def getNo(path_of_img):
  im = Image.open(path_of_img)
  width, height = im.size

  left = 260
  top = 400
  right = 670
  bottom =height-100

  img = im.crop((left, top, right, bottom))
  text = pytesseract.image_to_string(img,"eng")
  text.strip()
  return text

# def face_recog(img_path):
#     recognition = DeepFace.find(img_path = "img/2.jpeg", db_path = "data/")
# print(recognition)


# def getAddress(path_of_img):
#     im = Image.open(path_of_img)
#     width, height = im.size
#     img = im.crop((110, 170, 900, height-180))
#     text = pytesseract.image_to_string(img,"eng")
#     text.strip("\n")
#     words = text.split()
#     for i in words:
#         if i == "Address":
#             words.remove(i)
#     text = ""
#     for i in words:
#         text += i + ' '
#     return text


# def getDataFromIDcard(path_of_img):
#     im = Image.open(path_of_img)
#     width, height = im.size
#     img = im.crop((110, 170, 900, height-180))
#     name = "data/others/" + str(uuid.uuid4()) + ".jpg"
#     img.save(name)
#     img = Image.open(name, "r")
#     text = pytesseract.image_to_string(name, "eng")
#     text.strip()
#     words = text.split("\n")
#     words = text.split()
#     details=[]
#     (name,dob,gender)=(words[0],words[1],words[2])
#     dobr = ""
#     for i in dob:
#         if str(i).isnumeric() or i == '/':
#             dobr += i

#     im = Image.open(path_of_img)
#     width, height = im.size
#     img = im.crop((250, 400, 670, height-100))
#     abc = pytesseract.image_to_string(img,"eng")
#     # abc.strip("\n")
#     # abc.strip("!")
#     for i in SpecialSym:
#         abc.strip(i)
#     abc.strip("\n")
#     abc.strip()

#     details.append(name)
#     details.append(dobr)
#     details.append(abc)
#     details.append(gender)

#     return details
