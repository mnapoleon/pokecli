from click.testing import CliRunner
from pokecli import pokecli

def test_pokecli():
    runner = CliRunner()
    result = runner.invoke(pokecli, ['--help'])
    assert result.exit_code == 0

def test_pokecli_rarity():
    runner = CliRunner()
    result = runner.invoke(pokecli, ['rarity'])
    assert result.exit_code == 0
    assert "Rare" in result.output