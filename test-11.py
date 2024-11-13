import cv2
import mediapipe as mp
import pyautogui

processor = "cpu"  # Trueに設定するとGPUを使用します

pyautogui.FAILSAFE = True

# ビデオファイルをキャプチャ
cap = cv2.VideoCapture(0)

# 手を検出するモデルを作成する
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

if processor == "gpu":
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1)
else:
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=0)

# 左手と右手の指の位置を保持する変数
prev_finger_positions_left = None
prev_finger_positions_right = None

while True:
    success, img = cap.read()

    if not success:
        print("ビデオファイルの読み取りに失敗しました。")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            landmarks = []
            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)

            for landmark in hand_lms.landmark:
                h, w, _ = img.shape
                x, y = int(landmark.x * w), int(landmark.y * h)
                landmarks.append((x, y))

            if landmarks[0][0] < landmarks[9][0]:  # 左手
                if prev_finger_positions_left is not None:
                    left_diff = []
                    left_count = []
                    for i, (prev, curr) in enumerate(zip(prev_finger_positions_left, landmarks[1:]), start=1):
                        dx, dy = curr[0] - prev[0], curr[1] - prev[1]
                        left_diff.append([dx, dy])
                        left_count.append([curr[0], curr[1]])

                    print(left_diff, left_count)
                    
                    with open("left_diff.txt", "w") as o:
                        print(left_diff, file=o)

                    with open("left_count.txt", "w") as o:
                        print(left_count, file=o)

                prev_finger_positions_left = landmarks[1:]
            else:  # 右手
                if prev_finger_positions_right is not None:
                    right_diff = []
                    right_count = []
                    for i, (prev, curr) in enumerate(zip(prev_finger_positions_right, landmarks[1:]), start=1):
                        dx, dy = curr[0] - prev[0], curr[1] - prev[1]
                        right_diff.append([dx, dy])
                        right_count.append([curr[0], curr[1]])

                    print(right_diff, right_count)
                    
                    with open("right_diff.txt", "w") as o:
                        print(right_diff, file=o)

                    with open("right_count.txt", "w") as o:
                        print(right_count, file=o)

                prev_finger_positions_right = landmarks[1:]
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


