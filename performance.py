import argparse
import subprocess
import time
import os

def main():
    parser = argparse.ArgumentParser(description="Run a day file and measure its execution time.")
    parser.add_argument("--day", type=int, required=True, help="The day number to run (e.g., 1 for day01.py).")

    args = parser.parse_args()
    day_file = f"day{args.day:02d}.py"  # Format as day01.py, day02.py, etc.

    # Check if the file exists
    if not os.path.exists(day_file):
        print(f"Error: {day_file} does not exist.")
        return

    # Measure execution time
    start_time = time.time()
    try:
        subprocess.run(["python", day_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {day_file} exited with an error.")
        return
    end_time = time.time()

    print(f"Execution time for {day_file}: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()