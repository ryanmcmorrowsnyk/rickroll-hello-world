#!/usr/bin/env python3
"""
Rick Roll Hello World App
A Python GUI application that displays "Hello World" and rickrolls when you click "World"
"""

import tkinter as tk
from tkinter import ttk, PhotoImage
import pygame
import os
import sys
from PIL import Image, ImageTk, ImageDraw, ImageFont
import threading

class RickRollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello World - Rick Roll Edition")
        self.root.geometry("600x500")
        self.root.configure(bg='#000000')
        
        # Initialize pygame mixer for MIDI playback
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)
        
        # State variables
        self.is_playing = False
        self.midi_file = 'never_gonna_give_you_up.mid'
        self.image_file = 'rick_astley_8bit_dancing.gif'
        
        # Animation variables
        self.gif_frames = []
        self.current_frame = 0
        self.animation_running = False
        self.animation_after_id = None
        
        # Setup the GUI
        self.setup_gui()
        
        # Load resources
        self.load_resources()
    
    def setup_gui(self):
        """Set up the GUI components"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        title_frame = tk.Frame(main_frame, bg='#000000')
        title_frame.pack(pady=(0, 30))
        
        # "Hello" text (normal)
        self.hello_label = tk.Label(
            title_frame, 
            text="Hello ", 
            font=("Courier", 36, "bold"),
            fg='#00FF00',
            bg='#000000'
        )
        self.hello_label.pack(side=tk.LEFT)
        
        # "World" text (clickable)
        self.world_label = tk.Label(
            title_frame, 
            text="World", 
            font=("Courier", 36, "bold"),
            fg='#FF0000',
            bg='#000000',
            cursor='hand2'
        )
        self.world_label.pack(side=tk.LEFT)
        self.world_label.bind("<Button-1>", self.toggle_rickroll)
        self.world_label.bind("<Enter>", self.on_hover_enter)
        self.world_label.bind("<Leave>", self.on_hover_leave)
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Click 'World' to experience the magic! 🎵",
            font=("Courier", 12),
            fg='#FFFFFF',
            bg='#000000'
        )
        self.status_label.pack(pady=(10, 20))
        
        # Image frame (initially hidden)
        self.image_frame = tk.Frame(main_frame, bg='#000000')
        
        # Image label (will hold Rick Astley image)
        self.image_label = tk.Label(self.image_frame, bg='#000000')
        self.image_label.pack()
        
    def load_resources(self):
        """Load MIDI file and image"""
        # Check if MIDI file exists
        if not os.path.exists(self.midi_file):
            self.status_label.config(
                text="⚠️  MIDI file not found! Please download never_gonna_give_you_up.mid",
                fg='#FFFF00'
            )
        else:
            # Try to create trimmed version to skip initial silence
            if os.path.exists('never_gonna_give_you_up.mid'):
                if self.create_trimmed_midi():
                    print("Created trimmed MIDI file to skip initial silence")
        
        # Load or create 8-bit Rick Astley image
        if not os.path.exists(self.image_file):
            self.create_placeholder_image()
        else:
            self.load_image()
    
    def create_placeholder_image(self):
        """Create an animated 8-bit style dancing Rick Astley GIF"""
        try:
            frames = []
            
            # Create 4 dancing frames
            for frame_num in range(4):
                # Create an 8-bit style image (256x256)
                img = Image.new('RGB', (256, 256), color='#000033')
                draw = ImageDraw.Draw(img)
                
                # Base positions
                base_x = 128
                base_y = 128
                
                # Dance movement - side to side and arm positions
                if frame_num == 0:
                    # Frame 1: Center position, arms down
                    body_x, arm_offset = 0, 0
                elif frame_num == 1:
                    # Frame 2: Slight left, left arm up
                    body_x, arm_offset = -8, -15
                elif frame_num == 2:
                    # Frame 3: Center position, both arms up
                    body_x, arm_offset = 0, -20
                else:
                    # Frame 4: Slight right, right arm up
                    body_x, arm_offset = 8, -15
                
                # Hair (orange/brown)
                draw.rectangle([base_x-48+body_x, base_y-98, base_x+48+body_x, base_y-48], fill='#CC6600')
                
                # Face (pink)
                draw.rectangle([base_x-38+body_x, base_y-48, base_x+38+body_x, base_y+12], fill='#FFCCAA')
                
                # Eyes
                draw.rectangle([base_x-28+body_x, base_y-38, base_x-18+body_x, base_y-28], fill='#000000')
                draw.rectangle([base_x+18+body_x, base_y-38, base_x+28+body_x, base_y-28], fill='#000000')
                
                # Nose
                draw.rectangle([base_x-2+body_x, base_y-23, base_x+2+body_x, base_y-13], fill='#FF9999')
                
                # Mouth (smile)
                draw.rectangle([base_x-18+body_x, base_y-8, base_x+18+body_x, base_y+2], fill='#FF0000')
                
                # Body (suit)
                draw.rectangle([base_x-58+body_x, base_y+12, base_x+58+body_x, base_y+92], fill='#333333')
                
                # Shirt
                draw.rectangle([base_x-38+body_x, base_y+12, base_x+38+body_x, base_y+52], fill='#FFFFFF')
                
                # Tie
                draw.rectangle([base_x-6+body_x, base_y+12, base_x+6+body_x, base_y+72], fill='#FF0000')
                
                # Arms (animated based on frame)
                # Left arm
                if frame_num == 1:
                    # Left arm up
                    draw.rectangle([base_x-75+body_x, base_y+5+arm_offset, base_x-45+body_x, base_y+25+arm_offset], fill='#FFCCAA')
                else:
                    # Left arm down/middle
                    draw.rectangle([base_x-75+body_x, base_y+20, base_x-45+body_x, base_y+40], fill='#FFCCAA')
                
                # Right arm
                if frame_num == 3:
                    # Right arm up
                    draw.rectangle([base_x+45+body_x, base_y+5+arm_offset, base_x+75+body_x, base_y+25+arm_offset], fill='#FFCCAA')
                elif frame_num == 2:
                    # Both arms up
                    draw.rectangle([base_x+45+body_x, base_y+arm_offset, base_x+75+body_x, base_y+20+arm_offset], fill='#FFCCAA')
                    draw.rectangle([base_x-75+body_x, base_y+arm_offset, base_x-45+body_x, base_y+20+arm_offset], fill='#FFCCAA')
                else:
                    # Right arm down/middle
                    draw.rectangle([base_x+45+body_x, base_y+20, base_x+75+body_x, base_y+40], fill='#FFCCAA')
                
                # Legs (simple)
                draw.rectangle([base_x-25+body_x, base_y+92, base_x-10+body_x, base_y+130], fill='#000080')
                draw.rectangle([base_x+10+body_x, base_y+92, base_x+25+body_x, base_y+130], fill='#000080')
                
                # Add dancing text
                try:
                    font = ImageFont.load_default()
                    if frame_num % 2 == 0:
                        draw.text((50, 230), "♪ Never Gonna Give You Up! ♪", fill='#FFFFFF', font=font)
                    else:
                        draw.text((60, 230), "♫ Dancing Rick Astley! ♫", fill='#FFFF00', font=font)
                except:
                    draw.text((50, 230), "Never Gonna Dance!", fill='#FFFFFF')
                
                frames.append(img)
            
            # Save as animated GIF
            frames[0].save(
                self.image_file,
                save_all=True,
                append_images=frames[1:],
                duration=500,  # 500ms per frame
                loop=0  # Infinite loop
            )
            self.load_image()
            
        except Exception as e:
            # Fallback: create a simple text placeholder
            self.gif_frames = []
            print(f"Error creating animated GIF: {e}")
    
    def load_image(self):
        """Load the animated Rick Astley GIF frames"""
        try:
            self.gif_frames = []
            pil_gif = Image.open(self.image_file)
            
            # Extract all frames from the GIF
            frame_count = 0
            while True:
                try:
                    pil_gif.seek(frame_count)
                    frame = pil_gif.copy()
                    frame = frame.resize((256, 256), Image.Resampling.NEAREST)  # 8-bit style resize
                    photo_frame = ImageTk.PhotoImage(frame)
                    self.gif_frames.append(photo_frame)
                    frame_count += 1
                except EOFError:
                    break
            
            if self.gif_frames:
                # Set initial frame
                self.current_frame = 0
                self.image_label.config(image=self.gif_frames[0])
                
        except Exception as e:
            print(f"Error loading animated GIF: {e}")
            self.gif_frames = []
    
    def animate_gif(self):
        """Animate the GIF by cycling through frames"""
        if self.animation_running and self.gif_frames:
            # Update to next frame
            self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
            self.image_label.config(image=self.gif_frames[self.current_frame])
            
            # Schedule next frame
            self.animation_after_id = self.root.after(500, self.animate_gif)  # 500ms per frame
    
    def start_animation(self):
        """Start the GIF animation"""
        if self.gif_frames and not self.animation_running:
            self.animation_running = True
            self.animate_gif()
    
    def stop_animation(self):
        """Stop the GIF animation"""
        self.animation_running = False
        if self.animation_after_id:
            self.root.after_cancel(self.animation_after_id)
            self.animation_after_id = None
        # Reset to first frame
        if self.gif_frames:
            self.current_frame = 0
            self.image_label.config(image=self.gif_frames[0])
    
    def create_trimmed_midi(self):
        """Create a trimmed version of the MIDI file without the initial silence"""
        try:
            # Try to use mido library for MIDI manipulation
            import mido
            
            original_file = self.midi_file
            trimmed_file = 'never_gonna_give_you_up_trimmed.mid'
            
            # Load the MIDI file
            mid = mido.MidiFile(original_file)
            
            # Create a new MIDI file
            new_mid = mido.MidiFile()
            
            # Copy tracks but shift timing to skip initial silence
            skip_ticks = int(3.0 * mid.ticks_per_beat * 2)  # Approximate 3 seconds
            
            for track in mid.tracks:
                new_track = mido.MidiTrack()
                current_time = 0
                
                for msg in track:
                    current_time += msg.time
                    
                    # Skip messages in the first few seconds
                    if current_time > skip_ticks:
                        # Adjust timing for the first message after skip
                        if len(new_track) == 0:
                            new_msg = msg.copy(time=0)
                        else:
                            new_msg = msg.copy()
                        new_track.append(new_msg)
                    elif msg.type in ['program_change', 'control_change']:
                        # Always keep setup messages
                        new_msg = msg.copy(time=0 if len(new_track) == 0 else msg.time)
                        new_track.append(new_msg)
                
                new_mid.tracks.append(new_track)
            
            # Save the trimmed file
            new_mid.save(trimmed_file)
            self.midi_file = trimmed_file
            
            return True
            
        except ImportError:
            # mido not available, fall back to original file
            return False
        except Exception as e:
            print(f"Error creating trimmed MIDI: {e}")
            return False
    
    def on_hover_enter(self, event):
        """Handle mouse hover enter"""
        self.world_label.config(fg='#FFFF00')
    
    def on_hover_leave(self, event):
        """Handle mouse hover leave"""
        color = '#00FF00' if self.is_playing else '#FF0000'
        self.world_label.config(fg=color)
    
    def toggle_rickroll(self, event):
        """Toggle the Rick Roll (audio and visual)"""
        if self.is_playing:
            self.stop_rickroll()
        else:
            self.start_rickroll()
    
    def start_rickroll(self):
        """Start the Rick Roll experience"""
        self.is_playing = True
        
        # Update UI
        self.world_label.config(fg='#00FF00')
        self.status_label.config(
            text="🎵 Never gonna give you up, never gonna let you down! 🎵",
            fg='#00FF00'
        )
        
        # Show animated image
        if self.gif_frames:
            self.image_frame.pack(pady=20)
            self.start_animation()  # Start the dancing animation!
        
        # Play MIDI file
        if os.path.exists(self.midi_file):
            try:
                pygame.mixer.music.load(self.midi_file)
                pygame.mixer.music.play(-1)  # Loop indefinitely
            except pygame.error as e:
                self.status_label.config(
                    text=f"Error playing MIDI: {e}",
                    fg='#FF0000'
                )
        else:
            self.status_label.config(
                text="🎵 (MIDI file not found, but imagine Rick Astley singing!) 🎵",
                fg='#FFFF00'
            )
    
    def stop_rickroll(self):
        """Stop the Rick Roll experience"""
        self.is_playing = False
        
        # Stop the dancing animation
        self.stop_animation()
        
        # Update UI
        self.world_label.config(fg='#FF0000')
        self.status_label.config(
            text="Click 'World' to experience the magic! 🎵",
            fg='#FFFFFF'
        )
        
        # Hide image
        self.image_frame.pack_forget()
        
        # Stop music
        pygame.mixer.music.stop()
    
    def on_closing(self):
        """Handle application closing"""
        # Stop animation if running
        self.stop_animation()
        pygame.mixer.quit()
        self.root.destroy()

def main():
    """Main function to run the application"""
    # Check Python version
    if sys.version_info < (3, 6):
        print("This application requires Python 3.6 or higher")
        return
    
    # Create and configure the main window
    root = tk.Tk()
    app = RickRollApp(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
