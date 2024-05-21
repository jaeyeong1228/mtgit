import cv2

def main():
    video_path = "sky.mp4"

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    frame_index = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("End of video")
            break

        filename = f"frame_{frame_index}.jpg"
        cv2.imwrite(filename, frame)

        print(f"Saved frame: {filename}")

        frame_index += 1

    cap.release()

if __name__ == "__main__":
    main()
