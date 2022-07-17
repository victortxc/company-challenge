
<template>
<div id="main">
    <Navbar />
    <Footer />
</div>

</template>

<script>
  import Navbar from './components/Navbar.vue';
  import Footer from './components/Footer.vue';

export default {
  components: {
    Navbar,
    Footer
  }
}
</script>


<style scoped>
  #main {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
</style>
