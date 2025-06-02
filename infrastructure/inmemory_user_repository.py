from domain.repository.user_repository import UserRepository
from domain.user import User

class InMemoryUserRepository(UserRepository):
    """
    メモリ上にUserを保存する簡易実装
    """
    def __init__(self):
        self.users = {}
    
    def save(self, user:User) -> None:
        self.users[user.name] = user

    def find_by_name(self, name:str) -> User:
        user = self.users.get(name)
        if user is None:
            raise ValueError(f"{name}に一致するユーザーが見つかりません")
        return user
