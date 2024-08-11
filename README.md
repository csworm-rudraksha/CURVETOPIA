# Curvetopia - Advanced SVG Curve Processing
Welcome to **Curvetopia**, an advanced tool designed to process SVG files by completing incomplete shapes, identifying curve types, and transforming them into refined, accurate vector graphics. This project is part of Adobe's GenSolve initiative, which aims to provide robust solutions for vector graphic editing and enhancement.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Input and Output](#input-and-output)
- [Project Structure](#project-structure)
- [Acknowledgments](#acknowledgments)

## Project Overview

Curvetopia is an algorithmic solution for processing SVG (Scalable Vector Graphics) files with a focus on curve detection, completion, and transformation. The tool reads SVG inputs, converts them to CSV format for analysis, identifies the type of curve (e.g., Bézier, quadratic), and performs the necessary transformations to enhance the graphic. The final output is a polished SVG file with completed and refined shapes, ready for use in high-quality graphic design.

## Features

- **Curve Completion**: Automatically completes any incomplete shapes in SVG files.
- **Curve Identification**: Accurately identifies different types of curves, such as Bézier or quadratic curves.
- **Data Transformation**: Converts SVG data to CSV for easier manipulation and back to SVG after processing.
- **SVG Output**: Delivers the final curve in SVG format, maintaining compatibility with design tools.
- **Advanced Geometric Analysis**: Utilizes sophisticated techniques for precise curve detection and transformation.

## Installation

To install and run Curvetopia, follow these steps:

### Clone the Repository

```bash
git clone https://github.com/csworm-rudraksha/CURVETOPIA.git
cd CURVETOPIA
```
### Install Dependencies
Make sure you have Python installed. Then, install the necessary packages:
```bash
pip install -r requirements.txt
```
### Run the Application
```bash
python main.py
```
### Usage
- **Prepare your SVG File**: Ensure that your SVG file is formatted correctly and located in the input directory.
- **Run the Script**: Execute the script to process the SVG file.
```bash
python main.py -i input/yourfile.svg
```
- **View Output**: The completed and transformed SVG will be saved in the output directory.

### Input and Output
- **Input**: SVG files that may contain incomplete shapes or curves that need identification and transformation.
- **Output**: A fully completed and transformed SVG file, with precise curve adjustments.
### Project Structure
```bash
PROJECT/
├── data/examples/
│  └── isolated.csv
│
├── src/
│  ├── pycache/
│  │   ├── completion.cpython-310.pyc
│  │   ├── convert.cpython-310.pyc
│  │   ├── regularization.cpython-310.pyc
│  │   ├── symmetry.cpython-310.pyc
│  │   ├── utils.cpython-310.pyc
│  │   ├── utils.cpython-312.pyc
│  │   └── visualize.cpython-310.pyc
│  │
│  ├── _init_.py
│  ├── completion.py
│  ├── convert.py
│  ├── main.py
│  ├── regularization.py
│  ├── symmetry.py
│  ├── utils.py
│  └── visualize.py
│
├── poetry.lock
├── pyproject.toml
├── replit_zip_error_log.txt
└── requirments.txt
```
### Acknowledgments
This project is developed as part of the Adobe GenSolve Curvetopia initiative, aiming to provide cutting-edge solutions for shape processing.
### TEAM
Team Uzee - 
- Rudraksha Kushwaha
- Mahak sharma 
- Pratham Parashar
