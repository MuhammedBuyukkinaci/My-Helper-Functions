from dataclasses import dataclass

@dataclass
class Paths:
    log: str
    data: str


@dataclass
class Params:
    epoch_count: int
    lr: float
    batch_size: int


@dataclass
class ConfigDC:
    paths: Paths
    params: Params
