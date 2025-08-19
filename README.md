
# 📋 Student Feedback System (Flask + Bootstrap + Docker)

A lightweight web application to collect structured feedback from students for multiple subjects using a 1–5 rating scale. Built with **Flask (Python)** and **Bootstrap**, it includes a secure **Admin Panel** to view responses and is fully containerized using **Docker** for easy deployment.

---

## 🔧 Features
- Subject-wise feedback form (PCS551–PCS573)
- Rating scale: 1 (Poor) to 5 (Excellent)
- Secure admin login to view all submissions
- Responsive user interface using Bootstrap
- Dockerized for easy local or cloud deployment

---

## 🛠 Tech Stack
| Component     | Technology         |
|---------------|--------------------|
| Backend       | Flask (Python)     |
| Frontend      | HTML, CSS, Bootstrap |
| Storage       | In-memory (Python list) |
| Deployment    | Docker             |
| Admin Access  | Flask Sessions     |

---

## 🚀 Getting Started

### 🔨 Build and Run with Docker
```bash
docker build -t student-feedback-app .
docker run -d -p 5000:5000 student-feedback-app
```

Open the app in your browser: [http://localhost:5000](http://localhost:5000)

---

## 📷 Screenshots


> - Feedback Form
> - Admin Login Page
> - Feedback Summary Table
> - Thank You Page
<img width="1234" height="402" alt="Screenshot 2025-08-19 130222" src="https://github.com/user-attachments/assets/b68b2238-0122-464d-9e3e-1b820efbe243" />
<img width="1291" height="436" alt="Screenshot 2025-08-19 125919" src="https://github.com/user-attachments/assets/e3cb5b52-3f52-4eaf-9082-f235af7de9eb" />
<img width="1274" height="428" alt="Screenshot 2025-08-19 125703" src="https://github.com/user-attachments/assets/7100bc3f-9972-43f7-a2c0-e64f905d3ec0" />
<img width="369" height="370" alt="Screenshot 2025-08-19 125638" src="https://github.com/user-attachments/assets/7034fdfb-c814-42b5-83d0-e84b0262a490" />
<img width="433" height="258" alt="Screenshot 2025-08-19 125614" src="https://github.com/user-attachments/assets/7b314748-e0f0-4e7d-a572-3b3e561cbd4d" />
<img width="1146" height="495" alt="Screenshot 2025-08-19 125537" src="https://github.com/user-attachments/assets/bb9924f9-61ea-477c-8523-bfa6fb0aec8e" />



---

## ✅ Future Scope
- Use a database like SQLite or MySQL for persistent feedback storage
- Add email notifications for admin or confirmation to students
- Implement CI/CD using Jenkins or GitHub Actions

---



---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
