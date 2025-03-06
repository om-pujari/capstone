// Array of maintenance tips
const maintenanceTips = [
    {
        title: "Battery Care",
        content: "Keep your e-bike battery between 20% and 80% charge for optimal longevity. Avoid extreme temperatures.",
        category: "battery"
    },
    {
        title: "Tire Pressure",
        content: "Check your tire pressure weekly. Proper inflation improves range and handling while preventing flats.",
        category: "tires"
    },
    {
        title: "Chain Maintenance",
        content: "Clean and lubricate your chain every 200-300 km for smooth operation and extended component life.",
        category: "drivetrain"
    },
    {
        title: "Brake Check",
        content: "Inspect brake pads monthly for wear. Listen for unusual sounds and ensure consistent brake response.",
        category: "brakes"
    },
    {
        title: "Weather Protection",
        content: "Store your e-bike in a dry place and wipe it down after riding in wet conditions to prevent corrosion.",
        category: "general"
    },
    {
        title: "Display Care",
        content: "Keep the display clean and protected from direct sunlight when parked to prevent damage.",
        category: "electronics"
    },
    {
        title: "Regular Inspection",
        content: "Perform a quick pre-ride check of brakes, lights, and tire pressure before each journey.",
        category: "safety"
    },
    {
        title: "Motor Care",
        content: "Keep the motor clean and free from debris. Avoid high-pressure water near the motor housing.",
        category: "motor"
    }
];

class MaintenanceTipManager {
    constructor() {
        this.createPopupElement();
        this.currentTipIndex = 0;
        this.tipInterval = null;
        this.isVisible = false;
    }

    createPopupElement() {
        const popup = document.createElement('div');
        popup.className = 'maintenance-tip-popup';
        popup.innerHTML = `
            <div class="tip-header">
                <h5></h5>
                <button class="close-tip">&times;</button>
            </div>
            <div class="tip-content"></div>
        `;
        document.body.appendChild(popup);
        
        this.popup = popup;
        this.titleElement = popup.querySelector('h5');
        this.contentElement = popup.querySelector('.tip-content');
        
        // Setup close button
        popup.querySelector('.close-tip').addEventListener('click', () => this.hideTip());
    }

    showTip() {
        if (this.isVisible) return;
        
        const tip = maintenanceTips[this.currentTipIndex];
        this.titleElement.textContent = tip.title;
        this.contentElement.textContent = tip.content;
        
        this.popup.classList.add('show');
        this.isVisible = true;
        
        // Auto hide after 5 seconds
        setTimeout(() => this.hideTip(), 5000);
        
        // Move to next tip
        this.currentTipIndex = (this.currentTipIndex + 1) % maintenanceTips.length;
    }

    hideTip() {
        this.popup.classList.remove('show');
        this.isVisible = false;
    }

    startTips(interval = 30000) { // Default: show a tip every 30 seconds
        if (this.tipInterval) return;
        
        // Show first tip after 5 seconds
        setTimeout(() => this.showTip(), 5000);
        
        // Setup interval for subsequent tips
        this.tipInterval = setInterval(() => {
            if (!document.hidden) { // Only show tips when page is visible
                this.showTip();
            }
        }, interval);
    }

    stopTips() {
        if (this.tipInterval) {
            clearInterval(this.tipInterval);
            this.tipInterval = null;
        }
        this.hideTip();
    }
}

// Initialize tips manager when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const tipManager = new MaintenanceTipManager();
    tipManager.startTips();
    
    // Stop tips when page is hidden
    document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
            tipManager.hideTip();
        }
    });
});
