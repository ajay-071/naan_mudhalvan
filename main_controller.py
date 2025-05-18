import cv2
from traffic_sign_detection import detect_traffic_signs
from obstacle_detection import read_distance
from line_follower import follow_line
from motor_control import move_forward, stop

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detect_traffic_signs(frame)
        follow_line(frame)

        distance = read_distance()
        if distance and distance < 20:
            stop()
            print("Obstacle detected - stopping.")
        else:
            move_forward()

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    stop()
    cap.release()
    cv2.destroyAllWindows()