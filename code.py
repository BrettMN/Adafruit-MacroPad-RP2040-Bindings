# SPDX-FileCopyrightText: 2021 John Park for Adafruit Industries
# SPDX-License-Identifier: MIT
# Minecraft Turbopad for Adafruit Macropad RP2040
import time
import displayio
import terminalio
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from adafruit_macropad import MacroPad



import MinecraftClass
import ColorsClass
import ActionTypesClass
import KeyPressTypesClass


colors = ColorsClass.Colors()
actionTypes = ActionTypesClass.ActionTypes()
keyPressTypes = KeyPressTypesClass.KeyPressTypes()


macropad = MacroPad()

minecraft = MinecraftClass.Minecraft(macropad, colors, keyPressTypes, actionTypes)

# print('minecraft')
# print(minecraft.__dict__)



keymap = minecraft.keymap

# --- Variable setup for action types
# actionTypes.KEEB = 0
# MEDIA = 1
# actionTypes.MOUSE = 2
# actionTypes.KBMOUSE = 3
# actionTypes.COMMAND = 4

# keyPressTypes.KEY_MOMENT = 0  # momentary press/release keys
# keyPressTypes.KEY_HOLD = 1  # toggle keys

# --- LED colors
# GREEN = 0x00ff00
# RED = 0xff0000
# MAGENTA = 0xff0033
# YELLOW = 0xffdd00
# AQUA = 0x00ffff
LATCH_COLOR = colors.YELLOW

# --- Key mappings
# (<key>): (<color>, <action type>, <key hold>, <keycodes>, <"text">, <enter>)
# keymap = {
#     (0): (AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "gamemode creative", [macropad.Keycode.ENTER], "zero"),
#     (1): (AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "gamemode survival", [macropad.Keycode.ENTER], "one"),
#     (2): (AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "say Dinner Time!", [macropad.Keycode.ENTER], "two"),

#     (3): (AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "time set day", [macropad.Keycode.ENTER], "three"),
#     (4): (AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "time set night", [macropad.Keycode.ENTER], "four"),
#     (5): (AQUA, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "kill", [macropad.Keycode.ENTER], "five"),

#     (6): (GREEN, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "weather clear", [macropad.Keycode.ENTER], "six"),
#     (7): (GREEN, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "weather rain", [macropad.Keycode.ENTER], "seven"),
#     (8): (GREEN, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "weather thunder", [macropad.Keycode.ENTER], "eight"),

#     (9): (RED, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#           "summon minecraft:bee", [macropad.Keycode.ENTER], "nine"),
#     (10): (RED, actionTypes.KBMOUSE, keyPressTypes.KEY_HOLD,  [macropad.Keycode.W], [macropad.Mouse.LEFT_BUTTON], "ten"),
#     (11): (RED, actionTypes.COMMAND, keyPressTypes.KEY_MOMENT, [macropad.Keycode.FORWARD_SLASH],
#            "playsound minecraft:block.bell.use ambient @a ~ ~ ~", [macropad.Keycode.ENTER], "eleven"),
# }


latched = [False] * 12  # list of the latched states, all off to start

last_knob_pos = macropad.encoder  # store knob position state

labels = []

# --- Pixel setup --- #
macropad.pixels.brightness = 0.1
for i in range(12):
    macropad.pixels[i] = (keymap[i][0])


def setUI(header_text, label_text):
    print(header_text)
    print(label_text)

    main_group = displayio.Group()
    macropad.display.show(main_group)
    title = label.Label(
        y=4,
        font=terminalio.FONT,
        color=0x0,
        text=header_text,
        background_color=0xFFFFFF,
    )
    layout = GridLayout(x=0, y=5, width=128, height=54, grid_size=(3, 4), cell_padding=5)

    for j in range(12):
        text = label_text[j]
        print("Label: " + text)
        labels.append(label.Label(terminalio.FONT, text=text))

    for index in range(12):
        x = index % 3
        y = index // 3
        layout.add_content(labels[index], grid_position=(x, y), cell_size=(1, 1))

    main_group.append(title)
    main_group.append(layout)




# label_text = [
#     "CREATE", "SURVIV", "SAY",
#     "DAY", "NIGHT", "KILL",
#     "CLEAR", "RAIN", "THUNDR",
#     "BEE", "MINE", "SOUND",
# ]

label_text = minecraft.keyText



# header_text = " -Minecraft Turbopad- "
header_text = minecraft.headerText


setUI(" -Minecraft Turbopad- ", label_text)


while True:
    key_event = macropad.keys.events.get()  # check for key press or release

    if key_event:
        if key_event.pressed:
            key = key_event.key_number

            print(key)
            labels[key].color = 0x0
            labels[key].background_color = 0xffffff

            if keymap[key][1] == actionTypes.KEEB:
                if keymap[key][2] == keyPressTypes.KEY_HOLD:
                    macropad.keyboard.press(*keymap[key][3])  # * expands the variable to list
                else:
                    macropad.keyboard.send(*keymap[key][3])

            elif keymap[key][1] == actionTypes.MOUSE:
                macropad.mouse.click(*keymap[key][3])

            elif keymap[key][1] == actionTypes.KBMOUSE:
                if keymap[key][2] == keyPressTypes.KEY_HOLD:
                    if latched[key] is False:
                        macropad.keyboard.press(*keymap[key][3])
                        time.sleep(0.01)
                        macropad.mouse.press(*keymap[key][4])
                        latched[key] = True
                    else:
                        macropad.keyboard.release(*keymap[key][3])
                        time.sleep(0.01)
                        macropad.mouse.release_all()
                        latched[key] = False

            elif keymap[key][1] == actionTypes.COMMAND:
                macropad.keyboard.send(*keymap[key][3])
                time.sleep(0.1)
                macropad.keyboard_layout.write(keymap[key][4])
                time.sleep(0.1)
                macropad.keyboard.send(*keymap[key][5])
                time.sleep(0.1)
            macropad.pixels[key] = LATCH_COLOR

        if key_event.released:
            key = key_event.key_number
            if keymap[key][1] == actionTypes.KEEB:
                if keymap[key][2] == keyPressTypes.KEY_HOLD:
                    macropad.keyboard.release(*keymap[key][3])

            if latched[key] is False:
                macropad.pixels[key] = (keymap[key][0])
                labels[key].color = 0xffffff
                labels[key].background_color = 0x0

    current_knob_position = macropad.encoder


    if macropad.encoder > last_knob_pos:
        macropad.mouse.move(wheel=-1)
        last_knob_pos = current_knob_position

    if macropad.encoder < last_knob_pos:
        macropad.mouse.move(wheel=+1)
        last_knob_pos = current_knob_position
