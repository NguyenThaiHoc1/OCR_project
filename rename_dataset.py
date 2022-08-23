from pathlib import Path
import random
import json
import os
from data_split import split_data

from utlis.utlis import load_json, save_json


def rename(json_file_name):
    data = load_json(json_file_name)

    for i, item in enumerate(data):
        new_image_path = item["image_path"].replace(item["image_path"].split(r'\\')[-1], str(i) + '.jpg')
        new_path_images_path = Path(item["image_path"]).parent / new_image_path
        os.rename(Path(item["image_path"]), new_path_images_path)

        new_gt_path = item["gt_path"].replace(item["gt_path"].split(r'\\')[-1], str(i) + '.txt')
        new_path_labels_path = Path(item["gt_path"]).parent / new_gt_path
        os.rename(item["gt_path"], new_path_labels_path)

        item["image_path"] = str(new_path_images_path)
        item["gt_path"] = str(new_path_labels_path)

    save_json(data, json_file_name)


if __name__ == '__main__':
    data = split_data(data_folder=r"Dataset")
    json_filename = Path(r'./Dataset/data/data.json')
    with open(json_filename, 'w') as f:
        json.dump(data, f)
    rename(json_filename)
