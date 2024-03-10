from typing import Any
from data_load.data_load import load_data
from key_extraction.base import Agent
from embeddings.models import BaseEmbedder

class KeywordsExtraction(Agent) :
    def __init__(self, 
                 sentencce : str, 
                 embedding : BaseEmbedder) :
        
        self.sentence = sentencce
        self.embedding = embedding
        
    async def apply_embedding(self) :
        """임베딩 모델을 적용시키는 코드"""
        pass
    
    async def run(self) :
        """키워드 추출을 시작하는 코드"""