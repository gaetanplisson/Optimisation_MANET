%trouver les chemins optimaux

include "globals.mzn";

% Nombre d'agents
int: n;

% Matrice des coûts entre les agents
array[1..n, 1..n] of int: costs;

% L'agent leader
int: leader;

% Variables de décision : les chemins optimaux
array[1..n] of var 1..n: predecessors; % Le prédécesseur de chaque agent dans le chemin optimal

% Fonction objectif : minimiser la somme des coûts des chemins depuis le leader à tous les autres agents
var int: total_cost = sum(i in 1..n where i != leader) (costs[predecessors[i], i]);

constraint
    % Les coûts doivent être symétriques (coût de i à j est le même que de j à i)
    forall(i in 1..n, j in 1..n where i != j) (
        costs[i, j] = costs[j, i]
    );

constraint
    % Le leader n'a pas de prédécesseur
    predecessors[leader] = leader;

constraint
    % Chaque agent doit avoir un prédécesseur différent de lui-même sauf le leader
    forall(i in 1..n where i != leader) (
        predecessors[i] != i
    );

constraint
    % Les prédécesseurs doivent former un arbre couvrant
    forall(i in 1..n where i != leader) (
        exists(j in 1..n) (predecessors[i] = j)
    );

solve minimize total_cost;

output [
    "Leader: \(leader)\n",
    "Total cost: \(total_cost)\n",
    "Predecessors: \(predecessors)\n"
];
