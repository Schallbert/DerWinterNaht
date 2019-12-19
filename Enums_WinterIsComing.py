
# Enums and data structures
#----------------------------------------------
class Action_id():
    VIEW = 0
    GOTO = 1
    OPEN = 2
    USE = 3
    GET = 4
    NOC_YES = 5 #NO Choice, answer is YES
    NOC_NO = 6 #NO Choice, answer is NO
    
class Exchange_dir():
    """Spot exchange direction. FORWARD takes the first set of elements as 'from'
    and the second set of elemtent as 'to', and vice verca."""
    FORWARD = 1
    REVERT = -1
    
class Reach():
    ROOM = 1
    SPOT = 2

class Mod_typ():
    #None = no mod
    EFFONE = 1 #Once usable, effect on calling player
    EFFALL = 2 #Once usable, effect on all players
    NOTUSABLE = 3 #Item that cannot be used without a combination
    PERMANENT = 4 #Item cannot be consumed, it is permanently available
    
class cmd_inpt():
    UNKNOWN = 0
    QUIT = -1
    
class playermod():
    CURRMOD = 0
    LASTMOD = 1


class consts():
    GUI_WAIT_UPDATE = 500
    GUI_LINEWRITE_WAIT = 500
    GUI_TYPEWRITE_WAIT = 40
    GUI_FONT = ["Lucida Console", "12"]
    GUI_BOLD = ["Lucida Console", "12", "bold"]
    
    @classmethod
    def shortenWaits(cls):
        cls.GUI_WAIT_UPDATE = 100
        cls.GUI_LINEWRITE_WAIT = 100
        cls.GUI_TYPEWRITE_WAIT = 5
    
    @classmethod    
    def normalWaits(cls):
        cls.GUI_WAIT_UPDATE = 500
        cls.GUI_LINEWRITE_WAIT = 500
        cls.GUI_TYPEWRITE_WAIT = 40
        
class sounds():
    dictMusic = {\
        100: "Sound/DerWinterNaht_MainTheme.ogg",\
        110: "Sound/Bootloader.mp3",\
        }