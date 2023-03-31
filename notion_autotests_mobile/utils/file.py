def abs_path_from_project(relative_path: str):
    import notion_autotests_mobile
    from pathlib import Path

    return (
        Path(notion_autotests_mobile.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
