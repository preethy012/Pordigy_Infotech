#Task 02

Pixel Manipulation for Image Encryption
-----------------------------------------------------------------------------------------------------------------------------------------------------

This tool lets you hide an image by changing its colors using a secret number (key). You can also get the original image back using the same key.

----------------------------------------------------------------------------------------------------------------------------------------------------

What You Need ?
Python installed on your computer

Use Pillow library (for working with images)

----------------------------------------------------------------------------------------------------------------------------------------------------
How to Use?

Put the image you want to encrypt in the project folder. Name it original.jpg.

Run the program 
The program will create two new images:

encrypted.png (the hidden/encrypted image)

decrypted.jpg (the original image restored)

----------------------------------------------------------------------------------------------------------------------------------------------------

How It Works?

The program changes the color of each pixel by adding a secret number (key).

To get the original image, it subtracts that same number from each pixel.

If you use the wrong key, the image won’t look right.

Change the Key
In the code, you can change the number here to any value between 1 and 255:


key = 50

