<template>
    <div id="nav">
        <img src="../../public/img/Voxy_logo.png" alt="Voxy logo" width="100"/>
        <h2 id="text">Code Challenge</h2>
    </div>
</template>

<script>

export default {
    name: "Navbar"
}
</script>

<style scoped>
    #nav {
        background-color:#DAD6E3 ;
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    #text {
        color: #302D68;
    }
</style>
