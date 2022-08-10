import os


def fix_rttms(folder: str):
    for rttm in os.listdir(folder):
        if ".rttm" in rttm:
            path = f"{folder}/{rttm}"
            new_lines = []
            with open(path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    new_lines.append(line.replace(".wav", ""))
            with open(path, "w") as file2:
                file2.writelines(new_lines)
                file2.close()


def score_folders(ref: str, sys: str):
    ref_files = f"{ref}/*.rttm"
    sys_files = f"{sys}/*.rttm"

    os.system(f"python score.py -r {ref_files} -s {sys_files}")

if __name__ == "__main__":
    ref = "../VoxConverse/voxconverse_labels/dev"
    for sys in ["../Multi-Stream-Voice-Activity-Detection/rttm_0"]:
        fix_rttms(sys)
        score_folders(ref, sys)