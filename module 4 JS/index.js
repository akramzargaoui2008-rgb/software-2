'use strict';

const form = document.getElementById('search-form');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', function (event) {
  // Prevent the form from navigating to the API URL (step 2 onwards)
  event.preventDefault();

  // Get the value from the input
  const value = document.getElementById('query').value;

  // Step 2: fetch from TVMaze API
  fetch(`https://api.tvmaze.com/search/shows?q=${value}`)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Step 2: print result to console
      console.log(data);

      // Step 3: clear old results before showing new ones
      resultsDiv.innerHTML = '';

      // Step 3 & 4: loop through results and build articles
      for (let i = 0; i < data.length; i++) {
        const tvShow = data[i];

        // Step 4: ternary operator for missing image (replaces optional chaining)
        const imgSrc = tvShow.show.image
          ? tvShow.show.image.medium
          : 'https://placehold.co/210x295?text=Not%20Found';

        const name = tvShow.show.name;
        const url = tvShow.show.url;
        const summary = tvShow.show.summary;

        // Create article
        const article = document.createElement('article');

        // h2 - name
        const h2 = document.createElement('h2');
        h2.textContent = name;

        // a - link to details
        const a = document.createElement('a');
        a.href = url;
        a.target = '_blank';
        a.textContent = 'More details';

        // img - medium image
        const img = document.createElement('img');
        img.src = imgSrc;
        img.alt = name;

        // div - summary (not <p> because summary already contains <p>)
        const div = document.createElement('div');
        div.innerHTML = summary;

        // Assemble article
        article.appendChild(h2);
        article.appendChild(a);
        article.appendChild(img);
        article.appendChild(div);

        // Append article to results
        resultsDiv.appendChild(article);
      }
    });
});
