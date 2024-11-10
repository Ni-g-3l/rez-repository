import os
from rez.vendor import yaml

class PackageRepositoryHandler:

    def __init__(self, config, repositories, action):
        self._repositories = set([os.path.abspath(repo) for repo in repositories])
        self._config_repositories = set(config.packages_path)
        self._config = config
        self._action = action

    def run(self):
        if not hasattr(self, self._action):
            return
        getattr(self, self._action)()

    def list(self):
        for package_folder in self._config.packages_path:
            print(package_folder)

    def remove(self):
        for repo in self._repositories:
            if repo not in self._config_repositories:
                print(f"{repo} not in package repositories")
                continue
            self._config_repositories.discard(repo)
        self._save_repositories()

    def add(self):
        if not self._repositories:
            print("No folder to add to package repositories")
            return
        self._config_repositories.update(self._repositories)
        self._save_repositories()

    def _save_repositories(self):
        self._config.packages_path = list(self._config_repositories)
        with open(self._config.filepaths[-1], 'w') as file:
            yaml.dump(self._config.data, file, default_flow_style=False)