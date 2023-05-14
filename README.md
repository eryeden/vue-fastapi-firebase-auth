# vue-fastapi-firebase-auth

This repo is intended to be a template which consists of `Vue.js` and `FastAPI` , and `Firebase auth`.
The following features are included in this repo:
- User authentication on frontend using Vue.js
- Sign in screen provided by the firebase auth UI
- User verification on backend using FastAPI

## API
This repo has the following API endpoints, some of which require authentication:

| End point | Description              | Authentication |
|-----------|--------------------------|---------------|
| /hello    | Welcome message          | not required  |
| /user     | User specific infomation | required      |

The api will be hosted under `http://127.0.0.1:8000/` by default.

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

## Configurations
You need to make sure the configurations are properly set for both FastAPI and Vue.js.
Depending on your setup, port numbers may change, os make sure to adjust them accordingly.

### Environment variables
The following variables shall be configured properly and stored in `vue-fastapi/.env.local`.
Please refer to the firebase console and fill them.
This file is not contained in this repo, so make sure to it will be generated.

```.env
VITE_apiKey=****,
VITE_authDomain=****,
VITE_projectId=***,
VITE_storageBucket=****,
VITE_messagingSenderId=****,
VITE_appId=****,
VITE_measurementId=****"
```

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
poetry add fastapi[all] firebase_admin
```

- Vue3+Vite set up
```bash
npm init vue@latest
cd vue-fastapi/
npm install axios vue-axios firebaseui firebase-tools
npm install
```


#### Firebase error

以下エラーがFastAPIからFirebaseAuthでTokenを検証する際に発生していた。
```
{"detail":"Invalid authentication credentials. 'HTTPResponse' object has no attribute 'strict'"}e
```

下記ページを見るとurllib3のバージョンによって生じる問題らしい。以下バージョンに固定することで検証ができるようになった。
- https://github.com/ionrock/cachecontrol/issues/292
- https://github.com/ionrock/cachecontrol/issues/292#issuecomment-1539171576

Poetryでは以下コマンドでバージョン固定ができる:
```bash
poetry add urllib3==1.26.15
```

#### `this`
関数Objectだと`this`にアクセスできない？アロー関数で`this`にアクセスしデータを出力することができる。

