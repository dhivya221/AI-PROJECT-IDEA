# 📖 Quick Reference Card

## 🚀 Getting Started (Copy-Paste)

### Step 1: Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python main.py
```

### Step 2: Frontend Setup (New Terminal)
```bash
cd frontend
npm install
npm start
```

### Step 3: Open Browser
```
http://localhost:3001
```

---

## 🔑 API Keys Needed

### OpenAI
- **Website**: https://platform.openai.com/api-keys
- **Format**: `sk-...`
- **Cost**: Pay-as-you-go

### Pinecone
- **Website**: https://www.pinecone.io
- **Index Dimension**: 1536
- **Type**: Serverless
- **Free Tier**: Available

---

## 📋 Essential Files

| File | Purpose | Location |
|------|---------|----------|
| **START_HERE.md** | Main intro | Root |
| **QUICKSTART.md** | 5-min setup | Root |
| **README.md** | Full docs | Root |
| **API.md** | Endpoints | Root |
| **orchestrator.py** | Main logic | backend/src/ |
| **App.js** | Main UI | frontend/src/ |

---

## 🔗 API Endpoints

```bash
POST /evaluate
  Input: {domain, context}
  Output: Complete evaluation

GET /health
  Returns: Service status

GET /docs
  Opens: Swagger UI documentation
```

---

## 📊 Each Evaluation Returns

```
5 Project Ideas
├─ Title, description, use case
├─ Potential impact
└─ Complexity score

Tech Stack (per idea)
├─ Backend, frontend, database
├─ Deployment, AI/ML libraries
└─ Why each choice

Complexity Analysis
├─ Overall score (0-10)
├─ Dev timeline estimate
├─ Difficulty level
└─ Key challenges

Scoring Results
├─ Feasibility (0-100)
├─ Innovation (0-100)
├─ Market Potential (0-100)
└─ Overall Score

Recommendations
├─ Priority ranking
├─ Team composition
├─ Partnerships needed
└─ Risk mitigation
```

---

## 🎯 Common Tasks

### Try a Different Domain
1. Go to http://localhost:3001
2. Enter domain: "EdTech", "Fintech", "Climate Tech", etc.
3. Click "Generate Ideas"
4. See results in 30-60 seconds

### Check API Status
```bash
curl http://localhost:3000/health
```

### View API Docs
```bash
Open http://localhost:3000/docs
```

### Test API Call
```bash
curl -X POST http://localhost:3000/evaluate \
  -H "Content-Type: application/json" \
  -d '{"domain":"Healthcare AI"}'
```

### Customize Prompts
Edit these files:
- `backend/src/idea_generator.py` → Change idea prompt
- `backend/src/scoring_module.py` → Change scoring logic
- `backend/src/tech_stack_recommender.py` → Change tech suggestions

### Change Number of Ideas
Edit `backend/src/app.py`:
```python
num_ideas=5  # Change to any number
```

---

## 🐛 Troubleshooting Quick Fixes

### "OPENAI_API_KEY not set"
```bash
# Check .env file exists and has your key
cat backend/.env
# Should show: OPENAI_API_KEY=sk-...
```

### "Cannot connect to Pinecone"
```bash
# Verify credentials are correct
# Check index is created in Pinecone
# Ensure dimension is 1536
```

### Port 3000 Already in Use
```bash
# Edit backend/.env
PORT=3001  # Use different port
```

### Module Not Found
```bash
# Reinstall Python packages
pip install -r backend/requirements.txt

# Reinstall Node packages
npm install  # in frontend directory
```

---

## 🎓 Learning Path

```
Day 1: Try It
  1. Follow QUICKSTART.md
  2. Generate ideas for your domain
  3. Explore the UI

Day 2: Understand It
  1. Read README.md
  2. Review ARCHITECTURE.md
  3. Look at code structure

Day 3: Customize It
  1. Modify prompts
  2. Change scoring logic
  3. Update UI colors

Day 4: Deploy It
  1. Read DEPLOYMENT.md
  2. Choose platform
  3. Deploy to cloud
```

---

## 📱 Project Commands

### Backend
```bash
cd backend
python main.py              # Run server
pip install -r requirements.txt  # Install deps
python -m pytest            # Run tests
```

### Frontend
```bash
cd frontend
npm start                   # Run dev server
npm run build              # Production build
npm test                   # Run tests
npm run eject              # Expose config
```

### Docker (Optional)
```bash
docker-compose up          # Start all services
docker-compose down        # Stop services
docker-compose logs        # View logs
```

---

## 🔐 Security Checklist

### Before Production
- [ ] Change default API endpoint
- [ ] Add authentication
- [ ] Enable HTTPS/TLS
- [ ] Set up rate limiting
- [ ] Configure firewall
- [ ] Enable logging
- [ ] Set up backups
- [ ] Review CORS settings
- [ ] Rotate API keys regularly
- [ ] Monitor API usage

---

## 📊 System Specs

- **Python**: 3.9+
- **Node**: 16+
- **Backend Port**: 3000 (configurable)
- **Frontend Port**: 3001 (default)
- **First Request**: 30-60 seconds
- **Cached Request**: 20-30 seconds
- **Concurrent Users**: Unlimited

---

## 🎨 Customization Options

### Easy (5 minutes)
- Change UI colors
- Update domain examples
- Modify prompt temperature
- Add more ideas per domain

### Medium (30 minutes)
- Add authentication
- Change API responses
- Add new UI tabs
- Modify scoring weights

### Advanced (2+ hours)
- Add database
- Integrate different LLM
- Custom training data
- Advanced analytics

---

## 📞 Quick Help Index

| Problem | Solution | Time |
|---------|----------|------|
| Won't start | Check API keys | 2 min |
| Port in use | Change PORT in .env | 1 min |
| Slow response | Check internet | 1 min |
| Module error | pip install | 5 min |
| UI not loading | Check npm install | 5 min |
| API error | Check .env file | 2 min |

---

## 🌐 Deploy Shortcuts

### Heroku
```bash
heroku create app-name
heroku config:set OPENAI_API_KEY=...
git push heroku main
```

### Vercel (Frontend)
```bash
npm install -g vercel
vercel --prod
```

### Docker
```bash
docker-compose up -d
```

---

## 📚 Documentation Map

```
START HERE
    ↓
00_START_HERE.md (this project summary)
    ↓
QUICKSTART.md (get it running)
    ↓
README.md (understand it)
    ↓
ARCHITECTURE.md (deep dive)
    ↓
DEPLOYMENT.md (go live)
```

---

## ✅ Success Checklist

- [ ] Got OpenAI API key
- [ ] Got Pinecone API key
- [ ] Ran QUICKSTART.md
- [ ] Backend running (localhost:3000)
- [ ] Frontend running (localhost:3001)
- [ ] Generated first ideas
- [ ] Explored all tabs
- [ ] Read documentation
- [ ] Ready to customize!

---

## 🚀 Next Quick Win

1. Get your API keys (5 min)
2. Run QUICKSTART.md (5 min)
3. Enter domain: "Your Interest" (30 sec)
4. See 5 ideas generated! (60 sec)

**Total: 12 minutes to amazing results!**

---

## 💡 Pro Tips

- Try specific domains for best results
- Add context for personalized ideas
- Check "Scoring" tab for best ideas
- Use "Tech Stack" for implementation
- Read "Recommendations" for strategy

---

**Ready? Start with QUICKSTART.md!** 🎉

Questions? Check INDEX.md for full docs.

*Last updated: 2024*
