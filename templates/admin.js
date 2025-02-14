// Admin Dashboard JavaScript
document.addEventListener('DOMContentLoaded', () => {
    // TODO: Add authentication check
    // if (!localStorage.getItem('token')) {
    //     window.location.href = '/login.html';
    //     return;
    // }

    // Initialize charts
    initializeCharts();
    
    // Load dashboard data
    loadDashboardData();

    // Handle date range changes
    document.getElementById('dateRange').addEventListener('change', (e) => {
        loadDashboardData(e.target.value);
    });

    // Handle navigation
    document.querySelectorAll('.admin-nav a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            document.querySelectorAll('.admin-nav a').forEach(l => l.classList.remove('active'));
            e.target.classList.add('active');
            loadSection(e.target.getAttribute('href').substring(1));
        });
    });
});

function initializeCharts() {
    // TODO: Connect to backend API to get real data
    // const salesData = await fetch('/api/admin/sales-data').then(r => r.json());
    // const modelsData = await fetch('/api/admin/popular-models').then(r => r.json());

    // Temporary: Sample data for charts
    const salesCtx = document.getElementById('salesChart').getContext('2d');
    const modelsCtx = document.getElementById('modelsChart').getContext('2d');

    // Sample sales data
    new Chart(salesCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [{
                label: 'Sales ($)',
                data: [12000, 19000, 15000, 25000, 22000, 30000],
                borderColor: '#e63946',
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    // Sample models data
    new Chart(modelsCtx, {
        type: 'doughnut',
        data: {
            labels: ['SuperSport R', 'Street Fighter V4', 'Adventure 1250', 'Cruiser Classic'],
            datasets: [{
                data: [30, 25, 20, 25],
                backgroundColor: ['#e63946', '#1d3557', '#457b9d', '#a8dadc']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

async function loadDashboardData(dateRange = 'month') {
    // TODO: Connect to backend API to get dashboard data
    // const data = await fetch(`/api/admin/dashboard?range=${dateRange}`).then(r => r.json());
    
    // Update statistics
    updateStats({
        testDrives: 15,
        maintenance: 8,
        reviews: 12,
        sales: 125000
    });

    // Load recent requests
    loadRecentRequests();
}

function updateStats(data) {
    // Update statistics cards
    document.querySelector('.stat-card:nth-child(1) .stat-number').textContent = data.testDrives;
    document.querySelector('.stat-card:nth-child(2) .stat-number').textContent = data.maintenance;
    document.querySelector('.stat-card:nth-child(3) .stat-number').textContent = data.reviews;
    document.querySelector('.stat-card:nth-child(4) .stat-number').textContent = 
        `$${data.sales.toLocaleString()}`;
}

async function loadRecentRequests() {
    // TODO: Connect to backend API to get recent requests
    // const requests = await fetch('/api/admin/recent-requests').then(r => r.json());
    
    // Temporary: Sample data
    const requests = [
        {
            date: '2024-01-15',
            customer: 'John Doe',
            type: 'Test Drive',
            model: 'SuperSport R',
            status: 'Pending'
        },
        // Add more sample requests as needed
    ];

    const tbody = document.getElementById('requestsTableBody');
    tbody.innerHTML = requests.map(request => `
        <tr>
            <td>${request.date}</td>
            <td>${request.customer}</td>
            <td>${request.type}</td>
            <td>${request.model}</td>
            <td>${request.status}</td>
            <td>
                <button onclick="handleRequest('${request.type}', '${request.status}')">
                    ${request.status === 'Pending' ? 'Review' : 'View'}
                </button>
            </td>
        </tr>
    `).join('');
}

function handleRequest(type, status) {
    // TODO: Implement request handling logic
    console.log(`Handling ${type} request with status: ${status}`);
}