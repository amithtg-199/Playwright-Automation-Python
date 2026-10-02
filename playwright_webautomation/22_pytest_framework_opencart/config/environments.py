import os
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass


ENV_PATH = Path(__file__).resolve().parent/".env"
load_dotenv(dotenv_path=ENV_PATH)

def get_required_env(name:str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Required environment variable '{name}' is not configured"
        )
    return value

@dataclass(frozen=True)
class EnvironmentConfig:
    name: str
    base_url: str
    username: str
    password: str

ENV_CONFIG = {
    "dev": EnvironmentConfig(
        name="dev",
        base_url=get_required_env("DEV_BASE_URL"),
        username=get_required_env("DEV_USERNAME"),
        password=get_required_env("DEV_PASSWORD"),
    ),

    "uat": EnvironmentConfig(
        name="uat",
        base_url=get_required_env("UAT_BASE_URL"),
        username=get_required_env("UAT_USERNAME"),
        password=get_required_env("UAT_PASSWORD"),
    ),

    "preprod": EnvironmentConfig(
        name="preprod",
        base_url=get_required_env("PREPROD_BASE_URL"),
        username=get_required_env("PREPROD_USERNAME"),
        password=get_required_env("PREPROD_PASSWORD"),
    ),
}
