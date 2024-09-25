from datetime import datetime
import os
folder_path = "results"

def get_information(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        if search_value in line:
            data = line.strip().split(';')
            print(f"{data}")
            create_html_file(data)
            found = True
        if not found:
         print('Ничего не найдено по базе данных')

def create_html_file(content):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{current_time}.html"
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Generated HTML</title>
        </head>
        <body>
            <h1>Запрос выполнен в {current_time}</h1>
            <p>{content}</p>
        </body>
        </html>
        """)

