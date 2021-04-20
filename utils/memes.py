import random

class MemeList:
    
    _memes: List[str]
    
    def _init_(self, memes: Iterable[str]):
        self._memes = list(memes)
        
    def add_meme(self, meme: str):
        self._memes.append(meme)
        
    def get_random_meme(self) -> str:
        return random.choice(self._memes)
        
    def count(self) -> int:
        return self.len(_memes)
    
    
