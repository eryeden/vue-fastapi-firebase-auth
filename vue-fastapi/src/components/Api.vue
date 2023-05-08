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
            const token = auth.currentUser?.getIdToken(true).then(idToken => {return idToken;})
            axios.get("user", {
                headers:{
                    "X-AUTH-TOKEN" : "Bearer " + token
                }
            }).then(
                (response) => (this.text = response.data)
            ).catch(
                (e) => console.log(e)
            );
        }
    },
}

</script>


<template>
    <h3>API result</h3>
    <h4>{{text}}</h4>
    <button @click="sendUser">USER</button>
</template>
