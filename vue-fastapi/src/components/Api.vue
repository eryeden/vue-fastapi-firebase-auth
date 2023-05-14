<script>

//import axios from "axios"
import {axios} from "@/plugins/axios"
import { getAuth} from "firebase/auth";

export default{
    name: "Api",
    props: {
        msg: String,
    },
    data() {
        return {
            text: null,
            api_response: "",
            token: ""
        }
    },
    mounted(){
        axios.get("hello").then(
            (response) => (this.text = response.data)
        ).catch(
            (e) => console.log(e)
        );
    },
    methods: {
        sendUser() {
            // task:
            // 1. getIdToken内で更新した内容を表示できればOK: done
            // 2. tokenとforce refreshせず、キャッシュする

            const auth = getAuth();
            this.token = auth.currentUser?.getIdToken(true).then(
                // ここでアロー関数を使うのがポイント。普通の関数Objectだとスコープ外のthisをキャプチャーできなくなる。
                // アロー関数だと、thisを明示的に持たないと一つ外のスコープのthisが採用される。
                // Reference: https://open8tech.hatenablog.com/entry/2021/01/05/193818
                (idToken) => {

                    this.token = idToken
                    console.log("ID token: " + this.token)

                    axios.get("user", {
                        headers:{
                            "Authorization" : "Bearer " + idToken
                        }
                    }).then(
                        (response) => {
                            console.log("API response:[/user]" + response)
                        this.api_response = response
                        }
                    ).catch(
                        (error) => {
                            console.log("Error API response:[/user]" + error)
                        }
                    )
                })
        }
    },
}

</script>


<template>
    <h3>API result</h3>
    <br/>
    <h4>{{text}}</h4>
    <br/>
    <button @click="sendUser">USER</button>
    <br/>
    <h4>{{token}}</h4>
    <br/>
    <h4>{{api_response}}</h4>

</template>
