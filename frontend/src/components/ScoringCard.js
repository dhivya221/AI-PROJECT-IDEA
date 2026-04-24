import React from 'react';
import { TrendingUp } from 'lucide-react';

export default function ScoringCard({ idea, score }) {
  const ScoreBar = ({ label, value }) => (
    <div className="mb-4">
      <div className="flex justify-between mb-1">
        <span className="text-sm text-slate-300">{label}</span>
        <span className="text-sm font-semibold text-purple-400">{value}/100</span>
      </div>
      <div className="w-full bg-slate-600 rounded-full h-2">
        <div
          className="bg-gradient-to-r from-purple-500 to-pink-500 h-2 rounded-full transition-all"
          style={{ width: `${value}%` }}
        />
      </div>
    </div>
  );

  return (
    <div className="bg-slate-700/50 rounded-lg p-6 border border-purple-500/20">
      <h3 className="text-xl font-bold text-purple-400 mb-6 flex items-center gap-2">
        <TrendingUp size={20} />
        {idea.title}
      </h3>

      <div className="space-y-6">
        <div>
          <ScoreBar label="Feasibility" value={score.feasibility_score} />
          <ScoreBar label="Innovation" value={score.innovation_score} />
          <ScoreBar label="Market Potential" value={score.market_potential_score} />
        </div>

        <div className="bg-slate-600/50 rounded-lg p-4 border border-purple-500/20">
          <div className="text-center">
            <p className="text-sm text-slate-400 mb-1">Overall Score</p>
            <p className="text-3xl font-bold text-purple-400">{score.overall_score.toFixed(1)}</p>
            <p className="text-xs text-slate-400 mt-1">/100</p>
          </div>
        </div>

        {score.breakdown && (
          <div className="text-sm space-y-2">
            {Object.entries(score.breakdown).map(([key, value]) => {
              if (typeof value === 'string') {
                return (
                  <div key={key}>
                    <p className="text-slate-400 capitalize">
                      {key.replace(/_/g, ' ')}:
                    </p>
                    <p className="text-slate-300 ml-2">{value}</p>
                  </div>
                );
              }
              return null;
            })}
          </div>
        )}
      </div>
    </div>
  );
}
