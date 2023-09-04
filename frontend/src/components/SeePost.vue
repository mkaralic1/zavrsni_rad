<template>
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
          <v-col>Stvoritelj</v-col>
          <v-col>{{ stvoritelj }}</v-col>
        </v-row>
        <v-row>
          <v-col>{{ sadrzaj }}</v-col>
        </v-row>
        <v-row>
          <v-col cols="3">{{ glasovi }}</v-col>
          <v-col cols="6"></v-col>
          <v-col cols="3">
            <v-btn depressed color="primary" @click="glasaj"> Like </v-btn>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "SeePost",
  props: ["naslov", "destinacija", "stvoritelj", "sadrzaj", "glasovi", "id"],
  data() {
    return {
      voteData: {
        post_id: this.id,
        dir: 1,
      },
    };
  },
  methods: {
    glasaj() {
      const config = {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      };
      this.axios
        .post("http://127.0.0.1:8000/vote", this.voteData, config)
        .then((response) => {
          console.log("glasano");
          console.log(response.data);
        });
    },
  },
};
</script>
