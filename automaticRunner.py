from typing import List

import playerColor

SCRIPT_RUNNER_MODE = True
AUTOMATIC_RUNNER_MODE = False

easy_test_input = [
    ["red1", "y", "0", "1", "n"],
    ["blue1", "y", "0", "2", "n"],
    ["red2", "y", "1", "1", "n"],
    ["blue2", "y", "1", "3", "n"],
    ["red3", "y", "0", "3", "n"],
    ["blue3", "n"],
    ["red4", "y", "0", "2", "n"],
    ["blue4", "n"],
    ["red5", "n"],
    ["blue5", "y", "1", "3", "n"],
    ["red6", "y", "1", "2", "n"],
    ["blue6", "n"]
]


class AutomaticRunner:
    turn: int = 0
    inside_turn: int = 0
    turn_logger: playerColor.PlayerColor = playerColor.PlayerColor.RED
    # TODO: add script here
    script: List[List[str]] = easy_test_input

    @staticmethod
    def input_wrap(prompt: str) -> str:
        # scripted input - test purposes
        if SCRIPT_RUNNER_MODE:
            scripted_input = AutomaticRunner.script[AutomaticRunner.turn][AutomaticRunner.inside_turn]
            AutomaticRunner.inside_turn += 1
            # end of turn
            if AutomaticRunner.inside_turn == len(AutomaticRunner.script[AutomaticRunner.turn]):
                AutomaticRunner.turn += 1
                AutomaticRunner.inside_turn = 0
            if scripted_input == 'n':
                AutomaticRunner.turn_logger = playerColor.PlayerColor.RED if AutomaticRunner.turn_logger == playerColor.PlayerColor.BLUE else playerColor.PlayerColor.BLUE
            return scripted_input
        # automatic input - bot training
        elif AUTOMATIC_RUNNER_MODE:
            raise RuntimeError("No Automatic Runner detected")
        # regular input
        else:
            return input(prompt)
