from click.testing import CliRunner
from pokecli import pokecli
from unittest.mock import patch

def test_pokecli_rarity():
    runner = CliRunner()
    with patch('pokecli.pokecli.find_rarities', return_value=['Rare','Common','Uncommon']) :
        result = runner.invoke(pokecli.cli, ['rarity'])
        assert result.exit_code == 0
        print (result.output)
        assert "Rare" in result.output
        assert result.output == """\nRarities\n--------\nRare\nCommon\nUncommon\n\n\n"""
