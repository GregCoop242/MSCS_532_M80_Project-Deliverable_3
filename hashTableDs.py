from sorting import merge_sort

class UserHashTable:
    def __init__(self):
        self.table = {}

    # O(1)
    def insert(self, user):
        self.table[user.user_id] = user

    # O(1)
    def search(self, user_id):
        return self.table.get(user_id, None)

    # O(1)
    def delete(self, user_id):
        if user_id in self.table:
            del self.table[user_id]

    def get_all_users(self):
        return list(self.table.values())