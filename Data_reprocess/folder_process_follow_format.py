from pathlib import Path
from utlis.utlis import load_json
from Data_reprocess.folder_paddocr import PaddleOCR


def run(file_train, file_test, output_dir, writter_class):
    file_train = Path(file_train)
    file_test = Path(file_test)
    output_dir = Path(output_dir)

    data_train = load_json(json_file_name=file_train)
    data_test = load_json(json_file_name=file_test)

    for data in data_train:
        info_bbox = writter_class.read(data['gt_path'])
        writter_class.write(data['image_path'], info_bbox, output_file=output_dir / "train.txt")

    for data in data_test:
        info_bbox = writter_class.read(data['gt_path'])
        writter_class.write(data['image_path'], info_bbox, output_file=output_dir / "test.txt")


if __name__ == '__main__':
    root_path = Path(__file__).parent.parent.resolve()
    file_train_json = root_path / "Dataset" / "data" / "train_data.json"
    file_test_json = root_path / "Dataset" / "data" / "test_data.json"
    output_folder = root_path / "Dataset" / "data"
    type_writter = "paddleocr"

    writter_class_main = None
    if type_writter == "paddleocr":
        writter_class_main = PaddleOCR

    assert writter_class_main is not None, "Please check type writter."
    run(file_train=str(file_train_json),
        file_test=str(file_test_json),
        output_dir=output_folder,
        writter_class=writter_class_main)
