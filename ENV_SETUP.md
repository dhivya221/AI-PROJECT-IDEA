# Environment Variables

## Backend (.env)

### Required Variables

```env
# OpenAI API Configuration
OPENAI_API_KEY=sk-xxx...
```

Get your OpenAI API key:
1. Visit https://platform.openai.com/api-keys
2. Create a new secret key
3. Add to .env file

### Pinecone Configuration

```env
PINECONE_API_KEY=xxx...
PINECONE_ENVIRONMENT=gcp-starter  # or your environment
PINECONE_INDEX_NAME=project-ideas-index
```

Setup Pinecone:
1. Create account at https://www.pinecone.io
2. Create a serverless index with dimension 1536
3. Copy API key and environment
4. Update .env file

### Server Configuration

```env
PORT=3000
HOST=127.0.0.1
```

## Frontend (.env.local)

```env
REACT_APP_API_URL=http://localhost:3000
REACT_APP_DEBUG=true
```

### React Environment Variables

- `REACT_APP_API_URL`: Backend API base URL
- `REACT_APP_DEBUG`: Enable debug logging

## Development vs Production

### Development

```env
# Loose CORS
DEBUG=true
LOG_LEVEL=DEBUG
```

### Production

```env
# Strict CORS
DEBUG=false
LOG_LEVEL=INFO
# Use environment-specific URLs
OPENAI_API_KEY=<production_key>
PINECONE_API_KEY=<production_key>
```

## Security Best Practices

1. **Never commit .env files** - Add to .gitignore
2. **Use .env.example** - Check in example with placeholder values
3. **Rotate keys regularly** - Especially for production
4. **Use secret managers** - AWS Secrets, HashiCorp Vault, etc.
5. **Environment-specific values** - Never hardcode production secrets

## Local .env Template

```env
# Copy this to .env and fill in your values

# OpenAI
OPENAI_API_KEY=sk-...

# Pinecone
PINECONE_API_KEY=...
PINECONE_ENVIRONMENT=gcp-starter
PINECONE_INDEX_NAME=project-ideas-index

# Server
PORT=3000
HOST=127.0.0.1
```

## Obtaining API Keys

### OpenAI

1. Go to https://platform.openai.com
2. Sign up or login
3. Navigate to API Keys
4. Click "Create new secret key"
5. Copy and save (shown only once!)

### Pinecone

1. Go to https://www.pinecone.io
2. Sign up or login
3. Create a new project
4. Create a serverless index:
   - Dimension: 1536
   - Metric: cosine
5. Get API key from organization settings
6. Note the environment (e.g., gcp-starter)

## Troubleshooting

### "OPENAI_API_KEY not set"
- Ensure .env file exists in backend directory
- Verify key is correctly formatted
- Restart backend after changing .env

### "Pinecone connection failed"
- Verify API key is correct
- Check Pinecone environment matches
- Ensure index is created
- Check firewall/network connectivity

### "Invalid API key"
- Copy key exactly (no spaces)
- Ensure key hasn't been revoked
- Try regenerating the key

## Rotating Keys

When rotating API keys:

1. Generate new key in OpenAI/Pinecone
2. Update .env with new key
3. Test connectivity
4. Revoke old key
5. Document rotation in security log
