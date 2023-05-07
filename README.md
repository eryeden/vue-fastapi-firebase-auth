# vue-fastapi


## Demo

To execute the API:
```bash
uvicorn api.main:app --reload
```

To run the dev server:
```bash
cd vue-fastapi
npm dev run
```

It appears there are two options for running development servers:
- Using a docker(with docker-compose)
- Running development servers separately in a local environment

## Configurations
You need to make sure the configurations are properly set for both FastAPI and Vue.js.
Depending on your setup, port numbers may change, os make sure to adjust them accordingly.

### FastAPI
- CORS: Specify the allowed origins, including correct port number.
```python
# api/main.py:14
allowed_origins = [
    "http://localhost:5173"
]
```
You should also set `allow_methods` and `allow_headers` appropriately.
However, there's no need to modify them for this project.

### Vue
- Back address: Make sure the backend address is configured correctly.
```javascript
// vue-fastapi/src/plugins/axios.js:6
export default {
    install(app) {
        // base url バックエンド(FastAPI) のURL:port を指定する
        app.config.globalProperties.$http.defaults.baseURL = 'http://127.0.0.1:8000/'
            ...
    }
    ...
}
```


## Prerequisites
- python 3.11
- poetry

## Project memo

- Virtual environment set up
```bash
pyenv local 3.11.3
python -m venv .venv
poetry init
poetry shell
```

- FastAPI set up
```bash
poetry add fastapi[all]
```

- Vue3+Vite set up
```bash
npm init vue@latest
cd vue-fastapi/
npm install axios vue-axios
npm install
```
