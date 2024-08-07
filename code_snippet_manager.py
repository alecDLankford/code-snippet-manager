import argparse
import json
import os

SNIPPETS_PATH = 'snippets/snippets.json'


def return_snippets():
    if os.path.exists(SNIPPETS_PATH):
        with open(SNIPPETS_PATH, 'r') as file:
            return json.load(file)
    return {}

def save_snippets(snippets):
    with open(SNIPPETS_PATH, 'w') as file:
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

    #listing snippets

    #retrieving a specific snippet

    #deleting a snippet

    #searching snippets


if __name__ == '__main__':
    main()
