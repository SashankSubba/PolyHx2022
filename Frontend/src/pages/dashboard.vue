<template>
    <div class="outer">
        <b-card 
        header="Write a post"
        header-variant="card-header" 
        bg-variant="secondary" 
        text-variant="light"
        style="padding:1rem; text-align:left">
            <label style="font-size:x-large">Title</label>
            <b-form-input class="input" v-model="post.title" id="title" size="lg" placeholder="Enter a title"></b-form-input>
        
            <label style="font-size:x-large">Area/Location</label>
            <b-form-tags class="input" v-model="post.tags" id="tag" size="lg" tag-variant="primary" separator=" " placeholder="Where it occured"></b-form-tags>
            <label style="font-size:x-large">Description</label>
            <b-form-textarea class="input" v-model="post.description" size="lg" id="description" placeholder="Write a post describing an encounter"></b-form-textarea>
        <b-button variant="primary" style="font-size:x-large; float:right; margin-top:2rem" @click="submit">Submit</b-button>
        </b-card>
        <h3 class="mt-5" style="text-align:left; color:white">Other Posts</h3>
    </div>
</template>
<script>
export default {
    name: "Dashboard",
    data() {
        return {
            post: {
                title: '',
                tags: [],
                description: ''
            }
        }
    },
    methods:{
        submit() {
            // post form to db
        }
    }
}

</script>
<style scoped>
.outer {
    padding:0 20rem 0 20rem;
}
.card-header {
    font-size:x-large;
    font-weight: bold;
}
label {
    margin-top:1rem;
    margin-right: 2rem;
}
.input {
    max-width: 750rem;
    margin-right: 10rem;
    margin-top: 1rem;
}

@media only screen and (max-width: 1000px){
    .outer {
        padding: 1rem;
    }
}
</style>
