from fastapi import APIRouter
from usecase.add_hobby_usecase import AddHobbyUseCase
from infrastructure.inmemory_user_repository import InMemoryUserRepository

router = APIRouter()
repo = InMemoryUserRepository()
usecase = AddHobbyUseCase(repo)

@router.post("/users/{name}/hobbies")
def add_hobby(name: str, hobby: str):
    result = usecase.execute(name, hobby)
    return {"message": result}
