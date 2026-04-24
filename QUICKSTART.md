# Quick Start Guide

## 5-Minute Setup

### Prerequisites Checklist

- [ ] Python 3.9+ installed
- [ ] Node.js 16+ installed
- [ ] OpenAI API key (free trial available)
- [ ] Pinecone account (free tier available)

### Step 1: Get Your API Keys (2 minutes)

**OpenAI:**
1. Visit https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy and save it

**Pinecone:**
1. Visit https://www.pinecone.io
2. Create a free account
3. Create an index: "project-ideas-index" (dimension: 1536)
4. Copy API key and environment

### Step 2: Backend Setup (2 minutes)

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Or activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env with your keys
# OPENAI_API_KEY=sk-xxx...
# PINECONE_API_KEY=xxx...
# PINECONE_ENVIRONMENT=gcp-starter

# Start backend
python main.py
```

✅ Backend running at http://localhost:3000

### Step 3: Frontend Setup (1 minute)

In a new terminal:

```bash
cd frontend

# Install dependencies
npm install

# Start frontend
npm start
```

✅ Frontend running at http://localhost:3001

### Step 4: Test It! (No wait!)

Go to http://localhost:3001 in your browser and:

1. Enter a domain: "Healthcare AI"
2. Add context: "Focus on diagnosis tools"
3. Click "Generate Ideas"
4. See results in 30-60 seconds!

## Common Issues & Quick Fixes

### "OPENAI_API_KEY not set"
```bash
# Make sure .env exists in backend directory
# and has your key
cat .env
```

### "Cannot connect to Pinecone"
```bash
# Verify your Pinecone credentials
# Check environment name matches exactly
# Ensure your index is created
```

### "Module not found" (Python)
```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

### "Port already in use"
```bash
# Change PORT in backend/.env
PORT=3001  # Use different port

# Or kill the process using the port
# Windows: netstat -ano | findstr :3000
```

## Next Steps

1. **Explore the API**: Visit http://localhost:3000/docs for interactive docs
2. **Try different domains**: Education, Finance, Climate Tech, etc.
3. **Check the code**: See how each component works
4. **Deploy**: Follow DEPLOYMENT.md for production setup
5. **Customize**: Modify prompts in each module for your needs

## Project Structure Overview

```
backend/
  ├── main.py              # Start here - entry point
  ├── src/
  │   ├── config.py        # API keys & settings
  │   ├── orchestrator.py  # Main logic pipeline
  │   └── [modules]...     # Individual components
  └── requirements.txt     # Dependencies

frontend/
  ├── src/
  │   ├── App.js          # Start here - main UI
  │   ├── api.js          # Connect to backend
  │   └── components/     # UI components
  └── package.json        # Dependencies
```

## Understanding the Flow

```
You Enter Domain
    ↓
Backend: Domain Analyzer (what is this domain?)
    ↓
Backend: Idea Generator (5 creative ideas)
    ↓
Backend: Complexity Estimator (how hard?)
    ↓
Backend: Tech Stack Recommender (what tools?)
    ↓
Backend: Scoring Module (how good? 0-100)
    ↓
Backend: Recommendation Engine (what to do?)
    ↓
Frontend: Display Results (beautifully!)
```

## Example Domains to Try

1. **Healthcare AI** - Diagnosis, treatment, monitoring
2. **EdTech** - Personalized learning, tutoring
3. **Climate Tech** - Carbon tracking, renewable energy
4. **Fintech** - Investment, lending, payments
5. **Robotics** - Automation, manufacturing
6. **Supply Chain** - Tracking, optimization
7. **Cybersecurity** - Detection, prevention, response

## API Quick Reference

### Generate Ideas
```bash
curl -X POST http://localhost:3000/evaluate \
  -H "Content-Type: application/json" \
  -d '{"domain": "Healthcare AI"}'
```

### Check Health
```bash
curl http://localhost:3000/health
```

## Tips for Best Results

1. **Be specific**: "Healthcare AI" > "AI stuff"
2. **Add context**: Mention target users, pain points
3. **Be clear**: Avoid jargon, use common language
4. **Provide constraints**: Budget, timeline, team size

## Customization

### Change Number of Ideas
Edit `backend/src/app.py`:
```python
num_ideas=5  # Change to desired number
```

### Change Model
Edit `backend/src/config.py`:
```python
OPENAI_MODEL = "gpt-4"  # or "gpt-3.5-turbo"
```

### Adjust Scoring Weights
Edit `backend/src/scoring_module.py`:
```python
# Modify weights in the scoring prompt
```

## Performance Notes

- First request: 30-60 seconds (parallel API calls)
- Subsequent requests: 20-30 seconds (cached)
- Large context: May take longer

## Support

- Check [README.md](README.md) for full documentation
- See [API.md](API.md) for API reference
- Review [DEPLOYMENT.md](DEPLOYMENT.md) for production setup
- Check logs for detailed error messages

## Next Level

Ready to go deeper?

1. Read [README.md](README.md) for architecture
2. Explore [API.md](API.md) for detailed endpoints
3. Check MCP server capabilities in [backend/src/mcp_server.py](backend/src/mcp_server.py)
4. Customize prompts for your use case
5. Add authentication and persistence
6. Deploy to production

---

**Happy idea generating! 🚀**

Questions? Check the documentation files or create an issue.
