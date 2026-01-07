from tasks import tasks
import os

PROGRESS_FILE = "progress.txt"
TOTAL_DAYS = 365


def get_current_day():
    if not os.path.exists(PROGRESS_FILE):
        return 0
    with open(PROGRESS_FILE, "r") as f:
        return int(f.read().strip())


def save_progress(day):
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(day))


def main():
    current_day = get_current_day()

    if current_day >= TOTAL_DAYS:
        print("\nChallenge completed. Respect.")
        return

    next_day = current_day + 1
    task = tasks.get(next_day, "Task not defined yet")

    print("\n==============================")
    print(f"DAY {next_day} CHALLENGE")
    print("==============================")
    print(task)

    input("\nPress ENTER after completing the task...")

    save_progress(next_day)
    print(f"\nDay {next_day} completed. See you tomorrow.")


if __name__ == "__main__":
    main()
