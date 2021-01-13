import os
from unittest.mock import patch

from flasche.build import ProjectBuilder


PROJECT = 'test-project'
TEST_BUILDER = ProjectBuilder(project=PROJECT, port=8000)


def test_create_src_dst():
    test_path = 'test-path'
    src, dst = TEST_BUILDER.create_src_dst(test_path)
    assert dst == os.path.join(PROJECT, test_path)
    assert src == os.path.join(TEST_BUILDER.template_path, test_path)


@patch(
    'flasche.build.ProjectBuilder.create_src_dst',
    return_value=('src', 'dst')
)
@patch('flasche.build.copy')
def test_copy_main(copy, create_src_dst):
    TEST_BUILDER.copy_main_py()
    create_src_dst.assert_called_with('main.py')
    copy.assert_called_with('src', 'dst')


@patch(
    'flasche.build.ProjectBuilder.create_src_dst',
    return_value=('src', 'dst')
)
@patch('flasche.build.copytree')
def test_copy_endpoints(copytree, create_src_dst):
    TEST_BUILDER.copy_endpoints()
    create_src_dst.assert_called_with('endpoints')
    copytree.assert_called_with('src', 'dst')
