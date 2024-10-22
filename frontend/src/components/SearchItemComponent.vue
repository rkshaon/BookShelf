<template>
  <li @click="handleClick"
    class="px-4 py-2 bg-white-600 hover:bg-gray-800 hover:text-white border border-gray-300 shadow-sm rounded-lg cursor-pointer">
    <h3 class="font-semibold">{{ result.title }}</h3>
    <p class="text-sm">
      <span v-for="(author, index) in result.authors" :key="index">
        {{ author.full_name }}<span v-if="index < result.authors.length - 1">, </span>
      </span>
    </p>
  </li>
</template>

<script>
export default {
  name: 'SearchResultItem',
  props: {
    result: {
      type: Object,
      required: true
    }
  },
  methods: {
    // handleClick () {
    //   // Emit an event or perform any action when the item is clicked
    //   this.$emit('select-result', this.result)
    //   console.log('clickked')
    //   this.$router.push(`/book/${this.result.book_code}`)
    // }
    handleClick () {
      // Emit an event or perform any action when the item is clicked
      this.$emit('select-result', this.result)

      // Force the router to reload even if the path is the same
      this.$router.push({
        path: `/book/${this.result.book_code}`,
        query: { reload: new Date().getTime() } // Adding a timestamp query to force reload
      })
    }
  }
}
</script>

<style scoped>
/* Custom styles for the search result item */
</style>
