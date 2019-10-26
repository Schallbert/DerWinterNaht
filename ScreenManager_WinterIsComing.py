from tkinter import *


# Window/helper classes
#----------------------------------------------
##class GameWindows:
##
textScreenText = "Euer Smartphone. Kann so ziemlich alles und ist natürlich auch mit Taschenlampe,\n\
Kamera und Navigationssystem ausgestattet.\n\
Hier draußen scheinen leider weder Mobilfunk noch Datenvervindung möglich zu sein.\n\
Zudem ist der Akkustand niedrig und ihr habt keine Powerbank dabei."
##    
##    root = Tk()
##    xWindowMargin = 144
##    yWindowMargin = 108
##    frameColor = "grey"
##    frameBorder = 3
##    
##    #textScreenSize = [int(screen_w*1/2),int(screen_h*4/5)]
##    #inventoryScreenSize = [int(screen_w),int(screen_h*1/5)]
##    root.geometry(str(screen_w)+"x"+str(screen_h)) #window size
##    
##
##    topFrame = Frame(root, bg=frameColor, bd=frameBorder)
##    topFrame.pack(anchor=NW)
##    bottomFrame = Frame(root, bg=frameColor, bd=frameBorder)
##    bottomFrame.pack(anchor=SW)
##    #leftFrame = Frame(root, bg=frameColor, bd=frameBorder)
##    #leftFrame.pack(side = LEFT)
##    #rightFrame = Frame(root, bg=frameColor,bd=frameBorder)
##    #rightFrame.pack(side = RIGHT)
##    
##    textScreen = Text(topFrame, bg="black", fg="lightgrey", width=85, height=34, padx=12, pady=9)
##    textScreen.insert(INSERT, textScreenText)
##    textScreen.pack(side = LEFT)
##    
##    inventoryScreen = Text(bottomFrame, bg="black", fg="lightgrey", width=110, height=10, padx=12, pady=9)
##    inventoryScreen.pack(side = LEFT)
##    statsScreen = Text(bottomFrame, bg="black", fg="lightgrey", width=40, height=10, padx=12, pady=9)
##    statsScreen.pack(side = LEFT)
##    inputScreen = Text(bottomFrame, bg="black", fg="lightgrey", width=14, height=10, padx=12, pady=9)
##    inputScreen.pack(side = LEFT)
##    
##    root.mainloop()
    
    #flags= pygame.NOFRAME
    #textWindow = pygame.display.set_mode(textScreenSize)
    #pygame.display.set_caption("Der Winter naht")

    # a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

def main():
    #textScreenText = "Hello World"
    xWindowMargin = 200
    yWindowMargin = 108
    frameColor = "grey"
    frameBorder = 3
    root = Tk()
    root.title("Der Winter Naht")
    screen_w = int(root.winfo_screenwidth() - xWindowMargin)
    screen_h = int(root.winfo_screenheight() - yWindowMargin)
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=screen_w, height=screen_h,\
                              bg="black")
    mycanvas.pack(fill=BOTH, expand=YES)

    img = PhotoImage(file='Noise.gif')
    
    # add some widgets to the canvas
    
    #tstxt = StringVar()
    mycanvas.textScrFr = Frame(mycanvas, bg=frameColor, bd=frameBorder)
    mycanvas.gameScrFr = Frame(mycanvas.textScrFr, bg="black", bd=frameBorder)
    mycanvas.invtScrFr = Frame(mycanvas, bg=frameColor, bd=frameBorder)
    mycanvas.statsScrFr = Frame(mycanvas, bg=frameColor, bd=frameBorder)
    mycanvas.inputScrFr = Frame(mycanvas, bg=frameColor, bd=frameBorder)

    mycanvas.textScrFr.pack(anchor=NW, fill=BOTH, expand=YES)
    mycanvas.gameScrFr.pack(side=RIGHT, fill=BOTH, expand=YES)
    mycanvas.invtScrFr.pack(anchor=S, side=LEFT, fill=X, expand=YES)
    mycanvas.statsScrFr.pack(anchor=S, side=LEFT, fill=X, expand=YES)
    mycanvas.inputScrFr.pack(anchor=S, side=LEFT, fill=X, expand=YES)
    
       
    mycanvas.textScreen = Text(mycanvas.textScrFr, bg="black", fg="lightgrey", width=85, height=20, padx=12, pady=9)
    mycanvas.textScreen.pack(side = LEFT, fill=Y, expand=YES)
    
    mycanvas.gameScreen = Label(mycanvas.gameScrFr, image=img, padx=12, pady=9, width=700, height=400)
    mycanvas.gameScreen.pack(anchor = CENTER, expand=YES)

    mycanvas.inventoryScreen = Text(mycanvas.invtScrFr, bg="black", fg="lightgrey", width=70, height=10, padx=12, pady=9)
    mycanvas.inventoryScreen.pack(side = BOTTOM, fill=X, expand=YES)

    mycanvas.statsScreen = Text(mycanvas.statsScrFr, bg="black", fg="lightgrey", width=40, height=10, padx=12, pady=9)
    mycanvas.statsScreen.pack(side = LEFT, fill=X, expand=YES)
    
    mycanvas.inputScreen = Text(mycanvas.inputScrFr, bg="black", fg="lightgrey", width=14, height=10, padx=12, pady=9)
    mycanvas.inputScreen.pack(side = LEFT, fill=X, expand=YES)

    mycanvas.textScreen.insert(INSERT, textScreenText)
    mycanvas.inputScreen.insert(INSERT, "Input:")
    mycanvas.inventoryScreen.insert(INSERT, "Inventory:")
    mycanvas.statsScreen.insert(INSERT, "stats")

    

    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()
    
