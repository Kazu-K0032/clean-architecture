from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str # ユーザー名
    age: int  # 年齢
    hobbies: List[str] = field(default_factory=list) # ユーザーの趣味
    
    def is_adult(self) -> bool:
        """
        成人かどうか判定(18歳以上を成人とする)
        """
        return self.age >= 18
    
    def add_hobby(self, hobby: str) -> None:
        """
        趣味を追加
        """
        if hobby not in self.hobbies:
            self.hobbies.append(hobby)
            
    def introduce(self) -> str:
        """
        自己紹介文を返す
        """
        hobby_text = "、 ".join(self.hobbies) if self.hobbies else "趣味はまだありません"
        return f"こんにちは、{self.name}です。年齢は{self.age}歳です。{hobby_text}が好きです。"
