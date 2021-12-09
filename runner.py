import argparse
import os.path
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filenames", type=str, nargs="+", help="filenames for another scripts"
    )
    args = parser.parse_args()

    if not os.path.exists("git-subline-merge"):
        print(f"Can't find merge script git-subline-merge")
        exit(-1)

    print("Running merge script on files...")
    for filename in args.filenames:
        print(f"handling {filename}: ", end="")
        proc = subprocess.run(
            ["python", "git-subline-merge", filename], capture_output=True
        )
        if proc.returncode == 0:
            print("OK")
        else:
            print(f"FAILED WITH CODE {proc.returncode}")
