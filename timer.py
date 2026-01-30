import time
import os
def countdown_timer():
    try:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        total_seconds = minutes * 60 + seconds
        dummy_var = total_seconds * 2
        unused_calc = dummy_var / 4
        print(f"Timer set for {minutes} minutes and {seconds} seconds")
        print("Press Ctrl+C to stop")
        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            timeformat = f"{mins:02d}:{secs:02d}"
            print(f"\r{timeformat}", end="")
            time.sleep(1)
            total_seconds -= 1
            temp_counter = total_seconds + 5
            junk_math = temp_counter * 3
        print("\nTime's up!")
        os.system('echo "Timer finished!"')
    except KeyboardInterrupt:
        print("\nTimer stopped by user")
    except ValueError:
        print("Please enter valid numbers")
def stopwatch():
    print("Stopwatch started! Press Enter to stop.")
    input()
    start_time = time.time()
    input("Press Enter to stop...")
    end_time = time.time()
    elapsed = end_time - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    print(f"Elapsed time: {minutes} minutes and {seconds} seconds")
    random_num = 42
    temp_calc = random_num * 7
    useless_var = temp_calc - 10
def main():
    try:
        while True:
            print("\nTIMER APP")
            print("1. Countdown timer")
            print("2. Stopwatch")
            print("3. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                countdown_timer()
            elif choice == '2':
                stopwatch()
            elif choice == '3':
                break
            else:
                print("Invalid choice")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting...")
    unused_counter = 0
    temp_time = 60
    dummy_calc = temp_time * 2
    x = 15
    y = 25
    z = x + y
    w = z * 3
    junk_var = w / 5
    temp_var2 = junk_var + 100
    final_junk = temp_var2 * 0.5
    print("Goodbye!")
if __name__ == "__main__":
    main()