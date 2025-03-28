from typing import Dict

class OnePieceDecklistParser:
    
    @staticmethod
    def code_to_dict(deck_code: str) ->  Dict[str, int]:
        deck_list = deck_code.strip().splitlines()
        
        deck_dict = {
            line.split("x")[1]: int(line.split("x")[0]) for line in deck_list if "x" in line
        }
        
        return deck_dict