<template>
  <div class="flex flex-col min-h-screen">
    <HeaderComponent />
    <!-- Main Content -->
    <main class="flex-grow">
      <router-view />
    </main>
    <!-- <HomePage /> -->
    <FooterComponent />
  </div>
</template>

<script>
// import HomePage from '@/pages/HomePage'
import HeaderComponent from './components/HeaderComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'

export default {
  name: 'App',
  components: {
    // HomePage,
    HeaderComponent,
    FooterComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
