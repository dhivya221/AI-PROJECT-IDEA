# Testing Guide

## Unit Tests

### Backend Tests

Create `backend/tests/test_modules.py`:

```python
import pytest
from src.domain_analyzer import get_domain_analyzer
from src.idea_generator import get_idea_generator
from src.complexity_estimator import get_complexity_estimator
from src.models import ProjectIdea

@pytest.fixture
def analyzer():
    return get_domain_analyzer()

@pytest.fixture
def generator():
    return get_idea_generator()

def test_domain_analysis(analyzer):
    """Test domain analyzer"""
    result = analyzer.analyze("Healthcare")
    assert "domain" in result
    assert "analysis" in result
    assert len(result["analysis"]) > 0

def test_idea_generation(generator):
    """Test idea generator"""
    analysis = "Test analysis of healthcare domain"
    ideas = generator.generate("Healthcare", analysis, num_ideas=2)
    
    assert len(ideas) == 2
    assert all(isinstance(idea, ProjectIdea) for idea in ideas)
    assert all(idea.title for idea in ideas)
    assert all(idea.description for idea in ideas)

def test_complexity_estimation(generator):
    """Test complexity estimator"""
    from src.complexity_estimator import get_complexity_estimator
    
    estimator = get_complexity_estimator()
    ideas = [ProjectIdea(
        title="Test Idea",
        description="Test description",
        use_case="Testing",
        potential_impact="High"
    )]
    
    results = estimator.estimate(ideas)
    
    assert len(results) == 1
    assert 0 <= results[0].overall_score <= 10
    assert results[0].difficulty_level in ["Beginner", "Intermediate", "Advanced"]
```

### Frontend Tests

Create `frontend/src/App.test.js`:

```javascript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';
import * as api from './api';

jest.mock('./api');

describe('App Component', () => {
  test('renders input form', () => {
    render(<App />);
    
    expect(screen.getByPlaceholderText(/Domain or Problem Area/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Additional Context/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Generate Ideas/i })).toBeInTheDocument();
  });

  test('handles form submission', async () => {
    const mockResult = {
      input_domain: "Healthcare",
      ideas: [],
      tech_stacks: [],
      complexity_analysis: [],
      scoring: [],
      recommendations: []
    };

    api.evaluateDomain.mockResolvedValueOnce(mockResult);

    render(<App />);

    fireEvent.change(screen.getByPlaceholderText(/Domain or Problem Area/i), {
      target: { value: 'Healthcare' }
    });

    fireEvent.click(screen.getByRole('button', { name: /Generate Ideas/i }));

    await waitFor(() => {
      expect(api.evaluateDomain).toHaveBeenCalledWith('Healthcare', '');
    });
  });

  test('displays error on API failure', async () => {
    api.evaluateDomain.mockRejectedValueOnce(new Error('API Error'));

    render(<App />);

    fireEvent.change(screen.getByPlaceholderText(/Domain or Problem Area/i), {
      target: { value: 'Healthcare' }
    });

    fireEvent.click(screen.getByRole('button', { name: /Generate Ideas/i }));

    await waitFor(() => {
      expect(screen.getByText(/API Error/i)).toBeInTheDocument();
    });
  });
});
```

## Integration Tests

### Backend Integration Test

Create `backend/tests/test_integration.py`:

```python
import pytest
from src.orchestrator import get_orchestrator

@pytest.fixture
def orchestrator():
    return get_orchestrator()

def test_full_evaluation_pipeline(orchestrator):
    """Test complete evaluation pipeline"""
    result = orchestrator.evaluate(
        domain="Fintech",
        context="Peer-to-peer lending",
        num_ideas=2
    )
    
    # Verify all components executed
    assert result.input_domain == "Fintech"
    assert len(result.ideas) == 2
    assert len(result.tech_stacks) == 2
    assert len(result.complexity_analysis) == 2
    assert len(result.scoring) == 2
    assert len(result.recommendations) > 0
    
    # Verify data integrity
    for score in result.scoring:
        assert 0 <= score.feasibility_score <= 100
        assert 0 <= score.innovation_score <= 100
        assert 0 <= score.market_potential_score <= 100
        assert 0 <= score.overall_score <= 100

def test_evaluation_with_context(orchestrator):
    """Test evaluation with additional context"""
    result = orchestrator.evaluate(
        domain="Fintech",
        context="Focus on underbanked populations in Africa",
        num_ideas=1
    )
    
    assert result.input_domain == "Fintech"
    assert len(result.ideas) == 1
```

## End-to-End Tests

### E2E Test Suite

Create `frontend/cypress/e2e/app.cy.js`:

```javascript
describe('AI Project Idea Generator E2E', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3001');
  });

  it('generates ideas for a domain', () => {
    // Enter domain
    cy.get('input[placeholder*="Domain"]').type('Healthcare AI');

    // Enter context
    cy.get('textarea').type('Focus on diagnosis tools');

    // Submit
    cy.get('button').contains('Generate Ideas').click();

    // Wait for loading to complete
    cy.contains('Results for:', { timeout: 60000 }).should('be.visible');

    // Verify results appear
    cy.contains('Ideas').should('be.visible');
    cy.contains('Scoring').should('be.visible');
    cy.contains('Tech Stack').should('be.visible');

    // Click on Scoring tab
    cy.contains('button', 'Scoring').click();
    cy.contains('Feasibility').should('be.visible');

    // Click on Tech Stack tab
    cy.contains('button', 'Tech Stack').click();
    cy.contains('Backend').should('be.visible');
  });

  it('displays error messages', () => {
    // Try to submit without domain
    cy.get('button').contains('Generate Ideas').click();
    cy.contains('Please enter a domain').should('be.visible');
  });

  it('clears form after successful submission', () => {
    cy.get('input[placeholder*="Domain"]').should('have.value', '');

    cy.get('input[placeholder*="Domain"]').type('EdTech');
    cy.get('button').contains('Generate Ideas').click();

    cy.contains('Results for:', { timeout: 60000 }).should('be.visible');

    cy.get('input[placeholder*="Domain"]').should('have.value', '');
  });
});
```

## Manual Testing Checklist

### Backend

- [ ] API starts without errors
- [ ] Health check endpoint works
- [ ] Can evaluate a domain
- [ ] All 5 ideas are generated
- [ ] Scoring ranges 0-100
- [ ] Tech stack has multiple items
- [ ] Recommendations are meaningful
- [ ] Error handling works (invalid input)
- [ ] Timeout handling works (slow API)

### Frontend

- [ ] Page loads correctly
- [ ] Form inputs accept text
- [ ] Loading indicator appears
- [ ] Results display after completion
- [ ] All tabs (Ideas, Scoring, etc.) work
- [ ] Responsive on mobile
- [ ] Error messages appear
- [ ] Can submit multiple requests

### Integration

- [ ] Backend and frontend communicate
- [ ] CORS headers are correct
- [ ] API authentication works (if enabled)
- [ ] Network errors are handled
- [ ] Retry logic works

## Performance Testing

### Load Testing

Create `backend/tests/test_load.py`:

```python
import time
from src.orchestrator import get_orchestrator

def test_concurrent_requests():
    """Test multiple concurrent requests"""
    import concurrent.futures
    
    orchestrator = get_orchestrator()
    
    def evaluate():
        start = time.time()
        orchestrator.evaluate("Healthcare")
        return time.time() - start
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        times = list(executor.map(lambda _: evaluate(), range(3)))
    
    avg_time = sum(times) / len(times)
    print(f"Average time: {avg_time:.2f}s")
    
    assert avg_time < 120  # Should complete in < 2 minutes
```

## Debugging

### Backend Debugging

```python
# Add logging
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Analyzing domain...")
logger.info("Ideas generated")
logger.error("Error during evaluation")
```

### Frontend Debugging

```javascript
// In browser console
localStorage.setItem('debug', '*');

// Or in code
console.debug('Domain:', domain);
console.log('Results:', evaluation);
console.error('Error:', error);
```

## Continuous Integration

### GitHub Actions

Create `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install -r backend/requirements.txt pytest
      - run: cd backend && pytest

  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '16'
      - run: cd frontend && npm install
      - run: npm run test -- --coverage
```

## Test Coverage

### Backend Coverage

```bash
pip install pytest-cov

pytest --cov=src --cov-report=html
```

### Frontend Coverage

```bash
npm run test -- --coverage
```

## Reporting Bugs

When reporting bugs, include:

1. **Steps to reproduce**
2. **Expected behavior**
3. **Actual behavior**
4. **Error logs**
5. **Environment** (OS, Python version, etc.)
6. **Screenshots** (if UI related)

Example:

```
Title: Error when evaluating "Healthcare" domain

Steps:
1. Enter "Healthcare" in domain field
2. Click "Generate Ideas"

Expected: Ideas are generated within 60 seconds
Actual: Timeout error after 30 seconds

Error Log:
```
Connection timeout to OpenAI API
```

Environment:
- OS: Windows 11
- Python: 3.11.0
- API Key: Valid (tested with OpenAI CLI)
```

---

**Run tests frequently during development!**

```bash
# Backend
cd backend
pytest -v

# Frontend
cd frontend
npm test -- --watch
```
