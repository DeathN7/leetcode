import pyttsx3
import speechrecognition as sr
import pyautogui

# Tạo một trình tổng hợp giọng nói
engine = pyttsx3.init()

# Tạo một trình nhận dạng giọng nói
recognizer = sr.Recognizer()

# Khởi tạo một vòng lặp vô hạn
while True:

    # Lắng nghe giọng nói người dùng
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    # Nhận dạng câu lệnh của người dùng
    try:
        command = recognizer.recognize_google(audio)
        print(command)
    except:
        command = None

    # Thực hiện câu lệnh của người dùng
    if command is not None:
        if command == "mở trình duyệt":
            pyautogui.hotkey("ctrl", "l")
        elif command == "đóng trình duyệt":
            pyautogui.hotkey("ctrl", "w")
        elif command == "mở ứng dụng":
            pyautogui.click(x=100, y=100)
        elif command == "đóng ứng dụng":
            pyautogui.click(x=200, y=200)
        elif command == "mở youtube":
            pyautogui.hotkey("ctrl", "t")
            pyautogui.write("youtube.com")
            pyautogui.press("enter")
        elif command == "tìm kiếm trên youtube":
            query = recognizer.recognize_google(audio)
            pyautogui.write("https://www.youtube.com/results?search_query=" + query)
            pyautogui.press("enter")
        elif command == "tự động gõ":
            text = recognizer.recognize_google(audio)
            pyautogui.write(text)

        # Phát âm câu trả lời của AI
        engine.say("Đã thực hiện yêu cầu của bạn")
        engine.runAndWait()
