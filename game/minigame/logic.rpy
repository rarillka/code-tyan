# 
# logic.rpy
# Unscripted Core
# 
# Created by Marquis Kurt on 01/08/20.
# Copyright © 2020 Marquis Kurt. All rights reserved.
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 

init 10 python:
    from random import shuffle  # Импортируем функцию shuffle для перемешивания списков
    import ast as py_ast  # Импортируем модуль ast для работы с абстрактным синтаксическим деревом

    class CodeItPuzzleLexer():
        """Маленький лексер для разбора Python кода, ищущий токен
        для обозначения переменной.
        """

        var_token = "%v"  # Токен для переменной

        def get_tokens(self, code=""):
            """Получает список "токенов", разбирая код.

            Args:
                code: Строка для разбора.
            """

            # Создаем переменные для создания списка токенов
            objs = []
            split_c = code.split("\n")  # Разделяем код на строки

            # Итерируем по каждой строке
            for item in split_c:
                
                # Если токен найден, начинаем разбор этой строки
                if self.var_token in item:

                    # Создаем небольшой лексем и флаг для отслеживания токена
                    cobj = ""
                    itoken = False

                    # Итерируем по каждому символу и индексу в строке
                    for i, char in enumerate(item):
                        
                        # Добавляем символ к текущей лексеме
                        cobj += char

                        # Если текущий символ - начало токена, начинаем цикл токена
                        if char == self.var_token[0]:
                            itoken = True

                        # Проверяем следующий символ, если это возможно
                        if i + 1 < len(item):

                            # Если мы разбираем токен, проверяем, что лексема завершена
                            if itoken:
                                if cobj == self.var_token:
                                    objs.append(self.var_token)  # Добавляем токен в список
                                    cobj = ""
                                    itoken = False
                            
                            # Если не разбираем токен, проверяем, что следующий символ - начало токена
                            else:
                                if item[i + 1] == self.var_token[0]:
                                    objs.append(cobj)  # Добавляем текущую лексему в список
                                    cobj = ""
                                    itoken = True
                        
                        # Если мы в конце строки, добавляем завершенную лексему
                        else:
                            objs.append(cobj)
                
                # В противном случае просто добавляем строку
                else:
                    objs.append(item)
                
                # Добавляем токен новой строки
                objs.append("newline")
            return objs

        def __init__(self, delimiter=""):
            """Конструктор лексера.

            Args:
                delimiter: Токен для обозначения отсутствующей переменной.
            """
            self.var_token = delimiter


    class CodeItPuzzle():
        """Базовый класс для головоломки CodeIt.
        """

        delimiter = "%v"  # Токен для переменной
        bits = []  # Список частей кода
        code_string = "print %v"  # Строка кода по умолчанию
        code_objects = []  # Объекты кода

        def check(self, solution=[]):
            """Проверяет, будет ли решение корректным AST
            и будет ли оно компилироваться правильно.

            Args:
                solution: Список отсутствующих переменных в порядке кода головоломки.
            """
            code, _ = self._insert_bits(bits=solution)  # Вставляем части кода
            error = None
            passed = True
            
            # Если не прошли тест AST, выходим
            if not self._verify_ast(code):
                passed = False
                error = "syntax"

            # Если не прошли тест компиляции, выходим
            if not self._verify_compile(code):
                passed = False
                error = "compile"

            return passed, error


        def _insert_bits(self, bits=None, assign=False):
            """Вставляет список частей в код.

            Args:
                bits: Список частей для вставки
                assign: Нужно ли переназначить объекты кода
                и строки в этом объекте на результаты.
            """

            # Создаем переменные для вставки правильных частей кода
            b = bits if bits is not None else self.bits
            new_code_obj = self.code_objects.copy()
            new_code_string = self.code_string
            bit_index = 0
            
            # Итерируем по каждому объекту кода в списке
            for index, object in enumerate(new_code_obj):

                # Если объект - наш токен переменной, заменяем его
                # на первую часть из списка.
                if self.delimiter in object:
                    new_code_obj[index] = object.replace(self.delimiter, bits[bit_index])
                    bit_index += 1

                # Если объект - новая строка, заменяем его на
                # символ новой строки.
                elif object == "newline":
                    new_code_obj[index] = "\n"
            
            # Компилируем новую строку, объединяя список объектов кода
            new_code_string = ''.join(new_code_obj)
            
            # Если мы переназначаем, устанавливаем атрибуты в этом объекте на
            # "собранные" значения.
            if assign:
                self.code_objects = new_code_obj
                self.code_string = new_code_string

            return new_code_string, new_code_obj


        def _verify_ast(self, code=None):
            """Проверяет, будет ли решение оцениваться как правильное
            абстрактное синтаксическое дерево.

            Args:
                code: Код для проверки
            """
            passed_ast = False
            code_str = code if code is not None else self.code_string
            try:
                py_ast.parse(code_str)  # Проверяем синтаксис
                passed_ast = True
            except SyntaxError:
                pass
            
            return passed_ast

        def _verify_compile(self, code=None):
            """Проверяет, будет ли решение компилироваться правильно.

            Args:
                code: Код для проверки
            """
            passed_compile = False
            code_str = code if code is not None else self.code_string

            try:
                c_compiled = compile(code_str, '<string>', mode='exec')  # Компилируем код
                passed_compile = True
            except SyntaxError:
                pass

            return passed_compile

        def _compile(self, code=None):
            """Компилирует код в объект кода для выполнения.

            Args:
                code: Код для компиляции.
            """
            code_str = code if code is not None else self.code_string

            print(code_str)  # Выводим код для отладки

            return compile(code_str, '<string>', mode="exec")


        def __init__(self, file=None, code="", bits=[], delimit="%v"):
            """Конструктор CodeItPuzzle.

            Args:
                file: Путь к Python файлу с разделителем.
                code: Строка кода для использования, если файл не указан.
                bits: Список частей для вставки в код.
                delimit: Разделитель для обозначения отсутствующей переменной.
            """
            self.delimiter = delimit
            self.lexer = CodeItPuzzleLexer(delimiter=self.delimiter)
            self.bits = bits

            if file is not None:
                with renpy.file(file) as fobj:
                    # Читаем код из файла и декодируем байты в строки
                    self.code_string = ''.join(line.decode('utf-8') for line in fobj.readlines())
            else:
                self.code_string = code

            self.code_objects = self.lexer.get_tokens(code=self.code_string)  # Получаем токены

    class CodeIt():
        """Класс для управления головоломками CodeIt."""

        puzzles = {
            "intro": ("puzzles/intro.py", ["print"]),
            #"compile": ("puzzles/compile.py", []),
            "oof": ("puzzles/oof.py", ["oof", "def", "return", "reverse"])
        }

        def run_puzzle(self, puzzle=""):
            """Запускает головоломку по имени.

            Args:
                puzzle: Имя головоломки для запуска.
            """
            complete = False
            puzzle_loc, puzzle_solv = self.puzzles.get(puzzle, None)
            nocomment = lambda p: "# " not in p
            
            if not puzzle:
                return
            
            full_puzzle_loc = "minigame/" + puzzle_loc

            if not renpy.loadable(full_puzzle_loc):
                print("Err: File %s is missing from the puzzles folder." % (full_puzzle_loc))
                return

            pieces = puzzle_solv.copy()
            shuffle(pieces)  # Перемешиваем части головоломки

            puzzle_obj = CodeItPuzzle(file=full_puzzle_loc, bits=pieces, delimit="%v")

            while not complete:
                submission = renpy.call_screen("code_minigame_puzzle", title=puzzle, pieces=pieces, objs=puzzle_obj.code_objects, template=puzzle_obj.delimiter)

                did_succeed, error = puzzle_obj.check(submission)  # Проверяем решение

                if did_succeed:
                    complete = True
                    # Вызываем экран успешного завершения головоломки
                    renpy.call_screen("ASSuccessAlert", message="Поздравляем!", withDetails="Вы успешно завершили головоломку!")
                    return

                if not did_succeed and error is not None:
                    renpy.call_screen("ASNotificationAlert", message="Ошибка в скрипте головоломки", withDetails="Скрипт для этой головоломки не сработал из-за ошибки %s. Пожалуйста, проверьте порядок следования фрагментов кода и убедитесь, что код работает, перед отправкой." % (error))
                    pieces = puzzle_solv.copy()
                    shuffle(pieces)  # Перемешиваем части головоломки заново

                    
                    
                    
    minigame = CodeIt()  # Создаем экземпляр головоломки

screen ASSuccessAlert(message="", withDetails=""):
    #modal True
    fixed xysize (1920, 1080):
        vbox:
            anchor (0.5,0.5)
            pos (0.5,0.5)
            vbox:
                xysize (900, 300)
                text "[message]"  align (0.5, 0.5) # Сообщение об успешном завершении
                text "[withDetails]" align (0.5, 0.5) # Дополнительные детали

            hbox:
                xysize (700, 300)
                anchor (0.5,0.5)
                pos (0.5,0.5)
                textbutton "Завершить игру" action [Return("start")]:  # Завершение игры
                    pos (0.5,0.5)
                    anchor (0.5,0.5)
                textbutton "Пройти заново" action [Jump("call_minigame"), SetVariable(puzzle,"intro")]:  # Повторное прохождение головоломки
                    pos (0.5,0.5)
                    anchor (0.5,0.5)

image effect black = "#000000"

label call_minigame:
    #"""Вызывает головоломку с указанным именем."""
    $ quick_menu = False
    window hide
    show effect black with fade
    
    $ minigame.run_puzzle(puzzle=puzzle)  # Запускаем головоломку
    hide effect black with dissolve
    window show
    return

# Пример использования:
# label start:
    # "Поиграем в головоломки"
    # menu:
        # "Первая головоломка intro.py":
            # $ puzzle="intro"
            # jump call_minigame
        # "Вторая головоломка oof.py":
            # $ puzzle="oof"
            # jump call_minigame
    # return
    
    