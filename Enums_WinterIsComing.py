from enum import IntEnum

# Enums and data structures
#----------------------------------------------
class Action_id(IntEnum):
    VIEW = 0
    GOTO = 1
    OPEN = 2
    USE = 3
    GET = 4
    NOC_YES = 5 #NO Choice, answer is YES
    NOC_NO = 6 #NO Choice, answer is NO

class Mod_typ(IntEnum):
    EFFONE = 0 #Once usable, effect on calling player
    EFFALL = 1 #Once usable, effect on all players
    NOTUSABLE = 2 #Item that cannot be used without a combination
    PERMANENT = 3 #Item cannot be consumed, it is permanently available
    
class cmd_inpt(IntEnum):
    UNKNOWN = 0
    QUIT = 1
