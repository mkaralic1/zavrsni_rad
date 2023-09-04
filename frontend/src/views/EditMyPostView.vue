<template>
  <div>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="5">
        <v-autocomplete
          v-model="postData.destination_id"
          :items="allDestinations"
          item-text="name"
          item-value="id"
          label="Destinacija"
        ></v-autocomplete>
      </v-col>
      <v-col cols="5">
        <v-btn depressed color="primary" @click="updatePost"> Spremi </v-btn>
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
  name: "EditMyPostView",
  data() {
    return {
      thisPost: [],
      allDestinations: [],
      postData: {
        title: "",
        content: "",
        destination_id: null,
      },
    };
  },
  mounted() {
    const postId = this.$route.params.postId;
    this.currentPost(postId);
    this.fetchDestinations();
  },
  methods: {
    currentPost(id) {
      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      };
      this.axios
        .get("http://127.0.0.1:8000/posts/" + id, config)
        .then((response) => {
          this.thisPost = response.data;
          if (this.thisPost && this.thisPost.Post) {
            this.postData.title = this.thisPost.Post.title;
            this.postData.content = this.thisPost.Post.content;
            this.postData.destination_id = this.thisPost.dest.id;
          }
          console.log(this.thisPost);
        });
    },
    fetchDestinations() {
      this.axios
        .get("http://127.0.0.1:8000/destination")
        .then((response) => {
          this.allDestinations = response.data;
        })
        .catch((error) => {
          console.log("greska", error);
        });
    },

    updatePost() {
      const id = this.$route.params.postId;
      const config = {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      };
      const postData = {
        title: this.postData.title,
        content: this.postData.content,
        destination_id: this.postData.destination_id,
      };
      this.axios
        .put("http://127.0.0.1:8000/posts/" + id, postData, config)
        .then((response) => {
          console.log("post ureden", response.data);
        })
        .catch((error) => {
          console.log("greska", error);
        });
    },
  },
};
</script>
