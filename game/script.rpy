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

    image city = im.Scale("images/bg city.jpg", 1920, 1080)
    image room  = im.Scale("images/bg room.jpg", 1920, 1080)

    scene city
    with Dissolve(1.5)

    pc "{cps=75}2040 год. За короткие сроки информационное
развитие смогло достичь своего пика.{/cps}"
    with Dissolve(0.5)

    pc"{cps=75}Все больше людей стали отдавать предпочтение
профессиям в сфере информационных
технологий, желание освоить
программирование стало навязанной нормой.{/cps}"
    pc"{cps=75}но.{/cps}"




    return
