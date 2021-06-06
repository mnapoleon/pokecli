import click
from pokemontcgsdk import Rarity
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import RestClient
from pokemontcgsdk import PokemonTcgException

RestClient.configure('6be6009f-84eb-4dec-84d0-f62c7bd14092')

@click.group()
def cli():
    """This is the pokemontcp cli.  It fronts the Pokemon TCG data found at 
    https://pokemontcg.io/ """
    pass

@cli.command()
@click.option('--set-id', '-sid', help='Id of the set you want to find.  Example xy.  If this option is present all others will be ignored.')
@click.option('--set-name', '-sn', help='Name of the set to find')
@click.option('--series', '-sr', help='Get list of sets from specified series. If series name contains whitespace the name should be surrounded with quotes')
def sets(set_id, set_name, series):
    """Returns all sets given the specified options."""
    if (set_id):
       find_set(set_id)
    else:
        params = build_up_set_params(set_name, series)
        print(params)
        param_list=''
        for k, v in params.items():
            param_list += (f'{k}:"{v}" ')
        param_list = param_list.strip()
        click.echo(param_list)  
        sets = Set.where(q=param_list)
        for pset in sets:
            format_set_info(pset)

def find_set(set_id):
    try:
        pset = Set.find(set_id)
        format_set_info(pset)    
    except PokemonTcgException:
        click.echo(f"No set found with id {set_id}.")   

def build_up_set_params(set_name, series):
    """Creates a dictionary of parameters to match parameter to name expected by pokemontcp api."""
    set_params = {}
    if (set_name):
        set_params['name'] = set_name
    if (series):
        set_params['series'] = series
    return set_params

@cli.command()
def rarity():
    """This will return a list of all the current rarities"""
    rarities = find_rarities()
    longest = 0
    for rarity in rarities:
        if (len(rarity) > longest): 
            longest = len(rarity)
    spacer = "".join(map(lambda x: x*longest, "-"))
    click.echo("\nRarities")
    click.echo(spacer)
    for rarity in rarities:
        click.echo(rarity)
    click.echo("\n")

def find_rarities():
    return Rarity.all()

@cli.command()
@click.option('--card-id', '-cid', help='Id of the card you want to find. Example : xy-1-1')
@click.option('--name', '-n', help='Name of card to lookup. Example : Charizard')
def card(card_id, name):
    if card_id :
        try: 
            card = Card.find(card_id)
            format_card_info(card)
        except PokemonTcgException:
            click.echo(f"No card found with id {card_id}.")            
    elif name :
        cards = Card.where(q=f"name:{name}")
        if len(cards) <= 0:
            click.echo("No cards found.")
        else:
            for card in cards:
                format_card_info(card)

def format_card_info(card):
    click.echo(f'Name : {card.name} - {card.id}')
    click.echo(f'Set :  {card.set.name}')

def format_set_info(pset):
    click.echo(f'Set Name : {pset.name} ({pset.id})')
