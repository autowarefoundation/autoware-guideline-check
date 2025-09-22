# Copyright 2025 The Autoware Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from pathlib import Path
from xml.etree import ElementTree

from ament_index_python.packages import get_package_share_directory


class Package:
    def __init__(self, path: Path):
        root = ElementTree.parse(path / "package.xml")
        self._path = path
        self._name = root.find("name").text
        self._files = []
        for export in root.findall("export"):
            for file in export.findall("autoware_guideline_check"):
                self._files.append(file.get("file"))

    @property
    def path(self):
        return self._path

    @property
    def name(self):
        return self._name

    @property
    def files(self):
        return [self._path / file for file in self._files]


class Workspace:
    def __init__(self, paths: list[str]):
        self._packages = self.__init_packages(paths)

    def get_package_share_directory(self, name: str):
        package = self._packages.get(name)
        return package.path if package else get_package_share_directory(name)

    @property
    def packages(self):
        return self._packages.values()

    @classmethod
    def __init_packages(cls, bases: list[str]):
        paths = sum(map(cls.__list_packages_paths, bases), [])
        pkgs = [Package(path) for path in paths]
        pkgs = {pkg.name: pkg for pkg in pkgs}
        return pkgs

    @classmethod
    def __list_packages_paths(cls, base: str):
        base = Path(base)
        if base.joinpath("COLCON_IGNORE").exists():
            return []
        if base.joinpath("package.xml").exists():
            return [base]
        paths = []
        for path in base.iterdir():
            if path.is_dir():
                paths.extend(cls.__list_packages_paths(path))
        return paths
