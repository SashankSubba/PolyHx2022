<template>
  <div class="p-4">
    <navbar/>
    <div class="outerDiv">
      <div class="text">
        <p>Start recording now. Feel free to fake a phone call, describe your encounter, or discuss anything that you
          feel could help you.</p>
        <p>Your emergency contact list will be alerted. </p>
        <p>Don't worry, you're not alone.</p>
      </div>

      <b-button v-if="!recording" pill size="lg" class="record-btn" @click="startRecording">Start Recording
        <img src="../assets/microphone.png" height="35px" class="record">
      </b-button>
      <b-button v-else pill class="stop-record" @click="stopRecording">
        <img src="../assets/telephone-handler.png" height="20px" class="hangup">
      </b-button>

      <b-modal id="after" v-model="showModal" centered no-close-on-backdrop hide-footer hide-header
               body-bg-variant="dark" body-text-variant="light">
        <div class="safe-div" v-if="!next">
          <p style="font-size:x-large; margin-bottom:2rem">Are you safe?</p>
          <div class="safe-buttons">
            <b-button class="safe-no modal-btn" variant="danger" @click="safe = false; next=true"> No</b-button>
            <b-button class="safe-yes modal-btn" @click="safe = true; next=true">Yes</b-button>
          </div>
        </div>
        <div v-if="safe==true && next==true" style="padding:1rem;">
          <p style="font-size:x-large; margin-bottom:1.5rem; text-align:center">Would you like to share your experience
            with others?</p>
          <p class="text-center" style="font-size:larger;">Your personal information will not be shared. You would only
            inform others of where you've experienced this encouter.</p>
          <div class="share-buttons safe-buttons">
            <b-button class="safe-no modal-btn" variant="danger" @click="$bvModal.hide('after'); next=false"> No
            </b-button>
            <b-button class="safe-yes modal-btn" @click="shareExperience">Yes</b-button>
          </div>
        </div>
        <div v-if="safe==false && next==true" style="padding:1rem;">
          <p style="font-size:x-large; margin-bottom:1.5rem; text-align:center">We are alerting your emergency contact
            list.</p>
          <div style="margin:1rem">
            <b-button variant="danger" class=" modal-btn" style="font-size:x-large;">REQUEST IMMEDIATE HELP FROM
              AUTHORITIES
            </b-button>
          </div>
          <div class="text-center mt-5">
            <p style="font-size:x-large"><strong>When you are safe, please inform us by clicking the button
              below.</strong></p>
            <b-button class="text-center modal-btn" variant="success" style="font-size:x-large;" @click="safe=true">I am
              safe.
            </b-button>
          </div>
        </div>
      </b-modal>

    </div>
  </div>
</template>

<script>
import navbar from "@/components/navbar.vue";
import axios from "axios";
import Vue from "vue";

export default {
  name: "Record",
  components: {
    navbar
  },
  data() {
    return {
      recording: false,
      showModal: false,
      next: false,
      safe: false,
      showMap: false,
      recorder: null,
      audioBlob: null,
      audioUrl: null,
      audioFile: null,
      audio: null,
      assemblyAITranscriptionID: null
    }
  },
  created() {
    this.next = false;
    this.safe = false;
    this.firstName = Vue.$cookies.get("firstName");
    this.lastName = Vue.$cookies.get("lastName");
    this.number = Vue.$cookies.get("number");
  },
  methods: {
    startRecording() {
      this.sendSMS()
      this.recording = true
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

          this.audioFile = new File([audioBlob], `recording.mp3`, {
            type: audioBlob.type,
            lastModified: Date.now()
          })

          this.audioUrl = audioUrl.replace("blob:", "")
          this.audio = audio
          // audio.play()

          this.sendFileToFlask(audioBlob)
        };
      });
    },
    stopRecording() {
      this.recording = false;
      this.showModal = true
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
              } else if (result.data.status == 'error') {
                throw "error"
              }
            })
            .catch(error => {
              console.log(error)
            })
      }
    },
    sendFileToFlask(audioBlob) {
      if (audioBlob != null) {
        let formData = new FormData();
        formData.append('file', this.audioFile)
        formData.append('file name', 'test')

        // for (let pair of formData.entries()) {
        //   console.log(pair[0] + ', ' + pair[1]);
        // }

        axios.post("http://localhost:5000/recording", formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              }
            }
        )
            .then((result) => {
              console.log(result)
            })
            .catch(error => {
              console.log(error)
            })
      }
    },
    shareExperience() {
      this.showMap = true
      this.$router.push('/dashboard')
    },
    sendSMS() {
      this.recording = true;
      axios.post('http://localhost:5000/sms',
          {
            "firstName": this.firstName,
            "lastName": this.lastName,
            "number": this.number
          }).then(result => {
        console.log(result)
      }).catch(error => {
        console.log(error)
      });
    }
  }
}
</script>
<style scoped>
.outerDiv {
  margin-top: 5rem;
  /* position: relative; */
}

.text {
  font-size: x-large;
  color: white;
  padding: 2rem 8rem 2rem 8rem;
}

.record-btn {
  font-size: x-large;
  width: 20rem;
  height: 5rem;
  margin-top: 4rem;
}

.stop-record {
  background-color: red;
  font-size: x-large;
  height: 6rem;
  width: 6rem;
  margin-top: 4rem;
  vertical-align: middle;
}

.safe-buttons {
  margin: 2rem auto 0rem auto;
  text-align: center;
}

.safe-no, .safe-yes {
  margin-left: 2rem;
  margin-right: 2rem;
  font-size: x-large;
  width: 5rem;
}

.safe-div {
  text-align: center;
  margin: 1rem;
}

@media only screen and (max-width: 768px) {
  .text {
    font-size: medium;
    padding: 0 2rem 2rem 2rem;
  }

  .stop-record {
    text-align: center;
    height: 5rem;
    width: 5rem;
    margin-top: 1rem;
  }

  .hangup {
    height: 1rem;
  }

  .record-btn {
    width: 15rem;
    height: 5rem;
    font-size: large;
    margin-top: 1rem;
  }

  .record {
    height: 2rem;
  }

  .safe-no, .safe-yes {
    margin-left: 1rem;
    margin-right: 1rem;
  }

  .modal-btn {
    font-size: large !important;
  }

  #after p {
    font-size: large !important;
  }
}

</style>