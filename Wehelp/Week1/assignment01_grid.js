document.addEventListener('DOMContentLoaded', function() {
  const burgerIcon = document.getElementById('burger-icon');
  const closeIcon = document.getElementById('close-icon');
  const mobileMenu = document.getElementById('mobile-menu');

  burgerIcon.addEventListener('click', function() {
    burgerIcon.style.display = 'none'; // 隱藏漢堡圖示
    mobileMenu.classList.add('show');
  });

  closeIcon.addEventListener('click', function() {
    burgerIcon.style.display = 'block'; // 顯示漢堡圖示
    mobileMenu.classList.remove('show');
  });
});
