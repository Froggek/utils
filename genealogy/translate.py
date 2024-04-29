import csv 


print("Hello, IT!")


with open('source.html', 'r') as tree_source_html:
    tree_raw = tree_source_html.read()

# print(tree_raw)

with open('genealogy.csv') as translations:
    translations_csv_reader = csv.reader(translations, delimiter=',', quotechar='"')

    # headers_row = ['initials', 'name', 'nickname', 'surname', 'birthsurname', 'birthdate', 'deathdate']
    headers_row = next(translations_csv_reader)

    for row in translations_csv_reader:
        initials = row[0]
        
        for idx, key in enumerate(headers_row):
            tree_raw = tree_raw.replace(
                f'{initials}{key}', #INname
                row[idx] # real name
            )
    
with open('target.html', 'w') as tree_target_html:
    tree_target_html.write(tree_raw)


