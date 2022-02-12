<template>
  <div>
    <b-button v-on:click="startRecording">Start Recording</b-button>
    <b-button v-on:click="stopRecording">Stop Recoding</b-button>
    <b-button v-on:click="sendToAssemblyAI">Send To Assembly</b-button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'recordAudio',
  data() {
    return {
      recorder: null,
      audioBlob: null,
      audioUrl: null,
      audio: null
    }
  },
  methods: {
    startRecording() {
      let audioRecorder = navigator.mediaDevices.getUserMedia({audio: true});

      audioRecorder.then((stream) => {

        this.recorder = new MediaRecorder(stream);
        this.recorder.start();

        let audioChunks = []

        this.recorder.ondataavailable = (event) => {
          audioChunks.push(event.data)

          let audioBlob = new Blob(audioChunks, {'type': 'audio/mp3;'})
          let audioUrl = URL.createObjectURL(audioBlob)
          let audio = new Audio(audioUrl)
          this.audio = audio
          audio.play()
        };
      });


    },
    stopRecording() {
      if (this.recorder !== null) {
        this.recorder.stop()
      }
    },
    sendToAssemblyAI() {
      if (this.audio != null) {
        axios.post("https://api.assemblyai.com/v2", {
          'firstName': this.user.firstName,
          'lastName': this.user.lastName,
          'email': this.user.email,
          'password': this.user.password
        }, {
          headers: {
            authorization: process.env.VUE_APP_ASSEMBLY_API_TOKEN,
            "content-type": "application/json",
          }
        })
            .then((result) => {
              console.log(result)
            })
            .catch(error => {
              console.log(error)
            })
      }

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
