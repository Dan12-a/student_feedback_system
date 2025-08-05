
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

> Add your screenshots here:
> - Feedback Form
> - Admin Login Page
> - Feedback Summary Table
> - Thank You Page

---

## ✅ Future Scope
- Use a database like SQLite or MySQL for persistent feedback storage
- Add email notifications for admin or confirmation to students
- Implement CI/CD using Jenkins or GitHub Actions

---



---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
