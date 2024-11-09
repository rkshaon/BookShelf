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
                    <!-- Default Body Content -->
                    <p class="text-gray-600">This is the default modal content. Replace it using the body slot.</p>
                </slot>
            </div>
            <div class="px-6 py-4 border-t border-gray-200 flex justify-end space-x-3">
                <slot name="footer">
                    <button @click="closeModal"
                        class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600 transition">
                        Cancel
                    </button>
                    <button @click="onConfirm"
                        class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition">
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
    }
  },
  emits: ['close', 'confirm'],
  methods: {
    closeModal () {
      this.$emit('close')
    },
    onConfirm () {
      this.$emit('confirm')
    }
  }
}
</script>
