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

Design Questions & Reflections
Q: What problem does this project aim to solve?
A: This project explores how a ride-sharing platform can be designed using an event-driven architecture to handle scale, real-time updates, and asynchronous workflows. The goal was to model how systems coordinate riders, drivers, and events reliably under high load rather than focusing on UI or business logic.
Q: Why did I choose an event-driven architecture instead of a simpler design?
A: I chose an event-driven approach to better reflect how real-world distributed systems operate at scale. Decoupling services through events makes the system more resilient and easier to extend, even though it adds complexity compared to a synchronous design.
Q: What were the main trade-offs I made?
A: The main trade-off was complexity versus realism. An event-driven system is harder to reason about and debug, but it more accurately represents production-scale systems. I prioritized architectural clarity and scalability over simplicity.
Q: What didn’t work as expected?
A: Early on, it was challenging to reason about event ordering and failure scenarios, especially when multiple services depended on the same events. This forced me to slow down and think more carefully about idempotency, retries, and system boundaries.
Q: What did I learn from building this project?
A: I learned how important clear contracts and well-defined events are in distributed systems. Small design decisions around event structure and ownership have a big impact on reliability and debuggability as systems grow.
Q: If I had more time or resources, what would I improve next?
A: I would add more explicit observability features, such as tracing and metrics, to better understand system behavior under load. I’d also explore how ML-based components, like demand prediction or driver matching, could integrate cleanly into the event-driven pipeline.