# Python Development Environment Setup

This document outlines my preferred way to set up a  machine for Python development. Instructions are tailored for 
macOS.

**Approach:** Use Conda as an environment manager, `pip` as the typical package installer, and Poetry as the dependency manager.

Benefits of this approach include:
- Better dependency management (often faster than conda dependency resolver)
- Having most package configurations (e.g., `pytest`, `coverage`, `bump2version`, etc.) in a single file
- The ability to install a Conda package if you have to (this should be a last resort!)
- Poetry can automatically add new packages to `pyproject.toml` file
- Poetry can show the list of library dependencies of individual packages
- Build a Python package and publishing to PyPI is as easy as running two commands
- No need to have separate environment files for production and development environments

Resources:
- [Homebrew](https://brew.sh)
- [Python Best Practices for a New Project in 2021](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/)
- [A Guide to Python Environment Dependency and Package Management: Conda + Poetry](https://ealizadeh.com/blog/guide-to-python-env-pkg-dependency-using-conda-poetry)
- [Does it make sense to use Conda + Poetry?](https://stackoverflow.com/questions/70851048/does-it-make-sense-to-use-conda-poetry#:~:text=Conda%20is%20primarily%20a%20environment,%2C%20an%20upgrade%20of%20Pyenv)
- [pyenv](https://github.com/pyenv/pyenv)
- [Conda](https://docs.conda.io/en/latest/)
- [Poetry](https://python-poetry.org/docs/)

## One-Time Steps Per Machine

Run these steps once per machine.

1. Install Homebrew or ensure it's up-to-date by running:
         
        $ brew update
2. Install Xcode
3. Install Xcode command line tools:

        $ xcode-select --install
4. Install other packages:

        $ brew install miniconda 
        $ brew install openssl readline sqlite3 xz zlib (???)
5. Configure your shell with Conda:

        $ conda init "$(basename "${SHELL}")"


## Project Steps

Run these steps whenever creating a new Python project.

**Naming conventions:**
- Directories, project, and package names are all lowercase, with words separated by single dashes (`-`)
- File names are all lowercase, with words separated by single underscores (`_`)
- Python variable names are all lowercase, with words separated by single underscores (`_`)
- Python constant variable names are all uppercase, with words separated by single underscores (`_`)
- Python class names are CamelCase

1. Create an `environment.yml` file that specifies the desired Python environment; this will be used by Conda to 
   create an isolated Python environment. A default `environment.yml` is provided below. At a minimum, specify the 
   project name in `name`. (Note: the `poetry` dependency is important; this will be used later on in the setup as 
   the dependency manager.)

   ```yaml
   name: python-project-template
   dependencies:
     - python=3.9
     - poetry=1.1.7
   ```

2. Activate the environment by specifying the project name to `conda activate` (in this example, 
   `python-project-template`):

        $ conda activate python-project-template
3. Verify the environment was activated correctly:

        $ conda env list         # should output all environments with a * next to the active env
        $ poetry --version       # should output Poetry version X.Y.Z
4. To deactivate the environment (and return to the `base` environment):
   
        $ conda deactivate
5. 



