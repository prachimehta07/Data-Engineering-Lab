import time
from lifecycle_automation import run_lifecycle


INTERVAL_SECONDS = 60


print("Storage lifecycle background automation started.")
print(f"Checking storage every {INTERVAL_SECONDS} seconds.")


while True:
    try:
        run_lifecycle()
        print("Next check in 60 seconds...")
        time.sleep(INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\nBackground automation stopped.")
        break

    except Exception as error:
        print(f"Error: {error}")
        print("Retrying in 60 seconds...")
        time.sleep(INTERVAL_SECONDS)