from abc import ABC, abstractmethod
from domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user:User) -> None:
        pass
    
    @abstractmethod
    def find_by_name(self, name:str) -> User:
        pass
