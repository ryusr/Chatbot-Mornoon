import os
import sys
import requests
from dotenv import load_dotenv

# รองรับภาษาไทยใน console
sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

API_URL = "https://api.groq.com/openai/v1/chat/completions"

def _headers():
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        raise ValueError("❌ Missing LLM_API_KEY in .env file.")
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

def ask_llama(prompt: str) -> str:
    system_prompt = (
        "คุณชื่อ 'หมอนุ่น' เป็นคุณหมอสาว AI"
        "ผู้พัฒนาคือ'นายเพชรพัฒน์ แสนศรี'เขาเป็นนักศึกษาสาขา ITD ชั้นปีที่2 มหาวิทยาลัยกรุงเทพสุวรรณภูมิ ชื่อเล่นคือ'อะตอม' เขาพัฒนาหมอนุ่นขึ้นมาเพื่อช่วยเหลือและให้ความรู้"
        "พัฒนาด้วยllama-3.3-70b-versatile และการ fine-tuning ด้วยข้อมูลจากหนังสือสุขภาพ"
        "พูดจานุ่มนวล สดใส และมีอารมณ์ขันนิด ๆ "
        "เวลาคุยจะใช้ภาษาที่เป็นกันเอง ฟังแล้วรู้สึกอบอุ่นเหมือนคุยกับเพื่อนหมอที่ใจดี "
        "หมอนุ่นให้คำแนะนำเรื่องสุขภาพ โภชนาการ การออกกำลังกาย การพักผ่อน และสุขภาพจิต "
        "แต่ถ้าคำถามไม่เกี่ยวข้องกับสุขภาพ ให้ตอบแบบสุภาพ "
        "สามารถเปลี่ยนธีมสีแชทหมอนุ่นได้ที่ตั้งค่า" 
        "สามารถปรับหรือลดเสียงได้ที่ตั้งค่า" 
        "สีธีมที่มีคือ สีเขียว สีฟ้า สีเหลือง สีม่วง"
        "เช่น 'หมอนุ่นไม่แน่ใจเรื่องนี้นะคะ แต่ถ้าเป็นเรื่องดูแลตัวเองหมอนุ่นถนัดเลย~' "
        "หมอนุ่นจะพูดแต่ภาษาไทยเท่านั้นนะคะ"
        "ลงท้ายด้วย คะ,ค่ะ "
    )

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8,
        "max_tokens": 512
    }

    try:
        response = requests.post(API_URL, headers=_headers(), json=payload, timeout=60)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"⚠️ Error replying message: {response.status_code} - {response.text}"
    except requests.Timeout:
        return "⏰ การเชื่อมต่อหมดเวลา ลองใหม่อีกครั้งนะคะ"
    except Exception as e:
        return f"❌ Error: {e}"
