import os
import glob

dir_path = os.path.dirname(os.path.realpath(__file__))


def match_sequentially():
    matches = []
    query = 'hello jina'
    txt_files = glob.glob(f'{dir_path}/resources/*.txt')
    for txt_file in txt_files:
        with open(txt_file, 'r') as f:
            if query in f.read():
                matches.append(txt_file)
    return matches


if __name__ == '__main__':
    matches = match_sequentially()
    print(matches)
