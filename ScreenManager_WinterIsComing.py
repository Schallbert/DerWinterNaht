import tkinter as tk
from Enums_WinterIsComing import cmd_inpt
from Enums_WinterIsComing import consts


# Window/helper classes
#----------------------------------------------
##class GameWindows:
##
textScreenText = "Euer Smartphone. Kann so ziemlich alles und ist natürlich auch mit Taschenlampe,\n\
Kamera und Navigationssystem ausgestattet.\n\
Hier draußen scheinen leider weder Mobilfunk noch Datenvervindung möglich zu sein.\n\
Zudem ist der Akkustand niedrig und ihr habt keine Powerbank dabei.\n"

# ------------------------------------
# HELPERS

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

# ------------------------------------
# CLASSES
class ResizingCanvas(tk.Canvas):
    """Class that generates the main frame all widgets are placed into.
To make it resizable, it listens to the width/height change event of the window.
In its init, it binds to the Configure event."""
#TODO: Enable flexible resizing of "video" window
    # a subclass of Canvas for dealing with resizing of windows
    def __init__(self,parent,**kwargs):
        tk.Canvas.__init__(self,parent,**kwargs)
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

class InputText(tk.Text):
    """Derived class from Text, with additional methods for text input handling.
It binds to the return key to take input"""
    #replace init function by "custom" init
    def __init__(self,parent,**kwargs):
        tk.Text.__init__(self,parent,**kwargs)
        self.__BindToKey('<Return>')
        #set modifyable special variable to bind events to it
        self.number = tk.IntVar()

    def GetInput(self):
        self.__Activate()
        #wait for variable "number" to be changed
        self.wait_variable(self.number)
        nmbr = self.number.get()
        self.insert(tk.INSERT, nmbr)
        self.__Deactivate()
        #return contents of variable
        return nmbr

    def __BindToKey(self, key):
        #bind self to event "return", calling inputCheck function
        #handing over its contents-last character (which is \n)
        self.bind(key, \
                  lambda event, \
                  : self.__EventHandler())

    def __EventHandler(self):
        #get input, deactivate box, check input
        inpt = self.get("1.0", "end-1c")
        """This routine takes an input string 'resp' and tries to convert it
        to the in-game used numbers. It also offers to quit the game if needed."""
        try :
            #Command valid
            intPt = int(inpt)
            self.number.set(intPt)
        except :
            if inpt.lower() == "quit":
                #Command quit
                self.number.set(cmd_inpt.QUIT.value)
            else:
                #Command invalid
                self.number.set(cmd_inpt.UNKNOWN.value)
        
    def __Activate(self):
        #Color and config set for activated status
        self.config(state=tk.NORMAL)
        self.delete('1.0', tk.END)
        self.config(fg=GuiVars.dictCP["Y5"])
        self.config(bg=GuiVars.dictCP["B2"])
        self.focus_set()
        
    def __Deactivate(self):
        #Color and config set for deactivated status
        self.config(fg=GuiVars.dictCP["B2"])
        self.config(bg=GuiVars.dictCP["B1"])
        self.config(state=tk.DISABLED)

class StatusText(tk.Text):
    """Derived from Text, optimized for player stats (table-type) colored text output
Offers public function Update that takes the player list to output the player's stats."""
    def __init__(self,parent,**kwargs):
        tk.Text.__init__(self,parent,**kwargs)
        
    def Update(self, playerList):
        self.__Activate()
        self.delete('1.0', tk.END)
        self.insert('1.0', "Name        Motivation      Müdigkeit\n")
        maxNamePlusSpaces = 12 #9 for name, 4 for whitespaces
        lineNr = 1
        for player in playerList:
            lineNr = lineNr + 1
            currMod = player.GetMod()
            modStr = "|"*10
            currName = player.GetName()
            nrSpaces = maxNamePlusSpaces - len(currName)
            #define contents and tags of texts to get colors right
            tagPlrS = str(lineNr)+'.0'
            tagPlrE = str(lineNr)+'.'+str(maxNamePlusSpaces)
            tagMotE = str(lineNr)+'.'+str(maxNamePlusSpaces + currMod[0])
            tagTirS = str(lineNr)+'.26'
            tagTirE = str(lineNr)+'.'+str(26 + currMod[1])
            tagModE = str(lineNr)+'.37'
            
            self.insert(tagPlrS, currName \
                        + " " * nrSpaces + modStr \
                        + " " * + 4 + modStr + "\n")
            self.tag_add(currName+"plrClr", tagPlrS, tagPlrE)
            self.tag_add(currName+"modClr", tagPlrE, tagModE)
            self.tag_add(currName+"motClr", tagPlrE, tagMotE)
            self.tag_add(currName+"tirClr", tagTirS, tagTirE)
            #define text colors
            self.tag_config(currName+"modClr", foreground=GuiVars.dictCP["B4"], font=consts.GUI_BOLD)
            self.tag_config(currName+"plrClr", foreground=player.GetColor())
            self.tag_config(currName+"motClr", foreground=self.__GetModColor(currMod[0]), font=consts.GUI_BOLD)
            self.tag_config(currName+"tirClr", foreground=self.__GetModColor(10-currMod[1]), font=consts.GUI_BOLD)
            self.update()
        self.after(consts.GUI_WAIT_UPDATE)
        self.__Deactivate()

    def __GetModColor(self, mod):
        if mod > 5 :
            return '#00FF00' #green
        elif mod > 2:
            return '#FFFF00' #yellow
        else:
            return '#FF0000' #red

    def __Activate(self):
        self.config(state=tk.NORMAL)
        self.config(fg=GuiVars.dictCP["Y4"])
        self.config(bg=GuiVars.dictCP["B2"])
        self.focus_set()
        
    def __Deactivate(self):
        self.config(bg=GuiVars.dictCP["B1"])
        self.config(state=tk.DISABLED)
        self.update()

class InventoryText(tk.Text):
    """Derived from Text, optimized for player inventory (table-type) text output
Offers public function Update that takes the inventory dict to present its contents"""
    def __init__(self,parent,**kwargs):
        tk.Text.__init__(self,parent,**kwargs)
        
    def Update(self, dictInventory):
        self.__Activate()
        self.delete('1.0', tk.END)
        self.insert('1.0', "Nr.   Gegenstand\n")
        cnt = 1
        for key, val in dictInventory.items():
            cnt = cnt + 1
            self.insert(str(cnt)+'.0', str(key) + "    " + val.name + "\n")
        self.after(consts.GUI_WAIT_UPDATE)
        self.__Deactivate()

    def __Activate(self):
        self.config(state=tk.NORMAL)
        self.config(fg=GuiVars.dictCP["Y4"])
        self.config(bg=GuiVars.dictCP["B2"])
        self.focus_set()
        
    def __Deactivate(self):
        self.config(bg=GuiVars.dictCP["B1"])
        self.config(state=tk.DISABLED)
        self.update()
        
class OutputText(tk.Text):
    #replace init function by "custom" init
    def __init__(self,parent,**kwargs):
        tk.Text.__init__(self,parent,**kwargs)
       
    def Clear(self):
        self.__Activate()
        self.delete('1.0', tk.END)
        self.__Deactivate()

    def LineWrite(self, text):
        self.__Activate()
        self.after(consts.GUI_LINEWRITE_WAIT)
        self.insert(tk.INSERT, text)
        self.update()
        self.__Deactivate()

    def TypeWrite(self, text):
        self.__Activate()
        self.__TypeWrite(text)
        self.__Deactivate()

    def NameWrite(self, player):
        self.__Activate()
        plName = player.GetName()
        linNr = int(self.index('end').split('.')[0])-1
        colSt = int(self.index('end').split('.')[-1])
        tagNameS = str(linNr) + '.' + str(colSt)
        tagNameE = str(linNr) + '.' + str(colSt+len(plName))
        self.__TypeWrite(plName)
        self.tag_add("plr", tagNameS, tagNameE)
        self.tag_config("plr", foreground=player.GetColor(), font=consts.GUI_BOLD)
        self.__Deactivate()

    def __TypeWrite(self, text):
        for text in text:
            self.insert(tk.INSERT, text)
            self.update()
            self.after(consts.GUI_TYPEWRITE_WAIT)
        
    def __Activate(self):
        self.config(state=tk.NORMAL)
        self.config(bg=GuiVars.dictCP["B2"])
        self.focus_set()
        
    def __Deactivate(self):
        #clear text then disable text screen
        self.config(bg=GuiVars.dictCP["B1"])
        self.config(state=tk.DISABLED)

class GameGui:

    def __init__(self):
        self.root = tk.Tk() #instantiate TKINTER (Gui package)
        img = tk.PhotoImage(file='Noise.gif') #TEST, to be replaced with game title image
        var = GuiVars() #variable container for gui setup
        self.root.title("Der Winter Naht")
        var.SetScrSize(int(self.root.winfo_screenwidth()), int(self.root.winfo_screenheight()))

        #Canvas
        myframe = tk.Frame(self.root)
        myframe.pack(fill=tk.BOTH, expand=tk.YES)
        canvas = ResizingCanvas(myframe,width=var.scr_w, height=var.scr_w, bg="black")
        canvas.pack(fill=tk.BOTH, expand=tk.YES)
        #Frames
        textScrFr = tk.Frame(canvas, bg=var.frClr, bd=var.frBdr)
        gameScrFr = tk.Frame(textScrFr, bg="black", bd=var.frBdr)
        invtScrFr = tk.Frame(canvas, bg=var.frClr, bd=var.frBdr)
        statsScrFr = tk.Frame(canvas, bg=var.frClr, bd=var.frBdr)
        inputScrFr = tk.Frame(canvas, bg=var.frClr, bd=var.frBdr)
        #Frame Pack
        textScrFr.pack(anchor=tk.NW, fill=tk.BOTH, expand=tk.YES)
        gameScrFr.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        invtScrFr.pack(anchor=tk.S, side=tk.LEFT, fill=tk.X, expand=tk.YES)
        statsScrFr.pack(anchor=tk.S, side=tk.LEFT, fill=tk.X, expand=tk.YES)
        inputScrFr.pack(anchor=tk.S, side=tk.LEFT, fill=tk.X, expand=tk.YES)

        #Screens   
        wid = textScrFr.winfo_id()
        self.textScreen = OutputText(textScrFr\
                                     , font=consts.GUI_FONT\
                                     , insertontime=0\
                                     , bg=var.scrBg\
                                     , fg=var.scrFg\
                                     , width=78\
                                     , height=20\
                                     , padx=12\
                                     , pady=9)  
        self.gameScreen = tk.Label(gameScrFr\
                                , font=consts.GUI_FONT\
                                , image=img\
                                , width=var.scr_w/2\
                                , height=var.scr_w*(9/32))
        self.inventoryScreen = InventoryText(invtScrFr\
                                          , font=consts.GUI_FONT\
                                          , bg=var.scrBg\
                                          , fg=var.scrFg\
                                          , width=25\
                                          , height=10\
                                          , padx=12\
                                          , pady=9)
        self.statsScreen = StatusText(statsScrFr\
                                      , font=consts.GUI_FONT\
                                      , bg=var.scrBg\
                                      , fg=var.scrFg\
                                      , width=40\
                                      , height=10\
                                      , padx=12\
                                      , pady=9)
        self.inputScreen = InputText(inputScrFr, font=("Lucida Console", "69") \
                                         ,insertbackground=var.scrFg\
                                         , insertofftime=1200\
                                         , insertontime=1200\
                                         , insertwidth=5\
                                         , width=5\
                                         , height=1\
                                         , padx=6\
                                         , bg=var.scrBg\
                                         , fg=var.scrFg\
                                         , pady=43)
        #Screen Pack
        self.textScreen.pack(side = tk.LEFT, fill=tk.Y, expand=tk.YES)
        self.gameScreen.pack(anchor = tk.CENTER, expand=tk.YES) 
        self.inventoryScreen.pack(side = tk.BOTTOM, fill=tk.X, expand=tk.YES) 
        self.statsScreen.pack(side = tk.LEFT, fill=tk.X, expand=tk.YES)  
        self.inputScreen.pack(side = tk.LEFT, fill=tk.X, expand=tk.YES)
   
