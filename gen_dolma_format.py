import json
import gzip
from datasets import load_dataset
import glob
import os

from prompts import PROMPTS

if __name__ == "__main__":
    all_examples = []

    for path in glob.glob("./data/*.tsv"):
        name = os.path.splitext(os.path.basename(path))[0]
        dataset = load_dataset('csv', data_files=path, split='train', sep="\t")

        prompt = PROMPTS[name[:-len("_rand")] if name.endswith("_rand") else name]
        n_inputs = len(dataset.features) - 1

        for example_idx in range(len(dataset)):
            row = dataset[example_idx]

            if any(x is None for x in row.values()):
                continue

            # spaces around are CUTE convention, but questionable...
            question = prompt.format(*[" " + row[f"input{i}"] + " " for i in range(1, n_inputs+1)])
            # don't put spaces around yes/no
            if name.startswith("contains_char") or name.startswith("contains_word"):
                answer = row["label"]
            else:
                answer = " " + row["label"] + " "

            example_text = question + "\nAnswer: \"" + answer + "\"."

            if example_idx == 0:
                print("Example Text:")
                print(example_text)

            all_examples.append({
                "id": f"{name}_{example_idx}",
                "text": example_text,
                "source": "CUTE",
            })

    with gzip.open("dolma/CUTE/documents/0.jsonl.gz", "wb") as f_out:
        for example in all_examples:
            f_out.write((json.dumps(example) + "\n").encode("utf-8"))