# Pokemon Search CLI Tool

## Overview

This is a command-line tool that allows users to search for Pokémon data from a CSV file. The tool supports searching by name, type, and various stats (HP, Attack, Defense, etc.). It utilizes in-memory caching to optimize repeated searches, ensuring quick responses.

## Features

* Search Pokémon by:

    * Name

    * Type (e.g., Fire, Water, Electric)

    * HP, Attack, Defense, and other stats

* Supports caching for optimized search performance

* Displays results in a well-formatted CLI output

* Optional fuzzy search for misspelled Pokémon names

* Supports exporting results to CSV or JSON (optional enhancement)

## Technologies Used

* Python

* argparse (for CLI argument parsing)

* rich (for formatted output)

## Installation

1. Clone the repository:

```
git clone https://github.com/dayathapa1234/pokemon-search.git
cd pokemon-search
```

2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Ensure you have a Pokémon CSV dataset (e.g., pokemon.csv) in the project folder.

## Usage

Run the CLI tool with the following command:
```
python main.py --name Pikachu
```
### Available Search Options

* Search by Name:
```
python main.py --name Pikachu
```
* Search by Type:
```
python main.py --type Fire
```
* Search by HP (greater than a value):
```
python main.py --hp 50
```
* Search by Speed (greater than a value):
```
python main.py --speed 80
```
* Search by Attack (greater than a value):
```
python main.py --attack 100
```
* Sort results by Name, Type, HP, Attack, Defense, or Speed:
```
python main.py --sort_by Name

python main.py --sort_by HP
```
Example Output
```
python3 main.py --name bla --sort_by Name
                   Pokémon Search Results                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━┳━━━━━━━━┳━━━━━━━━━┓
┃ Name                    ┃ Type   ┃ HP  ┃ Attack ┃ Defense ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━╇━━━━━━━━╇━━━━━━━━━┩
│ AegislashBlade Forme    │ Steel  │ 60  │ 150    │ 50      │
│ Blastoise               │ Water  │ 79  │ 83     │ 100     │
│ BlastoiseMega Blastoise │ Water  │ 79  │ 103    │ 120     │
│ Blaziken                │ Fire   │ 80  │ 120    │ 70      │
│ BlazikenMega Blaziken   │ Fire   │ 80  │ 160    │ 80      │
│ Doublade                │ Steel  │ 59  │ 110    │ 150     │
│ Karrablast              │ Bug    │ 50  │ 75     │ 45      │
│ KyuremBlack Kyurem      │ Dragon │ 125 │ 170    │ 100     │
└─────────────────────────┴────────┴─────┴────────┴─────────┘
```
