AI Content Agent 📝🤖
An AI-powered content generator that helps users create blog posts, video scripts, and social media captions with Ollama (Gemma:2B) for local AI processing.

🚀 Features

✅ Generate AI-Powered Content (Blog Posts, Video Scripts, Captions)

✅ Dark Mode Support 🌙

✅ Voting System for Captions (Choose the best caption)

✅ AI-Based Tiebreaker (Ollama decides in case of a tie)

✅ Drag & Drop Scheduling (Schedule posts easily)

✅ Date Picker for Scheduled Posts 📅

✅ Fast & Local AI Processing (No API Costs)




🛠 Installation

1️⃣ Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/ai-content-agent.git
cd ai-content-agent

2️⃣ Backend Setup (FastAPI + Ollama)
cd backend
python -m venv venv
source venv/Scripts/activate  # (For Windows)
pip install -r requirements.txt

Run the backend:
uvicorn app:app --reload

3️⃣ Start Ollama Locally
Ensure Ollama is running before using AI features:
ollama serve

4️⃣ Frontend Setup (Next.js + TailwindCSS)
cd frontend
npm install
npm run dev

🔗 API Endpoints
Method	Endpoint	Description
GET	/	Home API
POST	/generate	Generate AI-powered content
POST	/decide-tiebreaker	AI Tiebreaker Decision

🤖 How It Works

1️⃣ Enter a topic and select a content type (Blog, Script, Caption)

2️⃣ Click Generate Content to get AI-generated content

3️⃣ Vote on captions using the 👍 button

4️⃣ If there's a tie, click Let AI Decide

5️⃣ Schedule the selected post with a date picker

6️⃣ View Scheduled Posts with delete option 🗑️

🛠 Tech Stack

Frontend: Next.js, TailwindCSS
Backend: FastAPI, Ollama (Gemma:2B)
AI Model: Ollama Local LLM (Gemma:2B)
Database: N/A (Currently local state management)

🎯 To-Do & Future Improvements

 Database Integration (SQLite/PostgreSQL)
 User Authentication (Login/Signup)
 More AI Models Support (Mistral, TinyLlama)
 Post Automation (Auto-Publish to Social Media)

🤝 Contributing

1️⃣ Fork this repository
2️⃣ Create a feature branch (git checkout -b feature-name)
3️⃣ Commit changes (git commit -m "Added new feature")
4️⃣ Push to your branch (git push origin feature-name)
5️⃣ Open a Pull Request 🎉

📜 License

This project is licensed under the MIT License.

