<template>
  <div>
    <template>
      <v-row>
        <v-col cols="1"></v-col>
        <v-col cols="4">Profil: {{ myName }}</v-col>
        <v-col cols="7"></v-col>
      </v-row>
      <v-row>
        <v-col cols="12" v-for="dest in allPosts" :key="dest.Post.id">
          <my-posts
            :naslov="dest.Post.title"
            :destinacija="dest.dest.name"
            :stvoritelj="dest.owner.nickname"
            :sadrzaj="dest.Post.content"
            :glasovi="dest.votes"
            :id="dest.Post.id"
          >
          </my-posts>
        </v-col>
      </v-row>
    </template>
  </div>
</template>

<script>
import MyPosts from "@/components/MyPosts.vue";

export default {
  components: { MyPosts },
  name: "ProfileView",
  data() {
    return {
      allPosts: [],
      myName: null,
    };
  },
  mounted() {
    this.fetchMyPosts();
  },
  methods: {
    fetchMyPosts() {
      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      };
      this.axios
        .get("http://127.0.0.1:8000/posts/myposts", config)
        .then((response) => {
          this.allPosts = response.data;
          this.myName = this.allPosts[0].owner.nickname;
        });
    },
  },
};
</script>
