# Basic Keylogger

A simple keylogger written in Python using the `pynput` library. This script is designed to demonstrate how keyloggers work by capturing keystrokes and saving them to a local text file.

## Features

* Logs all key presses from the keyboard.
* Correctly formats special keys like `Space`, `Enter`, etc.
* Saves the captured keystrokes to a `keylog.txt` file upon exit.
* The listener stops when the `Esc` key is pressed.

## Technologies Used

* Python
* `pynput`

## Setup and Usage

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Ashin-06/basic-keylogger.git](https://github.com/Ashin-06/basic-keylogger.git)
    cd basic-keylogger
    ```

2.  **Install Dependencies:**
    This project requires the `pynput` library.
    ```bash
    pip install pynput
    ```

3.  **Run the Script:**
    Execute the Python script from your terminal. It will run in the background, capturing keystrokes.
    ```bash
    python keylogger.py
    ```
    To stop the script and save the logs, press the `Esc` key.

## ⚠️ Ethical and Legal Disclaimer

This tool is for **educational purposes only**. Using this software on a computer without the owner's explicit knowledge and consent is **illegal and unethical**. The author is not responsible for any misuse of this software. Always respect privacy and abide by the law.