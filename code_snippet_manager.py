import argparse
import json
import os

SNIPPETS_PATH = 'snippets/snippets.json'


def return_snippets():
    if os.path.exists(SNIPPETS_PATH):
        with open(SNIPPETS_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def save_snippets(snippets):
    with open(SNIPPETS_PATH, 'w', encoding='utf-8') as file:
        json.dump(snippets, file, indent = 4)

def add_new_snippet(title, code, tags):
    snippets = return_snippets()
    snippets[title] = {'code': code, 'tags': tags}
    save_snippets(snippets)
    print(f'Snippet {title} added')

def list_snippets(filter = None):
    snippets = return_snippets()

    for title, snippet, in snippets.items():
        if not filter or filter in snippet['tags']:
            print(f'Title: {title}')
            print(f'Tags {", ".join(snippet["tags"])}')
            print('----')

def return_specific_snippet(title):
    snippets = return_snippets()
    snippet = snippets.get(title)

    if snippet:
        print(f'Title: {title}')
        print(f'Tags: {", ".join(snippet["tags"])}')
        print('Code:')
        print(snippet['code'])
    else:
        print(f'{title} not found.')

def main():
    parser = argparse.ArgumentParser(description='Code Snippet Manager')
    subparsers = parser.add_subparsers(dest = 'command')

    #adding a new snippet
    add = subparsers.add_parser('add', help='Add a new code snippet')
    add.add_argument('title', type=str, help='Title of your new code snippet')
    add.add_argument('code', type=str, help='Code for the snippet')
    add.add_argument('tags', type=str, help='Tags for the new snippet (separate with commas)')

    #listing snippets
    list_parser = subparsers.add_parser('list', help='Lists all snippets')
    list_parser.add_argument('--tag', type=str, help='Filter snippets by a specific tag')

    #retrieving a specific snippet
    retrieve = subparsers.add_parser('rertrieve', help='Retrieve a specific code snippet using its title')
    retrieve.add_argument('title', type=str, help='Snippets Title')

    #deleting a snippet

    #searching snippets


if __name__ == '__main__':
    main()
