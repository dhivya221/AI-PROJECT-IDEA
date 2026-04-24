import React from 'react';
import { Code2 } from 'lucide-react';

export default function TechStackCard({ idea, stack }) {
  const getCategoryColor = (category) => {
    const colors = {
      'Backend Framework': 'bg-blue-900/30 border-blue-500/30 text-blue-300',
      'Backend': 'bg-blue-900/30 border-blue-500/30 text-blue-300',
      'Frontend Framework': 'bg-green-900/30 border-green-500/30 text-green-300',
      'Frontend': 'bg-green-900/30 border-green-500/30 text-green-300',
      'Database': 'bg-purple-900/30 border-purple-500/30 text-purple-300',
      'Deployment/Hosting': 'bg-pink-900/30 border-pink-500/30 text-pink-300',
      'AI/ML Libraries': 'bg-yellow-900/30 border-yellow-500/30 text-yellow-300',
    };
    return colors[category] || 'bg-slate-700/30 border-slate-500/30 text-slate-300';
  };

  return (
    <div className="bg-slate-700/50 rounded-lg p-6 border border-purple-500/20">
      <h3 className="text-xl font-bold text-purple-400 mb-6 flex items-center gap-2">
        <Code2 size={20} />
        {idea.title}
      </h3>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {stack.map((tech, idx) => (
          <div
            key={idx}
            className={`rounded-lg p-4 border ${getCategoryColor(tech.category)}`}
          >
            <div className="font-semibold mb-2">{tech.tool}</div>
            <div className="text-xs opacity-75 mb-2">{tech.category}</div>
            <div className="text-sm opacity-90">{tech.reason}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
