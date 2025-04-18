# 
# mg_screen.rpy
# Unscripted Core
# 
# Created by Marquis Kurt on 01/08/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 
init -10 python:
    def get_feather_icon(s):
        return "path/to/feather/icons/" + s + ".png"
init python:

    def transfer_lists(from_list, to_list):
        for item in from_list:
            to_list.append(item)
            from_list.remove(item)
            
    def var_position(list, delimiter, item):
        elist = [(i, e) for i, e in enumerate(list)]
        water_elist = filter(lambda a: a[1] == delimiter, elist)
        index = -1

        for list_index, list_item in enumerate(water_elist):
            if list_item == item:
                index = list_index
        return index

screen code_minigame_puzzle(title="", pieces=[], objs=[], template="%v"):
    zorder 10
    modal True
    style_prefix "code_it"

    default submission = []
    default game_title = title.title()
    default vars = []
    
    add AS_DESKTOP_IMG
    #add "gui/overlay/code_it.png"

    frame:
        
        has vbox:
            yalign 0.0
            yfill True
            spacing 0

            hbox:
                xfill True

                text "[game_title] - CodeIt Puzzle":
                    style "code_it_title"
                    
                hbox:
                    xalign 1.0
                    spacing 8

                    button action Function(transfer_lists, from_list=submission, to_list=pieces):
                        add get_feather_icon("refresh-cw"):
                            size (28, 28)
                    
                    button action [SensitiveIf(len(pieces) == 0), Return(submission)]:
                        add get_feather_icon("check-square"):
                            size (28, 28)
                            if len(pieces) != 0:
                                alpha 0.2

            null height 24

            vbox:
                hbox:
                    spacing 8
                    xfill True
                    vbox:
                        style_prefix "code_it_script"
                        style "code_it_panel"
                        
                        viewport:
                            mousewheel True
                            scrollbars "vertical"
                            style_prefix "ASInterfaceScrollbar"
                            xmaximum 1280 / 2
                            #xsize 1280 / 2
                            
                            hbox:
                                style_prefix "code_it_script_template"
                                box_wrap True

                                for i, obj in enumerate(objs):                                        

                                    if obj == template:

                                        python:
                                            pos = var_position(objs, template, (i, obj))                         
                                        if pos < len(submission):
                                            $ code = submission[pos]                   
                                            textbutton "[code]" action [Function(pieces.append, code), Function(submission.remove, code)]:
                                                style "code_it_script_template_button"
                                        else:
                                            frame:
                                                has hbox:
                                                    null height 16
                                                    null width 96

                                    elif obj == "newline":
                                        null width 1280 / 2

                                    elif obj.startswith("# "):
                                        text "[obj]" style "code_it_script_comment"

                                    else:
                                        text "[obj]"


                    vbox:
                        style "code_it_panel"
                        
                        hbox:
                            spacing 8
                            box_wrap True
                            xalign 0.0
                            for code in pieces:
                                textbutton "[code]" action [Function(submission.append, code), Function(pieces.remove, code)]:
                                    style "code_it_button_option"
                                    xalign 0.0

                null height 8

style code_it_frame is gui_frame:
    background None
    xalign 0.5
    yalign 0.5
    padding (24, 16)
    margin (0, 0)

style code_it_vbox is vbox:
    spacing 8

style code_it_title is gui_text:
    font AS_FONTS_DIR + "Bold.ttf"
    xalign 0.15
    size 20

style code_it_text is gui_text:
    size 18

style code_it_panel is code_it_vbox:
    xsize 640
    yfill True

style code_it_script_vbox is code_it_vbox

style code_it_script_text is gui_text:
    font "gui/font/FiraCode-Regular.ttf"
    size 16

style code_it_script_comment is code_it_script_text:
    color "#888888"

style code_it_button_option is ASInterfacePushButton:
    padding (12, 2)

style code_it_button_option_text is ASInterfacePushButton_text:
    font "gui/font/FiraCode-Regular.ttf"
    size 14

style code_it_script_template_vbox is code_it_vbox

style code_it_script_template_frame is gui_frame:
    background "#666666"
    padding (8, 2)

style code_it_script_template_button is gui_button:
    padding (8, 0)

style code_it_script_template_text is code_it_script_text
style code_it_script_template_button_text is code_it_script_text:
    idle_color gui.accent_color
    hover_color "#fb2046"