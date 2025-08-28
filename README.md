# Rick Roll Hello World App 🎵

A fun twist on the classic "Hello World" application that rickrolls you when you click on "World"!

## Features

- **Interactive GUI**: Displays "Hello World" with a clickable "World" text
- **Rick Roll Experience**: Click "World" to trigger Rick Astley's "Never Gonna Give You Up"
- **8-bit Visual**: Shows a custom-generated 8-bit style Rick Astley image
- **Toggle Functionality**: Click "World" again to stop the music and hide the image
- **Retro Styling**: Black background with green/red terminal-style colors

## How to Run

1. **Install Dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python3 hello_world_rickroll.py
   ```

3. **Enjoy the Rick Roll**:
   - The app will open with "Hello World" displayed
   - Click on the red "World" text to start the Rick Roll experience
   - Click again to stop the music and hide the image

## Technical Details

### Dependencies
- **pygame**: For MIDI audio playback
- **pillow**: For image processing and display
- **tkinter**: For GUI (included with Python)

### Files
- `hello_world_rickroll.py` - Main application file
- `never_gonna_give_you_up.mid` - MIDI file of the song
- `rick_astley_8bit_dancing.gif` - 8-bit animated dancing Rick Astley (auto-generated)
- `requirements.txt` - Python dependencies (secure versions)
- `LICENSE_NOTICE.md` - License compliance documentation

### Features Implemented
- ✅ Clickable "World" text with hover effects
- ✅ MIDI audio playback with looping and 3-second skip (bypasses silence)
- ✅ 8-bit animated dancing Rick Astley GIF
- ✅ 4-frame dancing animation synchronized with music
- ✅ Toggle on/off functionality
- ✅ Error handling for missing files
- ✅ Retro terminal-style UI design

## Customization

You can customize the app by:
- Replacing `rick_astley_8bit_dancing.gif` with your own animated 8-bit GIF
- Changing colors in the GUI code
- Modifying the dance animation frames
- Adjusting the 3-second skip timing for different MIDI files
- Adding more visual effects
- Using different audio formats (though MIDI gives that retro feel!)

## Known Issues

- MIDI playback may not work on all systems due to pygame limitations
- MIDI position seeking may not work on some systems (gracefully falls back to playing from beginning)
- The auto-generated dancing Rick Astley GIF is simple 8-bit art (you can replace it with a better one)

## Credits

- MIDI file sourced from BitMidi
- Built with Python, tkinter, pygame, and PIL
- Created as a fun coding exercise combining GUI programming with multimedia

**Never gonna give you up! 🎶**
