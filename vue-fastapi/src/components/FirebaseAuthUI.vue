<template>
    <div>
        <div id="firebaseui-auth-container"></div>
    </div>
</template>

<script>
import * as firebase from "firebase/app"
import * as firebase_auth from "firebase/auth"
import * as firebaseui from 'firebaseui'
import 'firebaseui/dist/firebaseui.css'

export default {
    name: 'FirebaseAuthentication',
    props: {
    },
    data: () => ({
        // https://firebaseopensource.com/projects/firebase/firebaseui-web/#configuration
        firebaseConfigUI: {
            signInFlow: "redirect",
            signInSuccessUrl: "/",
            signInOptions: [
                // Leave the lines as is for the providers you want to offer your users.
                // These need to be independently enabled through the web console.
                firebase_auth.GoogleAuthProvider.PROVIDER_ID,
                firebase_auth.EmailAuthProvider.PROVIDER_ID,
                //firebaseui.auth.AnonymousAuthProvider.PROVIDER_ID
            ],
            // tosUrl and privacyPolicyUrl accept either url string or a callback
            // function.
            // Terms of service url/callback.
            tosUrl: '<your-tos-url>',
            // Privacy policy url/callback.
            privacyPolicyUrl: function () {
                window.location.assign('<your-privacy-policy-url>');
            }
        }
    }),
    computed: {
    },
    methods: {
        signInAttempSuccessful(authResult, redirectUrl) {
            alert('Sign in successfull. See dev console for authorization response')
            console.log('authResult', authResult)
            console.log('redirectUrl', redirectUrl)
            // Do what you wish with authResult... save to session, cookie, etc.

/*             const auth = firebase_auth.getAuth()
            firebase_auth.signInWithCredential(auth, authResult.credential).then((userCredential) => {
                    // Signed in
                    const user = userCredential.user;
                    // ...
                    alert("You are succeeded to log in.");
                    this.$router.push("/")
                })
                .catch((error) => {
                    const errorCode = error.code;
                    const errorMessage = error.message;
                    alert(error.message)
                }); */
            this.$router.push("/")
        },
        // Note, bad credentials is not a sign-in failure
        signInAttempFailure(error) {
            alert('Sign in failed. See dev console for error response')
            console.log('error', error)
        },
        firebaseUiShown: function () {
            console.log('Firebase UI widget rendered')
        }
    },
    watch: {
    },
    mounted() {
        // Note, if running your application locally and relying on Vue CLI's hot reload
        // (npm run serve, $ vue-cli-service serve) you will get "Firebase App already exists" errors.
        // You'll need to reload the page manually to initialize FirebaseUI
        // Set callback functions to Firebase UI config.
        // These can be defined in Vue data but I prefer to assign them to Vue methods.
        this.firebaseConfigUI.callbacks = {
            signInSuccessWithAuthResult: this.signInAttempSuccessful,
            signInFailure: this.signInAttempFailure,
            uiShown: this.firebaseUiShown,
        }
        // Get the auth instance
        const auth = firebase_auth.getAuth();

        // Initialize the FirebaseUI Widget using the Firebase app.
        var ui = new firebaseui.auth.AuthUI(auth)
        // The start method will wait until the DOM is loaded.
        ui.start('#firebaseui-auth-container', this.firebaseConfigUI)
    }
}
</script>
