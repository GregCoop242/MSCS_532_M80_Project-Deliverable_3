from models import SocialUser
from arrayDs import UserArray
from hashTableDs import UserHashTable

def run_tests():
    print("\n--- Running Proof of Concept Tests ---\n")

    users = [
        SocialUser(1,"Alice",5000,20000,3.2),
        SocialUser(2,"Bob",2000,5000,2.5),
        SocialUser(3,"Charlie",8000,30000,4.1),
        SocialUser(4,"Diana",1000,2000,1.5)
    ]

    array_ds = UserArray()
    hash_ds = UserHashTable()

    # INSERT TEST
    for u in users:
        array_ds.insert(u)
        hash_ds.insert(u)

    print("Insert test passed")

    # SEARCH TEST
    print("\nSearching for user ID 3")
    print(array_ds.search(3))
    print(hash_ds.search(3))

    # DELETE TEST (edge case)
    print("\nDeleting user ID 2")
    array_ds.delete(2)
    hash_ds.delete(2)

    print("Search deleted user:", array_ds.search(2))

    # SORT TEST
    print("\nTop Influencers (Array DS)")
    for u in array_ds.rank_influencers():
        print(u.name, u.influence_score())

    print("\nTop Influencers (Hash Table DS)")
    for u in hash_ds.rank_influencers():
        print(u.name, u.influence_score())