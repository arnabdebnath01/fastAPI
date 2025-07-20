from abc import ABC, abstractmethod

class AIPlatform(ABC):
    @abstractmethod
    def chat(self, prompt: str) -> str:
        """Sends a prompt to AI and returns a response text"""
        pass