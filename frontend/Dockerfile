# ใช้ node image เวอร์ชัน LTS เป็นฐาน
FROM node:18-alpine

# กำหนด working directory
WORKDIR /app

# คัดลอกไฟล์ package.json และ package-lock.json (หรือ yarn.lock) ไปยัง container
COPY package*.json ./

# ติดตั้ง dependencies
RUN npm install

# คัดลอกโค้ดทั้งหมดไปยัง container
COPY . .

# Build แอปสำหรับ production
RUN npm run build

# กำหนด port ที่แอปจะรัน (ตามค่า default ของ Next.js)
EXPOSE 3000

# รันแอป
CMD ["npm", "start"]
