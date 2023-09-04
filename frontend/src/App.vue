<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat>
      <v-container class="py-0 fill-height">
        <v-btn v-for="[ikona, ruta] in links" :key="ikona" :to="ruta" text>
          {{ ikona }}
        </v-btn>

        <v-spacer></v-spacer>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col>
            <v-sheet min-height="70vh" rounded="lg">
              <router-view></router-view>
              <!--  -->
            </v-sheet>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="1"></v-col>
          <v-col cols="10"><p>Izradio Martin Karalić 2023.</p></v-col>
          <v-col cols="1"></v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    links: [
      ["Naslovna", "/"],
      ["Destinacije", "/destinacije"],
      ["Recenzije", "/recenzije"],
      ["Dodaj", "/dodaj"],
      ["Prijava", "/prijava"],
      ["Registracija", "/registracija"],
      ["Moj profil", "/moj_profil"],
    ],
  }),
};
</script>
