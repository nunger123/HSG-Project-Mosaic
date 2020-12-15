#Importing the required libraries
import os
from PIL import Image, ImageOps 
import numpy as np 

input_images = []
avgs = [] 

def getRGBAverage(image): 
 #Given Image, return average RGB value as triplet
  im = np.array(image) 
  sh = im.shape
  if (len(sh) > 2): 
    w,h,b = im.shape 
    return tuple(np.average(im.reshape(w*h, b), axis=0)) 
  else:
    return tuple([94.17938659, 96.4187611, 31.38851464])
  
def splitImage(image, size): 
  #split image into m*n small images 
  m, n = size 
  w, h = int(image.size[0]/n), int(image.size[1]/m) 
  imgs = [] 
  for j in range(m): 
    for i in range(n):
      imgs.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h))) 
  return imgs 
  
def getImages(imageDir): 
  #get images from a Folder of images
  folder = os.listdir(imageDir) 
  images = [] 
  for file in folder: 
    filePath = os.path.abspath(os.path.join(imageDir, file)) 
    fp = open(filePath, "rb") 
    im = Image.open(fp) 
    images.append(im) 
    # force loading image data from file 
    im.load()  
    # close the file 
    fp.close()  
  return images 
  
def findBestMatch(input_avg): 
  #return list index of image with closted RGB average
  global avgs
  global input_images
  avg = input_avg 
    
  # get the closest RGB value to input, based on x/y/z distance 
  index = 0
  best_index = 0
  best = float("inf")
  for val in avgs: 
    if val != []:
      dist = ((val[0] - avg[0])*(val[0] - avg[0]) +
            (val[1] - avg[1])*(val[1] - avg[1]) +
            (val[2] - avg[2])*(val[2] - avg[2])) 
      if dist < best: 
        best = dist 
        best_index = index
    index += 1
  return best_index

def createMosaic(images, dims): 
  #create m*n mosaic from list with the chosen small images

  m, n = dims
  width = max([img.size[0] for img in images]) 
  height = max([img.size[1] for img in images]) 
  
  # fill mosaic image with chosen images
  new_mosaic_image = Image.new('RGB', (n*width, m*height)) 
    
  for index in range(len(images)):
    row = int(index/n) 
    col = index - n*row 
    new_mosaic_image.paste(images[index], (col*width, row*height)) 

  return new_mosaic_image 
  
def main(): 
  global input_images
  global avgs
  output_images = [] 

  #Inputs, file names
  target_image = 'Colour_Spectrum_Target.png'
  input_folder = 'Bees'
  output_filename = 'Output.jpg'
  grid_size = (40, 40)

  # read inputs
  target_image = Image.open(target_image) 
  input_images = getImages(input_folder) 

   # calculate input image average RGB
  for img in input_images: 
    avgs.append(getRGBAverage(img))

  # split target image into smaller images
  target_images = splitImage(target_image, grid_size)

  ind = 0
  count = 0
  #for each target image chose the optimal image from input images
  for img in target_images: 
    avg = getRGBAverage(img)

    # find match index 
    match_index = findBestMatch(avg)
    img_with_border = ImageOps.expand(input_images[match_index],border=10,fill='white')
    output_images.append(img_with_border)
    # user feedback 
    if count > 0 and count % 100 == 0: 
      print('processed %d so far...' %(count)) 
    count += 1
    avgs[match_index] = [] #so we dont have doubles of input images

  mosaic = createMosaic(output_images, grid_size) 
  mosaic.save(output_filename, 'PNG') 

if __name__ == '__main__': 
  main()
