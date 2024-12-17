import tkinter as tk
import cv2
import dlib
import numpy as np
from PIL import Image, ImageTk
import face_recognition  

class FaceRecognitionApp:
    def __init__(self, parent):
        # Create a top-level window (internal frame)
        self.top = tk.Toplevel(parent)
        self.top.title("Face Recognition Scanner")

        # Initialize global variables
        self.cap = cv2.VideoCapture(0)
        self.detector = dlib.get_frontal_face_detector()  # Using dlib's frontal face detector
        self.registered_face_encoding = None  # Store the registered face encoding
        self.video_running = True
        self.face_captured = False

        # UI Elements
        self.canvas = tk.Canvas(self.top, width=640, height=480)
        self.canvas.pack()

        self.register_button = tk.Button(self.top, text="Register Face", command=self.capture_face)
        self.register_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.verify_button = tk.Button(self.top, text="Verify Face", command=self.verify_face)
        self.verify_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.quit_button = tk.Button(self.top, text="Quit", command=self.quit_app)
        self.quit_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Start updating the frame
        self.update_frame()

    def update_frame(self):
        """
        Continuously updates the video feed in the Tkinter canvas.
        """
        ret, frame = self.cap.read()
        if ret:
            # Convert BGR to RGB for Tkinter display
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Detect faces using dlib
            faces = self.detector(rgb_frame, 1)
            
            # Draw rectangles around the faces
            for face in faces:
                # Accessing coordinates of the face rectangle
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Convert frame to an image object for Tkinter
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            photo = ImageTk.PhotoImage(image=image)
            
            # Update the canvas with the new frame
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.top.photo = photo  # Keep a reference to avoid garbage collection

        # Keep updating the frame
        if self.video_running:
            self.top.after(10, self.update_frame)

    def capture_face(self):
        """
        Captures the face and displays the image for confirmation.
        """
        ret, frame = self.cap.read()
        if not ret:
            print("Unable to access the camera.")
            return

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect faces using dlib
        faces = self.detector(rgb_frame, 1)

        if faces:
            # Assume only one face for simplicity
            self.captured_frame = frame

            # Stop the video feed and show the captured image
            self.video_running = False
            captured_image = Image.fromarray(cv2.cvtColor(self.captured_frame, cv2.COLOR_BGR2RGB))
            photo = ImageTk.PhotoImage(image=captured_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.top.photo = photo  # Keep reference
            self.face_captured = True

            # Capture face encoding
            face_encoding = face_recognition.face_encodings(rgb_frame, faces)[0]
            self.registered_face_encoding = face_encoding
            print("Face Registered.")
        else:
            print("No face detected. Please try again.")

    def verify_face(self):
        """
        Verifies the detected face against the registered face.
        """
        if self.registered_face_encoding is None:
            print("No registered face. Please register a face first.")
            return

        ret, frame = self.cap.read()
        if not ret:
            print("Unable to access the camera.")
            return

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect faces using dlib
        faces = self.detector(rgb_frame, 1)

        if faces:
            # Assume only one face for simplicity
            face_encoding = face_recognition.face_encodings(rgb_frame, faces)[0]

            # Compare the captured face with the registered face encoding
            matches = face_recognition.compare_faces([self.registered_face_encoding], face_encoding)

            if matches[0]:
                print("Face verified successfully!")
                self.display_message("Face verified successfully!")
            else:
                print("Face verification failed.")
                self.display_message("Face verification failed.")
        else:
            print("No face detected. Please try again.")

    def display_message(self, message):
        """
        Display a message in the Tkinter window.
        """
        self.canvas.create_text(320, 240, text=message, fill="red", font=("Helvetica", 24))

    def quit_app(self):
        """
        Releases resources and exits the application.
        """
        self.video_running = False
        self.cap.release()
        self.top.destroy()

# Create the Tkinter root window
#root = tk.Tk()

# Instantiate the FaceRecognitionApp class, passing the root window as parent
#app = FaceRecognitionApp(root)

# Start the Tkinter event loop
#root.mainloop()
