
# TicTacToe

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <a href="#ScreenShoots">ScreenShoots</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#building-executeable-distribution">Build Executeable</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

TicTacToe is Python based Multiplayer TicTacToe game using TCP socket.

<!-- ScreenShoots -->
## ScreenShoots

<div>
  <p align="center">
    Main Window
  </p>
  <p align="center">
    <img src="docs/main_window.jpg" width="300">
    <img src="docs/waitClient_window.jpg" width="300">
  </p>
</div>

<div>
  <p align="center">
    Game Window
  </p>
  <p align="center">
    <img src="docs/host-game.jpg" width="300">
    <img src="docs/client-game.jpg" width="300">
  </p>
</div>

<div>
  <p align="center">
    Menu Window
  </p>
  <p align="center">
    <img src="docs/host-menu.jpg" width="300">
    <img src="docs/client-menu.jpg" width="300">
  </p>
</div>

<!-- GETTING STARTED -->
## Getting Started

This application running with python 3.7

### Prerequisites

* [Chocolatey](https://docs.chocolatey.org/en-us/choco/setup)  
  Install Chocolatey using powershell
    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    ```
  Upgrade Chocolatey (optional)
    ```
    choco upgrade chocolatey
    ```
* [Python](https://www.python.org/)
  Install Python using chocolatey
    ```powershell
    choco install -y python3
    ```
  Check Python version
    ```powershell
    python -V
    ```
### Installation

1. Create python virtual env
   ```powershell
   python -m venv .env
   ```
2. Activate virtual env
   ```powershell
   & ./.env/Scripts/Activate.ps1
   ```
   ```sh
   ./.env/Scripts/Activate
   ```
3. Install python packages
   ```powershell
   pip install -r requirements.txt
   ```
3. Run application
  ```powershell
  python tictactoe.py
  ```

### Building Executeable Distribution

1. Distribution with console opened
   ```
   pyinstaller tictactoe.py --onefile --name TicTacToe
   ```
2. Distribution without console opened
   ```sh
   pyinstaller tictactoe.py -w --onefile --name TicTacToe
   ```



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/frostygum/TicTacToe.svg?style=for-the-badge
[contributors-url]: https://github.com/frostygum/TicTacToe/graphs/contributors
[license-shield]: https://img.shields.io/github/license/frostygum/TicTacToe.svg?style=for-the-badge
[license-url]: https://github.com/frostygum/TicTacToe/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/juan-anthonius-kusjadi/