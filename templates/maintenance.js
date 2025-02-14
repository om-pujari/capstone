// Maintenance Modal JavaScript
document.addEventListener('DOMContentLoaded', () => {
    initializeMaintenanceForm();
});

function bookService(type) {
    const modal = document.getElementById('maintenanceModal');
    const serviceTypeSelect = document.getElementById('serviceType');
    
    serviceTypeSelect.value = type;
    modal.style.display = 'block';

    const closeBtn = modal.querySelector('.close');
    closeBtn.onclick = () => modal.style.display = 'none';

    window.onclick = (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };
}

function initializeMaintenanceForm() {
    const form = document.getElementById('maintenanceForm');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = {
            bikeModel: document.getElementById('bikeModel').value,
            serviceType: document.getElementById('serviceType').value,
            serviceDate: document.getElementById('serviceDate').value,
            serviceTime: document.getElementById('serviceTime').value,
            issues: document.getElementById('issues').value
        };

        try {
            // Simulate backend submission
            alert(`Service for ${formData.bikeModel} scheduled successfully!`);
            document.getElementById('maintenanceModal').style.display = 'none';
            form.reset();
        } catch (error) {
            console.error('Failed to schedule maintenance:', error);
            alert('Failed to schedule maintenance. Please try again.');
        }
    });

    // Set minimum date to tomorrow
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    document.getElementById('serviceDate').min = tomorrow.toISOString().split('T')[0];
}
