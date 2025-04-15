# 🖥️ ServerDocs – Sistema de Documentación de Infraestructura TI

ServerDocs es una aplicación web desarrollada con Django que permite a equipos de TI documentar, visualizar y gestionar servidores, entradas DNS, sistemas operativos y métricas clave de infraestructura tecnológica.

---

## 📌 Descripción General

ServerDocs nace con el objetivo de proporcionar una herramienta sencilla pero potente para la documentación y seguimiento de recursos de infraestructura. A través de un panel visual moderno, el usuario puede registrar servidores, asociarlos a entradas DNS, asignarles sistemas operativos personalizados, y visualizar datos clave en tiempo real mediante gráficos y KPIs.

---

## ⚙️ Funcionalidades Incluidas

-  **Gestión de servidores:** Registro, edición, eliminación y listado con filtros.
-  **Entradas DNS:** Asociación de entradas A, CNAME y otros tipos a servidores.
-  **Sistemas Operativos:** Registro de SO con imagen/logotipo visible.
- **Dashboard visual:** Contadores, gráficas (Chart.js) y últimas entradas.
-  **Autenticación:** Login requerido para todas las vistas sensibles.
-  **Pruebas manuales y automatizadas:** Pruebas funcionales y flujo de login con Selenium.

---

## 💻 Tecnologías utilizadas

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Gráficas:** Chart.js
- **Interactividad:** JavaScript, Fetch API
- **Base de Datos:** SQLite (desarrollo) / PostgreSQL (producción opcional)
- **Pruebas:** Selenium, Django Test Client
- **Gestión:** Azure DevOps (User Stories, Epics, Test Plans)

---

## 🚀 Sprint Planning

### 📅 Sprint Único (1 semana)

| Día        | Actividad principal                                               |
|------------|--------------------------------------------------------------------|
| 10 abril   | Sprint Planning, backlog y estructura de proyecto                  |
| 11 abril   | Modelos y migraciones (`Server`, `OS`, `DNSServer`, `DNSEntry`)    |
| 12 abril   | Implementación de vistas y formularios CRUD                        |
| 13 abril   | Integración del dashboard, contadores y Chart.js                   |
| 14 abril   | Integración de DataTables y validaciones visuales                  |
| 15 abril   | Pruebas manuales y mejoras de seguridad                            |
| 16 abril   | Automatización de login y flujos clave con Selenium                |
| 17 abril   | Sprint Review + presentación final + documentación de pruebas      |

---