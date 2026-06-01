import os


def get_env(name: str) -> str:
    value = os.getenv(name)

    if value is None:
        raise ValueError(
            f"Environment variable '{name}' not found"
        )

    return value


def get_env_int(name: str) -> int:
    return int(get_env(name))