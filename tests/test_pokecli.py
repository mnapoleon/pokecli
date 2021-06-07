import unittest
from click.testing import CliRunner
from pokecli.pokecli import pokecli
from unittest.mock import Mock, patch

class TestCli(unittest.TestCase):
     
    def setUp(self):
        self.runner = CliRunner()  
    
    def test_pokecli(self):
        result = self.runner.invoke(pokecli.cli, ['--help'])
        assert result.exit_code == 0

    def test_pokecli_rarity(self):
        runner = CliRunner()
        with patch('pokecli.find_rarities', return_value=['Rare','Common','Uncommon']) :
            result = self.runner.invoke(pokecli.cli, ['rarity'])
            assert result.exit_code == 0
            print (result.output)
            assert "Rare" in result.output
            self.assertEqual(result.output, """\nRarities\n--------\nRare\nCommon\nUncommon\n\n\n""")

    def test_build_up_set_params(self):
        results = pokecli.build_up_set_params("Sword & Shield", "Sword & Shield")
        self.assertEqual(results['name'], "Sword & Shield")
        self.assertEqual(results['series'], "Sword & Shield")
        