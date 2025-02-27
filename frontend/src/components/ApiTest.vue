<template>
    <div>
      <h2>Flask API Response</h2>
      <p v-if="loading">Loading...</p>
      <p v-else-if="error" class="error">{{ error }}</p>
      <p v-else>{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        message: "",
        error: null,
        loading: true
      };
    },
    mounted() {
      axios.get("http://localhost:5000/api/test")
        .then(response => {
          this.message = response.data.message;
        })
        .catch(error => {
          this.error = "Failed to fetch data.";
        })
        .finally(() => {
          this.loading = false;
        });
    }
  };
  </script>
  
  <style scoped>
  .error {
    color: red;
  }
  </style>
  