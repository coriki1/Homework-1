import os

folder_path = '/home/coriki1/progalap1/nagyhazi/cards'
os.makedirs(folder_path, exist_ok=True)

# Iterate through each card and create a file for each
cards = [
    '.-------.\n|A      |\n|   ♠   |\n|      A|\n`-------`',
    '.-------.\n|A      |\n|   ♥   |\n|      A|\n`-------`',
    '.-------.\n|A      |\n|   ♦   |\n|      A|\n`-------`',
    '.-------.\n|A      |\n|   ♣   |\n|      A|\n`-------`',
    '.-------.\n|2      |\n|   ♠   |\n|      2|\n`-------`',
    '.-------.\n|2      |\n|   ♥   |\n|      2|\n`-------`',
    '.-------.\n|2      |\n|   ♦   |\n|      2|\n`-------`',
    '.-------.\n|2      |\n|   ♣   |\n|      2|\n`-------`',
    '.-------.\n|3      |\n|   ♠   |\n|      3|\n`-------`',
    '.-------.\n|3      |\n|   ♥   |\n|      3|\n`-------`',
    '.-------.\n|3      |\n|   ♦   |\n|      3|\n`-------`',
    '.-------.\n|3      |\n|   ♣   |\n|      3|\n`-------`',
    '.-------.\n|4      |\n|   ♠   |\n|      4|\n`-------`',
    '.-------.\n|4      |\n|   ♥   |\n|      4|\n`-------`',
    '.-------.\n|4      |\n|   ♦   |\n|      4|\n`-------`',
    '.-------.\n|4      |\n|   ♣   |\n|      4|\n`-------`',
    '.-------.\n|5      |\n|   ♠   |\n|      5|\n`-------`',
    '.-------.\n|5      |\n|   ♥   |\n|      5|\n`-------`',
    '.-------.\n|5      |\n|   ♦   |\n|      5|\n`-------`',
    '.-------.\n|5      |\n|   ♣   |\n|      5|\n`-------`',
    '.-------.\n|6      |\n|   ♠   |\n|      6|\n`-------`',
    '.-------.\n|6      |\n|   ♥   |\n|      6|\n`-------`',
    '.-------.\n|6      |\n|   ♦   |\n|      6|\n`-------`',
    '.-------.\n|6      |\n|   ♣   |\n|      6|\n`-------`',
    '.-------.\n|7      |\n|   ♠   |\n|      7|\n`-------`',
    '.-------.\n|7      |\n|   ♥   |\n|      7|\n`-------`',
    '.-------.\n|7      |\n|   ♦   |\n|      7|\n`-------`',
    '.-------.\n|7      |\n|   ♣   |\n|      7|\n`-------`',
    '.-------.\n|8      |\n|   ♠   |\n|      8|\n`-------`',
    '.-------.\n|8      |\n|   ♥   |\n|      8|\n`-------`',
    '.-------.\n|8      |\n|   ♦   |\n|      8|\n`-------`',
    '.-------.\n|8      |\n|   ♣   |\n|      8|\n`-------`',
    '.-------.\n|9      |\n|   ♠   |\n|      9|\n`-------`',
    '.-------.\n|9      |\n|   ♥   |\n|      9|\n`-------`',
    '.-------.\n|9      |\n|   ♦   |\n|      9|\n`-------`',
    '.-------.\n|9      |\n|   ♣   |\n|      9|\n`-------`',
    '.-------.\n|10     |\n|   ♠   |\n|     10|\n`-------`',
    '.-------.\n|10     |\n|   ♥   |\n|     10|\n`-------`',
    '.-------.\n|10     |\n|   ♦   |\n|     10|\n`-------`',
    '.-------.\n|10     |\n|   ♣   |\n|     10|\n`-------`',
    '.-------.\n|J      |\n|   ♠   |\n|      J|\n`-------`',
    '.-------.\n|J      |\n|   ♥   |\n|      J|\n`-------`',
    '.-------.\n|J      |\n|   ♦   |\n|      J|\n`-------`',
    '.-------.\n|J      |\n|   ♣   |\n|      J|\n`-------`',
    '.-------.\n|Q      |\n|   ♠   |\n|      Q|\n`-------`',
    '.-------.\n|Q      |\n|   ♥   |\n|      Q|\n`-------`',
    '.-------.\n|Q      |\n|   ♦   |\n|      Q|\n`-------`',
    '.-------.\n|Q      |\n|   ♣   |\n|      Q|\n`-------`',
    '.-------.\n|K      |\n|   ♠   |\n|      K|\n`-------`',
    '.-------.\n|K      |\n|   ♥   |\n|      K|\n`-------`',
    '.-------.\n|K      |\n|   ♦   |\n|      K|\n`-------`',
    '.-------.\n|K      |\n|   ♣   |\n|      K|\n`-------`',
]

# Create subfolders for each color
colors = ['spades', 'hearts', 'diamonds', 'clubs']
for color in colors:
    color_folder_path = os.path.join(folder_path, color)
    os.makedirs(color_folder_path, exist_ok=True)

# Iterate through each card and create a file for each
for card in cards:
    # Extract the color and value from the card string
    color = card.split('\n')[2].split()[1]
    value = card.split('\n')[3].split()[1]

    # Create the file name
    file_name = f"{color[0].lower()}{value}"

    # Determine the color folder path based on the card color
    if color == '♠':
        color_folder_path = os.path.join(folder_path, 'spades')
    elif color == '♥':
        color_folder_path = os.path.join(folder_path, 'hearts')
    elif color == '♦':
        color_folder_path = os.path.join(folder_path, 'diamonds')
    elif color == '♣':
        color_folder_path = os.path.join(folder_path, 'clubs')

    # Create the file path
    file_path = os.path.join(color_folder_path, file_name)

    # Write the card content to the file
    with open(file_path, 'w') as file:
        file.write(card)