<template>
  <div>
    <!-- Start leftpart -->
    <div class="leftpart">
      <div class="leftpart_inner">
        <div class="logo">
          <router-link to="/"
            ><img src="../assets/img/logo/dark.png" alt=""
          /></router-link>
        </div>
        <!-- End .logo -->
        <div class="menu">
          <a
            v-on:click="activetab = 1"
            :class="[activetab === 1 ? 'active' : '']"
          >
            <img
              class="svg"
              src="../assets/img/svg/home-run.svg"
              alt="homerun"
            />
            <span class="menu_content">Home</span></a
          >
          <!-- End Home -->
          <a
            v-on:click="activetab = 2"
            :class="[activetab === 2 ? 'active' : '']"
          >
            <img class="svg" src="../assets/img/svg/avatar.svg" alt="avatar" />
            <span class="menu_content">About</span></a
          >
          <!-- End About -->
          <!-- <a
            v-on:click="activetab = 3"
            :class="[activetab === 3 ? 'active' : '']"
          >
            <img
              class="svg"
              src="../assets/img/svg/briefcase.svg"
              alt="briefcase"
            />
            <span class="menu_content">Portfolio</span></a
          > -->
          <!-- End Portfolio -->
          <a v-on:click="projects()"
            ><img class="svg" src="../assets/img/svg/paper.svg" alt="paper" />
            <span class="menu_content">projects</span></a
          >
          <a v-on:click="blog()"
            ><img class="svg" src="../assets/img/svg/paper.svg" alt="paper" />
            <span class="menu_content">Blogs</span></a
          >
          <!-- End News -->
          <a
            v-on:click="activetab = 5"
            :class="[activetab === 5 ? 'active' : '']"
          >
            <img class="svg" src="../assets/img/svg/mail.svg" alt="mail" />
            <span class="menu_content"> Contact</span></a
          >
          <!-- End Contact -->
        </div>
      </div>
    </div>
    <!-- End leftpart -->

    <!-- Start rightpart -->
    <div class="rightpart">
      <div class="rightpart_in">
        <div class="tokyo_tm_section">
          <div class="container">
            <div v-if="activetab === 1" class="tabcontent">
              <Home />
            </div>
            <!-- End Home tabcontent -->
            <div v-if="activetab === 2" class="tabcontent">
              <About />
            </div>
            <!-- End About tabcontent  -->
            <div v-if="activetab === 3" class="tabcontent">
              <Portfolio />
            </div>
            <!-- End Portfolio tabcontent -->
            <div v-if="activetab === 4" class="tabcontent">
              <Blog />
            </div>
            <!-- End News tabcontent -->
            <div v-if="activetab === 5" class="tabcontent">
              <Contact />
            </div>
            <!-- End Contact tabcontent -->
          </div>
        </div>
      </div>
    </div>
    <!-- End rightpart -->
  </div>
</template>

<script>
import Home from "../components/Home";
import About from "../components/About";
import Portfolio from "../components/Portfolio";
import Blog from "../components/Blog";
import Contact from "../components/Contact";
export default {
  components: {
    Home,
    About,
    Portfolio,
    Blog,
    Contact,
  },
  data() {
    return {
      activetab: 1,
    };
  },
  methods: {
    blog() {
      window.open("https://jayeshsomala.hashnode.dev/");
    },
    projects() {
      window.open("https://github.com/JayeshSomala");
    },
  },
};
</script>

<style lang="scss" scoped></style>
