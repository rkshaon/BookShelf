<template>
    <div>
        <pdf src="http://localhost:8001/media/books/190117633520240911194805674430.pdf"
        ></pdf>
    </div>
</template>

<script>

import pdf from 'vue-pdf'

export default {
  name: 'BookReadComponent',
  components: {
    pdf
  },
  data () {
    return { }
  }
}

</script>
