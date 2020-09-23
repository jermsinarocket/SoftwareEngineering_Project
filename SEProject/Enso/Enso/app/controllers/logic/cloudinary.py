import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests

def getImageURL(imageName,extension,folderName = ""):
    return cloudinary.utils.cloudinary_url(folderName + "" + imageName + "." + extension,secure=True)[0]

def getImageList(tagName):
        r = requests.get("http://res.cloudinary.com/hgdcwue1c/image/list/" + str(tagName) +".json")
        return r.json()['resources']

def uploadFile(file,publicID):
    cloudinary.uploader.upload(file, public_id = publicID)
