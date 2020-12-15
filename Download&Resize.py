#This code is merely meant to show how we obtained the bee pictures

#We searched, resized and downloaded 1800 flickr bee pictures to then use further

#Importing the relevant libraries
import requests
from PIL import Image
from flickrapi import FlickrAPI
from io import BytesIO

#Below refers to the Flickr API Keys. When creating an account we received them (removed from here since they are private)
FLICKR_PUBLIC = '*****************************'
FLICKR_SECRET = '***************'

#Folder path (unique to user, in this case Nikolas Unger)
path = r'C:\Users\Nikolas Unger\Desktop\Projects\hsg-mosaic-python\test\flickr_biene\''
  
def fetch_images(search):
    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    response = flickr.photos.search(text=search, per_page=200, sort='relevance', page = 9, privacy_filter=1)
    photo = response['photos']['photo']

    size=(333,333)

    count = 0
    for i in range(len(photo)):
        url = "https://farm" + str(photo[i]['farm']) +".staticflickr.com/"+photo[i]['server']+ "/" +str(photo[i]['id'])+"_"+photo[i]['secret']+".jpg"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img_width, img_height = img.size
        crop_height = min (img_width, img_height)
        crop_width = min (img_width, img_height)
        if crop_width>332:
            square = img.crop(((img_width - crop_width) // 2,
                            (img_height - crop_height) // 2,
                            (img_width + crop_width) // 2,
                            (img_height + crop_height) // 2))
            square = square.resize(size)
            name = (path + 'z_flickr_chinesisch_' + str(1800+ i))
            square.save(name, 'JPEG') 
        if count%100 == 0: 
            print('processed so far...' + str(count))
        count += 1

        
#Execute the function for search term "bee"        
fetch_images('bee')
