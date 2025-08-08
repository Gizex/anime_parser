const words = [
  { en: 'apple', ru: 'яблоко' },
  { en: 'book', ru: 'книга' },
  { en: 'cat', ru: 'кот' },
  { en: 'dog', ru: 'собака' },
  { en: 'water', ru: 'вода' },
  { en: 'sun', ru: 'солнце' },
  { en: 'moon', ru: 'луна' },
  { en: 'car', ru: 'машина' },
  { en: 'house', ru: 'дом' },
  { en: 'friend', ru: 'друг' }
];

let current = null;
const card = document.getElementById('card');
const showBtn = document.getElementById('show');
const nextBtn = document.getElementById('next');

function nextWord() {
  current = words[Math.floor(Math.random() * words.length)];
  card.textContent = current.en;
}

function showTranslation() {
  if (current) {
    card.textContent = `${current.en} – ${current.ru}`;
  }
}

showBtn.addEventListener('click', showTranslation);
nextBtn.addEventListener('click', nextWord);
