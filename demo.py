from hashTableDs  import UserHashTable
from sorting import merge_sort
from dataGenerator import generate_users
import time

def run_demo(dataset_size):
    print(f"\nRunning test with {dataset_size} users")

    # Generate dataset
    users = generate_users(dataset_size)
    table = UserHashTable()

    # Insert timing
    start = time.time()
    for user in users:
        table.insert(user)
    print("Insert time:", round(time.time() - start, 4), "seconds")

    # Search timing
    start = time.time()
    table.search(dataset_size // 2)
    print("Search time:", round(time.time() - start, 6), "seconds")

    # Ranking timing
    start = time.time()
    sorted_users = merge_sort(table.get_all_users())
    print("Ranking time:", round(time.time() - start, 4), "seconds")

    print("\nTop 5 Influencers:")
    for user in sorted_users[:5]:
        print(user)


if __name__ == "__main__":
    # Small, Medium, Large datasets
    run_demo(10)
    run_demo(1000)
    run_demo(10000)