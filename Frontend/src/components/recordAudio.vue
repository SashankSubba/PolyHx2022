<template>
  <div>
    <b-button style="margin-right: 10px" v-on:click="startRecording">Start Recording</b-button>
    <b-button style="margin-right: 10px" v-on:click="stopRecording">Stop Recoding</b-button>
    <b-button style="margin-right: 10px" v-on:click="sendToAssemblyAI">Send To Assembly</b-button>
    <b-button v-on:click="getResultFromAssemblyAI">Get Processed Transcription from Assembly</b-button>
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
      audio: null,
      assemblyAITranscriptionID: null
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

          this.audioUrl = audioUrl.replace("blob:", "")
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
        axios.post("https://api.assemblyai.com/v2/transcript", {
          'audio_url': this.audioUrl
        }, {
          headers: {
            authorization: process.env.VUE_APP_ASSEMBLY_API_TOKEN,
            "content-type": "application/json",
          }
        })
            .then((result) => {
              // console.log(result)
              this.assemblyAITranscriptionID = result.data.id
            })
            .catch(error => {
              console.log(error)
            })
      }
    },
    getResultFromAssemblyAI() {
      if (this.assemblyAITranscriptionID != null) {
        axios.get("https://api.assemblyai.com/v2/transcript/" + this.assemblyAITranscriptionID, {
          headers: {
            authorization: process.env.VUE_APP_ASSEMBLY_API_TOKEN,
            "content-type": "application/json",
          }
        })
            .then((result) => {
              if (result.data.status == 'completed') {
                console.log("analysis completed")
                console.log(result.data)
              } else if (result.data.status == 'error') {
                throw "error"
              }
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
