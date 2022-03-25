from click.testing import CliRunner
from python_project_template.cli import hello


def test_hello():
    runner = CliRunner()
    result = runner.invoke(hello, ["--count=3", "--name=Brian"])
    assert result.exit_code == 0
    assert result.output == "Hello Brian!\nHello Brian!\nHello Brian!\n"
