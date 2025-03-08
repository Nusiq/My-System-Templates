[
    # GIT & PRETTIER
    {
        "source": "regolith/.gitignore",
        "target": "./"
    },
    {
        "source": "regolith/.prettierignore",
        "target": "./"
    },
    # VSCODE
    *[{
        "source": p.as_posix(),
        "target": p.relative_to("regolith").as_posix(),
        "json_template": True
    } for p in Path("regolith/.vscode/").rglob("*.json") if p.is_file()],
    # NODEJS SETUP
    {
        "source": "regolith/package.json",
        "target": "./",
        "json_template": True
    },
    # REGOLITH
    {
        "source": "regolith/config.json",
        "target": "./",
        "json_template": True
    },
    # WORKSPACES
    {
        "source": "regolith/main.code-workspace",
        "target": f"{project_name}.code-workspace",
    },
    {
        "source": "regolith/debug.code-workspace",
        "target": f"{project_name} Debug.code-workspace",
    },
    # REGOLITH -> DEBUG
    *[{
        "source": p.as_posix(),
        "target": p.relative_to("regolith").as_posix(),
        "json_template": True
    } for p in Path("regolith/debug/.vscode/").rglob("*.json") if p.is_file()],
    {
        "source": "regolith/debug/.vscode/prepare_debug.bat",
        "target": "debug/.vscode/prepare_debug.bat",
    },
    # REGOLITH -> FILTERS DATA
    {
        "source": "regolith/filters_data/scope.json",
        "target": "filters_data/scope.json",
    },
    {
        "source": "regolith/filters_data/system_template_esbuild/main.ts",
        "target": "filters_data/system_template/main.ts"
    },
    {
        "source": "regolith/filters_data/system_template/auto_map.json",
        "target": "filters_data/system_template/auto_map.json",
        "json_template": True
    },
    {
        "source": "regolith/filters_data/system_template/.gitignore",
        "target": "filters_data/system_template/.gitignore"
    },
    *[{
        "source": p.as_posix(),
        "target": p.relative_to("regolith").as_posix(),
    } for p in Path("regolith/filters_data/system_template/_plugins").rglob("*") if p.is_file()],
    # REGOLITH -> PACKS
    # JSON files
    *[{
        "source": p.as_posix(),
        "target": p.relative_to("regolith").as_posix(),
        "json_template": True
    } for p in Path("regolith/packs/").rglob("*.json")],
    # Lang Files
    *[{
        "source": p.as_posix(),
        "target": p.relative_to("regolith").as_posix(),
        "subfunctions": True
    } for p in Path("regolith/packs/").rglob("*.lang")],
    # WORLDS
    *[{
        "source": p.as_posix(),
        "target": p.relative_to("regolith").as_posix()\
            .replace("/world/", f'/{project_name_dashes}/'),
        "json_template": True
    } for p in Path("regolith/worlds/").rglob("*.json")],
    # Lang Files
    *[{
        "source": p.as_posix(),
        "target": p.relative_to("regolith").as_posix()\
            .replace("/world/", f'/{project_name_dashes}/'),
        "subfunctions": True
    } for p in Path("regolith/worlds/").rglob("*.lang")],
    # Postprocessing
    {
        "source": "postprocess.py",
        "target": "./",  # Used as working directory, the script gets removed
        "python_script": True
    }
]