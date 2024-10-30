<template>
  <div>
    <TopBarComponent />
    <NavBarComponent />
  </div>
</template>

<script>
import TopBarComponent from '@/components/header/TopBarComponent'
import NavBarComponent from '@/components/header/NavBarComponent'

export default {
  name: 'HeaderComponent',
  components: {
    TopBarComponent,
    NavBarComponent
  }
}
</script>
