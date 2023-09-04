<template>
  <div>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="4">
        <h2>Prijava</h2>
      </v-col>
      <v-col cols="7"></v-col>
    </v-row>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="4">
        <v-text-field
          v-model="loginData.email"
          max-width="344"
          :rules="[rules.required]"
          type="email"
          label="E-mail"
        ></v-text-field>
      </v-col>
      <v-col cols="7"></v-col>
    </v-row>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="4">
        <v-text-field
          max-width="344"
          label="Zaporuka"
          v-model="loginData.password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required]"
          :type="show1 ? 'text' : 'password'"
          name="input-10-1"
          @click:append="show1 = !show1"
        >
        </v-text-field>
      </v-col>
      <v-col cols="7"></v-col>
    </v-row>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="4">
        <v-btn depressed color="primary" @click="Prijava"> Prijava </v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      show1: false,
      loginData: {
        email: "",
        password: "",
      },
      rules: {
        required: (value) => !!value || "Required",
      },
    };
  },
  methods: {
    Prijava() {
      const formData = new FormData();
      formData.append("username", this.loginData.email);
      formData.append("password", this.loginData.password);

      this.axios
        .post("http://127.0.0.1:8000/login", formData)
        .then((response) => {
          const token = response.data.access_token;
          this.$store.commit("SET_TOKEN", token);
          console.log("Token:", token);

          this.loginData = {
            email: "",
            password: "",
          };
        })
        .catch((error) => {
          console.error("greska", error);
        });
    },
  },
};
</script>
