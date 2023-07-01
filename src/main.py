import time
import actions
import os

# Make sure pip packages are installed
try:
    from tqdm import tqdm
    from colorama import Fore, Style
except ImportError:
    print("Required pip packages not installed.")
    # Ask if they want to auto install them
    inp_val = input("Would you like to install them? (y/N): ")
    # Validate input
    match inp_val.lower():
        # Install case
        case "y" | "yes":
            os.system("pip install -r ../requirements.txt")
            input("Packages done installing. Restart app")
        # Reject case
        case "n" | "N":
            input("Packages must be installed to run app")
        # Unknown case
        case _:
            input("Unknown input given")

def unlock_fps() -> None:
    tasks = [
        {"description": "Loading", "action": actions.nothing},
        {"description": "Unlocking", "action": actions.unlock_fps},
        {"description": "Done", "action": actions.nothing},
    ]

    # Initialize the progress bar
    progress_bar = tqdm(total=len(tasks), unit='task', colour="#00ff00",
                        bar_format=Fore.LIGHTYELLOW_EX + "{desc}{percentage:3.0f}%|" + Style.RESET_ALL + "{bar:10}" + Fore.LIGHTYELLOW_EX + "| {n_fmt}/{total_fmt}")

    for task in tasks:
        # Update the progress bar and display the current task
        progress_bar.set_description(task['description'])

        # Execute the task's action
        task['action']()

        # Sleep for 1 second just for some delay
        time.sleep(1)

        # Update task
        progress_bar.update(1)

    # Close the progress bar
    progress_bar.close()


if __name__ == '__main__':
    try:
        unlock_fps()
        input()
    except Exception as err:
        print(err)