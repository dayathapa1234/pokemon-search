import csv
import argparse
from rich import print
from rich.table import Table

data_cache = {}

def load_pokemon_data(csv_file):
    if csv_file in data_cache:
        return data_cache[csv_file]
    
    pokemon_list = []
    with open(csv_file,mode='r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row_key = row['Name'].lower()
            data_cache[row_key] = row
            pokemon_list.append(row)
        
    data_cache[csv_file] = pokemon_list
    return pokemon_list
    
    

def search_pokemon(name=None, p_type=None, hp=None, speed=None, attack=None, sort_by=None):
    load_pokemon_data("pokemon.csv")
    results = []
    
    for row_key, data in  data_cache.items():
        if row_key.endswith(".csv"):
            continue
        if name and name.lower() not in data['Name'].lower():
            continue
        if p_type and p_type.lower() not in data['Type 1'].lower():
            continue
        if hp and int(data['HP']) < int(hp):
            continue
        if speed and int(data['Speed']) < int(speed):
            continue
        if attack and int(data['Attack']) < int(attack):
            continue
        results.append(data)
        
    if sort_by and results:
        if sort_by in ['HP', 'Attack', 'Defense', 'Speed']:
            results.sort(key=lambda x: int(x[sort_by]), reverse=True)
        elif sort_by in ['Name', 'Type 1']:
            results.sort(key=lambda x: x[sort_by])
    
    return results
            
def display_results(results):
    if not results:
        print("[red]No Pokémon found.[/red]")
        return
    
    table = Table(title="Pokémon Search Results")
    table.add_column("Name", style="cyan")
    table.add_column("Type", style="green")
    table.add_column("HP", style="yellow")
    table.add_column("Attack", style="magenta")
    table.add_column("Defense", style="blue")
    
    for pokemon in results:
        table.add_row(pokemon['Name'], pokemon['Type 1'], pokemon['HP'], pokemon['Attack'], pokemon['Defense'])
    
    print(table)
       
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search Pokémon from CSV file")
    parser.add_argument("--name", type=str, help="Search Pokémon by name")
    parser.add_argument("--type", type=str, help="Search Pokémon by type")
    parser.add_argument("--hp", type=int, help="Search Pokémon with HP greater than a value")
    parser.add_argument("--speed", type=int, help="Search Pokémon with Speed greater than a value")
    parser.add_argument("--attack", type=int, help="Search Pokémon with Attack greater than a value")
    parser.add_argument("--sort_by", type=str, choices=['HP', 'Attack', 'Defense', 'Speed', 'Name', 'Type 1'], help="Sort results by a stat or attribute")
    args = parser.parse_args()
    
    results = search_pokemon(name=args.name, p_type=args.type, hp=args.hp, speed=args.speed, attack=args.attack, sort_by=args.sort_by)
    display_results(results)