# keylogger-project

This project is a basic keylogger implemented in Python using the `pynput` library. The keylogger logs the keystrokes of the user and saves them in a text file. It was developed as an educational project to understand how keyloggers work.

## Features

- Logs keystrokes pressed by the user.
- Saves the logged keystrokes to a text file (`keylog.txt`).
- Supports special keys like `esc` to stop the logging process.
- Built with the `pynput` library for capturing keyboard events.

## Requirements

Before running the keylogger, make sure you have the following dependencies installed:

- Python 3.x
- `pynput` library

You can install the required dependencies using the following command:

```bash
pip install pynput
```

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/ItsAkanksha1/keylogger-project-v2.git
   ```

2. Navigate to the project directory:

   ```bash
   cd keylogger-project-v2
   ```

3. Run the keylogger script:

   ```bash
   python keylogger.py
   ```

   The keylogger will start logging keystrokes and save them in `keylog.txt`.

4. To stop the keylogger, press the `Escape` key.

## Disclaimer

This project is intended for educational purposes only. Using keyloggers without proper consent is illegal and unethical. Make sure to use this project responsibly and only in ethical environments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
