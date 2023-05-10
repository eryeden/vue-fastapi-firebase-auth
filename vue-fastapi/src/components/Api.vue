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
            const auth = getAuth();
            this.token = auth.currentUser?.getIdToken(true).then(idToken => {return idToken;})

            auth.currentUser.getIdToken(/* forceRefresh */ true).then(function(idToken) {
                // Send token to your backend via HTTPS
                // ...
                // this.token = idToken
                console.log(idToken)

                axios.get("user", {
                    headers:{
                        "Authorization" : "Bearer " + idToken
                    }
                }).then(
                    (response) => {
                        console.log(response.data)
                        this.api_response = response.data
                    }
                ).catch(
                    (e) => console.log(e)
                );

            }).catch(function(error) {
                // Handle error
                console.log(error)
            });




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
    <h4>{{api_response}}</h4>

</template>
