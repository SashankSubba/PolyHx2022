<template>
  <div class="p-4">
    <navbar/>
    <div class="outer">
      <b-card
          header="Encounter Details"
          header-variant="card-header"
          bg-variant="secondary"
          text-variant="light"
          style="padding:1rem; text-align:left">

        <b-row>
          <b-col cols="6">
            <label style="font-size:x-large">Processed Audio</label>

            <b-form-textarea :readonly=true v-model="audioTranscription" rows="10"
                             max-rows="20"></b-form-textarea>
          </b-col>
          <b-col cols="6">
            <label style="font-size:x-large">Processed Sentiment</label>
            <b-list-group style="color: black" v-for="(sentiment, value) in sentiments" :key="value">
              <b-list-group-item>{{ sentiment["sentiment"] }}</b-list-group-item>
            </b-list-group>
          </b-col>
        </b-row>

        <label style="font-size:x-large">Title</label>
        <b-form-input class="input" v-model="post.title" id="title" size="lg"
                      placeholder="Enter a title"></b-form-input>

        <label style="font-size:x-large">Area/Location</label>
        <b-form-input class="input" size="lg" tag-variant="primary" placeholder="Where it occured"></b-form-input>


        <label class="mt-5" style="font-size:x-large">Resolved</label>
        <b-form-checkbox class="input" v-model="post.resolved"></b-form-checkbox>

        <label style="font-size:x-large">Private</label>
        <b-form-checkbox class="input" v-model="post.isPrivate"></b-form-checkbox>

        <b-button variant="primary" style="font-size:x-large; float:right; margin-top:2rem" @click="submit">Submit
        </b-button>
      </b-card>
    </div>
  </div>
</template>
<script>
import navbar from "@/components/navbar.vue";
import Vue from "vue";
import axios from "axios";

export default {
  name: "Dashboard",
  components: {
    navbar
  },
  data() {
    return {
      post: {
        title: '',
        tags: [],
        resolved: false,
        isPrivate: false
      },
      transcriptionId: null,
      audioTranscription: null,
      sentiments: null,
      latitude: 0,
      longitude: 0,
      currentLocation: {
        longitude: 0,
        latitude: 0
      },
      googleMapOptions: {
        streetViewControl: false,
        mapTypeControl: false
      },
      center: {lat: 45.508, lng: -73.587},
      circleOptions: {
        fillColor: 'red',
        fillOpacity: 0.2
      }
    }
  },
  methods: {
    submit() {
      // post form to db

      let sentimentTags = ""
      this.sentiments.forEach(sentiment => {
        sentimentTags += sentiment["sentiment"] + " "
      })

      axios.post("http://localhost:5000/encounter", {
        'userId': Vue.$cookies.get('userId'),
        'transcribedAudio': this.audioTranscription,
        'sentimentTags': sentimentTags,
        'transcriptionId': this.transcriptionId,
        'latitude': this.latitude,
        'longitude': this.longitude,
        'resolved': this.post.resolved,
        'isPrivate': this.post.isPrivate
      }, {
        'Content-Type': 'application/json',
      })
          .then((result) => {
            console.log(result.data)
            this.$router.push('/record')
          })
          .catch(error => {
            console.log(error)
          })
    },
    getLocation() {
      navigator.geolocation.getCurrentPosition(
          position => {
            this.center.lng = position.coords.longitude
            this.center.lat = position.coords.latitude
          },
          error => {
            console.log(error.message);
          },
      )
    },
    setPlace(autocompleteResult) {
      if (autocompleteResult.geometry != null) {
        this.center = {
          lat: autocompleteResult.geometry.location.lat(),
          lng: autocompleteResult.geometry.location.lng(),
        };
      }
    }
  },
  beforeMount() {
      this.getLocation()
  },
  created() {
    this.transcriptionId = Vue.$cookies.get("transcriptionId");

    if (this.transcriptionId !== undefined) {

      axios.post("http://localhost:5000/getProcessedAudio", {
        'transcriptionId': this.transcriptionId,
      }, {
        'Content-Type': 'application/json'
      })
          .then((result) => {
            this.audioTranscription = result.data.text
            this.sentiments = result.data.sentiment
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}

</script>
<style scoped>
.outer {
  padding: 0 20rem 0 20rem;
}

.card-header {
  font-size: x-large;
  font-weight: bold;
}

label {
  margin-top: 1rem;
  margin-right: 2rem;
}

.input {
  max-width: 750rem;
  margin-right: 10rem;
  margin-top: 1rem;
}

@media only screen and (max-width: 1000px) {
  .outer {
    padding: 1rem;
  }
}
</style>
