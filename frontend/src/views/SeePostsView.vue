<template>
  <div>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="5">
        <v-autocomplete
          v-model="selectedDestination"
          :items="allDestinations"
          item-text="name"
          item-value="id"
          label="Destinacija"
        ></v-autocomplete>
      </v-col>
      <v-col cols="5">
        <v-btn depressed color="primary" @click="search"> Pretraži </v-btn>
      </v-col>
      <v-col cols="1"></v-col>
    </v-row>
    <v-row>
      <template>
        <v-col cols="12" v-for="dest in allPosts" :key="dest.Post.id">
          <see-post
            :naslov="dest.Post.title"
            :destinacija="dest.dest.name"
            :stvoritelj="dest.owner.nickname"
            :sadrzaj="dest.Post.content"
            :glasovi="dest.votes"
            :id="dest.Post.id"
          >
          </see-post>
        </v-col>
      </template>
    </v-row>
  </div>
</template>

<script>
import SeePost from "@/components/SeePost.vue";

export default {
  components: { SeePost },
  name: "SeePostsView",
  data() {
    return {
      selectedDestination: null,
      allDestinations: [],
      allPosts: [],
    };
  },
  mounted() {
    this.fetchDestinations();
  },
  methods: {
    fetchDestinations() {
      this.axios.get("http://127.0.0.1:8000/destination").then((response) => {
        console.log("destinacije", response.data);
        this.allDestinations = response.data;
      });
    },
    search() {
      const id = this.selectedDestination;
      const destination = this.allDestinations.find((dest) => dest.id === id);
      this.axios
        .get("http://127.0.0.1:8000/posts?search=" + destination.name)
        .then((response) => {
          this.allPosts = response.data;
          console.log(this.allPosts);
        });
    },
  },
};
</script>
