<h1 align="center">GrowScan - GUI Version of Nmap</h1>
<h3 align="center">v1.5.0</h3>
<p align="center">
  <a href="https://nmap.org/docs.html">also see original software</a>
</p>

GrowScan is a user-friendly graphical interface for Nmap, the powerful and flexible network scanning tool. This project was created using Qt Designer to make Nmap more accessible with an intuitive user interface.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.5.1-green.svg)

<p align="center">
  <img src="https://i.ibb.co/64Jx3XL" alt="GrowScan Screenshot">
</p>

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Features
- Easy-to-use graphical interface
- Quick access to common Nmap commands
- Customizable scan options
- Real-time scan results
- Save and load scan configurations

## Installation
Follow these steps to get the project up and running on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/CrIzSec/GrowScan.git
    ```
2. Navigate to the project directory:
    ```bash
    cd GrowScan
    ```
3. Install dependencies:
   - Make sure Nmap is installed on your device:
     ```bash
     sudo apt install nmap
     choco install nmap
     ```
   - Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    python main.py
    ```

## Usage
Using Nmap GUI is straightforward. Launch the application and start exploring the network with just a few clicks. Here’s a quick example:

1. Select a scan type from the dropdown menu.
2. Enter the target IP address or range.
3. Click the "Start Scan" button.
4. View the results in real-time as they appear in the output window.

## Contact
<p align="center">
  <a href="https://www.instagram.com/cr1zsec/">@cr1zsec</a>
</p>
