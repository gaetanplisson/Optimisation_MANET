from interfaces import *
from utils import *
import minizinc
def compute_route(agent, csp_prog, constants):
    """Compute the route of the network: la route optimale pour un broadcast depuis l'agent
    Renvoit un dictionnaire tel que {agent: [suceceurs_neighbours]}
    """
    generic({ agent: []})
    
    model = minizinc.Model()
    model.add_file('compute_route.mzn')
    
    gecode = minizinc.Solver.lookup('gecode')
    instance = minizinc.Instance(gecode, model)
    
    instance['num_agents'] = agent.get_manet_agent_numbers()
    instance['num_positions'] = len(agent.position_graph().positions())
    instance['Mp'] = agent.position_graph().graph_matrix()
    instance['position_range'] = 1.
    
    # Solve the instance
    result = instance.solve()
    
    # Process the result
    if result.status.has_solution():
        solution = result.solution
        # Extract the relevant information from the solution
        # For example, you can extract the routes or other variables
        route = {agent: solution["route"][agent] for agent in range(1, constants["num_agents"] + 1)}
        return route
    else:
        print("No solution found")
        return None
    
    pass