<template>
  <ul class="social">
    <li v-for="(social, i) in socialList" :key="i">
      <a :href="social.link" target="_blank" rel="noreferrer"
        ><img class="svg" :src="social.src" alt="social"
      /></a>
    </li>
  </ul>
  <!-- End. social -->
</template>

<script>
  export default {
    data() {
      return {
        socialList: [
          {
            link: "https://twitter.com/SomalaJayesh",
            src: require("../assets/img/svg/social/twitter.svg"),
          },
          {
            link: "https://www.linkedin.com/in/jayesh-somala-9a9b97211/",
            src: require("../assets/img/svg/social/linkedin.svg"),
          },
          {
            link: "https://github.com/JayeshSomala",
            src: require("../assets/img/svg/social/github.svg"),
          },
          {
            link: "https://jayeshsomala.hashnode.dev/",
            src: require("../assets/img/svg/social/website.svg"),
          },
        ],
      };
    },
  };
</script>

<style lang="scss" scoped></style>
