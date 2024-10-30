<template>
    <div class="dashboard-page">
        <header>
            <h1>User Dashboard</h1>
        </header>
        <main>
            <section class="stats">
                <h2>Statistics</h2>
                <!-- Add your statistics components or data here -->
            </section>
            <section class="recent-activities">
                <h2>Recent Activities</h2>
                <!-- Add your recent activities components or data here -->
            </section>
        </main>
    </div>
</template>

<script>
export default {
  name: 'DashboardPage',
  data () {
    return {
      // Add your data properties here
    }
  },
  methods: {
    // Add your methods here
  },
  mounted () {
    // Fetch data or perform actions when the component is mounted
  }
}
</script>

<style scoped>
.dashboard-page {
    padding: 20px;
}

header {
    background-color: #f5f5f5;
    padding: 10px;
    text-align: center;
}

main {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}

section {
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 20px;
    width: 45%;
}

h2 {
    margin-top: 0;
}
</style>
