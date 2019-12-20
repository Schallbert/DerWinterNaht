
# Enums and data structures
#----------------------------------------------
class ACTIONID():
    VIEW = 0
    GOTO = 1
    OPEN = 2
    USE = 3
    GET = 4
    NOC_YES = 5 #NO Choice, answer is YES
    NOC_NO = 6 #NO Choice, answer is NO
    
class EXCHANGEDIR():
    """Spot exchange direction. FORWARD takes the first set of elements as 'from'
    and the second set of elemtent as 'to', and vice verca."""
    FORWARD = 1
    REVERT = -1
    
class REACH():
    ROOM = 1
    SPOT = 2

class MOD():
    #None = no mod
    EFFONE = 1 #Once usable, effect on calling player
    EFFALL = 2 #Once usable, effect on all players
    NOTUSABLE = 3 #Item that cannot be used without a combination
    PERMANENT = 4 #Item cannot be consumed, it is permanently available
    #Player's mod value
    CURRMOD = 5 #Get current player motivation/tiredness stat
    LASTMOD = 6 #Get previous player motivation/tiredness stat
    #Values and ranges for Motivation modificators on start/load game
    LORANGE = 2 #values below this value
    HIRANGE = 8 #values above this value
    RNDM_VLRANGE = range(0,2)
    RNDM_LORANGE = range(1,5)
    RNDM_MIRANGE = range(3,7)
    RNDM_HIRANGE = range(5,10)
    #Time ranges for modificators on Restart Game
    SHORTBREAK = 600 #seconds
    BREAK = 7200
    LONGBREAK = 86400
    
class CMDINPUT():
    UNKNOWN = 0
    QUIT = -1
    
class GUICONSTS():
    """This class contains all constants relevant for the gui to build."""
    #current screen size
    screenWidth = 0
    screenHeight = 0
    
    #Currently only used in GUI to define GUI specific contents
    GUI_WAIT_UPDATE = 500 #milliseconds
    GUI_LINEWRITE_WAIT = 500
    GUI_TYPEWRITE_WAIT = 40
    GUI_FONT = ["Lucida Console", "12"]
    GUI_BOLD = ["Lucida Console", "12", "bold"]
    GUI_TITLE = ["Lucida Console", "18", "bold"]
    
    #number of spaces to center text of title menu
    CTRSTR = " "*24
    
    #Color Palette used throughout the game
    DICTCOLORPALETTE = {
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
    __XWINDOWMARGIN = 200  
    __YWINDOWMARGIN = 200
    #color selection
    FRAMECOLOR = DICTCOLORPALETTE["Y4"]
    FONTCOLOR = DICTCOLORPALETTE["Y4"]
    BGNDCOLOR = DICTCOLORPALETTE["B1"]
    FRAMEBORDER = 2 #pixels, looks nice ;)
    
    @classmethod
    def setGameGuiSize(cls, varWidHeight):
        cls.screenWidth = int(varWidHeight[0]-cls.__XWINDOWMARGIN)
        cls.screenHeight = int(varWidHeight[1]-cls.__YWINDOWMARGIN)
    
    @classmethod
    def shortenWaits(cls):
        cls.GUI_WAIT_UPDATE = 100 #milliseconds
        cls.GUI_LINEWRITE_WAIT = 100
        cls.GUI_TYPEWRITE_WAIT = 5
    
    @classmethod    
    def normalWaits(cls):
        cls.GUI_WAIT_UPDATE = 500 # milliseconds
        cls.GUI_LINEWRITE_WAIT = 500
        cls.GUI_TYPEWRITE_WAIT = 40
        
class SOUNDS():
    SOUND_FADEOUT_TIME = 2000
    DICTMUSIC = {\
        100: "Sound/DerWinterNaht_MainTheme.ogg",\
        110: "Sound/Bootloader.mp3",\
        }
        
class VIDEOS():
    VIDEO_FRAMERATE = 25 #frames per second
    DICTVIDEO = {\
        0: "Video/SplashScreen.mp4"}