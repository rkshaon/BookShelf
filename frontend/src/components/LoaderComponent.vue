<template>
    <div class="flex justify-center items-center h-screen">
        <div class="flex space-x-2">
            <div class="dot bg-blue-500"></div>
            <div class="dot bg-blue-500"></div>
            <div class="dot bg-blue-500"></div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'LoaderComponent'
}
</script>

<style scoped>
.dot {
    height: 1.25rem;
    /* 20px */
    width: 1.25rem;
    /* 20px */
    border-radius: 50%;
    animation: bounce 0.6s infinite ease-in-out;
}

.dot:nth-child(1) {
    animation-delay: -0.2s;
}

.dot:nth-child(2) {
    animation-delay: -0.1s;
}

@keyframes bounce {
    0%,
    100% {
        transform: scale(0);
    }

    50% {
        transform: scale(1);
    }
}
</style>
