# 🎬 AI Content Recommendation System (Netflix-Style)

A full-stack, Netflix-inspired content recommendation system that suggests movies and TV shows based on user age, genre preferences, and content maturity settings.

The project uses a **real Netflix dataset from Kaggle**, a **Python Flask backend** for recommendation logic, and a **modern HTML/CSS/JavaScript frontend** with interactive toggles and genre chips.

---

## ✨ Features

- 🎯 Personalized recommendations based on:
  - User age
  - Selected genres
  - Content type (Movies / TV Shows)
  - Mature content preference
- 🧠 Content-based filtering using real Netflix metadata
- 🔞 Age-aware and rating-aware content filtering
- 🎨 Modern, Netflix-style UI with:
  - Toggle switches
  - Selectable genre chips
  - Animated buttons
  - Recommendation cards
- 🌐 REST API built with Flask
- 📦 Uses a real Kaggle dataset (`netflix_titles.csv`)

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- Flask-CORS
- Pandas
- Scikit-learn (optional for future extensions)

### Frontend
- HTML
- CSS (Glassmorphism-style UI)
- JavaScript (Fetch API)

### Dataset
- **Netflix Movies and TV Shows Dataset (Kaggle)**


---
## 🚀 How It Works

1. User selects:
   - Age
   - Content type (Movie / TV Show)
   - Preferred genres
   - Mature content toggle
2. Frontend sends user preferences to the Flask API.
3. Backend filters content based on:
   - Content type
   - Age-appropriate ratings
   - Genre relevance (substring matching)
4. Top recommendations are returned and displayed as cards in the UI.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd content-recommendation-system

