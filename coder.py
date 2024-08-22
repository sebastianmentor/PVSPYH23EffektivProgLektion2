class Coder:
    def __init__(self, name:str ,coding_speed:float) -> None:
        self.name = name
        self._coding_speed = coding_speed

    @property
    def coding_speed(self):
        return self._coding_speed

    def __eq__(self, other:object) -> bool:
        return True if other.coding_speed == self.coding_speed else False
    
    def __lt__(self, other:object) -> bool:
        return True if self.coding_speed < other.coding_speed  else False
    
    def __gt__(self, other:object) -> bool:
        return True if self.coding_speed > other.coding_speed  else False
    
    def __str__(self) -> str:
        return f'{self.name}-{self.coding_speed}'