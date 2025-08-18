document.addEventListener('DOMContentLoaded', function() {

    // Lógica para el menú de hamburguesa
    const hamburgerButton = document.getElementById('hamburger-button');
    const mobileMenu = document.getElementById('mobile-menu');
    if (hamburgerButton && mobileMenu) {
        hamburgerButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Lógica para el slideshow principal (hero)
    const slideshow = document.getElementById('hero-slideshow');
    if (slideshow) {
        const slides = slideshow.querySelectorAll('.slide');
        const prevButton = document.getElementById('prev-slide-button');
        const nextButton = document.getElementById('next-slide-button');
        
        if (slides.length > 0) {
            let currentSlide = 0;
            const intervalTime = 5000;
            let slideInterval;

            function showSlide(index) {
                slides[currentSlide].classList.remove('active');
                currentSlide = index;
                slides[currentSlide].classList.add('active');
            }

            function nextSlide() {
                const newIndex = (currentSlide + 1) % slides.length;
                showSlide(newIndex);
            }

            function prevSlide() {
                const newIndex = (currentSlide - 1 + slides.length) % slides.length;
                showSlide(newIndex);
            }
            
            function startSlideShow() {
                slideInterval = setInterval(nextSlide, intervalTime);
            }

            function resetSlideShow() {
                clearInterval(slideInterval);
                startSlideShow();
            }

            if (nextButton && prevButton) {
                nextButton.addEventListener('click', () => {
                    nextSlide();
                    resetSlideShow(); 
                });

                prevButton.addEventListener('click', () => {
                    prevSlide();
                    resetSlideShow(); 
                });
            }
            
            startSlideShow();
        }
    }

    // Animación para el título de secciones
    const animatedTitle = document.querySelector('#featured-title');
    if (animatedTitle) { 
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('in-view');
                } else {
                    entry.target.classList.remove('in-view');
                }
            });
        }, {
            threshold: 0.5
        });
        observer.observe(animatedTitle);
    }
    
    // Inicialización del carrusel Swiper (para categorías o productos relacionados)
    const swiperContainer = document.querySelector(".mySwiper");
    if (swiperContainer) {
        const loopEnabled = swiperContainer.dataset.loopEnabled === 'true';

        new Swiper(".mySwiper", {
            slidesPerView: 2,
            spaceBetween: 20,
            loop: loopEnabled, 
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            breakpoints: {
                640: { slidesPerView: 4, spaceBetween: 24 },
                768: { slidesPerView: 4, spaceBetween: 24 },
                1024: { slidesPerView: 4, spaceBetween: 24 },
            },
        });
    }
});