<template>
  <div>
    <b-button v-on:click="startRecording">Start Recording</b-button>
    <b-button v-on:click="stopRecording">Stop Recoding</b-button>
  </div>
</template>

<script>
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

          audio.play()
        };
      });


    },
    stopRecording() {
      if (this.recorder !== null) {
        this.recorder.stop()
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
