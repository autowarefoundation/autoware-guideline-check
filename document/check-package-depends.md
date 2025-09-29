# check-package-depends

Checks for dependencies on packages not listed in package.xml.
Dependent packages are listed using the following method.

- Search for `$(find-pkg-share <name>)` in launch.xml files (exec_depend).
