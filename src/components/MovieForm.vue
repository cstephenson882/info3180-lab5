<template>
    <form id="movieForm" @submit.prevent="saveMovie">
        <!-- {{ form.hidden_tag() }}         -->
        <!-- CSRF token -->
    <input type="hidden" name="csrf_token" :value="csrfToken" />
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" v-model="title" name="title" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea v-model="description" name="description" class="form-control"></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input type="file" ref="poster" name="poster" class="form-control-file" />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const title = ref('');
  const description = ref('');
  const poster = ref(null); // Using ref for file input

  const saveMovie = () => {
    // const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);
    fetch("/api/v1/movies", {
      method: 'POST',
    //   headers: {
    //     'X-CSRFToken': csrfToken  // Include CSRF token in headers
    // },
      body: form_data
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Display success message or handle response data
    })
    .catch(error => {
      console.error(error);
      // Handle error
    });
  };
  </script>
  