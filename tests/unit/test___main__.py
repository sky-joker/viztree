import pytest
from viztree.__main__ import make_dir_info, make_file_info, merge_directory_path


@pytest.mark.parametrize("test_dir_name", [
    ("test")
])
def test_make_dir_info(test_dir_name):
    assert make_dir_info(test_dir_name) == dict(
        title=test_dir_name,
        expanded=True,
        folder=True,
        children=[]
    )


@pytest.mark.parametrize("test_files", [
    (["file1"])
])
def test_file_info(test_files):
    assert make_file_info(test_files)[0] == dict(
        title=test_files[0],
        file=True
    )


@pytest.mark.parametrize("test_path_dict", [
    ({
        "1": [
            dict(
                title="test1",
                expanded=True,
                folder=True,
                sub_dirs=[
                    "test2",
                    "test3"
                ],
                children=[
                    dict(
                        title="file1.txt",
                        file=True
                    )
                ]
            )
        ],
        "2": [
            dict(
                title="test2",
                expanded=True,
                folder=True,
                sub_dirs=[
                    "test4"
                ],
                children=[],
                parent_dir_name="test1"
            ),
            dict(
                title="test3",
                expanded=True,
                folder=True,
                sub_dirs=[
                    "test5"
                ],
                children=[],
                parent_dir_name="test1"
            )

        ],
        "3": [
            dict(
                title="test4",
                expanded=True,
                folder=True,
                sub_dirs=[],
                children=[],
                parent_dir_name="test2"
            ),
            dict(
                title="test5",
                expanded=True,
                folder=True,
                sub_dirs=[],
                children=[],
                parent_dir_name="test3"
            )

        ]
    })
])
def test_merge_directory_path(test_path_dict):
    assert merge_directory_path(test_path_dict) == dict(
        title="test1",
        expanded=True,
        folder=True,
        children=[
            dict(
                title="file1.txt",
                file=True
            ),
            dict(
                title="test2",
                expanded=True,
                folder=True,
                children=[
                    dict(
                        title="test4",
                        expanded=True,
                        folder=True,
                        children=[]
                    )
                ]
            ),
            dict(
                title="test3",
                expanded=True,
                folder=True,
                children=[
                    dict(
                        title="test5",
                        expanded=True,
                        folder=True,
                        children=[]
                    )
                ]
            )
        ]
    )
