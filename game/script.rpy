# Вы можете расположить сценарий своей игры в этом файле.

init python:
    def pychan_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voices/chan voice demo.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def c_chan_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voices/chan 2 voice.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def gen_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voices/general_1.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    

# Определение персонажей игры.
define Пайчан = Character("пасхалко", callback=pychan_voice, color="#d3c612")
define you = Character("", callback=gen_voice)
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

    "{cps=50}2040 год. За короткие сроки информационное
развитие смогло достичь своего пика.{/cps}"
    with Dissolve(0.5)

    "{cps=50}Все больше людей стали отдавать предпочтение
профессиям в сфере информационных
технологий, желание освоить
программирование стало навязанной нормой.{/cps}"




    return
