
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

TicTacToe is Python based Multiplayer TicTacToe game using TCP socket.

<!-- GETTING STARTED -->
## Getting Started

This application running with python 3.7

### Prerequisites

* [https://docs.chocolatey.org/en-us/choco/setup](Chocolatey)   
  ```powershell
  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
  ```
  ```
  choco upgrade chocolatey
  ```
* [https://www.python.org/](Python)
  ```chocolatey
  choco install -y python3
  ```
  ```python
  python -V
  ```
### Installation

1. Create python virtual env
   ```
   python -m venv env
   ```
2. Activate virtual env
   ```sh
   & ./env/Scripts/Activate.ps1
   ```
3. Install python packages
   ```sh
   pip install -r requirements.txt
   ```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.