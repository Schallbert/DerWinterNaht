import tkinter as tk
import imageio
from timeit import default_timer as timer
from pygame import mixer as mix
from PIL import Image, ImageTk
from Enums_WinterIsComing import cmd_inpt
from Enums_WinterIsComing import consts
from Enums_WinterIsComing import sounds
from Enums_WinterIsComing import playermod
from GameStatClass_WinterIsComing import GameStats


# Window/helper classes
#----------------------------------------------
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
    __yWMgn = 200
    #color selection
    frClr = dictCP["Y4"]
    scrFg = dictCP["Y4"]
    scrBg = dictCP["B1"]
    frBdr = 2 #pixels, looks nice ;)

    def setGameGuiSize(self, varWidHeight):
        self.scr_w = varWidHeight[0]-self.__xWMgn
        self.scr_h = varWidHeight[1]-self.__yWMgn

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
        #invokeTextScreenFontResize()

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
            intPt = abs(intPt) #make absolute to not allow entering hidden IDs
            self.number.set(intPt)
        except :
            if inpt.lower() == "quit":
                #Command quit
                self.number.set(cmd_inpt.QUIT)
            else:
                #Command invalid
                self.number.set(cmd_inpt.UNKNOWN)
        
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
        maxNamePlusSpaces = 12 #planned 9 for name, 4 for whitespaces
        lineNr = 1
        modStr = "|"*10
        for player in playerList:
            lineNr = lineNr + 1
            currMod = player.GetMod(playermod.CURRMOD)
            lastMod = player.GetMod(playermod.LASTMOD)
            currName = player.GetName()
            nrSpaces = maxNamePlusSpaces - len(currName)
            if nrSpaces < 0 :
                #name must be elided, does not fit into screen...
                currName = currName[0:maxNamePlusSpaces-4]+"..." #-4 to leave one space blank
                nrSpaces = 0       
            #define contents and tags of texts to get colors right
            tagPlrS = str(lineNr)+'.0'
            tagPlrE = str(lineNr)+'.'+str(maxNamePlusSpaces)
            tagMotE = str(lineNr)+'.'+str(maxNamePlusSpaces + currMod[0])
            taglMotE = str(lineNr)+'.'+str(maxNamePlusSpaces + lastMod[0])
            tagTirS = str(lineNr)+'.26'
            tagTirE = str(lineNr)+'.'+str(26 + 10 - currMod[1]) #tiredness is calculated inversely
            taglTirE = str(lineNr)+'.'+str(26 + 10 - lastMod[1])
            tagModE = str(lineNr)+'.37'
            
            self.insert(tagPlrS, currName \
                        + " " * nrSpaces + modStr \
                        + " " * + 4 + modStr + "\n")
            self.tag_add(currName+"plrClr", tagPlrS, tagPlrE) #player colour
            self.tag_add(currName+"modClr", tagPlrE, tagModE) #background blue
            self.tag_add(currName+"lMotClr", tagPlrE, taglMotE) #last tiredness: brown
            self.tag_add(currName+"lTirClr", tagTirS, taglTirE) #last motivation: brown
            self.tag_add(currName+"motClr", tagPlrE, tagMotE) #motivation's color G/Y/O/R
            self.tag_add(currName+"tirClr", tagTirS, tagTirE) #tiredness's color
            #define text colors
            self.tag_config(currName+"modClr", foreground=GuiVars.dictCP["B4"], font=consts.GUI_BOLD)
            self.tag_config(currName+"plrClr", foreground=player.GetColor())
            self.tag_config(currName+"lMotClr", foreground=GuiVars.dictCP["Y2"], font=consts.GUI_BOLD)
            self.tag_config(currName+"lTirClr", foreground=GuiVars.dictCP["Y2"], font=consts.GUI_BOLD)
            self.tag_config(currName+"motClr", foreground=self.__GetModColor(currMod[0]), font=consts.GUI_BOLD)
            self.tag_config(currName+"tirClr", foreground=self.__GetModColor(currMod[1]), font=consts.GUI_BOLD)
            self.update()
            self.after(consts.GUI_WAIT_UPDATE)
        self.__Deactivate()
    
    def TypeWrite(self, text):
        self.__Activate()
        self.__TypeWrite(text)
        self.__Deactivate()

    def __TypeWrite(self, text):
        for text in text:
            self.insert(tk.INSERT, text)
            self.update()
            self.after(consts.GUI_TYPEWRITE_WAIT)

    def __GetModColor(self, mod):
        if mod > 5 :
            return '#00FF00' #green
        elif mod > 2:
            return '#FFFF00' #yellow
        elif mod > 1:
            return '#FF8000' #orange
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
        
    def TypeWrite(self, text):
        self.__Activate()
        self.__TypeWrite(text)
        self.__Deactivate()

    def __TypeWrite(self, text):
        for text in text:
            self.insert(tk.INSERT, text)
            self.update()
            self.after(consts.GUI_TYPEWRITE_WAIT)

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
        self.__nrOfTags = 0
        self.__BindToKey('<space>')
        
    def __BindToKey(self, key):
        #bind self to event "space", calling function
        #to draw text more quickly on this screen
        self.bind(key, \
                  lambda event, \
                  : consts.shortenWaits()) #reduce typing speed
       
    def Clear(self):
        self.__Activate()
        self.delete('1.0', tk.END)
        self.__nrOfTags = 0
        self.__Deactivate()
        consts.normalWaits() #extend typing speed to normal

    def LineWrite(self, text):
        self.__Activate()
        self.after(consts.GUI_LINEWRITE_WAIT)
        self.insert(tk.INSERT, text)
        self.update()
        self.__Deactivate()

    def NameWrite(self, player):
        self.__Activate()
        self.update()
        self.__nrOfTags += 1
        plName = player.GetName()
        endIndx = self.index('end-1c').split('.') #-1character added as tkinter adds an invisible newline char :/
        linNr = int(endIndx[0])
        colSt = int(endIndx[-1])
        tagNameS = str(linNr) + '.' + str(colSt)
        tagNameE = str(linNr) + '.' + str(colSt+len(plName))
        self.__TypeWrite(plName)
        self.tag_add(self.__nrOfTags, tagNameS, tagNameE)
        self.tag_config(self.__nrOfTags, foreground=player.GetColor(), font=consts.GUI_BOLD)
        self.__Deactivate()
    
    def TypeWrite(self, text):
        self.__Activate()
        self.__TypeWrite(text)
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

class GameGui(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        
        var = GuiVars() #variable container for gui setup
        screenSize= [int(self.winfo_screenwidth()), int(self.winfo_screenheight())]
        var.setGameGuiSize(screenSize)
        #Display splash video
        splash = Splash(screenSize) #call splash "loading" image
        
        # Setup main window and widgets     
        self.title("Der Winter Naht")
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: GameStats.Quit(arg)) #lambda needed as protocol does not take arguments
        
        #Canvas
        myframe = tk.Frame(self)
        myframe.pack(fill=tk.BOTH, expand=tk.YES)
        canvas = ResizingCanvas(myframe,width=var.scr_w, height=var.scr_w, bg="black")
        canvas.pack(fill=tk.BOTH, expand=tk.YES)
        #Frames
        textScrFr = tk.Frame(canvas, bg=var.frClr, bd=var.frBdr)
        invtScrFr = tk.Frame(canvas, bg=var.frClr, bd=var.frBdr)
        statsScrFr = tk.Frame(canvas, bg=var.frClr, bd=var.frBdr)
        inputScrFr = tk.Frame(canvas, bg=var.frClr, bd=var.frBdr)
        #Frame Pack
        textScrFr.pack(anchor=tk.W, side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        invtScrFr.pack(anchor=tk.SW,side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        statsScrFr.pack(anchor=tk.SW,side=tk.TOP, fill=tk.X, expand=tk.NO)
        inputScrFr.pack(anchor=tk.SW, side=tk.TOP, fill=tk.X, expand=tk.NO)
        
        #Screens   
        wid = textScrFr.winfo_id()
        self.textScreen = OutputText(textScrFr\
                                     , font=consts.GUI_FONT\
                                     , insertontime=0\
                                     , fg=var.scrFg\
                                     , bg=var.scrBg\
                                     , width=82\
                                     , height=35\
                                     , padx=12\
                                     , pady=9)  
        self.inventoryScreen = InventoryText(invtScrFr\
                                          , font=consts.GUI_FONT\
                                          , insertontime=0\
                                          , bg=var.scrBg\
                                          , fg=var.scrFg\
                                          , width=4\
                                          , height=10\
                                          , padx=12\
                                          , pady=9)
        self.statsScreen = StatusText(statsScrFr\
                                      , font=consts.GUI_FONT\
                                      , insertontime=0\
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
        self.textScreen.pack(side = tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.inventoryScreen.pack(side = tk.LEFT, fill=tk.BOTH, expand=tk.YES) 
        self.statsScreen.pack(side = tk.LEFT, fill=tk.BOTH, expand=tk.YES)  
        self.inputScreen.pack(side = tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.audioStream = Audio()
        #finished loading so destroy splash
        splash.destroy()
        #Show main window
        self.deiconify()
    
            
class Splash(tk.Toplevel):
    def __init__(self, screenSize):
        width = 540
        height = 314
        tk.Toplevel.__init__(self, width=width, height=height)
        self.myFrame = tk.Frame(self)
        self.myFrame.pack(anchor=tk.CENTER, fill=tk.BOTH, expand=tk.NO)
        self.videoScreen = tk.Label(self.myFrame, width=width, height=height)
        centerCoordinates = [screenSize[0]/2 - width/2, screenSize[1]/2 - height/2]
        self.geometry("+%d+%d" % (centerCoordinates[0], centerCoordinates[1]))
        self.videoScreen.pack(anchor=tk.CENTER, expand=tk.NO)
        self.overrideredirect(True)
        self.PlayVideo()
        
    def PlayVideo(self):
        video_name = "SplashScreen.mp4" #This is the splash video file path
        self.video = imageio.get_reader(video_name)
        self.frameRate = 25
        self.stream()
        
    def stream(self):
        for image in self.video.iter_data():
                start = timer()
                frame_image = ImageTk.PhotoImage(Image.fromarray(image)) #load image from object
                self.videoScreen.config(image=frame_image) #load image into label
                self.videoScreen.image = frame_image #display image
                end = timer()
                frameTimems = int(1000*(1/self.frameRate - (end-start))) #in milliseconds
                if frameTimems > 0 :
                    self.after(frameTimems)
                self.videoScreen.update()
                self.videoScreen.update_idletasks()

def invokeTextScreenFontResize(self):
    print(self.textScrFr.width)
  
class Audio():
    def __init__(self):
        mix.init()
        self.currentlyPlayingId = 0
    
    def play(self, itemNr):
        if itemNr in sounds.dictMusic:
            if not self.currentlyPlayingId == itemNr: #requested song is already playing
                if mix.get_busy(): #mixer currently playing
                    mix.music.fadeout(2000) #fadeout current song
                self.currentlyPlayingId =itemNr
                mix.music.load(sounds.dictMusic[itemNr])
                mix.music.play(loops=-1) #loop indefinetely
            else:
                pass #requested song is already playing
        else:
            mix.music.fadeout(2000) #no song requested
    
    def end(self):
        mix.music.stop()
        mix.quit()