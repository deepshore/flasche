from unittest.mock import patch

from flasche.run import ProjectRunner


PROJECT = 'test'
TEST_RUNNER = ProjectRunner(project=PROJECT)


@patch('flasche.run.ProjectRunner.run')
def test_run(flask_run):
    TEST_RUNNER.run()
    flask_run.assert_called_once()
