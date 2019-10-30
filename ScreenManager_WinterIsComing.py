from tkinter import *


# Window/helper classes
#----------------------------------------------
##class GameWindows:
##
textScreenText = "Euer Smartphone. Kann so ziemlich alles und ist natürlich auch mit Taschenlampe,\n\
Kamera und Navigationssystem ausgestattet.\n\
Hier draußen scheinen leider weder Mobilfunk noch Datenvervindung möglich zu sein.\n\
Zudem ist der Akkustand niedrig und ihr habt keine Powerbank dabei."

# ------------------------------------
# HELPERS
def inputCheck(resp):
    try :
        number = int(resp)
        print(str(number))
    except :
        if resp.lower() == "quit":
            quitSave()
        else:
            print("Bitte eine Zahl eingeben oder das Spiel mittels 'quit' beenden.")
            mycanvas.inputScreen.Activate()

# ------------------------------------
# CLASSES
class ResizingCanvas(Canvas):
    # a subclass of Canvas for dealing with resizing of windows
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

class InputText(Text):
    #replace init function by "custom" init
    def __init__(self,parent,**kwargs):
        Text.__init__(self,parent,**kwargs)
        #bind self to event "return", calling inputCheck function
        #handing over its contents-last character (which is \n)
        self.bind('<Return>', \
                    lambda event, \
                    : self.__EventHandler())

    def __EventHandler(self):
        #get input, deactivate box, check input
        inpt = self.get("1.0", "end-1c")
        self.__Deactivate() 
        inputCheck(inpt)     
        
    def Activate(self):
        self.config(state=NORMAL)
        self.focus_set()
        
    def __Deactivate(self):
        #clear text then disable text screen
        self.delete('1.0', END)
        self.config(state=DISABLED)

#variables needed for gui setup
class GuiVars:
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
    #game window margin to screen size [pixels] 
    __xWMgn = 200  
    __yWMgn = 0
    #color selection
    frClr = dictCP["Y4"]
    scrFg = dictCP["Y4"]
    scrBg = dictCP["B1"]
    frBdr = 2 #pixels, looks nice ;)

    def SetScrSize(self, w, h):
        self.scr_w = w-self.__xWMgn
        self.scr_h = h-self.__yWMgn

def SetupGui():
    root = Tk() #instantiate TKINTER (Gui package)
    var = GuiVars() #variable container for gui setup
    root.title("Der Winter Naht")
    var.SetScrSize(int(root.winfo_screenwidth()), int(root.winfo_screenheight()))

    img = PhotoImage(file='Noise.gif') #TEST, to be replaced with game title image

    #Canvas
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=var.scr_w, height=var.scr_w, bg="black")
    mycanvas.pack(fill=BOTH, expand=YES)
    #Frames
    mycanvas.textScrFr = Frame(mycanvas, bg=var.frClr, bd=var.frBdr)
    mycanvas.gameScrFr = Frame(mycanvas.textScrFr, bg="black", bd=var.frBdr)
    mycanvas.invtScrFr = Frame(mycanvas, bg=var.frClr, bd=var.frBdr)
    mycanvas.statsScrFr = Frame(mycanvas, bg=var.frClr, bd=var.frBdr)
    mycanvas.inputScrFr = Frame(mycanvas, bg=var.frClr, bd=var.frBdr)

    mycanvas.textScrFr.pack(anchor=NW, fill=BOTH, expand=YES)
    mycanvas.gameScrFr.pack(side=RIGHT, fill=BOTH, expand=YES)
    mycanvas.invtScrFr.pack(anchor=S, side=LEFT, fill=X, expand=YES)
    mycanvas.statsScrFr.pack(anchor=S, side=LEFT, fill=X, expand=YES)
    mycanvas.inputScrFr.pack(anchor=S, side=LEFT, fill=X, expand=YES)

    #Screens   
    mycanvas.textScreen = Text(mycanvas.textScrFr, bg=var.scrBg, fg=var.scrFg, width=83, height=20, padx=12, pady=9)  
    mycanvas.gameScreen = Label(mycanvas.gameScrFr, image=img, width=var.scr_w/2, height=var.scr_w*(9/32))
    mycanvas.inventoryScreen = Text(mycanvas.invtScrFr, bg=var.scrBg, fg=var.scrFg, width=60, height=10, padx=12, pady=9)
    mycanvas.statsScreen = Text(mycanvas.statsScrFr, bg=var.scrBg, fg=var.scrFg, width=40, height=10, padx=12, pady=9)
    mycanvas.inputScreen = InputText(mycanvas.inputScrFr, font=("Helvetica", "63"), width=5, height=1, padx=24, bg=var.scrBg, fg=var.scrFg, pady=42)
    
    mycanvas.textScreen.pack(side = LEFT, fill=Y, expand=YES)
    mycanvas.gameScreen.pack(anchor = CENTER, expand=YES) 
    mycanvas.inventoryScreen.pack(side = BOTTOM, fill=X, expand=YES) 
    mycanvas.statsScreen.pack(side = LEFT, fill=X, expand=YES)  
    mycanvas.inputScreen.pack(side = LEFT, fill=X, expand=YES)

    #Texts
    mycanvas.textScreen.insert(INSERT, textScreenText)
    mycanvas.inputScreen.Activate()
    mycanvas.inventoryScreen.insert(INSERT, "Inventar")
    mycanvas.statsScreen.insert(INSERT, "Name          Motivation     Müdigkeit")



# def main():
    # root.mainloop()
    
    

   
    
# if __name__ == "__main__":
    # main()
    
