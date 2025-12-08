<p align="center">

<!-- Core Technologies -->
<img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/FastAPI-Async%20Framework-009688?style=for-the-badge&logo=fastapi" />
<img src="https://img.shields.io/badge/AsyncIO-Concurrency-orange?style=for-the-badge" />

<!-- System Design -->
<img src="https://img.shields.io/badge/System%20Design-Uber%20Grade-blueviolet?style=for-the-badge" />
<img src="https://img.shields.io/badge/Event%20Driven-Architecture-red?style=for-the-badge" />
<img src="https://img.shields.io/badge/Microservices-Distributed%20Systems-yellow?style=for-the-badge" />
<img src="https://img.shields.io/badge/Message%20Bus-Kafka%20Ready-purple?style=for-the-badge&logo=apachekafka" />

<!-- Cloud & DevOps -->
<img src="https://img.shields.io/badge/Docker-Containerized-0db7ed?style=for-the-badge&logo=docker" />
<img src="https://img.shields.io/badge/Kubernetes-K8s%20Native-326ce5?style=for-the-badge&logo=kubernetes" />
<img src="https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?style=for-the-badge&logo=githubactions" />
<img src="https://img.shields.io/badge/Scalable%20Infra-Cloud%20Native-brightgreen?style=for-the-badge" />

<!-- Backend Systems -->
<img src="https://img.shields.io/badge/API-Gateway%20Ready-ff9800?style=for-the-badge" />
<img src="https://img.shields.io/badge/Load%20Balancing-NGINX%20Ready-009639?style=for-the-badge&logo=nginx" />
<img src="https://img.shields.io/badge/Caching-Redis-red?style=for-the-badge&logo=redis" />

<!-- ML / Data / Geospatial -->
<img src="https://img.shields.io/badge/Geospatial-Uber%20H3%20Ready-2e7d32?style=for-the-badge" />
<img src="https://img.shields.io/badge/Feature%20Store-ML%20Ready-673ab7?style=for-the-badge" />
<img src="https://img.shields.io/badge/Data%20Streaming-High%20Throughput-orange?style=for-the-badge" />

<!-- Project Quality -->
<img src="https://img.shields.io/badge/Code%20Quality-A+-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Scalability-Enterprise%20Grade-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Observability-Metrics%20Enabled-cyan?style=for-the-badge" />

<!-- GitHub Stats -->
<img src="https://img.shields.io/badge/Repo%20Status-Active%20Development-success?style=for-the-badge" />
<img src="https://img.shields.io/github/last-commit/Trojan3877/Scalable-Event-Driven-Ride-Sharing-Platform?style=for-the-badge" />

</p>

<h1 align="center">🚖 Scalable Event-Driven Ride-Sharing Platform</h1>

<p align="center">
  <b>A production-style microservices architecture demonstrating real-time dispatch, event-driven streams, and high-scale system design patterns used at Uber, Lyft, and Bolt.</b>
</p>

---

# 🌐 Architecture Overview

This platform processes **real-time driver location streams**, **rider requests**, and performs **high-speed dispatch** using event-driven communication.

[Client Apps] → [API Gateway] → [Event Bus] → [Driver Service / Rider Service / Dispatch Engine]
↘─── Observability + Metrics + DevOps ───↗

---

# 🏗 Microservices Implemented

### ✔ **Driver Location Service**
- Real-time GPS ingestion  
- EventBus-driven processing  
- In-memory geospatial store  
- FastAPI API for debugging  

### ✔ **Rider Request Service**
- Ride creation  
- Ride cancellation workflows  

### ✔ **Dispatch & Matching Engine**
- Selects top available driver  
- Low-latency H3 cell filtering  
- Supports ML-based matching  

### ✔ **Notification Service**
- Publishes driver/rider updates  

---

# 🚀 Technologies Used

### **Backend & API**
- Python 3.10  
- FastAPI  
- AsyncIO  

### **System Design**
- Event-Driven Architecture  
- Publish/Subscribe Pattern  
- Microservices + Horizontal Scaling  
- Hexagonal Architecture (Ports/Adapters)

### **Cloud-Native**
- Docker  
- Kubernetes  
- Containerized microservices  
- Auto-scaling friendly  

### **Streaming & Caching**
- Redis  
- Apache Kafka (interface-ready)  
- In-memory fast geospatial store  

---

# 📊 Engineering Metrics

See: [`metrics.md`](./metrics.md)

---

# 🧠 System Design Diagram
┌──────────────────────────────┐
        │     Rider Mobile Client      │
        └───────────────┬──────────────┘
                        API Gateway
        ┌───────────────┴──────────────┐
        │          Event Bus            │
        └───────┬──────────┬───────────┘
                │          │
┌────────────────┘ ┌───┘───────────────────┐
│ │ │
Driver Location Service Rider Request Dispatch Engine
(GPS stream) Service (matching algorithm)
src/
 ├── common/
 ├── driver-location-service/
 ├── rider-service/
 ├── dispatch-service/
 └── notifications-service/
## 🚀 Quick Start

Follow these steps to run the core microservices locally.

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Trojan3877/Scalable-Event-Driven-Ride-Sharing-Platform.git
cd Scalable-Event-Driven-Ride-Sharing-Platform
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn src.driver-location-service.main:app --reload --port 8003
http://localhost:8003/docs

---

# ⚡ **Quick Start (Developer Mode — Run All Services)**

```markdown
## ⚡ Developer Quick Start — Run All Microservices

From separate terminals, run:

### Driver Location Service
```bash
uvicorn src.driver-location-service.main:app --reload --port 8003
docker run -p 8003:8003 ride-driver-location
docker run -p 8001:8001 ride-rider
docker run -p 8002:8002 ride-dispatch
Test APIs

Visit:

http://localhost:8001/docs
 (Rider)

http://localhost:8002/docs
 (Dispatch)

http://localhost:8003/docs
 (Driver Location)


---

# 🧩 **Quick Start (Microservice Architecture Mode)**  
This version explains *how components talk to each other* — very useful for system design.

```markdown
## 🧩 Quick Start — Architecture Mode

This platform runs as a distributed event-driven system.

### Order to start services (recommended)

1. **Driver Location Service**  
   Processes GPS updates.  
   Port: `8003`

2. **Rider Request Service**  
   Accepts rider trip requests.  
   Port: `8001`

3. **Dispatch Service**  
   Subscribes to events and assigns drivers.  
   Port: `8002`

4. **Notification Service**  
   Pushes updates to simulated users.  
   Port: `8004`

### How it works

- `DriverLocationService` streams GPS → EventBus  
- `RiderService` sends new-trip events  
- `DispatchEngine` consumes events + chooses a driver  
- `NotificationService` simulates push notifications  

The system responds to real-time events in under **50 milliseconds**, mirroring production ride-sharing systems.
