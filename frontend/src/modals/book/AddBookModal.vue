<template>
  <div v-if="visible" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white rounded-lg shadow-lg w-full max-w-lg">
      <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center">
        <h3 class="text-lg font-semibold text-gray-700">{{ title }}</h3>
        <button @click="closeModal" class="text-gray-400 hover:text-gray-600 text-xl">
          &times;
        </button>
      </div>
      <div class="p-6">
        <slot name="body">
          <form @submit.prevent="onConfirm">
            <!-- <div class="mb-4">
              <label for="name" class="block text-gray-700 text-sm font-bold mb-2">First Name:</label>
              <input type="text" id="name" v-model="localAuthor.first_name"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            </div> -->
            <!-- <div class="mb-4">
              <label for="name" class="block text-gray-700 text-sm font-bold mb-2">Middle Name:</label>
              <input type="text" id="name" v-model="localAuthor.middle_name"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            </div> -->
            <!-- <div class="mb-4">
              <label for="name" class="block text-gray-700 text-sm font-bold mb-2">Last Name:</label>
              <input type="text" id="name" v-model="localAuthor.last_name"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            </div> -->
            <!-- <div class="mb-4">
              <label for="bio" class="block text-gray-700 text-sm font-bold mb-2">Biography:</label>
              <textarea id="bio" v-model="localAuthor.biography"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
              </textarea>
            </div> -->
            <!-- <div class="mb-4">
              <label for="birthdate" class="block text-gray-700 text-sm font-bold mb-2">Birthdate:</label>
              <input type="date" id="birthdate" v-model="localAuthor.birthdate"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                >
            </div> -->
            <!-- <div class="mb-4">
              <label for="dieddate" class="block text-gray-700 text-sm font-bold mb-2">Died Date:</label>
              <input type="date" id="birthdate" v-model="localAuthor.died_date"
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                >
            </div> -->
            <div class="flex justify-end">
              <button type="submit" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition">{{ title }}</button>
            </div>
          </form>
        </slot>
      </div>
      <div class="px-6 py-4 border-t border-gray-200 flex justify-end space-x-3">
        <slot name="footer">
          <button @click="closeModal" class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600 transition">
            Cancel
          </button>
          <button @click="onConfirm" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition">
            Confirm
          </button>
        </slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AddAuthorModal',
  props: {
    visible: {
      type: Boolean,
      required: true
    },
    title: {
      type: String,
      default: 'Modal Title'
    },
    book: {
      type: Object,
      default: () => ({
        title: '',
        genres: [],
        topics: [],
        authors: [],
        publisher: '',
        description: '',
        edition: '',
        isbn: '',
        published_year: '',
        languages: '',
        book: '',
        cover_image: ''
      })
    }
  },
  data () {
    return {
      localBook: { ...this.book }
    }
  },
  emits: ['close', 'confirm'],
  methods: {
    closeModal () {
      this.$emit('close')
    },
    onConfirm () {
      this.$emit('confirm', this.localBook)
    }
  }
}
</script>
