"""Configuration for the Cedarbrook triage service.

Decided here and only here: defaults below, environment
variables override. (Fictional codebase, written for FDE 1.07.)
"""
import os

DEFAULTS = {
    "data_path": "data/tickets_export.csv",
    "retry_limit": 3,
    "batch_size": 50,
}

ENV_OVERRIDES = {
    "data_path": "TRIAGE_DATA_PATH",
    "retry_limit": "TRIAGE_RETRY_LIMIT",
    "batch_size": "TRIAGE_BATCH_SIZE",
}


def load_config():
    config = dict(DEFAULTS)
    for key, env_var in ENV_OVERRIDES.items():
        raw = os.environ.get(env_var)
        if raw is not None:
            config[key] = int(raw) if key != "data_path" else raw
    return config
