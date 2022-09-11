from core.settings import BASE_DIR
from deepface import DeepFace
from PIL import Image
import pytesseract
import uuid


def getDetails(im):
    width, height = im.size
    img = im.crop((110, 170, 900, height-180))
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

    width, height = im.size
    img = im.crop((260, 400, 670, height-100))
    id_no = pytesseract.image_to_string(img,"eng")
    id_no.strip("\n")
    id_no.strip()
    
    details.append(name)
    details.append(dobr)
    details.append(id_no)
    details.append(gender)
    return details

db_path = str(BASE_DIR) + "/data/user_img"

def match_face(img_path):
    try:
        df = DeepFace.find(img_path=img_path, db_path=db_path)
        val = df.values.tolist()
        return val[0][0]
    except Exception as e:
        return False
