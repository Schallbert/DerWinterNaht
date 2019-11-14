
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

class Mod_typ():
    EFFONE = 0 #Once usable, effect on calling player
    EFFALL = 1 #Once usable, effect on all players
    NOTUSABLE = 2 #Item that cannot be used without a combination
    PERMANENT = 3 #Item cannot be consumed, it is permanently available
    
class cmd_inpt():
    UNKNOWN = 0
    QUIT = 1


class consts():
    GUI_WAIT_UPDATE = 500
    GUI_LINEWRITE_WAIT = 500
    GUI_TYPEWRITE_WAIT = 30
    GUI_FONT = ["Lucida Console", "12"]
    GUI_BOLD = ["Lucida Console", "12", "bold"]