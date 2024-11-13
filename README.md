# Key Code Detector

A modern, user-friendly GUI application that displays the key code and name of any key pressed on your keyboard. Perfect for developers, testers, or anyone needing to identify specific key codes for keyboard inputs.

![Key Code Detector Screenshot](https://i.imgur.com/moYFleT.png)

## Features

- 🎯 Real-time key code detection
- 🖥️ Modern, clean user interface
- ⚡ Visual feedback on key presses
- 📝 Displays both key codes and key names
- 💾 Last pressed key history
- 🎨 Adaptive styling based on operating system
- 🖱️ Proper window management and positioning

## Installation

### Option 1: Running the Executable (Windows)

1. Download the latest release from the releases page
2. Extract the ZIP file
3. Run `KeyCodeDetector.exe`

### Option 2: Running from Source

1. Ensure you have Python 3.7 or higher installed
2. Clone this repository:
```bash
git clone https://github.com/yourusername/key-code-detector.git
cd key-code-detector
```

3. Run the application:
```bash
python kc_detector.py
```

### Option 3: Building from Source

1. Install required packages:
```bash
pip install pyinstaller
```

2. Build the executable:
```bash
pyinstaller keycode_detector.spec
```

3. Find the executable in the `dist` folder

## Usage

1. Launch the application
2. Press any key on your keyboard
3. The application will display:
   - The key's numerical code
   - The key's name
   - A history of the last pressed key
4. Click "Exit" or close the window to quit

## Key Code Information

The application displays Windows Virtual-Key codes, which are standardized across all Windows machines. These codes are consistent regardless of keyboard layout or hardware, making them reliable for:

- Software development
- Game input mapping
- Automation scripts
- Keyboard event handling

## Troubleshooting

### Common Issues

1. **Application won't start**
   - Ensure you have appropriate permissions
   - Try running as administrator
   - Check if antivirus is blocking execution

2. **Missing visual styles**
   - Ensure you're using Windows 7 or later
   - Verify system theme settings

3. **Key codes not showing**
   - Check if other applications are intercepting keyboard input
   - Verify keyboard drivers are properly installed

## Development

### Prerequisites

- Python 3.7 or higher
- tkinter (usually comes with Python)
- PyInstaller (for building executable)

### Project Structure

```
key-code-detector/
│
├── kc_detector.py                 # Main application file
├── keycode_detector.spec          # PyInstaller specification
├── app_icon.ico                   # Application icon
├── README.md                      # This file
└── requirements.txt               # Python dependencies
```

### Building

To modify and build the application:

1. Make your changes to `kc_detector.py`
2. Update version number if applicable
3. Build new executable:
```bash
pyinstaller keycode_detector.spec
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


---
Made with ❤️ by WHEREISDAN