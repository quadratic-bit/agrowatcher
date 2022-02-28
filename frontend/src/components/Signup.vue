<template>
<div>
    <!-- Navigation -->
    <nav id="navbarExample" class="navbar navbar-expand-lg fixed-top navbar-light" aria-label="Main navigation">
      <div class="container">

        <!-- Image Logo -->
        <!-- <a class="navbar-brand logo-image" :href="/index/"><img src="@/assets/images/logo.svg" alt="alternative"></a>-->

        <!-- Text Logo -->
        <a class="navbar-brand logo-text" :href="/index/">Agrowatcher</a>

        <button class="navbar-toggler p-0 border-0" type="button" id="navbarSideCollapse"
                aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="navbar-collapse offcanvas-collapse" id="navbarsExampleDefault">
          <ul class="navbar-nav ms-auto navbar-nav-scroll">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" :href="/index#header/">Главная</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" :href="/index#features/">Возможности</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" :href="/index#details/">Подробнее</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" :href="/index#pricing/">Тарифы</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-bs-toggle="dropdown"
                 aria-expanded="false">Больше</a>
              <ul class="dropdown-menu" aria-labelledby="dropdown01">
                <li><a class="dropdown-item" :href="/terms/">Условия использования</a></li>
                <li>
                  <div class="dropdown-divider"></div>
                </li>
                <li><a class="dropdown-item" :href="/privacy/">Политика конфиденциальности</a></li>
              </ul>
            </li>
          </ul>
          <span class="nav-item">
                        <a class="btn-outline-sm" :href="/login/">Войти</a>
                    </span>
        </div> <!-- end of navbar-collapse -->
      </div> <!-- end of container -->
    </nav> <!-- end of navbar -->
    <!-- end of navigation -->

    <!-- Header -->
    <header class="ex-header">
      <div class="container">
        <div class="row">
          <div class="col-xl-10 offset-xl-1">
            <h1 class="text-center">Регистрация</h1>
          </div> <!-- end of col -->
        </div> <!-- end of row -->
      </div> <!-- end of container -->
    </header> <!-- end of ex-header -->
    <!-- end of header -->

    <!-- Basic -->
    <div class="ex-form-1 pt-5 pb-5">
      <div class="container">
        <div class="row">
          <div class="col-xl-6 offset-xl-3">
            <div class="text-box mt-5 mb-5">
              <p class="mb-4">Уже есть аккаунт? Перейти на страницу <a
                class="blue" :href="/login/">Входа</a></p>

              <!-- Sign Up Form -->
              <form :action="/index/" method="post">
                <div class="mb-4 form-floating">
                  <input required type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                  <label for="floatingInput">Email адрес</label>
                </div>
                <div class="mb-4 form-floating">
                  <input required type="text" class="form-control" id="floatingInput2" placeholder="Your name">
                  <label for="floatingInput">Ваше имя</label>
                </div>
                <div class="mb-4 form-floating">
                  <input required minlength="6" maxlength="128" type="password" class="form-control"
                         id="floatingPassword" placeholder="Password" v-on:input="updateStrength" aria-describedby="passStr">
                  <label for="floatingPassword">Пароль</label>
                  <small id="passStr" class="form-text text-muted">Этот пароль <span :class="strength">{{ strength }}</span></small>
                </div>
                <div class="mb-4 form-check">
                  <input required type="checkbox" class="form-check-input" id="exampleCheck1">
                  <label class="form-check-label" for="exampleCheck1">Я согласен с <a
                    :href="/privacy/">Политикой Конфиденциальности</a> и <a :href="/terms/">Условиями Использования</a></label>
                </div>
                <button type="submit" class="form-control-submit-button">Зарегистрироваться</button>
              </form>
              <!-- end of sign up form -->

            </div> <!-- end of text-box -->
          </div> <!-- end of col -->
        </div> <!-- end of row -->
      </div> <!-- end of container -->
    </div> <!-- end of ex-basic-1 -->
    <!-- end of basic -->

    <!-- Footer -->
    <div class="footer">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="footer-col first">
              <h6>О сайте</h6>
              <p class="p-small">Agrowatcher — приложение для точного земледелия, использующее лишь свободные данные со спутников.</p>
            </div> <!-- end of footer-col -->
            <div class="footer-col second">
              <h6>Ссылки</h6>
              <ul class="list-unstyled li-space-lg p-small">
                <li>Важное: <a :href="/terms/">Terms & Conditions</a>, <a :href="/privacy/">Privacy Policy</a>
                </li>
<!--                <li>Useful: <a href="#">Colorpicker</a>, <a href="#">Icon Library</a>, <a href="#">Illustrations</a>-->
<!--                </li>-->
                <li><a href='https://www.freepik.com/vectors/business'>Business vector created by pikisuperstar - www.freepik.com</a></li>
              </ul>
            </div> <!-- end of footer-col -->
            <div class="footer-col third">
                            <span class="fa-stack">
                                <a href="https://facebook.com">
                                    <i class="fas fa-circle fa-stack-2x"></i>
                                    <i class="fab fa-facebook-f fa-stack-1x"></i>
                                </a>
                            </span>
              <span class="fa-stack">
                                <a href="https://twitter.com">
                                    <i class="fas fa-circle fa-stack-2x"></i>
                                    <i class="fab fa-twitter fa-stack-1x"></i>
                                </a>
                            </span>
              <span class="fa-stack">
                                <a href="https://pinterest.com">
                                    <i class="fas fa-circle fa-stack-2x"></i>
                                    <i class="fab fa-pinterest-p fa-stack-1x"></i>
                                </a>
                            </span>
              <span class="fa-stack">
                                <a href="https://instagram.com">
                                    <i class="fas fa-circle fa-stack-2x"></i>
                                    <i class="fab fa-instagram fa-stack-1x"></i>
                                </a>
                            </span>
              <p class="p-small">Почта поддержки: <a href="mailto:example@example.com"><strong>example@example.com</strong></a>
              </p>
            </div> <!-- end of footer-col -->
          </div> <!-- end of col -->
        </div> <!-- end of row -->
      </div> <!-- end of container -->
    </div> <!-- end of footer -->
    <!-- end of footer -->

    <!-- Copyright -->
    <div class="copyright">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <p class="p-small">Copyright © <a href="#">Agrowatcher 2022</a></p>
          </div> <!-- end of col -->

          <div class="col-lg-6">
            <p class="p-small">Distributed By<a href="https://themewagon.com/" target="_blank"> Themewagon</a></p>
          </div> <!-- end of col -->
        </div> <!-- enf of row -->
      </div> <!-- end of container -->
    </div> <!-- end of copyright -->
    <!-- end of copyright -->

    <!-- Back To Top Button -->
    <button v-on:click="topFunction" id="myBtn">
      <img src="@/assets/images/up-arrow.png" alt="alternative">
    </button>
    <!-- end of back to top button -->
  </div>
</template>

<script>
import zxcvbn from 'zxcvbn'
import bootstrapValidate from 'bootstrap-validate'

export default {
  name: 'Signup',
  metaInfo () {
    return {
      title: 'Signup - Agrowatcher'
    }
  },
  data () {
    return {
      strength: 'ненадёжный'
    }
  },
  methods: {
    // When the user clicks on the button, scroll to the top of the document
    topFunction: function () {
      document.body.scrollTop = 0 // for Safari
      document.documentElement.scrollTop = 0 // for Chrome, Firefox, IE and Opera
    },
    updateStrength: function () {
      switch (zxcvbn(document.getElementById('floatingPassword').value).score) {
        case 0:
          this.strength = 'ненадёжный'
          break
        case 1:
          this.strength = 'ненадёжный'
          break
        case 2:
          this.strength = 'средний'
          break
        case 3:
          this.strength = 'надёжный'
          break
        case 4:
          this.strength = 'безопасный'
          break
        default:
          this.strength = 'ненадёжный'
      }
    }
  },
  mounted () {
    // Validation
    bootstrapValidate('#floatingInput', 'email:Введите валидный почтовый адрес')
    bootstrapValidate('#floatingPassword', 'min:6:Пароль должен быть не короче 6 символов')

    /* Navigation */
    // Collapse the navbar by adding the top-nav-collapse class
    window.onscroll = function () {
      scrollFunction()
      scrollFunctionBTT() // back to top button
    }

    window.onload = function () {
      scrollFunction()
    }

    function scrollFunction () {
      if (document.documentElement.scrollTop > 30) {
        document.getElementById('navbarExample').classList.add('top-nav-collapse')
      } else if (document.documentElement.scrollTop < 30) {
        document.getElementById('navbarExample').classList.remove('top-nav-collapse')
      }
    }

    // Navbar on mobile
    let elements = document.querySelectorAll('.nav-link:not(.dropdown-toggle)')

    for (let i = 0; i < elements.length; i++) {
      elements[i].addEventListener('click', () => {
        document.querySelector('.offcanvas-collapse').classList.toggle('open')
      })
    }

    let el = document.querySelector('.navbar-toggler')
    if (el != null) {
      el.addEventListener('click', () => {
        document.querySelector('.offcanvas-collapse').classList.toggle('open')
      })
    }

    // Hover on desktop
    function toggleDropdown (e) {
      const _d = e.target.closest('.dropdown')
      let _m = document.querySelector('.dropdown-menu', _d)

      setTimeout(
        function () {
          const shouldOpen = _d.matches(':hover')
          _m.classList.toggle('show', shouldOpen)
          _d.classList.toggle('show', shouldOpen)

          _d.setAttribute('aria-expanded', shouldOpen)
        },
        e.type === 'mouseleave' ? 300 : 0
      )
    }

    // On hover
    const dropdownCheck = document.querySelector('.dropdown')

    if (dropdownCheck !== null) {
      document.querySelector('.dropdown').addEventListener('mouseleave', toggleDropdown)
      document.querySelector('.dropdown').addEventListener('mouseover', toggleDropdown)

      // On click
      document.querySelector('.dropdown').addEventListener('click', (e) => {
        const _d = e.target.closest('.dropdown')
        let _m = document.querySelector('.dropdown-menu', _d)
        if (_d.classList.contains('show')) {
          _m.classList.remove('show')
          _d.classList.remove('show')
        } else {
          _m.classList.add('show')
          _d.classList.add('show')
        }
      })
    }

    /* Back To Top Button */
    // Get the button
    let myButton = document.getElementById('myBtn')

    // When the user scrolls down 20px from the top of the document, show the button
    function scrollFunctionBTT () {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        myButton.style.display = 'block'
      } else {
        myButton.style.display = 'none'
      }
    }
  }
}
</script>

<style scoped>
.weak {
  color: red;
  font-weight: bold;
}
.medium {
  color: orangered;
  font-weight: bold;
}
.great {
  color: darkgreen;
  font-weight: bold;
}
.secure {
  color: mediumslateblue;
  font-weight: bold;
}
</style>
