# Вы можете расположить сценарий своей игры в этом файле.

init python:
    def pychan_voice(event, **kwargs):
        if event == "show":
            renpy.music.play("voices/chan voice demo.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    

# Определение персонажей игры.
define ps = Character("пасхалко", callback=pychan_voice, color="#B22222")



# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    image bg room cu = im.Scale("images/bg room cu.png", 1920, 1080)

    scene bg room cu

    show paschalko
    
    
    
    ps "{cps=50}мяу мяу мяу мяу мяу мяу мяу мяу мяу мяу мяу мяу мяу мяу мяу мяу{/cps}"



    ps "{cps=50}гав гав{/cps}"
    
    
    
    ps "{cps=50}уау уау{/cps}"


    return
