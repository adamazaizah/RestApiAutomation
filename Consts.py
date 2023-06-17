from pathlib import Path

class ProjectConsts:
    current_dir = Path(__file__)
    # Root Directory of the project.
    ROOT_DIR = next(
        p for p in current_dir.parents if p.parts[-1] == 'RestApiAutomation'
    )
