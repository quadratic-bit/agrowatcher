<template>
  <div>
    <div v-html="msg"></div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Ping',
  metaInfo () {
    return {
      title: 'Ping-Pong'
    }
  },
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    getMessage () {
      const path = 'http://localhost:8000/ping'
      axios.get(path)
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.getMessage()
  }
}
</script>

<style scoped>

</style>
