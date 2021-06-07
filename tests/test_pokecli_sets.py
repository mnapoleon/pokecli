from click.testing import CliRunner
from pokecli import pokecli
from unittest.mock import patch
from pokemontcgsdk import Set

def test_build_up_set_params():
    results = pokecli.build_up_set_params("Sword & Shield", "Sword & Shield")
    assert results['name'] == "Sword & Shield"
    assert results['series'] == "Sword & Shield"