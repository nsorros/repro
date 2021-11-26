import json
import csv

import typer


def yield_processed_data(data_path):
    with open(data_path) as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            yield {"text": row["tweet"], "label": row["hate_speech"]}


def preprocess_data(data_path, output_path):
    with open(output_path, "w") as f:
        for example in yield_processed_data(data_path):
            f.write(json.dumps(example) + "\n")


if __name__ == "__main__":
    typer.run(preprocess_data)
