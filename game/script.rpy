# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define ps = Character('Пасхалко', color="#C0E7D6")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    image bg room cu = im.Scale("images/bg room cu.png", 1920, 1080)

    scene bg room cu

    show paschalko
    
    play voice "audio/chan voice demo.ogg"
    
    ps "мяу мяу"



    ps "гав гав"
    
    
    
    ps "уау уау"

    return
