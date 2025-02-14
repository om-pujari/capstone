document.getElementById('testDriveForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const bike = document.getElementById('bike').value;
    const date = document.getElementById('date').value;
  
    if (name && email && phone && bike && date) {
      alert(`Thank you, ${name}! Your test drive for ${bike} is booked for ${date}. We will contact you shortly.`);
      this.reset();
    } else {
      alert('Please fill out all required fields.');
    }
  });
  