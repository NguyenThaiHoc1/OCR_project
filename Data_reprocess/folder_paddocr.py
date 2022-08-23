"""
Build with format data
https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/dataset/ocr_datasets_en.md
https://www.codetd.com/en/article/13027276
"""
import json

from utlis.utlis import load_txt


class PaddleOCR(object):

    @staticmethod
    def read(data_gt_path):
        data = []
        lines = load_txt(data_gt_path)
        for line in lines:
            dict_line = dict()
            line_split = line.split(',')
            transcription = str(''.join(line_split[8:])).strip()
            length_box = len(line_split[:8])
            bbox = [[int(line_split[idx]), int(line_split[idx + 1])] for idx in range(0, length_box, 2)]
            dict_line["transcription"] = transcription.replace('\"', '\\"')
            dict_line["points"] = bbox
            data.append(dict_line)

        return data

    @staticmethod
    def write(image_path, data, output_file):
        with open(output_file, 'w') as f:
            f.write(image_path + '\t')
            json_object = json.dumps(data)
            f.write(json_object)
            f.write('\n')
