import os
from flasche.build import ProjectBuilder


PROJECT = 'test-project'
TEST_BUILDER = ProjectBuilder(project=PROJECT, port=8000)


def test_create_src_dst():
    test_path = 'test-path'
    src, dst = TEST_BUILDER.create_src_dst(test_path)
    assert dst == os.path.join(PROJECT, test_path)
    assert src == os.path.join(TEST_BUILDER.template_path, test_path)
