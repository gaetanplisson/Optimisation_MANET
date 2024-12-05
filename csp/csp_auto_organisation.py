from interfaces import *
from utils import *
import minizinc
import random

def auto_organisation(agent, constants):
    """Compute the route of the network: la route optimale pour un broadcast depuis l'agent
    Renvoit un dictionnaire tel que {agent: [suceceurs_neighbours]}
    """
    model = minizinc.Model()
    model.add_file("auto_organisation.mzn")

    gecode = minizinc.Solver.lookup("gecode")
    instance = minizinc.Instance(gecode, model)

    instance["num_agents"] = agent.get_manet_agent_numbers()
    instance["num_positions"] = len(agent.position_graph().positions())
    instance["Mp"] = agent.position_graph().graph_matrix()
    instance["position_range"] = 1.

    # Solve the instance
    result = instance.solve()

    # Process the result
    if result.status.has_solution():
        solution = result.solution
        # Extract the relevant information from the solution
        # For example, you can extract the routes or other variables
        pos = {agent: solution["positions"][agent] for agent in range(1, constants["num_agents"] + 1)}
        return pos
    else:
        print("No solution found")
        return None

# Example usage
constants = {
    "num_agents": 5,
    "num_positions": 5,
    "Mp": [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 1, 0, 1, 2], [3, 2, 1, 0, 1], [4, 3, 2, 1, 0]],
    "position_range": 2.0
}
agent = 1
csp_prog = "auto_organisation.mzn"
routes = auto_organisation(agent, csp_prog, constants)
print(routes)