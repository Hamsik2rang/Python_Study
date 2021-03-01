# Change All "-" in filename to "_" using pathlib
from pathlib import Path

SUFFIX = ".py"

p = Path("./")
python_file_list = list(p.glob(f"**/*{SUFFIX}"))


for file_path in python_file_list:
    stem = file_path.stem

    if stem.find("-") == -1:
        continue
    stem = stem.replace("-", "_")

    directory = file_path.parent
    new_name = f"{stem}{SUFFIX}"

    file_path.rename(Path(directory, new_name))
