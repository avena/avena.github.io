function runTypingEffect() {
  const text = 'Fernando Padilha Avena.';
  const typingElement = document.getElementById('typing-text');
  const typingDelay = 100;

  typeText(text, typingElement, typingDelay);
}

function updateActiveLang() {
  const path = window.location.pathname;
  const links = document.querySelectorAll('.language-switch a');
  links.forEach(link => {
    link.classList.remove('active');
    if (path === '/' && link.getAttribute('href') === '/') link.classList.add('active');
    if (path.startsWith('/en') && link.getAttribute('href') === '/en') link.classList.add('active');
    if (path.startsWith('/es') && link.getAttribute('href') === '/es') link.classList.add('active');
  });
}

function typeText(text, typingElement, delay) {
  for (let i = 0; i < text.length; i++) {
    setTimeout(() => {
      typingElement.textContent += text.charAt(i);
    }, delay * i);
  }
}

document.addEventListener('DOMContentLoaded', runTypingEffect);