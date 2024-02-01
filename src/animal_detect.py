import cv2
import numpy as np
import tensorflow as tf

class AnimalDetectionPod:
    def __init__(self):
        # Load the pre-trained object detection model
        self.model = tf.keras.applications.MobileNetV2(weights='imagenet')

    def detect_animals(self, frame):
        # Preprocess the frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (224, 224))
        frame = tf.keras.applications.mobilenet.preprocess_input(frame)

        # Make predictions using the model
        predictions = self.model.predict(np.expand_dims(frame, axis=0))
        predicted_classes = tf.keras.applications.mobilenet.decode_predictions(predictions, top=5)[0]

        # Extract animal class labels and confidence scores
        animal_labels = []
        confidence_scores = []
        for _, label, confidence in predicted_classes:
            if 'animal' in label.lower():
                animal_labels.append(label)
                confidence_scores.append(confidence)

        return animal_labels, confidence_scores

    def process_video(self, video_path):
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Process each frame in the video
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Detect animals in the frame
            animal_labels, confidence_scores = self.detect_animals(frame)

            # Print the detected animals and their confidence scores
            for label, score in zip(animal_labels, confidence_scores):
                print(f'Detected animal: {label}, Confidence: {score}')

            # Display the frame with bounding boxes (optional)
            # TODO: Add code to draw bounding boxes around detected animals

            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture and close any open windows
        cap.release()
        cv2.destroyAllWindows()

# Example usage
video_path = 'ressources\\mp4\\video_resized.mp4'
pod = AnimalDetectionPod()
pod.process_video(video_path)
