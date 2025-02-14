document.addEventListener('DOMContentLoaded', () => {
    initializeTabs();
    initialize360View();
});

// Initialize Tabs
function initializeTabs() {
    const tabs = document.querySelectorAll('.tab-btn');
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.dataset.tab;

            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            tab.classList.add('active');
            document.getElementById(target).classList.add('active');
        });
    });
}

// Initialize 360° View
function initialize360View() {
    const imageElement = document.getElementById('bike360Image');

    const images = Array.from({ length: 12 }, (_, i) => 
        `https://via.placeholder.com/500?text=View+${i * 30}°`
    );

    let currentAngle = 0;

    document.getElementById('rotateLeft').addEventListener('click', () => {
        currentAngle = (currentAngle - 30 + 360) % 360;
        updateView();
    });

    document.getElementById('rotateRight').addEventListener('click', () => {
        currentAngle = (currentAngle + 30) % 360;
        updateView();
    });

    document.getElementById('fullscreen').addEventListener('click', () => {
        const viewContainer = document.getElementById('bike360View');
        if (viewContainer.requestFullscreen) {
            viewContainer.requestFullscreen();
        }
    });

    function updateView() {
        const imageIndex = Math.floor(currentAngle / 30);
        imageElement.src = images[imageIndex];
        imageElement.alt = `Bike View ${currentAngle}°`;
    }

    updateView(); // Load initial view
}
