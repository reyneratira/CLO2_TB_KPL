# profile_runner.py
import os
from memory_profiler import profile
from modules.registration import create_valid_customer_data

# 1. Coverage test runner
def run_coverage():
    print("📊 Menjalankan unit test dengan coverage...\n")
    os.system("coverage run -m unittest discover -s tests")
    os.system("coverage report -m")

# 2. Memory profiling target
@profile
def memory_test():
    for _ in range(100000):
        create_valid_customer_data("User", "L01")

# 3. Jalankan semuanya
if __name__ == "__main__":
    run_coverage()
    print("\n🧠 Menjalankan memory profiling...\n")
    memory_test()