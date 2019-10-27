from tkinter import *


# Window/helper classes
#----------------------------------------------
##class GameWindows:
##
textScreenText = "Euer Smartphone. Kann so ziemlich alles und ist natürlich auch mit Taschenlampe,\n\
Kamera und Navigationssystem ausgestattet.\n\
Hier draußen scheinen leider weder Mobilfunk noch Datenvervindung möglich zu sein.\n\
Zudem ist der Akkustand niedrig und ihr habt keine Powerbank dabei."

#Color Palette used throughout the game
dictCP = {
    "B0" : '#000000',\
    "B1" : '#000040',\
    "B2" : '#003870',\
    "B3" : '#0064C0',\
    "B4" : '#3990C0',\
    "Y0" : '#5F4443',\
    "Y1" : '#9C7868',\
    "Y2" : '#E7E39B',\
    "Y3" : '#CEC098',\
    "Y4" : '#FFFFBF',\
    "Y5" : '#FFFFE6'
    }

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

def showInputOnLabel():
    pass


def main():
    xWindowMargin = 200
    yWindowMargin = 0
    frameColor = dictCP["Y4"]
    screenFG = dictCP["Y4"]
    screenBG = dictCP["B1"]
    
    frameBorder = 2
    root = Tk()
    root.title("Der Winter Naht")
    img = PhotoImage(file='Noise.gif') #to be replaced with game title image
    
    screen_w = int(root.winfo_screenwidth() - xWindowMargin)
    screen_h = int(root.winfo_screenheight() - yWindowMargin)

    #Canvas
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=screen_w, height=screen_h, bg="black")
    mycanvas.pack(fill=BOTH, expand=YES)
    #Frames
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
    
    #Screens   
    mycanvas.textScreen = Text(mycanvas.textScrFr, bg=screenBG, fg=screenFG, width=85, height=20, padx=12, pady=9)
    mycanvas.textScreen.pack(side = LEFT, fill=Y, expand=YES)   
    mycanvas.gameScreen = Label(mycanvas.gameScrFr, image=img, padx=12, pady=9, width=screen_w/2, height=screen_h/2)
    mycanvas.gameScreen.pack(anchor = CENTER, expand=YES)
    mycanvas.inventoryScreen = Text(mycanvas.invtScrFr, bg=screenBG, fg=screenFG, width=60, height=10, padx=12, pady=9)
    mycanvas.inventoryScreen.pack(side = BOTTOM, fill=X, expand=YES)
    mycanvas.statsScreen = Text(mycanvas.statsScrFr, bg=screenBG, fg=screenFG, width=40, height=10, padx=12, pady=9)
    mycanvas.statsScreen.pack(side = LEFT, fill=X, expand=YES)  
    mycanvas.inputScreen = Text(mycanvas.inputScrFr, font=("Helvetica", "63"), width=5, height=1, padx=24, bg=screenBG, fg=screenFG, pady=42)
    mycanvas.inputScreen.pack(side = LEFT, fill=X, expand=YES)

    #Texts
    mycanvas.textScreen.insert(INSERT, textScreenText)
    mycanvas.inputScreen.insert(INSERT, "01467")
    mycanvas.inventoryScreen.insert(INSERT, "Inventar")
    mycanvas.statsScreen.insert(INSERT, "Name          Motivation     Müdigkeit")

    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()
    
