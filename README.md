# image-compare-gui

This was a simple project I created for use by manual testers and as a simple tool to give validation remotely using capture devices over a network. 

REQUIREMENTS:
- Pillow
- PyQt6

The program calculates the absolute difference and maps them. The comparison function also returns a percent difference that can be viewed inside the GUI as well. 

Currently, the image generated as the resultant is a bit scrambled, and layers all of the different pixels, this will be revised in a future update.

NOTE: If images are extremely dissimilar the resultant image will be almost unusable. This is to be used on pictures with commonality but differences that aren't inherently obvious.

Example Usage:
1. Load Baseline
![image](https://github.com/user-attachments/assets/3c70606a-7314-4fc9-bf6d-6a96e204f134)

2. Load Actual
![image](https://github.com/user-attachments/assets/c49a183a-79d9-486b-8cc5-cdbd781ea87e)

3. Compare
![image](https://github.com/user-attachments/assets/b3a8d0c8-3186-4c8b-a1f1-f1c690a03ba8)


