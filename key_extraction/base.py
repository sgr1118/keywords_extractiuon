from abc import ABC, abstractmethod

class Agent(ABC) :
    def __init__(self, sentencce, embedding):
        
        pass
    
    @abstractmethod
    async def apply_embedding() :
        pass
    
    @abstractmethod
    def run() :
        pass
    
        