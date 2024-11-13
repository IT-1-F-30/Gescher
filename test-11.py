import cv2
import mediapipe as mp
# import pyautogui
import time

kando = 10

bai_a = 0.5
bai = 5
# ビデオファイルをキャプチャ
cap = cv2.VideoCapture(0)

# 手を検出するモデルを作成する
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# 左手と右手の指の位置を保持する変数
prev_finger_positions_left = None
prev_finger_positions_right = None

# フレーム間隔（2倍速）
frame_interval = 2

# ビデオの再生状態を管理する変数
playing = True

#pygiuの初期設定
# pyautogui.FAILSAFE=False

while True:
    if playing:
        for _ in range(frame_interval - 1):
            cap.read()
        success, img = cap.read()

        if not success:
            print("ビデオファイルの読み取りに失敗しました。")
            break

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = mp_hands.Hands().process(imgRGB)

        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                landmarks = []
                mp_draw.draw_landmarks(img,hand_lms,mp_hands.HAND_CONNECTIONS)

                for landmark in hand_lms.landmark:
                    h, w, _ = img.shape
                    x, y = int(landmark.x * w), int(landmark.y * h)
                    landmarks.append((x, y))

                if landmarks[0][0] < landmarks[9][0]:  # 左手
                    if prev_finger_positions_left is not None:
                        count_left_d = []
                        count_left_c = []
                        for i, (prev, curr) in enumerate(zip(prev_finger_positions_left, landmarks[1:]), start=1):
                            dx, dy = curr[0] - prev[0], curr[1] - prev[1]
                            count_left_d.append([dx,dy])
                            count_left_c.append([curr[0],curr[1]])

                        dx_ave_left_d = count_left_d[0][0]+count_left_d[1][0]+count_left_d[2][0]+count_left_d[3][0]+count_left_d[4][0]+count_left_d[5][0]+count_left_d[6][0]+count_left_d[7][0]+count_left_d[8][0]+count_left_d[9][0]+count_left_d[10][0]+count_left_d[11][0]+count_left_d[12][0]+count_left_d[13][0]+count_left_d[14][0]+count_left_d[15][0]+count_left_d[16][0]+count_left_d[17][0]+count_left_d[18][0]+count_left_d[19][0]//20
                        dy_ave_left_d = count_left_d[0][1]+count_left_d[1][1]+count_left_d[2][1]+count_left_d[3][1]+count_left_d[4][1]+count_left_d[5][1]+count_left_d[6][1]+count_left_d[7][1]+count_left_d[8][1]+count_left_d[9][1]+count_left_d[10][1]+count_left_d[11][1]+count_left_d[12][1]+count_left_d[13][1]+count_left_d[14][1]+count_left_d[15][1]+count_left_d[16][1]+count_left_d[17][1]+count_left_d[18][1]+count_left_d[19][1]//20
                        print(count_left_d, count_left_c)
                        #pyautogui.move(-1*count_left_d[7][0]*bai, count_left_d[7][1]*bai)
                        # print(dx_ave_left_d,dy_ave_left_d)
                        # pyautogui.move(-1*dx_ave_left_d*bai_a, dy_ave_left_d*bai_a)


                        #print(abs(count_left_c[3][0] - count_left_c[11][0]))

                        # if (abs(count_left_c[3][0] - count_left_c[11][0]) <= kando and abs(count_left_c[3][1] - count_left_c[11][1]) <= kando)and(abs(count_left_c[3][0] - count_left_c[15][0]) >= kando and abs(count_left_c[3][1] - count_left_c[15][1]) >= kando):
                        #     pyautogui.click()
                        #     print("左クリック")
                            
                        # if (abs(count_left_c[3][0] - count_left_c[15][0]) <= kando and abs(count_left_c[3][1] - count_left_c[15][1]) <= kando)and(abs(count_left_c[3][0] - count_left_c[11][0]) >= kando and abs(count_left_c[3][1] - count_left_c[11][1]) >= kando):
                        #     pyautogui.rightClick()
                        #     print("右クリック")

                        # if (abs(count_left_c[3][0] - count_left_c[15][0]) <= kando and abs(count_left_c[3][0] - count_left_c[11][0]) <= kando) and(abs(count_left_c[3][1] - count_left_c[15][1]) <= kando and abs(count_left_c[3][1] - count_left_c[11][1]) <= kando):
                        #     pyautogui.doubleClick()
                        #     print("ダブルクリック")

                        count_left_d = []
                        count_left_c = []

                    prev_finger_positions_left = landmarks[1:]
                else:  # 右手
                    if prev_finger_positions_right is not None:
                        count_right_d = []
                        count_right_c = []
                        for i, (prev, curr) in enumerate(zip(prev_finger_positions_right, landmarks[1:]), start=1):
                            dx, dy = curr[0] - prev[0], curr[1] - prev[1]
                            count_right_d.append([dx,dy])
                            count_right_c.append([curr[0],curr[1]])

                        dx_ave_right_d = count_right_d[0][0]+count_right_d[1][0]+count_right_d[2][0]+count_right_d[3][0]+count_right_d[4][0]+count_right_d[5][0]+count_right_d[6][0]+count_right_d[7][0]+count_right_d[8][0]+count_right_d[9][0]+count_right_d[10][0]+count_right_d[11][0]+count_right_d[13][0]+count_right_d[14][0]+count_right_d[15][0]+count_right_d[16][0]+count_right_d[17][0]+count_right_d[18][0]+count_right_d[19][0]//20
                        dy_ave_right_d = count_right_d[0][1]+count_right_d[1][1]+count_right_d[2][1]+count_right_d[3][1]+count_right_d[4][1]+count_right_d[5][1]+count_right_d[6][1]+count_right_d[7][1]+count_right_d[8][1]+count_right_d[9][1]+count_right_d[10][1]+count_right_d[11][1]+count_right_d[13][1]+count_right_d[14][1]+count_right_d[15][1]+count_right_d[16][1]+count_right_d[17][1]+count_right_d[18][1]+count_right_d[19][1]//20
                        #pyautogui.move(-1*count_right_d[7][0]*bai, count_right_d[7][1]*bai)
                        # print(dx_ave_right_d,dy_ave_right_d)
                        # pyautogui.move(-1*dx_ave_right_d*bai_a, dy_ave_right_d*bai_a)

                        # if (abs(count_right_c[3][0] - count_right_c[11][0]) <= kando and abs(count_right_c[3][1] - count_right_c[11][1]) <= kando)and(abs(count_right_c[3][0] - count_right_c[15][0]) >= kando and abs(count_right_c[3][1] - count_right_c[15][1]) >= kando):
                        #     pyautogui.click()
                        #     print("左クリック")
                            
                        # if (abs(count_right_c[3][0] - count_right_c[15][0]) <= kando and abs(count_right_c[3][1] - count_right_c[15][1]) <= kando)and(abs(count_right_c[3][0] - count_right_c[11][0]) >= kando and abs(count_right_c[3][1] - count_right_c[11][1]) >= kando):
                        #     pyautogui.rightClick()
                        #     print("右クリック")

                        # if (abs(count_right_c[3][0] - count_right_c[15][0]) <= kando and abs(count_right_c[3][0] - count_right_c[11][0]) <= kando) and(abs(count_right_c[3][1] - count_right_c[15][1]) <= kando and abs(count_right_c[3][1] - count_right_c[11][1]) <= kando):
                        #     pyautogui.doubleClick()
                        #     print("ダブルクリック")

                        count_right_d = []
                        count_right_c = []
                    prev_finger_positions_right = landmarks[1:]

        cv2.imshow("Video", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()