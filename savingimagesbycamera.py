import cv2
import os

def main():
    path_to_images = r"C:\Data\vs coding\HelloCV\HelloCV\tree images"
    output_video_path = r"C:\Data\vs coding\HelloCV\HelloCV\tree_video.avi"
    images = []

    # 이미지 파일 읽기
    for filename in os.listdir(path_to_images):
        file_path = os.path.join(path_to_images, filename)
        img = cv2.imread(file_path)
        if img is None:
            print(f"Could not open or find the image: {file_path}")
            continue
        images.append(img)

    # 이미지가 없을 경우
    if not images:
        print("No images found in the directory.")
        return

    # 비디오 작성
    frame_size = (images[0].shape[1], images[0].shape[0])
    fps = 30
    video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'MJPG'), fps, frame_size, True)

    for img in images:
        video.write(img)

    video.release()
    print("Video written successfully.")

if __name__ == "__main__":
    main()
