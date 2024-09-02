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
                <a href="/signup" class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">Sign Up</a>
                <a href="/login" class="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600">Sign In</a>
                <button class="px-3 py-1 bg-gray-700 text-white rounded hover:bg-gray-600">Language</button>
            </div>
        </div>
    </div>
</template>

<script>
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
