<template>
  <div class="bg-gray-600 text-white py-2">
    <div class="container mx-auto px-4 flex justify-between items-center">
      <!-- Left Part: Sliding Text Ad -->
      <div class="overflow-hidden h-6">
        <div class="flex flex-col animate-slide">
          <span v-for="(item, index) in adList" :key="index">
            <a :href="item.url" target="_blank" class="hover:text-gray-300">{{ item.title }}</a>
          </span>
        </div>
      </div>
      <!-- Right Part: Buttons -->
      <div class="flex space-x-4">
        <div v-if="isAuthenticated">
          <button @click="toggleDropdown" class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">
            <img src="path/to/profile-icon.png" alt="Profile" class="w-8 h-8 rounded-full">
            <span class="text-white">Profile</span>
          </button>
          <!-- <div>
            <router-link to="/profile" class="block px-4 py-2 text-gray-800 hover:bg-gray-200">My Profile</router-link>
            <router-link to="/settings" class="block px-4 py-2 text-gray-800 hover:bg-gray-200">Settings</router-link>
            <button @click="logout"
              class="block w-full text-left px-4 py-2 text-gray-800 hover:bg-gray-200">Logout</button>
          </div> -->
        </div>
        <div v-else>
          <router-link to="signup" class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">
            Sign Up
          </router-link>
          <router-link to="signin" class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">Sign
            In</router-link>
        </div>
        <button class="px-3 py-1 bg-gray-700 text-white rounded hover:bg-gray-600">Language</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'TopBarComponent',
  data () {
    return {
      adList: [
        {
          id: 1,
          title: 'Welcome to BookShelf!',
          url: ''
        },
        {
          id: 2,
          title: 'Follow the developer',
          url: 'https://rkshaon.info'
        },
        {
          id: 3,
          title: 'Join our community of book lovers!',
          url: 'https://rkshaon.info'
        }
      ]
    }
  },
  computed: {
    ...mapGetters({
      isAuthenticated: 'isAuthenticated'
    })
  }
}
</script>

<style scoped>
/* Animation for sliding text */
@keyframes slide {
    0% {
        transform: translateY(0);
    }

    33% {
        transform: translateY(-100%);
    }

    66% {
        transform: translateY(-200%);
    }

    100% {
        transform: translateY(0);
    }
}

.animate-slide {
    animation: slide 9s linear infinite;
}
</style>
