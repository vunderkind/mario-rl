# Mario RL
A simple exploration of `gymnasium` and reinforcement learning using the popular Nintendo game, Super Mario Bros.

## Installation and Setup

### Requirements
- **Python 3.13 or newer.** The Mario environment, [`gym-super-mario-bros`](https://pypi.org/project/gym-super-mario-bros/), requires it.
- **A C++ compiler.** The game runs on an NES emulator, [`nes-py`](https://github.com/Kautenja/nes-py), which is compiled on your machine during installation. On macOS, the Xcode Command Line Tools provide the compiler. Check that you have them with:

  ```bash
  xcode-select -p
  ```

  If this prints a path, you're set. If it prints an error, install the tools with `xcode-select --install`.
- **[uv](https://docs.astral.sh/uv/)** for creating the virtual environment and installing packages. Plain `python -m venv` and `pip` also work.

### Steps
1. Clone the repository and move into it:

   ```bash
   git clone https://github.com/vunderkind/mario-rl.git
   cd mario-rl
   ```

2. Create and activate a virtual environment:

   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. Install the Mario environment. This also installs `gymnasium`, `nes-py`, and `numpy`. Expect a short pause while `nes-py` compiles.

   ```bash
   uv pip install gym-super-mario-bros
   ```

4. Confirm that `python` points into the project's virtual environment:

   ```bash
   which python
   ```

   The path should end in `mario-rl/.venv/bin/python`.