%Trouver l'agent qui minimise les coûts
%Trouver l'agent qui minimise les coûts

include "globals.mzn";

% Nombre d'agents
int: n;

% Matrice des coûts entre les agents
array[1..n, 1..n] of int: costs;

% Variable de décision : l'agent choisi
var 1..n: chosen_agent;

% Fonction objectif : minimiser la somme des coûts entre l'agent choisi et tous les autres agents
var int: total_cost = sum(i in 1..n where i != chosen_agent) (costs[chosen_agent, i]);

constraint
    % Les coûts doivent être symétriques (coût de i à j est le même que de j à i)
    forall(i in 1..n, j in 1..n where i != j) (
        costs[i, j] = costs[j, i]
    );

solve minimize total_cost;

output ["Chosen agent: \(chosen_agent)\nTotal cost: \(total_cost)\n"];
