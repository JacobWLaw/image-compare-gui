# image-compare-gui

This was a simple project I created for use by manual testers and as a simple tool to give validation remotely using capture devices over a network. 

REQUIREMENTS:
- Pillow
- PyQt6

The program calculates the absolute difference and maps them with non-black for different pixels (RGB = 0,0,0). After that it converts to grayscale for simplicity, and any non-black pixels are turned to white while likeness remains black.

The comparison function also returns a percent difference that can be viewed inside the GUI as well. 

Threshold value is able to be set within the GUI - the number set here is the number you are content with them being the same. I.E entering 50 means a image that is 50% similar will be accepted as a pass.
