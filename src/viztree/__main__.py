from jinja2 import Template
from viztree.argments import create_base_parser
import json
import os


def make_dir_info(dir_name: str) -> dict:
    dir_info = {
        "title": dir_name,
        "expanded": True,
        "folder": True,
        "children": []
    }

    return dir_info


def make_file_info(files: list) -> list:
    file_info_array = []
    for file_name in files:
        file_info_array.append({
            "title": file_name,
            "file": True
        })

    return file_info_array


def merge_directory_path(path_dict: dict) -> list:
    _value = None
    for key, value in sorted(path_dict.items(), reverse=True):
        if _value is None:
            _value = value
        else:
            path_dict[key][0]['children'] += _value
            _value = value

    return path_dict[key][0]


def make_tree(startpath: str) -> dict:
    top_dir_info = {}
    path_dict = {}
    parsed_dict_info_array = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)

        dir_name = os.path.basename(root)

        if level == 0:
            top_dir_info = make_dir_info(dir_name)
            top_dir_info['children'] += make_file_info(files)

        else:
            if level not in path_dict:
                path_dict[level] = []

            if len(root.split('/')) == 2:
                if path_dict[level]:
                    parsed_dict_info_array.append(merge_directory_path(path_dict))

                # reset the variables to set new directory informations for level 1 or less
                path_dict = {}
                path_dict[level] = []

            dir_info = make_dir_info(dir_name)
            dir_info['children'] += make_file_info(files)
            path_dict[level].append(dir_info)

    if path_dict:
        parsed_dict_info_array.append(merge_directory_path(path_dict))

    # merge top_dir_info and parsed_dict_info
    for parsed_dict_info in parsed_dict_info_array:
        top_dir_info['children'].append(parsed_dict_info)

    return top_dir_info


def main():
    args = create_base_parser()
    parsed_dir_info = make_tree(args.path)

    # read template
    with open('/'.join(__file__.split('/')[:-1]) + '/templates/dir_tree_html.j2', 'r') as f:
        template = f.read()

    # generate directory tree html file
    with open('./' + args.save, 'w') as f:
        f.write(Template(template).render(
            tree=json.dumps([parsed_dir_info], indent=2),
            skin=args.skin
        ))


if __name__ == "__main__":
    main()
