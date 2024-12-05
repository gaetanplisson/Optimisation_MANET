% Nombre d'agents
int: n;

% Matrice des poids des arêtes
array[1..n, 1..n] of int: M;

% Énergie des agents
array[1..n] of int: e;

% Matrice des plus courts chemins
array[1..n, 1..n] of var int: d;

% Variable à optimiser : index du meneur
var 1..n: leader;

% Initialisation de la matrice des distances
constraint forall(i, j in 1..n) (
    d[i, j] = M[i, j]
);

% Application de l'algorithme de Floyd-Warshall
constraint forall(k in 1..n) (
    forall(i, j in 1..n) (
        d[i, j] = min(d[i, j], d[i, k] + d[k, j])
    )
);

% Définition de la distance moyenne D_i pour l'agent i
array[1..n] of var float: D = [
    sum(j in 1..n where j != i) (d[i, j]) / (n - 1) | i in 1..n
];

% Facteur multiplicatif de l'énergie disponible
array[1..n] of var float: lambda = [
    if sum(j in 1..n where j != i) (e[j] * M[i, j]) = 0 then 0 else 1.0 / sum(j in 1..n where j != i) (e[j] * M[i, j]) endif | i in 1..n
];

% Objectif : minimiser D_i * lambda_i
var float: objective = D[leader] * lambda[leader];

solve minimize objective;

output [
    "Leader: \(leader)\n",
    "Objective: \(objective)\n"
];
