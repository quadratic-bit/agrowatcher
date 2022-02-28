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
              <a class="nav-link active" aria-current="page" href="#header">Главная</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#features">Возможности</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#details">Подробнее</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#pricing">Тарифы</a>
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
    <header id="header" class="header">
      <div class="container">
        <div class="row">
          <div class="col-lg-7">
            <div class="text-container">
              <h1 class="h1-large">#1 приложение для <span class="replace-me">фермеров, агропредприятий</span>
              </h1>
              <p class="p-large">Исследуйте область точного земледелия вместе с нами</p>
              <a class="btn-solid-lg" :href="/signup/">Присоединиться</a>
            </div> <!-- end of text-container -->
          </div> <!-- end of col -->
          <div class="col-lg-5">
            <div class="image-container">
              <img class="img-fluid" src="@/assets/images/farmers.svg" alt="alternative">
            </div> <!-- end of image-container -->
          </div> <!-- end of col -->
        </div> <!-- end of row -->
      </div> <!-- end of container -->
    </header> <!-- end of header -->
    <!-- end of header -->

    <!-- Features -->
    <div id="features" class="cards-1">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <h2 class="h2-heading">Приложение Agrowatcher обладает <span>удивительными</span> возможностями</h2>
          </div> <!-- end of col -->
        </div> <!-- end of row -->
        <div class="row">
          <div class="col-lg-12">

            <!-- Card -->
            <div class="card">
              <div class="card-icon">
                <span class="fas fa-satellite"></span>
              </div>
              <div class="card-body">
                <h4 class="card-title">Агроскаутинг</h4>
                <p>Наблюдайте за полями онлайн</p>
              </div>
            </div>
            <!-- end of card -->

            <!-- Card -->
            <div class="card">
              <div class="card-icon green">
                <span class="fas fa-leaf"></span>
              </div>
              <div class="card-body">
                <h4 class="card-title">Индекс NDVI</h4>
                <p>Выявляйте проблемные участки</p>
              </div>
            </div>
            <!-- end of card -->

            <!-- Card -->
            <div class="card">
              <div class="card-icon blue">
                <span class="fas fa-cloud-sun"></span>
              </div>
              <div class="card-body">
                <h4 class="card-title">Время полива</h4>
                <p>Узнавайте точный прогноз погоды</p>
              </div>
            </div>
            <!-- end of card -->

          </div> <!-- end of col -->
        </div> <!-- end of row -->
      </div> <!-- end of container -->
    </div> <!-- end of cards-1 -->
    <!-- end of services -->

    <!-- Details 1 -->
    <div id="details" class="basic-1 bg-gray">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 col-xl-5">
            <div class="text-container">
              <h2>Следите за посевами при помощи веб-приложения</h2>
              <p>Спутниковые снимки подскажут, в каком состоянии находится каждый участок поля</p>
              <a class="btn-solid-reg" data-bs-toggle="modal" data-bs-target="#staticBackdrop">Присоединиться</a>
            </div> <!-- end of text-container -->
          </div> <!-- end of col -->
          <div class="col-lg-6 col-xl-7">
            <div class="image-container">
              <img class="img-fluid" src="@/assets/images/details-1.svg" alt="alternative">
            </div> <!-- end of image-container -->
          </div> <!-- end of col -->
        </div> <!-- end of row -->
      </div> <!-- end of container -->
    </div> <!-- end of basic-1 -->
    <!-- end of details 1 -->

<!--    &lt;!&ndash; Details Modal &ndash;&gt;-->
<!--    <div id="staticBackdrop" class="modal fade" tabindex="-1" aria-hidden="true">-->
<!--      <div class="modal-dialog">-->
<!--        <div class="modal-content">-->
<!--          <div class="row">-->
<!--            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>-->
<!--            <div class="col-lg-8">-->
<!--              <div class="image-container">-->
<!--                <img class="img-fluid" src="@/assets/images/details-modal.jpg" alt="alternative">-->
<!--              </div> &lt;!&ndash; end of image-container &ndash;&gt;-->
<!--            </div> &lt;!&ndash; end of col &ndash;&gt;-->
<!--            <div class="col-lg-4">-->
<!--              <h3>Goals Setting</h3>-->
<!--              <hr>-->
<!--              <p>In gravida at nunc sodales pretium. Vivamus semper, odio vitae mattis auctor, elit elit semper magna ac-->
<!--                tum nico vela spider</p>-->
<!--              <h4>User Feedback</h4>-->
<!--              <p>Sapien vitae eros. Praesent ut erat a tellus posuere nisi more thico cursus pharetra finibus posuere-->
<!--                nisi. Vivamus feugiat</p>-->
<!--              <ul class="list-unstyled li-space-lg">-->
<!--                <li class="d-flex">-->
<!--                  <i class="fas fa-chevron-right"></i>-->
<!--                  <div class="flex-grow-1">Tincidunt sem vel brita bet mala</div>-->
<!--                </li>-->
<!--                <li class="d-flex">-->
<!--                  <i class="fas fa-chevron-right"></i>-->
<!--                  <div class="flex-grow-1">Sapien condimentum sacoz sil necr</div>-->
<!--                </li>-->
<!--                <li class="d-flex">-->
<!--                  <i class="fas fa-chevron-right"></i>-->
<!--                  <div class="flex-grow-1">Fusce interdum nec ravon fro urna</div>-->
<!--                </li>-->
<!--                <li class="d-flex">-->
<!--                  <i class="fas fa-chevron-right"></i>-->
<!--                  <div class="flex-grow-1">Integer pulvinar biolot bat tortor</div>-->
<!--                </li>-->
<!--                <li class="d-flex">-->
<!--                  <i class="fas fa-chevron-right"></i>-->
<!--                  <div class="flex-grow-1">Id ultricies fringilla fangor raq trinit</div>-->
<!--                </li>-->
<!--              </ul>-->
<!--              <a id="modalCtaBtn" class="btn-solid-reg" href="#your-link">Details</a>-->
<!--              <button type="button" class="btn-outline-reg" data-bs-dismiss="modal">Close</button>-->
<!--            </div> &lt;!&ndash; end of col &ndash;&gt;-->
<!--          </div> &lt;!&ndash; end of row &ndash;&gt;-->
<!--        </div> &lt;!&ndash; end of modal-content &ndash;&gt;-->
<!--      </div> &lt;!&ndash; end of modal-dialog &ndash;&gt;-->
<!--    </div> &lt;!&ndash; end of modal &ndash;&gt;-->
<!--    &lt;!&ndash; end of details modal &ndash;&gt;-->

    <!-- Details 2 -->
    <div class="basic-2">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <div class="image-container">
              <img class="img-fluid" src="@/assets/images/details-2.png" alt="alternative">
            </div> <!-- end of image-container -->
          </div> <!-- end of col -->
          <div class="col-lg-6">
            <div class="text-container">
              <h2>Любой может начать пользоваться сервисом</h2>
              <p>Agrowatcher подойдёт для фермеров, не имеющих навыков работы с комплексными системами, а интуитивный интерфейс не даст Вам заблудиться</p>
            </div> <!-- end of text-container -->
          </div> <!-- end of col -->
        </div> <!-- end of row -->
      </div> <!-- end of container -->
    </div> <!-- end of basic-2 -->
    <!-- end of details 2 -->

<!--    &lt;!&ndash; Testimonials &ndash;&gt;-->
<!--    <div class="slider-1 bg-gray">-->
<!--      <div class="container">-->
<!--        <div class="row">-->
<!--          <div class="col-lg-12">-->
<!--            <h2 class="h2-heading">Few words from our clients</h2>-->
<!--          </div> &lt;!&ndash; end of col &ndash;&gt;-->
<!--        </div> &lt;!&ndash; end of row &ndash;&gt;-->
<!--        <div class="row">-->
<!--          <div class="col-lg-12">-->

<!--            &lt;!&ndash; Card Slider &ndash;&gt;-->
<!--            <div class="slider-container">-->
<!--              <div class="swiper-container card-slider">-->
<!--                <div class="swiper-wrapper">-->

<!--                  &lt;!&ndash; Slide &ndash;&gt;-->
<!--                  <div class="swiper-slide">-->
<!--                    <div class="card">-->
<!--                      <img class="card-image" src="@/assets/images/testimonial-1.jpg" alt="alternative">-->
<!--                      <div class="card-body">-->
<!--                        <p class="testimonial-text">Tortor sodales eget. Vivamus imperdiet leo eu risus tincidunt uris.-->
<!--                          Proin placerat, urna hendrerit placerat erase convallis</p>-->
<!--                        <p class="testimonial-author">Jude Thorn - Designer</p>-->
<!--                      </div>-->
<!--                    </div>-->
<!--                  </div> &lt;!&ndash; end of swiper-slide &ndash;&gt;-->
<!--                  &lt;!&ndash; end of slide &ndash;&gt;-->

<!--                  &lt;!&ndash; Slide &ndash;&gt;-->
<!--                  <div class="swiper-slide">-->
<!--                    <div class="card">-->
<!--                      <img class="card-image" src="@/assets/images/testimonial-2.jpg" alt="alternative">-->
<!--                      <div class="card-body">-->
<!--                        <p class="testimonial-text">Eros volutpat ante mauris euismod sem, ut varius nisi lectus in-->
<!--                          urna. Integer luctus, nunc eget maximus intem, orci risus</p>-->
<!--                        <p class="testimonial-author">Roy Smith - Developer</p>-->
<!--                      </div>-->
<!--                    </div>-->
<!--                  </div> &lt;!&ndash; end of swiper-slide &ndash;&gt;-->
<!--                  &lt;!&ndash; end of slide &ndash;&gt;-->

<!--                  &lt;!&ndash; Slide &ndash;&gt;-->
<!--                  <div class="swiper-slide">-->
<!--                    <div class="card">-->
<!--                      <img class="card-image" src="@/assets/images/testimonial-3.jpg" alt="alternative">-->
<!--                      <div class="card-body">-->
<!--                        <p class="testimonial-text">Sed congue ex quam, sit amet venenatis dolor lacinia vulputate. Nunc-->
<!--                          pulvinar ex ex, sit amet scelerisque tellus pretium semper</p>-->
<!--                        <p class="testimonial-author">Marsha Singer - Marketer</p>-->
<!--                      </div>-->
<!--                    </div>-->
<!--                  </div> &lt;!&ndash; end of swiper-slide &ndash;&gt;-->
<!--                  &lt;!&ndash; end of slide &ndash;&gt;-->

<!--                  &lt;!&ndash; Slide &ndash;&gt;-->
<!--                  <div class="swiper-slide">-->
<!--                    <div class="card">-->
<!--                      <img class="card-image" src="@/assets/images/testimonial-4.jpg" alt="alternative">-->
<!--                      <div class="card-body">-->
<!--                        <p class="testimonial-text">Etiam est lorem, interdum non semper ut, bibendum vitae ante.-->
<!--                          Pellente sollicitun sagittis lectus. Aenean in comod</p>-->
<!--                        <p class="testimonial-author">Tim Shaw - Designer</p>-->
<!--                      </div>-->
<!--                    </div>-->
<!--                  </div> &lt;!&ndash; end of swiper-slide &ndash;&gt;-->
<!--                  &lt;!&ndash; end of slide &ndash;&gt;-->

<!--                  &lt;!&ndash; Slide &ndash;&gt;-->
<!--                  <div class="swiper-slide">-->
<!--                    <div class="card">-->
<!--                      <img class="card-image" src="@/assets/images/testimonial-5.jpg" alt="alternative">-->
<!--                      <div class="card-body">-->
<!--                        <p class="testimonial-text">Quisque nec turpis placerat, accumsan lorem lobortis, vestibulum-->
<!--                          elit. Fusce finibus nisl varius semper elementum vivamus</p>-->
<!--                        <p class="testimonial-author">Lindsay Spice - Marketer</p>-->
<!--                      </div>-->
<!--                    </div>-->
<!--                  </div> &lt;!&ndash; end of swiper-slide &ndash;&gt;-->
<!--                  &lt;!&ndash; end of slide &ndash;&gt;-->

<!--                  &lt;!&ndash; Slide &ndash;&gt;-->
<!--                  <div class="swiper-slide">-->
<!--                    <div class="card">-->
<!--                      <img class="card-image" src="@/assets/images/testimonial-6.jpg" alt="alternative">-->
<!--                      <div class="card-body">-->
<!--                        <p class="testimonial-text">Vulputate sed tellus nec, imperdiet luctus purus. Morbi lobortis-->
<!--                          massa a mi interdum condimentum. Integer non gravida nisi</p>-->
<!--                        <p class="testimonial-author">Ann Blake - Developer</p>-->
<!--                      </div>-->
<!--                    </div>-->
<!--                  </div> &lt;!&ndash; end of swiper-slide &ndash;&gt;-->
<!--                  &lt;!&ndash; end of slide &ndash;&gt;-->

<!--                </div> &lt;!&ndash; end of swiper-wrapper &ndash;&gt;-->

<!--                &lt;!&ndash; Add Arrows &ndash;&gt;-->
<!--                <div class="swiper-button-next"></div>-->
<!--                <div class="swiper-button-prev"></div>-->
<!--                &lt;!&ndash; end of add arrows &ndash;&gt;-->

<!--              </div> &lt;!&ndash; end of swiper-container &ndash;&gt;-->
<!--            </div> &lt;!&ndash; end of slider-container &ndash;&gt;-->
<!--            &lt;!&ndash; end of card slider &ndash;&gt;-->

<!--          </div> &lt;!&ndash; end of col &ndash;&gt;-->
<!--        </div> &lt;!&ndash; end of row &ndash;&gt;-->
<!--      </div> &lt;!&ndash; end of container &ndash;&gt;-->
<!--    </div> &lt;!&ndash; end of slider-1 &ndash;&gt;-->
<!--    &lt;!&ndash; end of testimonials &ndash;&gt;-->

    <!-- Invitation -->
    <div class="basic-3">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <h4>Agrowatcher изменит Ваше предствление о земледелии</h4>
            <a class="btn-outline-lg page-scroll" :href="/signup/">Присоединиться</a>
          </div> <!-- end of col -->
        </div> <!-- end of row -->
      </div> <!-- end of container -->
    </div> <!-- end of basic-3 -->
    <!-- end of invitation -->

<!--    &lt;!&ndash; Pricing &ndash;&gt;-->
<!--    <div id="pricing" class="cards-2 bg-gray">-->
<!--      <div class="container">-->
<!--        <div class="row">-->
<!--          <div class="col-lg-12">-->
<!--            <h2 class="h2-heading">Free forever tier and 2 pro plans</h2>-->
<!--          </div> &lt;!&ndash; end of col &ndash;&gt;-->
<!--        </div> &lt;!&ndash; end of row &ndash;&gt;-->
<!--        <div class="row">-->
<!--          <div class="col-lg-12">-->

<!--            &lt;!&ndash; Card &ndash;&gt;-->
<!--            <div class="card">-->
<!--              <div class="card-body">-->
<!--                <div class="card-title">-->
<!--                  <img class="decoration-lines" src="@/assets/images/decoration-lines.svg"-->
<!--                       alt="alternative"><span>Free tier</span><img class="decoration-lines flipped"-->
<!--                                                                    src="@/assets/images/decoration-lines.svg"-->
<!--                                                                    alt="alternative">-->
<!--                </div>-->
<!--                <ul class="list-unstyled li-space-lg">-->
<!--                  <li>Fusce pulvinar eu mi acm</li>-->
<!--                  <li>Curabitur consequat nisl bro</li>-->
<!--                  <li>Reget facilisis molestie</li>-->
<!--                  <li>Vivamus vitae sem in tortor</li>-->
<!--                  <li>Pharetra vehicula ornares</li>-->
<!--                  <li>Vivamus dignissim sit amet</li>-->
<!--                  <li>Ut convallis aliquama set</li>-->
<!--                </ul>-->
<!--                <div class="price">Free</div>-->
<!--                <a :href="/signup/" class="btn-solid-reg">Sign up</a>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; end of card &ndash;&gt;-->

<!--            &lt;!&ndash; Card &ndash;&gt;-->
<!--            <div class="card">-->
<!--              <div class="card-body">-->
<!--                <div class="card-title">-->
<!--                  <img class="decoration-lines" src="@/assets/images/decoration-lines.svg"-->
<!--                       alt="alternative"><span>Advanced</span><img class="decoration-lines flipped"-->
<!--                                                                   src="@/assets/images/decoration-lines.svg"-->
<!--                                                                   alt="alternative">-->
<!--                </div>-->
<!--                <ul class="list-unstyled li-space-lg">-->
<!--                  <li>Nunc commodo magna quis</li>-->
<!--                  <li>Lacus fermentum tincidunt</li>-->
<!--                  <li>Nullam lobortis porta diam</li>-->
<!--                  <li>Announcing of invita mro</li>-->
<!--                  <li>Dictum metus placerat luctus</li>-->
<!--                  <li>Sed laoreet blandit mollis</li>-->
<!--                  <li>Mauris non luctus est</li>-->
<!--                </ul>-->
<!--                <div class="price">$19<span>/month</span></div>-->
<!--                <a :href="/signup/" class="btn-solid-reg">Sign up</a>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; end of card &ndash;&gt;-->

<!--            &lt;!&ndash; Card &ndash;&gt;-->
<!--            <div class="card">-->
<!--              <div class="card-body">-->
<!--                <div class="card-title">-->
<!--                  <img class="decoration-lines" src="@/assets/images/decoration-lines.svg"-->
<!--                       alt="alternative"><span>Professional</span><img class="decoration-lines flipped"-->
<!--                                                                       src="@/assets/images/decoration-lines.svg"-->
<!--                                                                       alt="alternative">-->
<!--                </div>-->
<!--                <ul class="list-unstyled li-space-lg">-->
<!--                  <li>Quisque rutrum mattis</li>-->
<!--                  <li>Quisque tristique cursus lacus</li>-->
<!--                  <li>Interdum sollicitudin maec</li>-->
<!--                  <li>Quam posuerei pellentesque</li>-->
<!--                  <li>Est neco gravida turpis integer</li>-->
<!--                  <li>Mollis felis. Integer id quam</li>-->
<!--                  <li>Id tellus hendrerit lacinia</li>-->
<!--                </ul>-->
<!--                <div class="price">$29<span>/month</span></div>-->
<!--                <a :href="/signup/" class="btn-solid-reg">Sign up</a>-->
<!--              </div>-->
<!--            </div>-->
<!--            &lt;!&ndash; end of card &ndash;&gt;-->

<!--          </div> &lt;!&ndash; end of col &ndash;&gt;-->
<!--        </div> &lt;!&ndash; end of row &ndash;&gt;-->
<!--      </div> &lt;!&ndash; end of container &ndash;&gt;-->
<!--    </div> &lt;!&ndash; end of cards-2 &ndash;&gt;-->
<!--    &lt;!&ndash; end of pricing &ndash;&gt;-->

    <!-- Questions -->
    <div class="accordion-1">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <h2 class="h2-heading">Часто задаваемые вопросы</h2>
          </div> <!-- end of col -->
        </div> <!-- end of row -->
        <div class="row">
          <div class="col-lg-12">
            <div class="accordion" id="accordionExample">

              <!-- Accordion Item -->
              <div class="accordion-item">
                <h2 class="accordion-header" id="headingOne">
                  <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne"
                          aria-expanded="true" aria-controls="collapseOne">Что такое точное земледелие?
                  </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                     data-bs-parent="#accordionExample">
                  <div class="accordion-body">Точное земледелие — принцип гибкого управления технологиями выращивания сельскохозяйственных культур и ресурсами агропредприятия для получения максимального урожая наилучшего качества. Источник: smartagro.ru
                  </div>
                </div>
              </div>
              <!-- end of accordion-item -->

<!--              &lt;!&ndash; Accordion Item &ndash;&gt;-->
<!--              <div class="accordion-item">-->
<!--                <h2 class="accordion-header" id="headingTwo">-->
<!--                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"-->
<!--                          data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">Is the Free-->
<!--                    Tier available for unlimited time or it will end more words after a while?-->
<!--                  </button>-->
<!--                </h2>-->
<!--                <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo"-->
<!--                     data-bs-parent="#accordionExample">-->
<!--                  <div class="accordion-body">Mauris faucibus placerat nisl. Sed eros odio, posuere at felis quis,-->
<!--                    tincidunt facilisis nibh. Nulla in ante sem. Nam aliquam urna nisi, cursus semper dolor convallis-->
<!--                    at. Duis vulputate est in consectetur, et condimentum elit tincidunt libero consectetur, et-->
<!--                    condimentum suis vulputate est in libero-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--              &lt;!&ndash; end of accordion-item &ndash;&gt;-->

<!--              &lt;!&ndash; Accordion Item &ndash;&gt;-->
<!--              <div class="accordion-item">-->
<!--                <h2 class="accordion-header" id="headingThree">-->
<!--                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"-->
<!--                          data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">Can I use-->
<!--                    the app on mobile devices or it’s limited more words to desktop use?-->
<!--                  </button>-->
<!--                </h2>-->
<!--                <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree"-->
<!--                     data-bs-parent="#accordionExample">-->
<!--                  <div class="accordion-body">Nullam at diam at mi facilisis consectetur at non turpis. Proin a felis-->
<!--                    nisi. Sed at orci rutrum, tincidunt magna vel, pharetra libero. Proin mauris orci, faucibus eget-->
<!--                    malesuada vel, consectetur, et condimentum elit tincidunt pellentesque vitae ligula. Pellentesque-->
<!--                    euismod tincidun-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--              &lt;!&ndash; end of accordion-item &ndash;&gt;-->

            </div> <!-- end of accordion -->
          </div> <!-- end of col -->
        </div> <!-- end of row -->
      </div> <!-- end of container -->
    </div> <!-- end of accordion-1 -->
    <!-- end of questions -->

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
import '@/assets/scripts/bootstrap.min.js'
import '@/assets/scripts/replaceme.min.js'
import Swiper from 'swiper'

export default {
  name: 'Home',
  metaInfo () {
    return {
      title: 'Главная - Agrowatcher'
    }
  },
  methods: {
    // When the user clicks on the button, scroll to the top of the document
    topFunction: function () {
      document.body.scrollTop = 0 // for Safari
      document.documentElement.scrollTop = 0 // for Chrome, Firefox, IE and Opera
    }
  },
  mounted () {
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

    /* Rotating Text - Word Cycle */
    let checkReplace = document.querySelector('.replace-me')
    if (checkReplace !== null) {
      // eslint-disable-next-line
      let replace = new ReplaceMe(document.querySelector('.replace-me'), {
        animation: 'animated fadeIn', // Animation class or classes
        speed: 2000, // Delay between each phrase in milliseconds
        separator: ',', // Phrases separator
        hoverStop: false, // Stop rotator on phrase hover
        clickChange: false, // Change phrase on click
        loopCount: 'infinite', // Loop Count - 'infinite' or number
        autoRun: true, // Run rotator automatically
        onInit: false, // Function
        onChange: false, // Function
        onComplete: false // Function
      })
    }

    /* Card Slider - Swiper */
    // eslint-disable-next-line
    let cardSlider = new Swiper('.card-slider', {
      autoplay: {
        delay: 4000,
        disableOnInteraction: false
      },
      loop: true,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
      },
      slidesPerView: 3,
      spaceBetween: 70,
      breakpoints: {
        // when window is <= 767px
        767: {
          slidesPerView: 1
        },
        // when window is <= 991px
        991: {
          slidesPerView: 2,
          spaceBetween: 40
        }
      }
    })

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

</style>
