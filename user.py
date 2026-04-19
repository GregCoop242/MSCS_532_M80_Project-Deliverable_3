class User:
    def __init__(self, user_id, name, likes, followers, engagement):
        self.user_id = user_id
        self.name = name
        self.likes = likes
        self.followers = followers
        self.engagement = engagement
        
        # Deliverable 3 Optimization: cached score
        self.influence_score = self.calculate_influence()

    def calculate_influence(self):
        return (self.engagement * self.likes) + self.followers

    def __repr__(self):
        return f"{self.name} | Score: {self.influence_score}"