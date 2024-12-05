% Auto Organisation du Manet

% Nombre d'agents dans le réseau
int: num_agents;
set of int: Agents = 1..num_agents;

% Nombre de positions
int: num_positions;
set of int: Positions = 1..num_positions;

% Matrice de positions
array[Positions, Positions] of int: Mp;

% Portée de la position
float: position_range;

% Matrice de distances M[i,j] = 1 si Mp[i,j] <= position_range, 0 sinon
array[Agents, Agents] of int: M = array2d(Agents, Agents, [if Mp[i, j] <= position_range then 1 else 0 endif | i in Agents, j in Agents]);

% Matrice de reachabilité
array[Agents, Agents] of int: R;

% Agent meneur
int: A0 = 1;

% Matrice des plus courts chemins
array[Agents, Agents] of var int: d;

% Énergie moyenne
var float: E = sum(i, j in Agents)(d[i, j]) / (num_agents * num_agents);

% Faiblesse énergétique d'un agent
array[Agents] of var float: DeltaE;
array[Agents] of var int: DeltaN;
array[Agents] of var float: f;

% Contraintes pour définir n
array[Agents] of var int: n_i;


% Initialisation de la matrice des distances
constraint forall(i, j in Agents)(
    d[i, j] = M[i, j]
);

% Application de l'algorithme de Floyd-Warshall
constraint forall(k in Agents)(
    forall(i, j in Agents)(
        d[i, j] = min(d[i, j], d[i, k] + d[k, j])
    )
);



% Définition de la faiblesse mixte
constraint forall(i in Agents)(
    f[i] = (DeltaN[i] + 1) * DeltaE[i]
);

% Définition de la robustesse
var float: robustness = sum(i in Agents)(f[i]);

% Algorithme de résolution par contrainte

% 1. Contraintes pour définir n
constraint forall(i in Agents)(
    n_i[i] = sum(j in Agents)(if R[i, j] != 0 \/ R[j, i] != 0 then 1 else 0 endif)
);

% 3. Perte d'agent
constraint forall(i in Agents)(
    let {
        array[Agents, Agents] of var int: M_2 = array2d(Agents, Agents, [if j != i then M[j, k] else 0 endif | j in Agents, k in Agents]);
        var int: n_i_prime = sum(j in Agents)(if M_2[i, j] != 0 \/ M_2[j, i] != 0 then 1 else 0 endif);
    } in
    DeltaN[i] = n_i[i] - n_i_prime
);

% 4. Perte énergétique
% Étape 1 : Calcul de M_prime
array[Agents, Agents] of var int: M_prime;
constraint forall(i in Agents)(
    forall(j, k in Agents)(
        M_prime[j, k] = if j != i /\ k != i then M[j, k] else -1 endif
    )
);

% Étape 2 : Initialisation de la matrice des distances pour M_prime
array[Agents, Agents] of var int: d_i;
constraint forall(i in Agents)(
    forall(j, k in Agents)(
        d_i[j, k] = M_prime[j, k]
    )
);

% Étape 3 : Application de l'algorithme de Floyd-Warshall pour M_prime
constraint forall(i in Agents)(
    forall(l in Agents)(
        forall(j, k in Agents)(
            d_i[j, k] = min(d_i[j, k], d_i[j, l] + d_i[l, k])
        )
    )
);

% Étape 4 : Calcul de E_i
array[Agents] of var float: E_i;
constraint forall(i in Agents)(
    E_i[i] = sum(j, k in Agents where j != i /\ k != i)(d_i[j, k]) / (num_agents * num_agents)
);

% Étape 5 : Calcul de DeltaE
constraint forall(i in Agents)(
    DeltaE[i] = E - E_i[i]
);

% 5. Faiblesse mixte
constraint forall(i in Agents)(
    f[i] = (DeltaN[i] + 1) * DeltaE[i]
);

% 6. Optimisation
solve minimize sum(i in Agents)(f[i]);

