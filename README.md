# File and Directory Name Normalizer

A Python script that recursively normalizes file and directory names to a consistent format. It converts names to lowercase, replaces spaces with underscores, and removes special characters.

## Features

- Recursively processes both files and directories
- Converts all names to lowercase
- Replaces spaces with underscores
- Removes duplicate underscores
- Removes special characters (keeps alphanumeric and underscores)
- Specifically handles .png files
- Prints operation logs during execution
- Safe directory traversal (processes bottom-up)
- Error handling for rename operations

## Prerequisites

- Python 3.x
- No additional packages required (uses only standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/lorenz-127/file-name-normalizer.git
cd file-name-normalizer
```

2. No additional installation required!

## Usage

1. Run the script:
```bash
python rename_script.py
```

2. Enter the directory path when prompted:
```
Enter the directory path to process: /path/to/your/directory
```

### Example Transformations

Files:
- `Egg_Sprite.png` → `egg_sprite.png`
- `Game Character.png` → `game_character.png`
- `PLAYER__ANIMATION.png` → `player_animation.png`

Directories:
- `Game Assets` → `game_assets`
- `Character_Sprites` → `character_sprites`
- `BACKGROUND__FILES` → `background_files`

## Safety Features

- The script processes directories bottom-up to handle nested directories correctly
- Error handling prevents script crashes on permission issues or invalid operations
- All operations are logged to console for tracking

## Important Notes

- **Always backup your files before running this script!**
- The script only processes .png files, but can be modified for other extensions
- Directory names at all levels will be renamed
- Special characters are removed from names
- File extensions are preserved but converted to lowercase

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Lorenz-127
