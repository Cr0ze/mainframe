"""
File: MGSCFP_msa.py
Author: Max S Appleton (msa)

Purpose 1: Access, manipulate, and save an image.
Purpose 2: Looping, or iterating, through each pixel in two images to composite them.
Extra 1: Choose from a variety of fitlers or no filter to apply to the image. 

Make sure to install pillow locally, execute via terminal
Windows:
py -m pip install pillow --user
Mac:
python3 -m pip install pillow --user
"""
#------------------------------------------------------------------------------
from PIL import Image, ImageFilter
#------------------------------------------------------------------------------
print("\nWelcome to Max's Green Screen Composite and Filter Program or MGSCFP for short\n")
#get the file name from the user
bckgrd_img = input('file name for the background image (include extension): ')
grnscr_img = input('file name for the green screen image (include extension): ')

#Reads the images into variables
image_bckgrd = Image.open(bckgrd_img)
image_grnscr = Image.open(grnscr_img)

#Creatinmg a new blank image
image_combined = Image.new("RGB", image_bckgrd.size)

#Resize the Green Screen to match the Background image
image_grnscr = image_grnscr.resize(image_bckgrd.size)

#Size of all images
width_bckgrd, height_bckgrd = image_bckgrd.size
width_grnscr, height_grnscr = image_grnscr.size

#Pixel info for all images
pixel_bckgrd = image_bckgrd.load()
pixel_grnscr = image_grnscr.load()
pixel_combined = image_combined.load()
#-------------------------------------------------------------------------------
#Modify pixel RGB values through FOR loops. 
#-------------------------------------------------------------------------------
#determining the Green Screen background color.
(r_grnscr, g_grnscr, b_grnscr) = pixel_grnscr[25, 25]

#for the new image x
for x in range (0 , 800):
    #for the new image y
    for y in range (0, 600):
        #eval if green screen pixel for (x, y) is (0, 255, 0)
        (r, g, b) = pixel_grnscr[x, y]
        #if green screen pixel != (0, 255, 0)
        if pixel_grnscr[x, y] != (r_grnscr, g_grnscr, b_grnscr):
            #write green screen pixel @ (x, y) to new image
            (r, g, b) = pixel_grnscr[x, y]
            pixel_combined[x, y] = (r, g, b)
        #if green screen pixel == (0, 255, 0)
        elif pixel_grnscr[x, y] == (r_grnscr, g_grnscr, b_grnscr):
            #write backfround pixel @ (x, y) to new image
            (r, g, b) = pixel_bckgrd[x, y]
            pixel_combined[x, y] = (r, g, b)
#-------------------------------------------------------------------------------
#Apply filters
#-------------------------------------------------------------------------------
#Filter menu
print('\nPlease select an option from this list')
print('1: Blur\n2: Sharpen\n3: Contour\n4: Detail\n5: Emboss\n0: None')
filter_choice = int(input('Enter the number of your selection: '))

#Blur effect
if filter_choice == 1:
    image_combined = image_combined.filter(ImageFilter.BLUR)
#Sharpen effect
elif filter_choice == 2:
    image_combined = image_combined.filter(ImageFilter.SHARPEN)
#Contour Effect
elif filter_choice == 3:
    image_combined = image_combined.filter(ImageFilter.CONTOUR)
#Detail effect
elif filter_choice == 4:
    image_combined = image_combined.filter(ImageFilter.DETAIL)
#Emboss effect
elif filter_choice == 5:
    image_combined = image_combined.filter(ImageFilter.EMBOSS)
else:
    print('\nNo filter selected.\n')
#-------------------------------------------------------------------------------
#Output of the new image and displaying the image
#-------------------------------------------------------------------------------
image_combined.save("composite_image.jpg")
image_combined.show()
