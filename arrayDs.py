from sorting import merge_sort

class UserArray:
    def __init__(self):
        self.users = []

    # INSERT
    def insert(self, user):
        self.users.append(user)

    # DELETE by ID
    def delete(self, user_id):
        for i, u in enumerate(self.users):
            if u.user_id == user_id:
                del self.users[i]
                return True
        return False

    # SEARCH by ID
    def search(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    # TRAVERSE
    def get_all_users(self):
        return self.users

    # SORT influencers
    def rank_influencers(self):
        return merge_sort(self.users)