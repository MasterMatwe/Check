from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Cấu hình CORS (cho phép tất cả các nguồn gốc trong môi trường development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Thay "*" bằng nguồn gốc cụ thể của frontend trong môi trường production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Định nghĩa mô hình dữ liệu đầu vào
class Numbers(BaseModel):
    a: float
    b: float

@app.post("/tinhtoan")
def tinhtoan(numbers: Numbers):
    a = numbers.a
    b = numbers.b
    try:
        return {
            "Tổng": a + b,
            "Hiệu": a - b,
            "Tích": a * b,
            "Thương": a / b if b != 0 else "Không thể chia cho 0"
        }
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Không thể chia cho 0")
