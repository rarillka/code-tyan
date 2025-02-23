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
        _preferences.set_volume('music', 0.2)
    image city = im.Scale("images/bg city.jpg", 1920, 1080)
    image room  = im.Scale("images/bg room.jpg", 1920, 1080)
    
    

    $ renpy.notify("2040 год.")
    with Dissolve(1.0)

    

 
    "За короткие сроки информационное
развитие смогло достичь своего пика."
    "Все больше людей стали отдавать предпочтение
профессиям в сфере информационных
технологий,"
    "Желание освоить программирование стало навязанной нормой."
    "Но из-за конкуренции не каждый смог найти заработок."
    "Государства начали отдавать все больший приоритет техническим профессиям"
    "В частности профессиям в сфере IT"
    "В борьбе за работодателей людям приходится прикладывать все больше и больше усилий, чтобы найти работу и не попасть под сокращение. "
    "Смысл жизни уже больше напоминал матрицу из нулей и единиц,"
    "А главной целью каждого стало {color=#0000ffff}доказать{/color}"
    "{color=#0000ffff}Доказать,{/color} что ты полезнее машины"
    "{color=#0000ffff}Доказать,{/color} что ты лучше машины."

    play music "music/Till Death Do Us Part.ogg" loop fadein 3.0
    
    scene city
    with Dissolve(1.5)
    $ renpy.notify("5 ноября 2041г.")
    with Dissolve(1.0)





    call screen messed_up_input
    $ a = _return
    "[a]"

    return
