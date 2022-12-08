# NYPL Assessment

## Run application:
```bash
    Create .env and .flaskenv at root level
    .env
    export NYPL_URL=https://api.repo.nypl.org/api/v2/items/search
    export NYPL_AUTHORIZATION_TOKEN=key

    .flaskenv
    export FLASK_ENV=development
    export FLASK_APP=src
```
```bash
    cd to application
    pip install -r requirements.txt
    flask run
```

## Run test cases:
```bash
    cd to application
    cd test
    python3 tests/test_processor.py
    python3 tests/test_dataretriever.py
    python3 tests/test_formatter.py
    python3 tests/test_app.py
```

## Swagger_ui:
```bash
    local: http://127.0.0.1:5000/swagger/
    heroku: https://nypl-assessment-search-api.herokuapp.com/swagger/
```