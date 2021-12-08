import argparse
import os.path
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filenames", type=str, nargs="+", help="filenames for another scripts"
    )
    parser.add_argument(
        "--python",
        type=str,
        default="python",
        help="python version to run the merge script with",
    )
    parser.add_argument(
        "--merge-script",
        type=str,
        default="git-subline-merge",
        help="merge script path",
    )
    args = parser.parse_args()

    if not os.path.exists(args.merge_script):
        print(f"Can't find merge script {args.merge_script}")
        exit(-1)

    print("Running merge script on files...")
    for filename in args.filenames:
        print(f"handling {filename}: ", end="")
        proc = subprocess.run(
            [args.python, args.merge_script, filename], capture_output=True
        )
        if proc.returncode == 0:
            print("OK")
        else:
            print(f"FAILED WITH CODE {proc.returncode}")
