'use strict';

const target = document.getElementById('target');

const items = ['First item', 'Second item', 'Third item'];

for (let i = 0; i < items.length; i++) {
  const li = document.createElement('li');
  li.textContent = items[i];

  // Add class 'my-item' to the second list item (index 1)
  if (i === 1) {
    li.classList.add('my-item');
  }

  target.appendChild(li);
}
