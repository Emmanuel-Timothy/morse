import cv2
import numpy as np

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

def morse_to_text(morse):
    reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = morse.split(' / ')
    return ' '.join(''.join(reverse_dict.get(symbol, '?') for symbol in word.split()) for word in words)

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    morse_signal = []
    prev_brightness = 0
    threshold = 100  # Brightness threshold to detect flashes
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    
    frame_count = 0
    flash_durations = []
    flash_duration = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness = np.mean(gray)  # Average brightness of frame
        
        if brightness > threshold:
            flash_duration += 1
        else:
            if flash_duration > 0:
                flash_durations.append(flash_duration)
                flash_duration = 0
        
        frame_count += 1
    
    cap.release()
    cv2.destroyAllWindows()
    
    if not flash_durations:
        print("No flashes detected.")
        return ""
    
    # Normalize flashes based on relative duration
    min_flash = min(flash_durations)
    morse_signal = []
    for duration in flash_durations:
        if duration <= min_flash * 1.5:
            morse_signal.append('.')
        else:
            morse_signal.append('-')
    
    morse_code = ''.join(morse_signal).replace('   ', ' / ')  # Space between words
    text = morse_to_text(morse_code)
    print("Detected Morse Code:", morse_code)
    print("Decoded Text:", text)
    
    return text

video_file = "File.mp4"  # Replace with file name
analyze_video(video_file)
