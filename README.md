
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
    ```chocolatey
    choco install -y python3
    ```
  Check Python version
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


<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/frostygum/TicTacToe.svg?style=for-the-badge
[contributors-url]: https://github.com/frostygum/TicTacToe/graphs/contributors
[license-shield]: https://img.shields.io/github/license/frostygum/TicTacToe.svg?style=for-the-badge
[license-url]: https://github.com/frostygum/TicTacToe/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/juan-anthonius-kusjadi/