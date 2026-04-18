from dataclasses import dataclass

@dataclass
class SocialUser:
    user_id: int
    name: str
    likes: int
    followers: int
    engagement: float

    def influence_score(self) -> float:
        # y = m*x + b
        return (self.engagement * self.likes) + self.followers