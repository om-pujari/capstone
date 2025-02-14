// Compare Page JavaScript
document.addEventListener('DOMContentLoaded', () => {
    // Initialize comparison when bikes are selected
    document.getElementById('bike1').addEventListener('change', updateComparison);
    document.getElementById('bike2').addEventListener('change', updateComparison);
});

// Bike data (would typically come from an API)
const bikeData = {
    supersport: {
        name: 'SuperSport R',
        engine: '999cc',
        power: '205 HP',
        torque: '117 Nm',
        weight: '172 kg',
        seatHeight: '830 mm',
        price: '$15,999',
        features: ['Quick Shifter', 'Traction Control', 'Wheelie Control', 'Launch Control']
    },
    streetfighter: {
        name: 'Street Fighter V4',
        engine: '1103cc',
        power: '208 HP',
        torque: '123 Nm',
        weight: '178 kg',
        seatHeight: '845 mm',
        price: '$19,999',
        features: ['Quick Shifter', 'Traction Control', 'Wheelie Control', 'Slide Control']
    },
    adventure: {
        name: 'Adventure 1250',
        engine: '1250cc',
        power: '150 HP',
        torque: '128 Nm',
        weight: '249 kg',
        seatHeight: '875 mm',
        price: '$17,999',
        features: ['Cruise Control', 'Off-road ABS', 'Hill Hold Control', 'Electronic Suspension']
    },
    cruiser: {
        name: 'Cruiser Classic',
        engine: '1868cc',
        power: '155 HP',
        torque: '163 Nm',
        weight: '320 kg',
        seatHeight: '705 mm',
        price: '$18,999',
        features: ['Cruise Control', 'Traction Control', 'Hill Hold Control', 'Infotainment System']
    }
};

function updateComparison() {
    const bike1 = document.getElementById('bike1').value;
    const bike2 = document.getElementById('bike2').value;

    if (!bike1 || !bike2) return;

    const bike1Data = bikeData[bike1];
    const bike2Data = bikeData[bike2];

    // Update bike names
    document.getElementById('bike1Name').textContent = bike1Data.name;
    document.getElementById('bike2Name').textContent = bike2Data.name;

    // Update specifications
    document.getElementById('bike1Engine').textContent = bike1Data.engine;
    document.getElementById('bike2Engine').textContent = bike2Data.engine;
    
    document.getElementById('bike1Power').textContent = bike1Data.power;
    document.getElementById('bike2Power').textContent = bike2Data.power;
    
    document.getElementById('bike1Torque').textContent = bike1Data.torque;
    document.getElementById('bike2Torque').textContent = bike2Data.torque;
    
    document.getElementById('bike1Weight').textContent = bike1Data.weight;
    document.getElementById('bike2Weight').textContent = bike2Data.weight;
    
    document.getElementById('bike1SeatHeight').textContent = bike1Data.seatHeight;
    document.getElementById('bike2SeatHeight').textContent = bike2Data.seatHeight;
    
    document.getElementById('bike1Price').textContent = bike1Data.price;
    document.getElementById('bike2Price').textContent = bike2Data.price;

    // Update features comparison
    updateFeaturesComparison(bike1Data, bike2Data);
}

function updateFeaturesComparison(bike1Data, bike2Data) {
    const featuresGrid = document.querySelector('.features-grid');
    const allFeatures = [...new Set([...bike1Data.features, ...bike2Data.features])];

    featuresGrid.innerHTML = allFeatures.map(feature => `
        <div class="feature-item">
            <span>${feature}</span>
            <div class="feature-bikes">
                <span class="${bike1Data.features.includes(feature) ? 'has-feature' : 'no-feature'}">
                    ${bike1Data.features.includes(feature) ? '✓' : '✗'}
                </span>
                <span class="${bike2Data.features.includes(feature) ? 'has-feature' : 'no-feature'}">
                    ${bike2Data.features.includes(feature) ? '✓' : '✗'}
                </span>
            </div>
        </div>
    `).join('');
}