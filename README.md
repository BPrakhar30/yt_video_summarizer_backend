# YouTube Video Summarizer

A web application that generates concise summaries of YouTube videos using OpenAI's GPT model.

## Features
- YouTube video transcript extraction
- AI-powered summary generation
- Clean and responsive user interface
- Section-based summary format (Title, Summary Points, Conclusion)

## Tech Stack
- Frontend: React.js with Vite
- Backend: Python Flask
- AI: OpenAI GPT API
- Styling: CSS with custom animations

## Setup
### 1. Clone the repository 

```bash
git clone https://github.com/bprakhar30/youtube-video-summarizer.git
```

### 2. Install frontend dependencies

```bash
cd frontend
npm install
```

### 3. Install backend dependencies

```bash
cd backend
python -m venv venv
venv\Scripts\activate (windows)
pip install -r requirements.txt
```

### 4. Run the application

#### Backend:
```bash
cd backend
python run.py
```

#### Frontend:
```bash
cd frontend
npm run dev
```

## Usage
1. Enter your OpenAI API key in the settings
2. Enter a YouTube video URL
3. Click "Generate Summary"
4. View the formatted summary with title, key points, and conclusion

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is not currently licensed. If you would like to contribute, feel free to open an issue to discuss licensing options.
