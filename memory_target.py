from modules.registration import create_valid_customer_data

def run_memory_test():
    for _ in range(10000):
        create_valid_customer_data("User", "L01")

if __name__ == "__main__":
    run_memory_test()