import cv2
import os

def extract_n_images(video_path, output_folder, num_images=5):
    """
    Extract a specified number of evenly spaced frames from a video.
    
    Args:
        video_path (str): Path to the video file.
        output_folder (str): Folder to save the extracted images.
        num_images (int): Number of images to extract. Default is 5.
    """
    # Check if the output folder exists; if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Load the video
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return
    
    # Get video properties
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_frames / fps  # Total duration in seconds

    # Calculate the frame interval for extracting N images
    interval = duration / num_images
    timestamps = [interval * i for i in range(num_images)]

    image_count = 0

    for timestamp in timestamps:
        # Set the video position to the desired timestamp
        cap.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)  # Convert seconds to milliseconds
        ret, frame = cap.read()
        if ret:
            image_name = f"frame_{image_count:04d}.jpg"
            image_path = os.path.join(output_folder, image_name)
            cv2.imwrite(image_path, frame)
            print(f"Saved: {image_path}")
            image_count += 1
        else:
            print(f"Error: Unable to capture frame at {timestamp} seconds.")
    
    cap.release()
    print(f"Extraction complete. Total frames saved: {image_count}")

# Example usage
video_path = "output.mp4"  # Replace with the path to your video file
output_folder = "extracted_frames"  # Replace with your desired output folder
extract_n_images(video_path, output_folder, num_images=5)
