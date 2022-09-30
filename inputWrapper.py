from typing import List

import playerColor


class InputWrapper:
    turn: int = 0
    inside_turn: int = 0
    turn_logger: playerColor.PlayerColor = playerColor.PlayerColor.RED
    script: List[List[str]] = None
    input_mode = None

    @staticmethod
    def init_script(script: List[List[str]]) -> None:
        InputWrapper.script = script

    @staticmethod
    def init_input_mode(mode: str) -> None:
        InputWrapper.input_mode = mode

    @staticmethod
    def input_wrap(prompt: str) -> str:
        # scripted input - test purposes
        if InputWrapper.input_mode == "scripted":
            scripted_input = InputWrapper.script[InputWrapper.turn][InputWrapper.inside_turn]
            InputWrapper.inside_turn += 1
            # end of turn
            if InputWrapper.inside_turn == len(InputWrapper.script[InputWrapper.turn]):
                InputWrapper.turn += 1
                InputWrapper.inside_turn = 0
            if scripted_input == 'n':
                InputWrapper.turn_logger = playerColor.PlayerColor.RED if InputWrapper.turn_logger == playerColor.PlayerColor.BLUE else playerColor.PlayerColor.BLUE
            return scripted_input
        # regular input
        elif InputWrapper.input_mode == "cli":
            return input(prompt)
        else:
            raise RuntimeError("InputWrapper wasn't properly configured")
