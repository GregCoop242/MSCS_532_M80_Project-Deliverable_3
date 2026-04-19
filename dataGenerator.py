import random
from user import User

def generate_users(n):
    users = []
    for i in range(n):
        users.append(
            User(
                user_id=i,
                name=f"User_{i}",
                likes=random.randint(10, 10000),
                followers=random.randint(50, 50000),
                engagement=random.uniform(0.1, 5.0)
            )
        )
    return users