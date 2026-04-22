'use strict';

const target = document.getElementById('target');

// Add list items using innerHTML
target.innerHTML = `
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
`;

// Add class to the target element
target.classList.add('my-list');
