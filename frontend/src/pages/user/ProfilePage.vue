<template>
    <div class="min-h-screen bg-gray-100 flex flex-col items-center">
        <div class="bg-white shadow-md rounded-lg p-6 mt-10 w-full max-w-md">
            <div class="flex flex-col items-center">
                <img
                    class="w-24 h-24 rounded-full object-cover"
                    src="https://via.placeholder.com/150"
                    alt="User Avatar"
                />
                <h2 class="mt-4 text-xl font-semibold">John Doe</h2>
                <p class="text-gray-600">johndoe@example.com</p>
            </div>
            <div class="mt-6">
                <h3 class="text-lg font-medium">Profile Information</h3>
                <div class="mt-4">
                    <label class="block text-gray-700">Full Name</label>
                    <input
                        type="text"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                        value="John Doe"
                    />
                </div>
                <div class="mt-4">
                    <label class="block text-gray-700">Email</label>
                    <input
                        type="email"
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                        value="johndoe@example.com"
                    />
                </div>
                <div class="mt-4">
                    <label class="block text-gray-700">Bio</label>
                    <textarea
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm"
                        rows="3"
                    >
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    </textarea>
                </div>
                <div class="mt-6 flex justify-end">
                    <button class="bg-blue-500 text-white px-4 py-2 rounded-md shadow-sm hover:bg-blue-600">
                        Save Changes
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'ProfilePage'
}
</script>

<style scoped>
/* Add any additional styling here */
</style>
