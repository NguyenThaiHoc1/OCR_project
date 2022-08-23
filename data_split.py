import os
from pathlib import Path
import json
from sklearn.model_selection import train_test_split


def split_data(data_folder):
    data = []
    image_folder = data_folder / "vietnamese_original" / "vietnamese" / "images"
    label_folder = data_folder / "vietnamese_original" / "vietnamese" / "labels"

    for gt_file in os.listdir(label_folder):
        index = os.path.splitext(gt_file)[0].split('_')[-1]
        image_file = str(int(index)) + '.jpg'
        item = dict()
        item['image_path'] = str(image_folder / image_file)
        item['gt_path'] = str(label_folder / gt_file)
        data.append(item)

    return data


if __name__ == '__main__':
    root_path = Path(__file__).parent.resolve()
    dataset_folder = "Dataset"
    data = split_data(data_folder=root_path / dataset_folder)
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=1)

    with open('Dataset/data/data.json', 'w') as f:
        json.dump(data, f)

    with open('Dataset/data/train_data.json', 'w') as f:
        json.dump(train_data, f)

    with open('Dataset/data/test_data.json', 'w') as f:
        json.dump(test_data, f)
