function recommend() {
  const age = Number(document.getElementById("age").value);
  const type = document.getElementById("typeToggle").checked
    ? "TV Show"
    : "Movie";
  const mature = document.getElementById("matureToggle").checked;

  if (!age || selectedGenres.length === 0) {
    alert("Please enter age and select at least one genre");
    return;
  }

  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "⏳ Fetching recommendations...";

  fetch("http://127.0.0.1:5000/recommend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      age: age,
      genres: selectedGenres,
      type: type,
      allow_mature: mature,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.length === 0) {
        resultsDiv.innerHTML = "😕 No recommendations found.";
        return;
      }

      let html = "<h3>🎬 Recommended for You</h3>";

      data.forEach((item) => {
        html += `
        <div class="card">
          <h4>${item.title}</h4>
          <p><b>Genres:</b> ${item.listed_in}</p>
          <p><b>Rating:</b> ${item.rating}</p>
        </div>
      `;
      });

      resultsDiv.innerHTML = html;
    })
    .catch((err) => {
      console.error(err);
      resultsDiv.innerHTML = "❌ Error fetching recommendations";
    });
}

let selectedGenres = [];

function toggleGenre(el) {
  el.classList.toggle("active");

  const genre = el.innerText;

  if (selectedGenres.includes(genre)) {
    selectedGenres = selectedGenres.filter((g) => g !== genre);
  } else {
    selectedGenres.push(genre);
  }

  console.log("Selected genres:", selectedGenres);
}
