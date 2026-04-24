# AI Project Idea Generator + Evaluator

A comprehensive AI-powered system that generates, analyzes, and evaluates project ideas based on user-provided domains. Built with FastAPI, React, OpenAI GPT-4, and Pinecone for RAG capabilities.

## 🎯 Features

- **Domain Analysis**: Analyzes domains to understand market context, stakeholders, and opportunities
- **Idea Generation**: Generates 5 creative and feasible project ideas per domain
- **Complexity Estimation**: Estimates development time, difficulty level, and key challenges
- **Tech Stack Recommendation**: Suggests optimal technology stacks for each idea
- **Intelligent Scoring**: Evaluates ideas on feasibility, innovation, and market potential
- **Recommendations Engine**: Provides strategic recommendations for implementation
- **Vector Search (RAG)**: Retrieves similar ideas using embeddings for context enrichment
- **MCP Server**: Full Model Context Protocol integration for seamless AI tool integration

## 🏗️ Architecture

```
USER INPUT (Domain/Idea)
    ↓
Domain Analyzer → Idea Generator → Complexity Estimator
    ↓                   ↓              ↓
Tech Stack Recommender → Scoring Module → Recommendation Engine
    ↓                      ↓              ↓
Vector Search (RAG) ← Embedding Engine ← All Components
    ↓
FINAL OUTPUT (Ideas + Scores + Tech Stack)
```

## 📋 Project Structure

```
AI project idea/
├── backend/
│   ├── src/
│   │   ├── config.py                 # Configuration management
│   │   ├── models.py                 # Pydantic data models
│   │   ├── embedding_engine.py       # Text to vector conversion
│   │   ├── vector_search.py          # Pinecone RAG integration
│   │   ├── domain_analyzer.py        # Domain analysis module
│   │   ├── idea_generator.py         # Idea generation module
│   │   ├── complexity_estimator.py   # Complexity analysis
│   │   ├── tech_stack_recommender.py # Tech recommendations
│   │   ├── scoring_module.py         # Idea scoring
│   │   ├── recommendation_engine.py  # Strategic recommendations
│   │   ├── mcp_server.py             # MCP server implementation
│   │   ├── orchestrator.py           # Pipeline orchestration
│   │   └── app.py                    # FastAPI application
│   ├── main.py                       # Entry point
│   ├── requirements.txt              # Python dependencies
│   └── .env.example                  # Environment variables template
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── IdeaCard.js          # Idea display component
│   │   │   ├── ScoringCard.js       # Scoring visualization
│   │   │   └── TechStackCard.js     # Tech stack display
│   │   ├── api.js                   # API client
│   │   ├── App.js                   # Main React component
│   │   ├── index.js                 # React entry point
│   │   └── index.css                # Tailwind styles
│   ├── public/
│   │   └── index.html               # HTML template
│   └── package.json                 # Node dependencies
│
└── README.md                        # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+
- OpenAI API key
- Pinecone account and API key

### Backend Setup

1. **Clone and navigate to backend:**
   ```bash
   cd backend
   ```

2. **Create Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run the backend:**
   ```bash
   python main.py
   ```
   API will be available at `http://localhost:3000`

### Frontend Setup

1. **Navigate to frontend:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```
   UI will be available at `http://localhost:3000`

## 📚 API Documentation

### Evaluate Domain

**Endpoint:** `POST /evaluate`

**Request:**
```json
{
  "domain": "Healthcare AI",
  "context": "Focus on chronic disease management"
}
```

**Response:**
```json
{
  "input_domain": "Healthcare AI",
  "ideas": [...],
  "tech_stacks": [...],
  "complexity_analysis": [...],
  "scoring": [...],
  "recommendations": [...]
}
```

### Health Check

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "service": "idea-generator"
}
```

## 🔧 Environment Variables

Create a `.env` file in the backend directory:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key

# Pinecone Configuration
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_environment
PINECONE_INDEX_NAME=project-ideas-index

# Server Configuration
PORT=3000
```

## 🔂 How It Works

### 1. Domain Analysis
- Analyzes the provided domain using GPT-4
- Identifies problem areas, stakeholders, competitors, and market size
- Provides technical requirements and industry trends

### 2. Idea Generation
- Generates 5 innovative project ideas based on domain analysis
- Each idea includes title, description, use case, and potential impact
- Uses GPT-4 with high temperature for creativity

### 3. Complexity Estimation
- Estimates development complexity (0-10 scale)
- Predicts development timeline
- Identifies difficulty level and key challenges
- Data-driven by domain and idea characteristics

### 4. Tech Stack Recommendation
- Recommends optimal tech stack per idea
- Suggests backend, frontend, database, deployment, and AI/ML tools
- Provides rationale for each recommendation

### 5. Scoring
- **Feasibility Score**: How realistic within 3 months
- **Innovation Score**: How novel/unique
- **Market Potential**: Addressable market size
- **Overall Score**: Average of the three metrics

### 6. Recommendations
- Strategic guidance on which idea to prioritize
- Team composition and skills needed
- Partnerships and resources required
- Risk mitigation strategies
- MVP roadmap and phasing

### 7. Vector Search (RAG)
- Embeddings created for all ideas using OpenAI
- Stored in Pinecone for fast semantic search
- Enables context-aware recommendations
- Future retrieval of similar ideas

## 🤖 MCP Server Integration

The system includes built-in Model Context Protocol support. Available tools:

- `analyze_domain`: Domain analysis
- `generate_ideas`: Idea generation
- `estimate_complexity`: Complexity estimation
- `recommend_tech_stack`: Tech stack recommendations
- `score_ideas`: Idea scoring
- `vector_search`: RAG-based search
- `get_recommendations`: Strategic recommendations

## 📈 Evaluation Output

Each evaluation returns:

1. **Project Ideas** (5 per domain)
   - Creative title and description
   - Use case and potential impact
   - Complexity metrics and timeline

2. **Tech Stacks** (per idea)
   - Backend, frontend, database recommendations
   - Deployment and AI/ML tool suggestions
   - Rationale for each choice

3. **Complexity Analysis**
   - Overall complexity score
   - Development timeline estimate
   - Difficulty level assessment
   - Key challenges and risks

4. **Scoring Results**
   - Feasibility, innovation, market potential scores
   - Detailed breakdown with reasoning
   - Overall composite score

5. **Recommendations**
   - Priority ranking
   - Team and resource needs
   - Implementation roadmap
   - Risk mitigation strategies

## 🔮 Future Enhancements

- **Phase 2**: Multi-user collaboration and project tracking
- **Phase 3**: Integration with GitHub for automatic setup
- **Phase 4**: Real-time market data integration
- **Phase 5**: Investor pitch generation
- **Phase 6**: Team formation suggestions
- **Phase 7**: Budget estimation and funding guidance

## 📝 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Contributions welcome! Please follow PEP 8 for Python and Prettier for JavaScript.

## 📧 Support

For issues or questions, create a GitHub issue or contact the development team.

---

**Built with ❤️ using FastAPI, React, OpenAI, and Pinecone**
