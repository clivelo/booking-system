const dateInput = document.getElementById('date');
dateInput.value = formatDate();

function padDigits(num) {
  return num.toString().padStart(2, '0');
}

function formatDate(date = new Date()) {
  return [
    date.getFullYear(),
    padDigits(date.getMonth() + 1),
    padDigits(date.getDate()),
  ].join('-');
}