
document.addEventListener('DOMContentLoaded', function() {
  var form = document.querySelector('form');
  var button = document.getElementById('button');

  form.addEventListener('submit', function() {
      button.disabled = true;
      button.innerHTML = 'Running...';
  });
});
