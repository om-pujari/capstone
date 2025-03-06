// Slideshow functionality
let currentSlide = 0;
const slides = [
    {
        image: 'https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1200',
        title: '2024 SuperSport R',
        description: 'Experience pure adrenaline with 200HP of raw power'
    },
    {
        image: 'https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=1200',
        title: 'Street Fighter V4',
        description: 'The ultimate naked bike for urban adventures'
    },
    {
        image: 'https://images.unsplash.com/photo-1615172282427-9a57ef2d142e?auto=format&fit=crop&w=1200',
        title: 'Adventure 1250',
        description: 'Conquer any terrain with confidence'
    }
];

function createSlideHTML(slide) {
    return `
        <div class="slide">
            <img src="${slide.image}" alt="${slide.title}">
            <div class="slide-content">
                <h2>${slide.title}</h2>
                <p>${slide.description}</p>
                <a href="/bikes/${slide.title.toLowerCase().replace(/\s+/g, '-')}.html" class="cta-button">Explore Now</a>
            </div>
        </div>
    `;
}

function initSlideshow() {
    const sliderContainer = document.querySelector('.hero-slider');
    sliderContainer.innerHTML = slides.map(createSlideHTML).join('');
    const allSlides = document.querySelectorAll('.slide');
    allSlides[0].classList.add('active');

    // Add navigation buttons
    const navHTML = `
        <button class="slide-nav prev">❮</button>
        <button class="slide-nav next">❯</button>
        <div class="slide-dots"></div>
    `;
    sliderContainer.insertAdjacentHTML('beforeend', navHTML);

    // Add dots
    const dotsContainer = document.querySelector('.slide-dots');
    slides.forEach((_, index) => {
        const dot = document.createElement('button');
        dot.classList.add('slide-dot');
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });

    // Add navigation click handlers
    document.querySelector('.prev').addEventListener('click', prevSlide);
    document.querySelector('.next').addEventListener('click', nextSlide);

    // Start automatic slideshow
    setInterval(nextSlide, 5000);
}

function goToSlide(index) {
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.slide-dot');
    
    slides[currentSlide].classList.remove('active');
    dots[currentSlide].classList.remove('active');
    
    currentSlide = index;
    
    slides[currentSlide].classList.add('active');
    dots[currentSlide].classList.add('active');
}

function nextSlide() {
    const nextIndex = (currentSlide + 1) % slides.length;
    goToSlide(nextIndex);
}

function prevSlide() {
    const prevIndex = (currentSlide - 1 + slides.length) % slides.length;
    goToSlide(prevIndex);
}

// Initialize when DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
    initSlideshow();
});
