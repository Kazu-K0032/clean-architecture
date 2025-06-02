from domain.user import User
from domain.repository.user_repository import UserRepository

class AddHobbyUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def execute(self, user_name: str, hobby: str) -> None:
        """
        指定したユーザーに趣味を追加し、紹介文を返す
        """
        user = self.user_repository.find_by_name(user_name)
        user.add_hobby(hobby)
        self.user_repository.save(user)
        return user.introduce()
