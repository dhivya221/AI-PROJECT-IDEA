# Setup and Deployment Guide

## Local Development

### Backend

1. **Python Environment:**
   ```bash
   cd backend
   python -m venv venv
   source venv/Scripts/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configuration:**
   ```bash
   cp .env.example .env
   # Update .env with your API keys
   ```

3. **Run:**
   ```bash
   python main.py
   ```

### Frontend

1. **Dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start Development:**
   ```bash
   npm start
   ```

3. **Build for Production:**
   ```bash
   npm run build
   ```

## Docker Deployment

### Backend Dockerfile

Create `backend/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

### Docker Compose

Create `docker-compose.yml` in root:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "3000:3000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - PINECONE_API_KEY=${PINECONE_API_KEY}
      - PINECONE_ENVIRONMENT=${PINECONE_ENVIRONMENT}
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    ports:
      - "3001:3000"
    depends_on:
      - backend
    environment:
      - REACT_APP_API_URL=http://backend:3000
```

### Deploy with Docker:

```bash
docker-compose up -d
```

## Deployment Platforms

### Heroku

1. **Backend:**
   ```bash
   heroku create idea-generator-api
   heroku config:set OPENAI_API_KEY=...
   heroku config:set PINECONE_API_KEY=...
   git push heroku main
   ```

2. **Frontend (Vercel):**
   ```bash
   vercel --prod
   ```

### AWS

1. **Backend (EC2 + RDS):**
   - Deploy to EC2 instance
   - Use RDS for data persistence
   - Configure security groups

2. **Frontend (S3 + CloudFront):**
   - Build React app
   - Upload to S3
   - Distribute via CloudFront

### Google Cloud

1. **Cloud Run (Backend):**
   ```bash
   gcloud run deploy idea-generator \
     --source . \
     --platform managed \
     --region us-central1
   ```

2. **Firestore (Data):**
   - Store evaluation history
   - Manage user projects

## Performance Optimization

### Backend

1. **Caching:**
   - Cache domain analyses
   - Cache idea generations
   - Use RedisAPI

2. **Async Processing:**
   - Queue long-running tasks
   - Use Celery for background jobs

3. **Database:**
   - Optimize queries
   - Add indexes
   - Use connection pooling

### Frontend

1. **Code Splitting:**
   - Lazy load components
   - Split routes

2. **Optimization:**
   - Minify and compress
   - Use CDN for static assets
   - Enable GZIP compression

## Monitoring

### Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Metrics

- API response time
- GPT-4 API usage
- Pinecone query count
- Error rates

### Health Checks

Use `/health` endpoint for monitoring

## Security

1. **API Keys:**
   - Store in environment variables
   - Rotate regularly
   - Use secrets manager

2. **CORS:**
   - Configure allowed origins
   - Validate requests

3. **Rate Limiting:**
   - Limit API requests per user
   - Implement throttling

4. **Authentication:**
   - Add user authentication
   - Implement API keys

## Scaling

### Horizontal Scaling

- Deploy multiple backend instances
- Use load balancer
- Distribute traffic

### Vertical Scaling

- Increase server resources
- Optimize algorithms
- Cache aggressively

### Database Scaling

- Use read replicas
- Implement sharding
- Archive old data
