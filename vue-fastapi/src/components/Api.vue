<script>

//import axios from "axios"
import {axios} from "@/plugins/axios"

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
}

</script>


<template>
    <h3>API result</h3>
    <h4>{{text}}</h4>
</template>
