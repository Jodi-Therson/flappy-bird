# flappy-bird
A Simple Flappy Bird Game
Key Features:
-A Yellow(255, 255, 0) Circle represents a bird
-Green(0, 200, 0) Rectangles represent the pipes
-Blue(70, 197, 206) as the sky

The bird can be modified by adding an imgae and rename the 
bird = Bird("bird.png")
to the image path.

Haven't used images for the bird, pipes, and the sky. The bird has static movement as a circle.
Uses collections.deque module, to optimize the FIFO module.

Important:
You need to have pygame installed. You can go to terminal and do
pip install pygame (Make sure you have Python installed)

or

1. You can create a venv by typing this in terminal
python -m venv venv
2. Then you want to activate the venv
venv\Scripts\activate
3. Lastly you can install the pygame with the same version as mine
pip install pygame==2.6.1
4. Then you can run the script
python {filename}.py
