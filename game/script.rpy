# Вы можете расположить сценарий своей игры в этом файле.

init python:
    def pychan_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voices/pychan voice.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    

# Определение персонажей игры.
define pc = Character("Пай-чан", callback=pychan_voice, color="#d3c612")
define you = Character("")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    python:
        _preferences.set_volume('music', 0.3)
    image city = im.Scale("images/bg city.jpg", 1920, 1080)
    image room  = im.Scale("images/bg room.jpg", 1920, 1080)
    play music "music/Till Death Do Us Part.ogg" loop fadein 3.0
    scene city
    with Dissolve(1.5)
    
    $ renpy.notify("2040 год.")
    with Dissolve(1.0)
    "{cps=40}За короткие сроки информационное
развитие смогло достичь своего пика.{/cps}"
    "{cps=40}Все больше людей стали отдавать предпочтение
профессиям в сфере информационных
технологий,{/cps}"
    "{cps=40}Желание освоить программирование стало навязанной нормой.{/cps}"
    "{cps=40}Но из-за конкуренции не каждый смог найти заработок.{/cps}"
    "{cps=40}Государства начали отдавать все больший приоритет техническим профессиям{/cps}"
    "{cps=40}В частности профессиям в сфере IT{/cps}"
    "{cps=40}В борьбе за работодателей людям приходится прикладывать все больше и больше усилий, чтобы найти работу и не попасть под сокращение. {/cps}"
    "{cps=40}Смысл жизни уже больше напоминал матрицу из нулей и единиц,{/cps}"
    "{cps=40}А главной целью каждого стало {color=#0000ffff}доказать{/color}{/cps}"
    "{cps=40}{color=#0000ffff}Доказать,{/color} что ты полезнее машины{/cps}"
    "{cps=40}{color=#0000ffff}Доказать,{/color} что ты лучше машины.{/cps}"





    return
