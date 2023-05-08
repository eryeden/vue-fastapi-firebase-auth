<script>
import { getAuth, signOut} from "firebase/auth";

export default {
    data() {
        return {
        }
    },
    methods: {
        signOut() {
            const auth = getAuth();
            signOut(auth).then(() => {
                // Sign-out successful.
                alert("Signed out")
            }).catch((error) => {
                // An error happened.
                alert("Failed to sign out: " + error.message)
            });
        }
    },
    mounted: function () {
    }
}
</script>

<template>
    <button @click="signOut">Sign out</button>
</template>