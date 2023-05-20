<template>
    <NavigationBar />
    <router-view></router-view>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue';
    export default {
        components: {
            NavigationBar
        },
        // compatConfig: {MODE: 3}
    }
</script>