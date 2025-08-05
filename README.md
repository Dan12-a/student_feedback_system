
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
<img width="1174" height="302" alt="Screenshot 2025-08-05 145726" src="https://github.com/user-attachments/assets/53e3cee1-1878-4e16-96ab-89445b86c2b8" />
<img width="352" height="305" alt="Screenshot 2025-08-05 145645" src="https://github.com/user-attachments/assets/703b7fc6-3fe0-4f2a-89e7-dafec4b6f399" />
<img width="1131" height="486" alt="Screenshot 2025-08-05 145621" src="https://github.com/user-attachments/assets/18ec4863-e6f9-48a7-8975-d61f3d093606" />
<img width="435" height="257" alt="Screenshot 2025-08-05 145511" src="https://github.com/user-attachments/assets/b1feb743-64c4-4ae9-b28e-e5e8b5d36c77" />
<img width="1140" height="505" alt="Screenshot 2025-08-05 145443" src="https://github.com/user-attachments/assets/cd1f70c4-5b77-494a-bb41-45fee1729e5c" />


---

## ✅ Future Scope
- Use a database like SQLite or MySQL for persistent feedback storage
- Add email notifications for admin or confirmation to students
- Implement CI/CD using Jenkins or GitHub Actions

---



---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
