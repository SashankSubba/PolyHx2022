<template>
  <div class="p-4">
    <navbar/>
    <b-container>
      <b-row>
        <b-col cols="2"></b-col>
        <b-col cols="6">
          <div v-if="points.length> 0">
            <vue-google-heatmap :points="points"
                                :width="700"
                                :height="700"/>
          </div>
        </b-col>
        <b-col cols="2"></b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import navbar from "@/components/navbar.vue";
import axios from "axios";

export default {
  name: "Record",
  components: {
    navbar
  },
  data() {
    return {
      points: [
        {lat: 37.786117, lng: -122.440119},
        {lat: 37.786564, lng: -122.440209},
        {lat: 37.786905, lng: -122.440270},
        {lat: 37.786956, lng: -122.440279},
        {lat: 37.800224, lng: -122.433520},
        {lat: 37.800155, lng: -122.434101},
        {lat: 37.800160, lng: -122.434430},
        {lat: 37.800378, lng: -122.434527},
        {lat: 37.800738, lng: -122.434598},
        {lat: 37.800938, lng: -122.434650},
        {lat: 37.801024, lng: -122.434889},
        {lat: 37.800955, lng: -122.435392},
        {lat: 37.800886, lng: -122.435959}
      ]
    }
  },
  created() {
    axios.get("http://localhost:5000/locations",)
        .then((result) => {
          let locationsTemp = []
          result.data.allLocations.forEach(location => {
            locationsTemp.push({'lat': location.latitude, 'lng': location.longitude})
          })
        })
        .catch(error => {
          console.log(error)
        })
  }
}
</script>
<style>

</style>