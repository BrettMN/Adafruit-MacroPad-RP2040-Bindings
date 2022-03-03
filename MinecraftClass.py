

class Minecraft:
    # keymap = {}

    


    # keyText:[
    #     "not", "set", "yet",
    #     "not", "set", "yet",
    #     "not", "set", "yet",
    #     "not", "set", "yet"
    # ]

    # headerText = ""



            # default constructor
    def __init__(self, macropad, colors, keyPressTypes, actionTypes):
        # self.macropad = macropad
        # self.colors = colors
        # self.keyPressTypes = keyPressTypes
        # self.actionTypes = actionTypes

        self.keyText = [
            "CREATE", "SURVIV", "SAY",
            "DAY", "NIGHT", "KILL",
            "CLEAR", "RAIN", "THUNDR",
            "BEE", "MINE", "SOUND",
        ]

        self.headerText = " -Minecraft Turbopad- "
        
        # --- Key mappings
        # (<key>): (<color>, <action type>, <key hold>, <keycodes>, <"text">, <enter>)
        self.keymap = {
            (0): (colors.AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "gamemode creative", [macropad.Keycode.ENTER], "zero"),
            (1): (colors.AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "gamemode survival", [macropad.Keycode.ENTER], "one"),
            (2): (colors.AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "say Dinner Time!", [macropad.Keycode.ENTER], "two"),

            (3): (colors.AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "time set day", [macropad.Keycode.ENTER], "three"),
            (4): (colors.AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "time set night", [macropad.Keycode.ENTER], "four"),
            (5): (colors.AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "kill", [macropad.Keycode.ENTER], "five"),

            (6): (colors.GREEN, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "weather clear", [macropad.Keycode.ENTER], "six"),
            (7): (colors.GREEN, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "weather rain", [macropad.Keycode.ENTER], "seven"),
            (8): (colors.GREEN, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "weather thunder", [macropad.Keycode.ENTER], "eight"),

            (9): (colors.RED, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "summon minecraft:bee", [macropad.Keycode.ENTER], "nine"),
            (10): (colors.RED, actionTypes.KBMOUSE, keyPressTypes.KEY_HOLD,  [macropad.Keycode.W], [macropad.Mouse.LEFT_BUTTON], "ten"),
            (11): (colors.RED, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
                "playsound minecraft:block.bell.use ambient @a ~ ~ ~", [macropad.Keycode.ENTER], "eleven"),
        }
    

