from click.testing import CliRunner
from pokecli import pokecli

def test_pokecli():
    runner = CliRunner()
    result = runner.invoke(pokecli.cli, ['--help'])
    assert result.exit_code == 0
