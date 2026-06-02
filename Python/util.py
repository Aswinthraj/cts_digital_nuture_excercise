import shutil
import os


def backup_files(files, backup_folder):

    copied_files = set()

    try:

        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)

        log = open("backup.log", "a")

        for file in files:

            if file in copied_files:
                log.write(f"Skipped Duplicate: {file}\n")
                continue

            shutil.copy(file, backup_folder)

            copied_files.add(file)

            log.write(f"Copied: {file}\n")

        log.close()

        print("Backup Completed Successfully")

    except FileNotFoundError:
        print("File Not Found")

    except PermissionError:
        print("Permission Denied")


files = [
    "data.txt",
    "report.txt",
    "data.txt"
]

backup_files(files, "backup")