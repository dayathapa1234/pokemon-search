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

* Pandas (for CSV processing)

* functools.lru_cache (for caching)

* argparse (for CLI argument parsing)

* rich (for formatted output)

* fuzzywuzzy (for fuzzy search, optional)
