import os


def list_files_in_directory(directory):
    files_list = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            files_list.append(filename)
    return files_list


def write_template_to_file(directory, output_file):
    template = '''
    {
  "pools": [
    {
      "rolls": 1,
      "entries": ['''
    template_entry = '''    {
        "type": "minecraft:item",
        "name": "minecraft:stone",
        "functions": [
            {
                "function": "minecraft:set_nbt",
                "tag": "{structure_data:{name:\\"speedbuilders:FILENAME\\",posY:0}, loot:1b}"
            }
        ]
    }'''

    with open(output_file, 'w') as f:
        f.write(template)
        files = list_files_in_directory(directory)
        for i, filename in enumerate(files):
            f.write(template_entry.replace('FILENAME', filename[:-4]))
            if i < len(files) - 1:
                f.write(',\n')
        f.write('''      
        ]
    }
  ]
}
''')


directory_path = 'structures'
output_file_path = 'loot_tables/all.json'

write_template_to_file(directory_path, output_file_path)
