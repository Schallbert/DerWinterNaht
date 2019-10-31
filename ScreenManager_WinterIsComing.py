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
            gui.inputScreen.Activate()

def textReader(widget, index, text):
    if len(text) > 0:
        widget.insert(index, text[0])
        if len(text) > 1:
            # compute index of next char
             index = widget.index("%s + 1 char" % index)
             # type next char [ms]
             widget.after(30, textReader, widget, index, text[1:])
             #add blip-like sound on output?
        else:
            widget.config(fg=GuiVars.dictCP["Y4"])
            widget.config(bg=GuiVars.dictCP["B1"])
            widget.config(state=DISABLED)

def quitSave():
    print("Speichern...")
    save()
    print("Spiel wird beendet.")
    quit()

def save():
    print("IMPLEMENT SAVE!")
    print("Gespeichert!")

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

    def BindToKey(self, key):
        #bind self to event "return", calling inputCheck function
        #handing over its contents-last character (which is \n)
        self.bind(key, \
                  lambda event, \
                  : self.__EventHandler())

    def __EventHandler(self):
        #get input, deactivate box, check input
        inpt = self.get("1.0", "end-1c")
        self.__Deactivate() 
        inputCheck(inpt)

    def Update(self, text):
        self.config(state=NORMAL)
        self.delete('2.0', END)
        self.insert(INSERT, text)
        self.config(state=DISABLED)

    def Write(self, text):
        self.Activate()
        textReader(self, '1.0', text)
        
    def Activate(self):
        self.config(state=NORMAL)
        self.delete('1.0', END)
        self.config(fg=GuiVars.dictCP["Y5"])
        self.config(bg=GuiVars.dictCP["B2"])
        self.focus_set()
        
    def __Deactivate(self):
        #clear text then disable text screen
        self.config(fg=GuiVars.dictCP["B2"])
        self.config(bg=GuiVars.dictCP["B1"])
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

class GameGui:
    
    def __init__(self):
        root = Tk() #instantiate TKINTER (Gui package)
        img = PhotoImage(file='Noise.gif') #TEST, to be replaced with game title image
        var = GuiVars() #variable container for gui setup
        root.title("Der Winter Naht")
        var.SetScrSize(int(root.winfo_screenwidth()), int(root.winfo_screenheight()))

        #Canvas
        myframe = Frame(root)
        myframe.pack(fill=BOTH, expand=YES)
        canvas = ResizingCanvas(myframe,width=var.scr_w, height=var.scr_w, bg="black")
        canvas.pack(fill=BOTH, expand=YES)
        #Frames
        self.textScrFr = Frame(canvas, bg=var.frClr, bd=var.frBdr)
        self.gameScrFr = Frame(self.textScrFr, bg="black", bd=var.frBdr)
        self.invtScrFr = Frame(canvas, bg=var.frClr, bd=var.frBdr)
        self.statsScrFr = Frame(canvas, bg=var.frClr, bd=var.frBdr)
        self.inputScrFr = Frame(canvas, bg=var.frClr, bd=var.frBdr)

        self.textScrFr.pack(anchor=NW, fill=BOTH, expand=YES)
        self.gameScrFr.pack(side=RIGHT, fill=BOTH, expand=YES)
        self.invtScrFr.pack(anchor=S, side=LEFT, fill=X, expand=YES)
        self.statsScrFr.pack(anchor=S, side=LEFT, fill=X, expand=YES)
        self.inputScrFr.pack(anchor=S, side=LEFT, fill=X, expand=YES)

        #Screens   
        self.textScreen = InputText(self.textScrFr, insertontime=0, bg=var.scrBg, fg=var.scrFg, width=83, height=20, padx=12, pady=9)  
        self.gameScreen = Label(self.gameScrFr, image=img, width=var.scr_w/2, height=var.scr_w*(9/32))
        self.inventoryScreen = InputText(self.invtScrFr, bg=var.scrBg, fg=var.scrFg, width=60, height=10, padx=12, pady=9)
        self.statsScreen = InputText(self.statsScrFr, bg=var.scrBg, fg=var.scrFg, width=40, height=10, padx=12, pady=9)
        self.inputScreen = InputText(self.inputScrFr, font=("Helvetica", "63") \
                                         ,insertbackground=var.scrFg\
                                         , insertofftime=1200\
                                         , insertontime=1200\
                                         , insertwidth=5\
                                         , width=5\
                                         , height=1\
                                         , padx=24\
                                         , bg=var.scrBg\
                                         , fg=var.scrFg\
                                         , pady=42)
        
        self.textScreen.pack(side = LEFT, fill=Y, expand=YES)
        self.gameScreen.pack(anchor = CENTER, expand=YES) 
        self.inventoryScreen.pack(side = BOTTOM, fill=X, expand=YES) 
        self.statsScreen.pack(side = LEFT, fill=X, expand=YES)  
        self.inputScreen.pack(side = LEFT, fill=X, expand=YES)

        self.inputScreen.BindToKey('<Return>')
        #Texts
        self.inventoryScreen.insert(INSERT, "Inventar")
        self.statsScreen.insert(INSERT, "Name          Motivation     Müdigkeit")

gui = GameGui()
gui.textScreen.Write(textScreenText)
gui.inputScreen.Activate()

# def main():
    # root.mainloop()
    
    

   
    
# if __name__ == "__main__":
    # main()
    
