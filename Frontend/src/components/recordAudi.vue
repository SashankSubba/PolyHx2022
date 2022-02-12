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
      recorder: null
    }
  },
  methods: {
    startRecording() {
      let audoRecorder = navigator.mediaDevices.getUserMedia({ audio: true });

      audoRecorder.then((stream) => {
        this.recorder = new MediaRecorder(stream);
        this.recorder.ondataavailable = (e) => {
           console.log(e)
        };
      });
    },
    stopRecording() {
      if (recorder != null){
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
