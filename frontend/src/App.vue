
<template>
<div id="main">
    <Navbar />
    <Form />
    <Footer />

</div>

</template>

<script>
  import Navbar from './components/Navbar.vue';
  import Footer from './components/Footer.vue';
  import Form from './components/Form.vue';

export default {
  components: {
    Navbar,
    Footer,
    Form
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
