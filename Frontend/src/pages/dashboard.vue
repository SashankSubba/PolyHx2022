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
        <b-form-tags class="input" v-model="post.tags" id="tag" size="lg" tag-variant="primary" separator=" "
                     placeholder="Where it occured"></b-form-tags>
        <label style="font-size:x-large">Resolved</label>
        <b-form-checkbox class="input" v-model="post.resolved"></b-form-checkbox>

        <label style="font-size:x-large">Private</label>
        <b-form-checkbox class="input" v-model="post.isPrivate"></b-form-checkbox>

        <b-button variant="primary" style="font-size:x-large; float:right; margin-top:2rem" @click="submit">Submit
        </b-button>
      </b-card>
      <h3 class="mt-5 mb-5" style="text-align:left; color:white">Other Encounters</h3>
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
      sentiments: null
    }
  },
  methods: {
    submit() {
      // post form to db
    }
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
            console.log(result.data)
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
