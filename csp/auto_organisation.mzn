% Auto Organisation du Manet

% Nombre d'agents dans le réseau
int: num_agents;
set of int: Agents = 1..num_agents;


% Matrice de transition
array[Agents, Agents] of var int: M;

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

solve satisfy;

% Calcul de la matrice de reachabilité R
constraint forall(i, j in Agents)(
    R[i, j] = if i == j then 1 else if M[i, j] != 0 then 1 else 0 endif
);% simplification

% Définition de la faiblesse énergétique d'un agent
constraint forall(i in Agents)(
    DeltaE[i] = let {
        array[Agents, Agents] of var int: M_prime = [if j != i and k != i then M[j, k] else int(inf) endif | j, k in Agents];
        array[Agents, Agents] of var int: d_i = array2d(Agents, Agents, [if j != i and k != i then M[j, k] else int(inf) endif | j, k in Agents]);
    } in
    % Application de l'algorithme de Floyd-Warshall pour M_prime
    forall(l in Agents)(
        forall(j, k in Agents)(
            d_i[j, k] = min(d_i[j, k], d_i[j, l] + d_i[l, k])
        )
    ) /\
    let {
        var float: E_i = sum(j, k in Agents where j != i and k != i)(d_i[j, k]) / (num_agents * num_agents)
    } in
    E - E_i
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
    n_i[i] = sum(j in Agents)(if R[i, j] != 0 or R[j, i] != 0 then 1 else 0 endif)
);

% 3. Perte d'agent
constraint forall(i in Agents)(
    let {
        array[Agents, Agents] of var int: M_prime = [if j != i then M[j, k] else 0 endif | j, k in Agents];
        var int: n_i_prime = sum(j in Agents)(if M_prime[i, j] != 0 or M_prime[j, i] != 0 then 1 else 0 endif);
    } in
    DeltaN[i] = n_i[i] - n_i_prime
);

% 4. Perte énergétique
constraint forall(i in Agents)(
    let {
        array[Agents, Agents] of var int: M_prime = [if j != i and k != i then M[j, k] else int(inf) endif | j, k in Agents];
        array[Agents, Agents] of var int: d_i;

        % Initialisation de la matrice des distances pour M_prime
        constraint forall(j, k in Agents)(
            d_i[j, k] = M_prime[j, k]
        );

        % Application de l'algorithme de Floyd-Warshall pour M_prime
        constraint forall(l in Agents)(
            forall(j, k in Agents)(
                d_i[j, k] = min(d_i[j, k], d_i[j, l] + d_i[l, k])
            )
        );

        % solve minimize sum(i, j in Agents)(d_i[i, j]);
        solve satisfy;

        var float: E_i = sum(j, k in Agents)(d_i[j, k]) / (num_agents * num_agents);
    } in
    DeltaE[i] = E - E_i
);

% 5. Faiblesse mixte
constraint forall(i in Agents)(
    f[i] = (DeltaN[i] + 1) * DeltaE[i]
);

% 6. Optimisation
solve minimize sum(i in Agents)(f[i]);

