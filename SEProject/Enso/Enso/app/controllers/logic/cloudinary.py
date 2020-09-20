import cloudinary
import cloudinary.uploader
import cloudinary.api

def getImageURL(imageName,extension,folderName = ""):
    return cloudinary.utils.cloudinary_url(folderName + "" + imageName + "." + extension,secure=True)[0]

def getImageList(tagName):
    r = requests.get("http://res.cloudinary.com/hgdcwue1c/image/list/" + tagName +".json")
    return r.json()

def uploadFile(file,publicID):
    cloudinary.uploader.upload(file, public_id = publicID)
