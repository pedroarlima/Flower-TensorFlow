import flwr as fl

def get_on_fit_config_fn() -> Callable[[int], Dict[str, str]]:

    def fit_config(rnd: int) -> Dict[str, str]:
        config = {
            "learning_rate": str(0.001),
            "batch_size": str(32),
        }
        return config

    return fit_config

strategy = fl.server.strategy.FedAvg(
    fraction_fit=0.1,
    min_fit_clients=5,
    min_available_clients=10,
    on_fit_config_fn=get_on_fit_config_fn(),
)

fl.server.start_server("localhost:8080", config={"num_rounds": 6}, strategy=strategy)

