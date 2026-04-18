from sorting import merge_sort

class UserHashTable:
    def __init__(self):
        self.table = {}  # Python dict = hash table

    # INSERT
    def insert(self, user):
        self.table[user.user_id] = user

    # DELETE
    def delete(self, user_id):
        if user_id in self.table:
            del self.table[user_id]
            return True
        return False

    # SEARCH (O(1)!)
    def search(self, user_id):
        return self.table.get(user_id, None)

    # TRAVERSE
    def get_all_users(self):
        return list(self.table.values())

    # SORT influencers
    def rank_influencers(self):
        return merge_sort(self.get_all_users())