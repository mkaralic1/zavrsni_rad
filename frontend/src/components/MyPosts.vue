<template>
  <div>
    <v-container>
      <v-card>
        <v-card-text>
          <p class="text-h6 text--primary">
            {{ naslov }}
          </p>
          <v-row>
            <v-col>{{ destinacija }}</v-col>
          </v-row>
          <v-row>
            <v-col>{{ sadrzaj }}</v-col>
          </v-row>
          <v-row>
            <v-col cols="3">{{ glasovi }}</v-col>
            <v-col cols="3"></v-col>
            <v-col cols="3">
              <v-btn depressed color="primary"
              :to="{ name: 'EditMyPostView', params: { postId: id } }">
                Uredi
              </v-btn>
            </v-col>
            <v-col cols="3">
              <v-btn depressed color="primary" @click="obrisiPost">
                Obriši
              </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "MyPosts",
  props: ["naslov", "destinacija", "stvoritelj", "sadrzaj", "glasovi", "id"],
  data() {
    return {
      del_id: this.id,
      link: "/editpost",
      put_id: this.id,
    };
  },
  methods: {
    obrisiPost() {
      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      };
      this.axios
        .delete("http://127.0.0.1:8000/posts/" + this.del_id, config)
        .then((response) => {
          console.log("Post deleted", response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
