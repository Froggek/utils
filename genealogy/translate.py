import csv
from datetime import date  


print("Hello, IT!")


with open('./data/source.html', 'r') as tree_source_html:
    tree_raw = tree_source_html.read()

# print(tree_raw)

with open('./data/genealogy.csv') as translations:
    translations_csv_reader = csv.reader(translations, delimiter=',', quotechar='"')

    # headers_row = ['initials', 'name', 'nickname', 'surname', 'birthsurname', 'birthdate', 'keybirthdate']
    headers_row = next(translations_csv_reader)

    for row in translations_csv_reader:
        initials = row[0]
        
        for idx, key in enumerate(headers_row):
            if key not in ['birthdate', 'keybirthdate']:
                tree_raw = tree_raw.replace(
                    f'{initials}{key}', #INname
                    row[idx] # real name
                )
            
            elif key == 'birthdate' and row[idx]:
                # See strftime() patterns
                # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes 
                birth_date = date.fromisoformat(row[idx])
                # If idxx contains 'birthdate', then (idx + 1) contains 'keybirthdate'
                birth_year = row[idx + 1]

                # FamilyScript - b19900101
                tree_raw = tree_raw.replace(
                    f'b{birth_year}0101',
                    birth_date.strftime('b%Y%m%d') 
                )
                # GEDCOM
                # By adding "-" ("#" on non-Unix systems), 
                # this removed the leading 0's (left padding) 
                # https://stackoverflow.com/questions/904928/python-strftime-date-without-leading-0 
                tree_raw = tree_raw.replace(
                    f'DATE 1 JAN {birth_year}', 
                    birth_date.strftime('DATE %-d %b %Y').upper() # DATE 1 JAN 1990
                )
                # CSV
                tree_raw = tree_raw.replace(
                    f'{birth_year},1,1', 
                    birth_date.strftime('%Y,%-m,%-d') # 1990,1,1
                )
                # Plain text
                tree_raw = tree_raw.replace(
                    f'1 Jan {birth_year}', 
                    birth_date.strftime('%-d %b %Y') # 1 Jan 1990
                )

        

    
with open('./data/target.html', 'w') as tree_target_html:
    tree_target_html.write(tree_raw)


