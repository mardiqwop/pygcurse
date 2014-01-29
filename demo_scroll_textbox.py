import pygcurse
import pygame
import sys
from pygame.locals import *

pygame.init()
boxregion = (1,1,20,20)
win = pygcurse.PygcurseWindow(80,50,' How to Scroll a PygcurseTextbox')


# make sure that scrollable is set to True
# scrollamount is how many words will get scrolled up in each event
testbox = pygcurse.PygcurseTextbox(win, region=boxregion,scrollable=True,scrollamount=3)

# instead of setting your text with testbox.text =
# set it with this :
testbox.fulltext = '''
We are the miracle of force and matter making itself over into imagination and will. Incredible. The Life Force experimenting with forms. You for one. Me for another. The Universe has shouted itself alive. We are one of the shouts.
 - Ray Bradbury
'''

# do this so fulltext will be shown before scroll is called
testbox.text = testbox.fulltext

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        # call scroll with any pygame event
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 4:
                testbox.scroll('up')
            elif event.button == 5:
                testbox.scroll('down')
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                testbox.scroll('up')
            elif event.key == K_DOWN:
                testbox.scroll('down')

    testbox.update()
    win.update()
