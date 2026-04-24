import React from 'react';
import { Zap, Clock, AlertTriangle } from 'lucide-react';

export default function IdeaCard({ idea, complexity }) {
  return (
    <div className="bg-slate-700/50 rounded-lg p-6 border border-purple-500/20 hover:border-purple-500/40 transition">
      <h3 className="text-xl font-bold text-purple-400 mb-2">{idea.title}</h3>
      <p className="text-slate-300 mb-4">{idea.description}</p>

      <div className="grid grid-cols-2 gap-4 mb-4">
        <div>
          <p className="text-sm text-slate-400">Use Case</p>
          <p className="text-slate-200">{idea.use_case}</p>
        </div>
        <div>
          <p className="text-sm text-slate-400">Potential Impact</p>
          <p className="text-slate-200">{idea.potential_impact}</p>
        </div>
      </div>

      {complexity && (
        <div className="border-t border-slate-600 pt-4 space-y-2">
          <div className="flex items-center gap-2">
            <Zap size={16} className="text-yellow-400" />
            <span className="text-sm text-slate-300">
              Complexity: <span className="font-semibold">{complexity.overall_score}/10</span>
            </span>
          </div>
          <div className="flex items-center gap-2">
            <Clock size={16} className="text-blue-400" />
            <span className="text-sm text-slate-300">
              Est. Time: <span className="font-semibold">{complexity.development_time}</span>
            </span>
          </div>
          <div className="flex items-center gap-2">
            <AlertTriangle size={16} className="text-red-400" />
            <span className="text-sm text-slate-300">
              Difficulty: <span className="font-semibold">{complexity.difficulty_level}</span>
            </span>
          </div>
        </div>
      )}
    </div>
  );
}
