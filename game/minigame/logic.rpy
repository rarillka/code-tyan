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
    from random import shuffle
    import ast as py_ast

    class CodeItPuzzleLexer():
        """A small lexer to parse Python code by looking for a token
        to mark as as variable.
        """

        var_token = "%v"

        def get_tokens(self, code=""):
            """Get the list of "tokens" by parsing through the code.

            Args:
                code: The string to parse through.
            """

            # Create setup variables to create the list of tokens
            objs = []
            split_c = code.split("\n")

            # Iterate through every item in the list we made earlier
            for item in split_c:
                
                # If the token is found, we must iterate through that
                # line.
                if self.var_token in item:

                    # We create a small lexeme and a flag to see if we
                    # are parsing the token currently.
                    cobj = ""
                    itoken = False

                    # Iterate through every character and index in the
                    # line.
                    for i, char in enumerate(item):
                        
                        # Add the character to the current lexeme.
                        cobj += char

                        # If the current character is the start of the
                        # token, start the token loop.
                        if char == self.var_token[0]:
                            itoken = True

                        # Look for the next character if possible.
                        if i + 1 < len(item):

                            # If we are parsing a token, check that the
                            # lexeme is the complete token, add the token,
                            # then exit the loop.
                            if itoken:
                                if cobj == self.var_token:
                                    objs.append(self.var_token)
                                    cobj = ""
                                    itoken = False
                            
                            # If we aren't parsing the token, check that
                            # the next character is the beginning of the
                            # token and add the current lexeme to the
                            # current list before resetting it.
                            else:
                                if item[i + 1] == self.var_token[0]:
                                    objs.append(cobj)
                                    cobj = ""
                                    itoken = True
                        
                        # If we're at the end of the line, we can just add
                        # the completed lexeme.
                        else:
                            objs.append(cobj)
                
                # Otherwise, we can just add it since it's real code
                # anyway.
                else:
                    objs.append(item)
                
                # Add the newline token to indicate a new line in the
                # script.
                objs.append("newline")
            return objs

        def __init__(self, delimiter=""):
            """Construct the Lexer.

            Args:
                delimiter: The token to mark as a missing variable.
            """
            self.var_token = delimiter


    class CodeItPuzzle():
        """The base class for a CodeIt puzzle.
        """

        delimiter = "%v"
        bits = []
        code_string = "print %v"
        code_objects = []

        def check(self, solution=[]):
            """Check whether the solution will make a valid AST
            and will compile correctly.

            Args:
                solution: The list of missing vars in order of the
                puzzle code.
            """
            code, _ = self._insert_bits(bits=solution)
            error = None
            passed = True
            
            # If we didn't pass the AST test, exit now.
            if not self._verify_ast(code):
                passed = False
                error = "syntax"

            # If we didn't pass the compile test, exit now.
            if not self._verify_compile(code):
                passed = False
                error = "compile"

            return passed, error


        def _insert_bits(self, bits=None, assign=False):
            """Insert the list of bits into the code.

            Args:
                bits: The list of bits to insert
                assign: Whether to re-assign the code objects
                and strings in this object to the results.
            """

            # Create setup variables to insert the correct pieces
            # of code.
            b = bits if bits is not None else self.bits
            new_code_obj = self.code_objects.copy()
            new_code_string = self.code_string
            bit_index = 0
            
            # Iterage through every code object in the list.
            for index, object in enumerate(new_code_obj):

                # If the object is our variable token, swap it out
                # with the first bit in the list.
                if self.delimiter in object:
                    new_code_obj[index] = object.replace(self.delimiter, bits[bit_index])
                    bit_index += 1

                # If the object is a new line, replace it with
                # the newline escape character.
                elif object == "newline":
                    new_code_obj[index] = "\n"
            
            # Compile a new string by concatenating the code object
            # list.
            new_code_string = ''.join(new_code_obj)
            
            # If we assign it, set the attributes in this object to
            # the 'compiled' values.
            if assign:
                self.code_objects = new_code_obj
                self.code_string = new_code_string

            return new_code_string, new_code_obj


        def _verify_ast(self, code=None):
            """Verify whether the solution will evaluate to a proper
            Python abstract syntax tree.

            Args:
                code: The code to verify
            """
            passed_ast = False
            code_str = code if code is not None else self.code_string
            try:
                py_ast.parse(code_str)
                passed_ast = True
            except SyntaxError:
                pass
            
            return passed_ast

        def _verify_compile(self, code=None):
            """Verify whether the solution will compile properly.

            Args:
                code: The code to verify
            """
            passed_compile = False
            code_str = code if code is not None else self.code_string

            try:
                c_compiled = compile(code_str, '<string>', mode='exec')
                passed_compile = True
            except SyntaxError:
                pass

            return passed_compile

        def _compile(self, code=None):
            """Compile the code into a code object for execution.

            Args:
                code: The code to compile.
            """
            code_str = code if code is not None else self.code_string

            print code_str

            return compile(code_str, '<string>', mode="exec")


        def __init__(self, file=None, code="", bits=[], delimit="%v"):
            """Construct the CodeItPuzzle.

            Args:
                file: The path to a Python file with a delimiter.
                code: The string of code to use, if a file is not present.
                bits: The list of bits to insert into the code.
                delimit: The delimiter to mark as a missing variable.
            """
            self.delimiter = delimit
            self.lexer = CodeItPuzzleLexer(delimiter=self.delimiter)
            self.bits = bits

            if file is not None:
                with renpy.file(file) as fobj:
                    self.code_string = ''.join(fobj.readlines())
            else:
                self.code_string = code

            self.code_objects = self.lexer.get_tokens(code=self.code_string)

    class CodeIt():

        puzzles = {
            "oof": ("puzzles/oof.py", ["oof", "def", "return", "die"]),
            "intro": ("puzzles/intro.py", ["print"]),
            
            #"compile": ("puzzles/compile.py", [])
        }

        def run_puzzle(self, puzzle=""):
            complete = False
            puzzle_loc, puzzle_solv = self.puzzles.get(puzzle, None)
            nocomment = lambda p: "# " not in p
            
            if not puzzle:
                return
            
            full_puzzle_loc = "core/minigame/" + puzzle_loc

            if not renpy.loadable(full_puzzle_loc):
                print("Err: File %s is missing from the puzzles folder." % (full_puzzle_loc))
                return

            pieces = puzzle_solv.copy()
            shuffle(pieces)

            puzzle_obj = CodeItPuzzle(file=full_puzzle_loc, bits=pieces, delimit="%v")

            while not complete:
                submission = renpy.call_screen("code_minigame_puzzle", 
                title=puzzle,
                pieces=pieces,
                objs=puzzle_obj.code_objects,
                template=puzzle_obj.delimiter)

                did_succeed, error = puzzle_obj.check(submission)

                if did_succeed:
                    complete = True
                    return

                if not did_succeed and error is not None:
                    renpy.call_screen("ASNotificationAlert",
                    message="Puzzle Script Failed",
                    withDetails = "The script for this puzzle failed due to a %s error. Please check the order of the code pieces and verify that the code works before submitting." % (error))
                    pieces = puzzle_solv.copy()
                    shuffle(pieces)
            

    minigame = CodeIt()

image effect black = "#000000"

label call_minigame(puzzle="intro"):
    $ quick_menu = False
    window hide
    show effect black with fade
    $ minigame.run_puzzle(puzzle=puzzle)
    hide effect black with dissolve
    window show
    return
