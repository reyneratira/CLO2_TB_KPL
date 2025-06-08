# profile_runner.py
import os

def run_coverage():
    print("Menjalankan unit test + coverage...\n")
    os.system("coverage run -m unittest discover -s tests")
    os.system("coverage report -m")

def run_memory_profiler():
    print("\n Menjalankan memory profiler + plot (mprof)...\n")
    os.system("mprof run --interval 0.1 memory_target.py")   # Profiling
    os.system("mprof plot --output memory_profile.png")  # Buat plot PNG
    print("Memory plot disimpan di: memory_profile.png")

if __name__ == "__main__":
    run_coverage()
    run_memory_profiler()