export let axios;

export default {
    install(app) {
        // base url バックエンド(FastAPI) のURL:port を指定する
        app.config.globalProperties.$http.defaults.baseURL = 'http://127.0.0.1:8000/';

        // request interceptor
        app.config.globalProperties.$http.interceptors.request.use(config => {
            config.headers.Accept = 'application/json';
            return config;
        })

        // response interceptor
        app.config.globalProperties.$http.interceptors.response.use(response => {

            return response;
        }, function(error) {

            return Promise.reject(error);
        })

        axios = app.config.globalProperties.$http;
    },
    get(url) {
        return axios.get(url);
    },
    post(url) {
        return axios.post(url);
    }
}