# models/deepseek/serve.py
import time

def run_model_service():
    print("DeepSeek-R1 model is running...")
    # จำลองการรัน model service แบบ loop ที่รอคำสั่ง
    while True:
        # สามารถรอรับคำสั่งหรือรัน inference ที่นี่
        time.sleep(60)

if __name__ == "__main__":
    run_model_service()
