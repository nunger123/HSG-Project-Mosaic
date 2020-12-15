# HSG-Project-Mosaic (Python3)

***Project Description***
This is a student project of the University of St. Gallen within the course Programming – Introduction Level. Python is the programming language used for the project. The goal of the project was to create a mosaic of small pictures, which on the whole imitates a larger picture. Since we, Nikolas and Moritz, are both very interested in art, we decided to take a picture of an artist with simple colours and recreate this image with many (1616 to be exact) smaller pictures. 

We focused on bees for the small pictures since xxxxx

In order to use and test the program, please see the "Use & Application" Section below.


***Structure***
Our whole project is divided into 2 parts:

1.	Downloading and resizing of 1616 bee pictures 
    We used Flickr's API to download pictures of bees, as it was relatively easy to use with python
    Subsequently we resized all pictures to the same size and saved them to the "Bees" folder
    
2.  From this bee-picture folder and our target image (e.g. Rothko painting), we now created a mosaic, matching the avg. RGB colour values of each bee picture, with the RGB value of a "pixel" of the target image (target image is divided into 1600 pixels)

In order to test this, only step 2 should be carried out (as step 1 takes quite long and involves more steps)!


***Instructions***
1.  Download the "Colour_Spectrum_Target"-image and the "Bees"-folder into a folder on you computer locally (has to be same folder)

2.  Numpy and Pillow (PIL) packages need to be installed on computer locally

3.  Copy the code from "Create_Mosaic" into your IDE and save the file in the same folder as the "Colour_Spectrum_Target"-image and "Bees"-folder

4.  Run the code file that you just saved (e.g. from terminal). It might take a few minutes to load. Afterward click on the newly created "Output"-image and the mosaic should   appear:)



The program first fetches bee pictures from Flickr since they appear in many different colors, making the final mosaic target picture more vivid. These pictures are downloaded and cropped to a unified shape. Resizing serves the purpose of creating a mosaic of a previously selected target picture by putting them together. In order to create the mosaic, the target image needs to be split in smaller images as a first step. For these smaller pictures the average RGB color needs to be calculated. Same needs to be done for the input images. The generated multiple target images and the input images can be compared for the best match index and finally, target images can be replaced by input images with the best match. The initial target picture is now displayed as a mosaic of colorful bee pictures.



***Thanks for your interest***

Should you have any questions, do not hesitate to contact nikolas.unger@student.unisg.ch or moritz.kaufhold@student.unisg.ch.

Hope you enjoy the project,

Nikolas & Moritz
