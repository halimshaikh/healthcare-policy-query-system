# Healthcare Chatbot - Setup Guide

## Quick Start

### Option 1: Using API (GitHub GPT-4.1) - Recommended for beginners
1. Create `.env` file with:
   ```
   LLM_TYPE=api
   GITHUB_TOKEN=your_github_token
   ```
2. Run: `python load_csvs.py`
3. Start: `streamlit run app.py`

### Option 2: Using Local SLM (Ollama) - Free, runs offline

#### Step 1: Install Ollama
- Download from [ollama.ai](https://ollama.ai)
- Or install via package manager:
  ```bash
  # Windows
  # Download from ollama.ai
  
  # macOS
  brew install ollama
  
  # Linux
  curl https://ollama.ai/install.sh | sh
  ```

#### Step 2: Download a Model
```bash
# Pull a model (first time takes time to download)
ollama pull mistral      # Recommended: fast, 7B params
# or
ollama pull llama2       # More capable: 7B-70B options
# or
ollama pull neural-chat  # Optimized for chat
```

#### Step 3: Start Ollama Server
```bash
ollama serve
# Server will run on http://localhost:11434
```

#### Step 4: Configure Your App
Update `.env`:
```
LLM_TYPE=local
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=mistral
```

#### Step 5: Run the App
```bash
python load_csvs.py
streamlit run app.py
```

## Switching Modes

Simply change `LLM_TYPE` in your `.env` file:
- `LLM_TYPE=api` → Uses GitHub GPT-4.1 (requires GITHUB_TOKEN)
- `LLM_TYPE=local` → Uses local Ollama (requires Ollama running)

## Available Local Models

| Model | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| mistral | 7B | ⚡⚡⚡ | ⭐⭐⭐⭐ | Best balance |
| neural-chat | 7B | ⚡⚡⚡ | ⭐⭐⭐⭐ | Chat optimized |
| llama2 | 7B-70B | ⚡⚡ | ⭐⭐⭐⭐⭐ | Most capable |
| dolphin-mixtral | 46B | ⚡ | ⭐⭐⭐⭐⭐ | Very capable |

## Troubleshooting

### "Cannot connect to Ollama"
- Make sure Ollama is running: `ollama serve`
- Check `OLLAMA_URL` in `.env` (default: http://localhost:11434)

### "Model not found"
- Pull the model: `ollama pull <model_name>`
- Check OLLAMA_MODEL in `.env`

### "API key error"
- If using API mode, ensure GITHUB_TOKEN is set correctly

## Database Setup

Run once to load your CSV data:
```bash
python load_csvs.py
```

This creates `healthcare_large.db` with tables:
- hospitals
- hospital_resources_daily
- district_health
- emergency_requests

## Project Structure

```
heathcare_chatbot/
├── app.py                           # Main Streamlit app
├── load_csvs.py                     # CSV to SQLite loader
├── requirement.txt                  # Dependencies
├── .env                             # Your configuration (create from .env.example)
├── .env.example                     # Example configuration
├── healthcare_large.db              # SQLite database (created by load_csvs.py)
├── hospitals_large.csv              # Input data
├── hospital_resources_large.csv     # Input data
├── district_health_large.csv        # Input data
└── emergency_requests_large.csv     # Input data
```

## Performance Tips

- **For CPU-only**: Use 7B models (mistral, llama2-7b)
- **For GPU**: Use 13B+ models or larger (llama2-70b, dolphin-mixtral)
- **First response is slow**: Ollama caches models in memory after first use
- **API mode**: Fastest for one-off queries but costs money

## Features

✅ Database-first search (checks SQLite before calling LLM)
✅ Seamless switching between API and local models
✅ Chat history tracking
✅ Error handling for both modes
✅ Configurable via .env file
