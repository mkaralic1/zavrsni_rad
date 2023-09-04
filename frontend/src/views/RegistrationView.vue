<template>
  <div>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="4">
        <div>
          <h2>Registracija</h2>
          <h5>Brzo i jednostavno</h5>
        </div>
      </v-col>
      <v-col cols="7"></v-col>
    </v-row>

    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="4">
        <v-text-field
          v-model="userData.nickname"
          max-width="344"
          label="Korisničko ime"
          :rules="[rules.required]"
        ></v-text-field>
      </v-col>
      <v-col cols="7"></v-col>
    </v-row>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="4">
        <v-text-field
          v-model="userData.email"
          max-width="344"
          :rules="[rules.required, rules.email]"
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
          v-model="userData.password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min]"
          :type="show1 ? 'text' : 'password'"
          name="input-10-1"
          label="Zaporuka"
          hint="At least 8 characters"
          counter
          @click:append="show1 = !show1"
        ></v-text-field>
      </v-col>
      <v-col cols="7"></v-col>
    </v-row>
    <v-row>
      <v-col cols="1"></v-col>
      <v-col cols="4">
        <v-btn depressed color="primary" @click="Registracija">
          Registracija
        </v-btn>
      </v-col>
      <v-col cols="7"></v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "RegistrationView",
  data() {
    return {
      show1: false,
      show2: true,
      show3: false,
      show4: false,
      userData: {
        nickname: "",
        email: "",
        password: "",
      },

      rules: {
        required: (value) => !!value || "Required.",
        min: (v) => v.length >= 8 || "Min 8 characters",
        emailMatch: () => `The email and password you entered don't match`,
        email: (value) => {
          const pattern =
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Invalid e-mail.";
        },
      },
    };
  },
  methods: {
    Registracija() {
      const config = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      this.axios
        .post("http://127.0.0.1:8000/users", this.userData, config)
        .then((response) => {
          console.log("uspješna registracija", response.data);
          this.userData = {
            nickname: "",
            email: "",
            password: "",
          };
        })
        .catch((error) => {
          console.log("greska", error);
        });
    },
  },
};
</script>
