import React, { useState } from 'react';
import { evaluateDomain } from './api';
import { Loader, AlertCircle } from 'lucide-react';
import IdeaCard from './components/IdeaCard';
import ScoringCard from './components/ScoringCard';
import TechStackCard from './components/TechStackCard';

function App() {
  const [domain, setDomain] = useState('');
  const [context, setContext] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [evaluation, setEvaluation] = useState(null);
  const [activeTab, setActiveTab] = useState('ideas');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!domain.trim()) {
      setError('Please enter a domain');
      return;
    }

    setLoading(true);
    setError('');
    setEvaluation(null);

    try {
      const result = await evaluateDomain(domain, context);
      setEvaluation(result);
      setDomain('');
      setContext('');
    } catch (err) {
      setError(err.message || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Header */}
      <header className="bg-slate-900 border-b border-purple-500/20">
        <div className="max-w-6xl mx-auto px-4 py-6">
          <h1 className="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">
            🧠 AI Project Idea Generator
          </h1>
          <p className="text-slate-400 mt-2">Generate and evaluate AI project ideas based on your domain</p>
        </div>
      </header>

      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Input Section */}
        <div className="bg-slate-800 rounded-lg border border-purple-500/20 p-6 mb-8">
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-300 mb-2">
                Domain or Problem Area
              </label>
              <input
                type="text"
                value={domain}
                onChange={(e) => setDomain(e.target.value)}
                placeholder="e.g., Healthcare, E-commerce, Education, Climate Tech..."
                className="w-full px-4 py-3 bg-slate-700 border border-purple-500/30 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:border-purple-500"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-300 mb-2">
                Additional Context (Optional)
              </label>
              <textarea
                value={context}
                onChange={(e) => setContext(e.target.value)}
                placeholder="Describe more about your domain, target users, or specific challenges..."
                rows="3"
                className="w-full px-4 py-3 bg-slate-700 border border-purple-500/30 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:border-purple-500"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 disabled:opacity-50 text-white font-semibold py-3 rounded-lg transition duration-200 flex items-center justify-center gap-2"
            >
              {loading ? (
                <>
                  <Loader className="animate-spin" size={20} />
                  Generating Ideas...
                </>
              ) : (
                'Generate Ideas'
              )}
            </button>
          </form>

          {error && (
            <div className="mt-4 p-4 bg-red-900/20 border border-red-500/50 rounded-lg flex gap-3 text-red-300">
              <AlertCircle size={20} className="flex-shrink-0" />
              <p>{error}</p>
            </div>
          )}
        </div>

        {/* Results Section */}
        {evaluation && (
          <div className="space-y-6">
            <div className="bg-slate-800 rounded-lg border border-purple-500/20 p-6">
              <h2 className="text-2xl font-bold text-purple-400 mb-4">
                Results for: <span className="text-white">{evaluation.input_domain}</span>
              </h2>

              {/* Tabs */}
              <div className="flex gap-2 mb-6 border-b border-slate-700">
                <button
                  onClick={() => setActiveTab('ideas')}
                  className={`px-4 py-2 font-medium transition ${
                    activeTab === 'ideas'
                      ? 'text-purple-400 border-b-2 border-purple-400'
                      : 'text-slate-400 hover:text-slate-300'
                  }`}
                >
                  Ideas
                </button>
                <button
                  onClick={() => setActiveTab('scoring')}
                  className={`px-4 py-2 font-medium transition ${
                    activeTab === 'scoring'
                      ? 'text-purple-400 border-b-2 border-purple-400'
                      : 'text-slate-400 hover:text-slate-300'
                  }`}
                >
                  Scoring
                </button>
                <button
                  onClick={() => setActiveTab('techstack')}
                  className={`px-4 py-2 font-medium transition ${
                    activeTab === 'techstack'
                      ? 'text-purple-400 border-b-2 border-purple-400'
                      : 'text-slate-400 hover:text-slate-300'
                  }`}
                >
                  Tech Stack
                </button>
                <button
                  onClick={() => setActiveTab('recommendations')}
                  className={`px-4 py-2 font-medium transition ${
                    activeTab === 'recommendations'
                      ? 'text-purple-400 border-b-2 border-purple-400'
                      : 'text-slate-400 hover:text-slate-300'
                  }`}
                >
                  Recommendations
                </button>
              </div>

              {/* Tab Content */}
              {activeTab === 'ideas' && (
                <div className="grid gap-4">
                  {evaluation.ideas.map((idea, idx) => (
                    <IdeaCard
                      key={idx}
                      idea={idea}
                      complexity={evaluation.complexity_analysis[idx]}
                    />
                  ))}
                </div>
              )}

              {activeTab === 'scoring' && (
                <div className="grid gap-4">
                  {evaluation.scoring.map((score, idx) => (
                    <ScoringCard
                      key={idx}
                      idea={evaluation.ideas[idx]}
                      score={score}
                    />
                  ))}
                </div>
              )}

              {activeTab === 'techstack' && (
                <div className="grid gap-4">
                  {evaluation.tech_stacks.map((stack, idx) => (
                    <TechStackCard
                      key={idx}
                      idea={evaluation.ideas[idx]}
                      stack={stack}
                    />
                  ))}
                </div>
              )}

              {activeTab === 'recommendations' && (
                <div className="bg-slate-700/50 rounded-lg p-6 border border-purple-500/20">
                  <h3 className="text-xl font-semibold text-purple-400 mb-4">Strategic Recommendations</h3>
                  <ul className="space-y-3">
                    {evaluation.recommendations.map((rec, idx) => (
                      <li key={idx} className="text-slate-300 flex gap-3">
                        <span className="text-purple-400 font-bold flex-shrink-0">{idx + 1}.</span>
                        <span>{rec}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Empty State */}
        {!evaluation && !loading && (
          <div className="text-center py-16">
            <p className="text-slate-400 text-lg">Enter a domain to get started generating ideas</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
