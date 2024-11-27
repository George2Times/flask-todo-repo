# Flask To-Do App

Aplikacja REST API do zarządzania zadaniami (To-Do List), z możliwością tworzenia, aktualizacji oraz usuwania zadań.

### Uruchomienie aplikacji
1. Zainstaluj wymagania:
    ```sh
    pip install -r requirements.txt
    ```
2. Uruchom aplikację:
    ```sh
    python app.py
    ```

Aplikacja korzysta z Flask oraz opcjonalnie z SQLite.

## Instrukcje
2.1 Create Flask app which will be REST API app for To-Do list, which allow user to 
(DONE) create task, list, 
(DONE) update and 
(DONE) delete them. 
Data could be “mocked”, 
(DONE) extra points for using SQLite or PostgreSQL. 
(DONE) URLS need to be in REST API convention.

## Test
Test w PowerShell:
Pobieranie wszystkich zadań (GET):
curl http://127.0.0.1:5000/tasks
lub
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks -Method Get

Dodawanie nowego zadania (POST):
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks -Method Post -Body '{"title": "Learn Flask"}' -ContentType "application/json"

Aktualizowanie zadania (PUT):
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks/1 -Method Put -Body '{"title": "Learn Flask and REST", "done": true}' -ContentType "application/json"

Usuwanie zadania (DELETE):
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks/1 -Method Delete

