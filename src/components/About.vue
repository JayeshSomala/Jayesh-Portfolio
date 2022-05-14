<template>
  <div class="tokyo_tm_about">
    <div class="about_image">
      <img src="../assets/img/slider/4.jpg" alt="about" />
    </div>
    <!-- End .about_image -->

    <div class="description">
      <h3 class="name">Somala Jayesh</h3>
      <div class="description_inner">
        <div class="left">
          <p>
            Self-starting and driven engineering student with a passion for producing software products and implementing new software platforms and a keen interest in working in a fast-paced environment, eager
            to learn more and grow in my skills so I can achieve organizational goals as part of a team which provides
            me with job satisfaction.
          </p>
          <div class="tokyo_tm_button">
            <button class="ib-button" @click="showModal">Read More</button>
          </div>
        </div>
        <!-- End .left -->

        <div class="right">
          <ul>
            <li>
              <p><span>Birthday:</span>10.08.2002</p>
            </li>
            <li>
              <p><span>Age:</span>19</p>
            </li>
            <li>
              <p><span>Address:</span>BANGLORE, KARNATAKA, INDIA</p>
            </li>
            <li>
              <p>
                <span>Email:</span
                ><a href="mailto:jayeshsomala27@gmail.com">jayeshsomala27@gmail.com</a>
              </p>
            </li>
            <li>
              <p>
                <span>Phone:</span
                ><a href="tel:+91 6301668661">+91 630 166 86 61</a>
              </p>
            </li>
            <li>
              <p><span>Study:</span>BMS COLLEGE OF ENGINEERING</p>
            </li>
            <li>
              <p><span>Freelance:</span>Available</p>
            </li>
          </ul>
          <!-- End ul -->
        </div>
        <!-- End .right -->
      </div>
    </div>

    <!-- Start Modalbox -->
    <transition name="fade">
      <!-- Modal -->
      <div
        :class="{ 'modal-mask': isActive }"
        id="modal"
        @click="closeModal"
        v-if="isVisible"
      >
        <div
          class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-user"
          @click.stop
        >
          <div class="modal-content">
            <div class="tokyo_tm_modalbox_about">
              <div class="close" @click="closeModal">
                <img
                  class="svg"
                  src="../assets/img/svg/cancel.svg"
                  alt="cancel-img"
                />
              </div>
              <!-- End .close -->
              <div class="my_box">
                <div class="left">
                  <div class="about_title">
                    <h3>Skills</h3>
                  </div>
                  <!-- End .abut_title -->
                  <div class="tokyo_progress">
                    <div class="progress_inner">
                      <span
                        ><span class="label">React JS</span
                        ><span class="number">90%</span></span
                      >
                      <div class="background">
                        <div class="bar">
                          <div class="bar_in" style="width:90%"></div>
                        </div>
                      </div>
                    </div>
                    <div class="progress_inner">
                      <span
                        ><span class="label">Mongo DB</span
                        ><span class="number">80%</span></span
                      >
                      <div class="background">
                        <div class="bar">
                          <div class="bar_in" style="width:80%"></div>
                        </div>
                      </div>
                    </div>
                    <!-- End progress_inner -->
                    <div class="progress_inner">
                      <span
                        ><span class="label">VUE JS</span
                        ><span class="number">80%</span></span
                      >
                      <div class="background">
                        <div class="bar">
                          <div class="bar_in" style="width:80%"></div>
                        </div>
                      </div>
                    </div>
                    <!-- End progress_inner -->
                    <div class="progress_inner">
                      <span
                        ><span class="label">Node JS</span
                        ><span class="number">85%</span></span
                      >
                      <div class="background">
                        <div class="bar">
                          <div class="bar_in" style="width:85%"></div>
                        </div>
                      </div>
                    </div>
                    <!-- End progress_inner -->
                  </div>
                  <!-- End .tokyo_progress -->
                </div>
                <!-- End .left -->
                <div class="right">
                  <div class="tokyo_progress">
                    <div class="progress_inner">
                      <span
                        ><span class="label">Docker</span
                        ><span class="number">80%</span></span
                      >
                      <div class="background">
                        <div class="bar">
                          <div class="bar_in" style="width:80%"></div>
                        </div>
                      </div>
                    </div>
                    <div class="progress_inner">
                      <span
                        ><span class="label">AWS</span
                        ><span class="number">80%</span></span
                      >
                      <div class="background">
                        <div class="bar">
                          <div class="bar_in" style="width:80%"></div>
                        </div>
                      </div>
                    </div>
                    <div class="progress_inner">
                      <span
                        ><span class="label">Express JS</span
                        ><span class="number">85%</span></span
                      >
                      <div class="background">
                        <div class="bar">
                          <div class="bar_in" style="width:85%"></div>
                        </div>
                      </div>
                    </div>
                    <div class="progress_inner">
                      <span
                        ><span class="label">Mysql</span
                        ><span class="number">85%</span></span
                      >
                      <div class="background">
                        <div class="bar">
                          <div class="bar_in" style="width:85%"></div>
                        </div>
                      </div>
                    </div>
                    <div class="progress_inner">
                      <span
                        ><span class="label">Ruby on Rails</span
                        ><span class="number">75%</span></span
                      >
                      <div class="background">
                        <div class="bar">
                          <div class="bar_in" style="width:75%"></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- End .right -->
              </div>
            </div>
            <!-- End .tokyo_tm_modalbox_about -->
          </div>
        </div>
      </div>
    </transition>
    <!-- End Modalbox -->
  </div>
</template>

<script>
export default {
  components: {
  },
  data() {
    return {
      isActive: false,
      isVisible: false,
    };
  },
  methods: {
    showModal: function() {
      this.isActive = true;
      this.isVisible = true;
    },
    closeModal: function() {
      this.isActive = false;
      this.isVisible = false;
    },
  },
};
</script>

<style lang="scss"></style>
