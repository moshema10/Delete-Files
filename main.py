import os
import argparse
import tempfile
import winshell
import win32





parser = argparse.ArgumentParser()
parser.add_argument("--bin", action="store_true", help="use --bin option. This will delete all the files from the recycle bin")
parser.add_argument("--temp", action="store_true", help="use --temp option. This will delete all the files from the temporary files")
arguments = parser.parse_args()


def clear_recycleBin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        print(f"Successfully deleted all the recycle bin files!!")
    except Exception as e:
        print(f"Error occured!!! Reason ===> {e}")
def clear_tempFile():
    temp_folder = tempfile.gettempdir()
    count = count2 = 0
    for file in os.listdir(temp_folder):
        file_path = os.path.join(temp_folder,file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                count += 1
            
        except Exception as e:
            count2 += 1
    if count2 != 0:
        print(f"{count2} could not delete as it is currently being used by another process")

    print(f"Total Temporary Files Deleted: {count}")


if __name__ == "__main__":
    if arguments.bin:
        clear_recycleBin()
    if arguments.temp:
        clear_tempFile()
