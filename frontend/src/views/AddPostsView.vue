<template>
  <div>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="4">
        <h2>Dodavanje postova</h2>
      </v-col>
      <v-col cols="7"></v-col>
    </v-row>
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
        <v-btn depressed color="primary" @click="addPost"> Dodaj </v-btn>
      </v-col>
      <v-col cols="1"></v-col>
    </v-row>

    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="10">
        <v-text-field label="Naslov" v-model="postData.title"></v-text-field>
      </v-col>
      <v-col cols="1"></v-col>
    </v-row>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="10">
        <v-textarea
          counter
          label="Sadržaj"
          v-model="postData.content"
        ></v-textarea>
      </v-col>
      <v-col cols="1"></v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "AddPostsView",
  data() {
    return {
      selectedDestination: null,
      allDestinations: [],
      postData: {
        title: "",
        content: "",
        destination_id: null,
      },
      post: [],
    };
  },
  mounted() {
    this.fetchDestinations();
  },
  methods: {
    fetchDestinations() {
      this.axios
        .get("http://127.0.0.1:8000/destination")
        .then((response) => {
          this.allDestinations = response.data;
        })
        .catch((error) => {
          console.error("greska", error);
        });
    },
    addPost() {
      const config = {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      };

      const postData = {
        title: this.postData.title,
        content: this.postData.content,
        destination_id: this.selectedDestination,
      };

      this.axios
        .post("http://127.0.0.1:8000/posts", postData, config)
        .then((response) => {
          console.log("dodan post", response.data);
          this.post.push(response.data);
        })
        .catch((error) => {
          console.error("greska", error);
        });
    },
  },
};
</script>
