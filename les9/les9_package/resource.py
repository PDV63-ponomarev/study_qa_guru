from pathlib import Path

import les9


def path(file_name):
    return str(
        Path(les9.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )
