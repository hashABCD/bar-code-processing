import cv2
from pyzbar.pyzbar import decode
import os
import platform

def beep():
    # Check the platform and use appropriate method to produce a beep sound
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(1000, 2000)  # Frequency and duration in milliseconds
    else:
        # For MacOS and Linux
        os.system('echo -n "\a"; sleep 0.2')  # May vary depending on terminal

def scan_barcode():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if frame is captured
        if not ret:
            print("Failed to grab frame")
            break

        # Decode the barcodes in the frame
        barcodes = decode(frame)

        if barcodes:
            for barcode in barcodes:
                # Extract the bounding box location of the barcode
                (x, y, w, h) = barcode.rect
                # Draw the bounding box around the barcode
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Convert the barcode data from bytes to string
                barcode_data = barcode.data.decode("utf-8")
                barcode_type = barcode.type

                # Display the barcode type and data on the frame
                text = f"{barcode_type}: {barcode_data}"
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Print the barcode data to the console
                print(f"Found {barcode_type} barcode: {barcode_data}")

                # Play a beep sound to alert the user
                beep()

                # Release the capture and close windows
                cap.release()
                cv2.destroyAllWindows()
                return  # Exit the function after reading the barcode

        # Display the resulting frame
        cv2.imshow("Barcode Scanner", frame)

        # Press 'q' to exit the loop manually (if needed)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows in case of manual exit
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_barcode()
