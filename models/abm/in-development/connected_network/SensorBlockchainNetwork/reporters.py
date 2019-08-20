import numpy as np
import pandas as pd

def get_total_data_collected(agent):
    return agent.db.sum()


def get_active_sensors_at_current_tick(model):
    return len([a for a in model.schedule.agents if np.isnan(a.dead)])


def get_informational_currency(agent):
    """
    Calculate the proportion of data collected by a
    sensor that has been committed to the chain.

    **Note: This counts each tick as equal, even if
    different volumes of data were collected during
    the ticks.**

    Attributes:
        agent: The Sensor for which to calculate
            informational currency measure.
        window: The window through which to measure.

            If window = 1, check proportion of data
            reflected on chain from all time.

            If window > 1, check proportion of data in
            most recent n=window ticks that is reflected
            on chain
    """

    model = agent.model
    agent_id = agent.unique_id
    window = model.info_currency_window

    if window == 1 or window > len(model.blockchain.chain):
        try:
            return model.blockchain.chain[agent_id].value_counts()[True] / len(model.blockchain.chain[agent_id])
        except KeyError:
            return 0

    else:
        df = model.blockchain.chain[window * -1 :] # Last n rows
        try:
            return df[agent_id].value_counts()[True] / len(df[agent_id])
        except KeyError:
            return 0
