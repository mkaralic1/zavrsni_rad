<template>
  <div class="about">
    <h3>Unos nove destinacije</h3>

    <v-row>
      <v-col>
        <v-text-field
          max-width="344"
          label="Ime destinacije"
          clearable
          v-model="newDestName"
        ></v-text-field>
      </v-col>
      <v-col>
        <v-btn depressed color="primary" @click="novaDestinacija"> Unos </v-btn>
      </v-col>
    </v-row>

    <h3>Postojeće destinacije</h3>

    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">Ime destinacije</th>
            <th class="text-left">ID destinacije</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="dest in destinacije" :key="dest.id">
            <td>{{ dest.name }}</td>
            <td>{{ dest.id }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: "DestiantionView",
  data() {
    return {
      destinacije: [],
      newDestName: "",
    };
  },
  mounted: function () {
    this.axios.get("http://127.0.0.1:8000/destination").then((response) => {
      this.destinacije = response.data;
      console.log(this.destinacije);
    });
  },
  methods: {
    novaDestinacija() {
      const newDestination = {
        name: this.newDestName,
      };
      const config = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      this.axios
        .post("http://127.0.0.1:8000/destination", newDestination, config)
        .then((response) => {
          console.log("nova destinacija dodana:", response.data);
          this.destinacije.push(response.data);
          this.newDestName = "";
        })
        .catch((error) => {
          console.error("greska", error);
        });
    },
  },
};
</script>
