# API Reference

## Base URL

```
http://localhost:3000
```

## Authentication

Currently no authentication required. Future versions will include API keys.

## Endpoints

### 1. Evaluate Domain

**Endpoint:** `POST /evaluate`

Generate project ideas and analysis for a given domain.

**Request Body:**
```json
{
  "domain": "string (required)",
  "context": "string (optional)"
}
```

**Example:**
```bash
curl -X POST http://localhost:3000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "domain": "Healthcare AI",
    "context": "Focus on disease diagnosis using machine learning"
  }'
```

**Response:**
```json
{
  "input_domain": "Healthcare AI",
  "ideas": [
    {
      "title": "AI Diagnostics Platform",
      "description": "...",
      "use_case": "...",
      "potential_impact": "..."
    }
  ],
  "tech_stacks": [
    [
      {
        "category": "Backend Framework",
        "tool": "FastAPI",
        "reason": "..."
      }
    ]
  ],
  "complexity_analysis": [
    {
      "overall_score": 7.5,
      "development_time": "2-3 months",
      "difficulty_level": "Advanced",
      "key_challenges": [...]
    }
  ],
  "scoring": [
    {
      "feasibility_score": 75,
      "innovation_score": 80,
      "market_potential_score": 70,
      "overall_score": 75,
      "breakdown": {...}
    }
  ],
  "recommendations": [...]
}
```

**Status Codes:**
- `200`: Success
- `400`: Invalid request
- `500`: Server error (check API keys and Pinecone connection)

---

### 2. Health Check

**Endpoint:** `GET /health`

Check API health status.

**Response:**
```json
{
  "status": "healthy",
  "service": "idea-generator"
}
```

---

### 3. Root

**Endpoint:** `GET /`

Basic health check and API information.

**Response:**
```json
{
  "message": "AI Project Idea Generator API is running"
}
```

---

## Data Models

### DomainInput

```typescript
{
  domain: string,        // e.g., "Healthcare", "Finance"
  context?: string       // Additional context about the domain
}
```

### ProjectIdea

```typescript
{
  title: string,
  description: string,
  use_case: string,
  potential_impact: string
}
```

### ComplexityAnalysis

```typescript
{
  overall_score: number,           // 0-10
  development_time: string,        // e.g., "2-3 weeks"
  difficulty_level: string,        // "Beginner" | "Intermediate" | "Advanced"
  key_challenges: string[]
}
```

### TechStackItem

```typescript
{
  category: string,      // e.g., "Backend Framework"
  tool: string,          // e.g., "FastAPI"
  reason: string         // Why this tool is recommended
}
```

### ScoringResult

```typescript
{
  feasibility_score: number,       // 0-100
  innovation_score: number,        // 0-100
  market_potential_score: number,  // 0-100
  overall_score: number,           // 0-100
  breakdown: object                // Detailed reasoning
}
```

### ProjectEvaluation

```typescript
{
  input_domain: string,
  ideas: ProjectIdea[],
  tech_stacks: TechStackItem[][],
  complexity_analysis: ComplexityAnalysis[],
  scoring: ScoringResult[],
  recommendations: string[]
}
```

---

## Error Handling

### Error Response Format

```json
{
  "detail": "Error message describing what went wrong"
}
```

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `OPENAI_API_KEY not set` | Missing OpenAI credentials | Set `OPENAI_API_KEY` in `.env` |
| `PINECONE_API_KEY not set` | Missing Pinecone credentials | Set `PINECONE_API_KEY` in `.env` |
| `Invalid request` | Malformed JSON or missing required fields | Check request format |
| `500 Server Error` | API timeout or service issue | Check logs, retry with backoff |

---

## Rate Limiting

Currently no rate limits implemented. In production, implement:

- 10 requests per minute per IP
- 100 requests per hour per user
- Exponential backoff on errors

---

## Pagination

Not yet implemented. Future versions will support pagination for idea history.

---

## Filtering & Search

Vector search endpoint (MCP tool available):

```
POST /mcp/tools/vector_search
{
  "query": "healthcare diagnosis",
  "top_k": 5
}
```

---

## Batch Operations

Future feature to process multiple domains in one request.

---

## Webhooks

Future feature for async processing and status updates.

---

## SDK/Client Libraries

### Python Client

```python
import requests

def evaluate_domain(domain, context=None):
    response = requests.post('http://localhost:3000/evaluate', json={
        'domain': domain,
        'context': context
    })
    return response.json()

result = evaluate_domain('Healthcare AI')
```

### JavaScript Client

Already provided in `frontend/src/api.js`:

```javascript
import { evaluateDomain } from './api';

const result = await evaluateDomain('Healthcare AI', 'Optional context');
```

---

## Deprecation Policy

API versions: Maintain v1 for at least 12 months after v2 release.

---

## Support

For API issues:
1. Check logs: `docker logs <container-id>`
2. Verify environment variables
3. Test with provided sample requests
4. Create GitHub issue with error details
