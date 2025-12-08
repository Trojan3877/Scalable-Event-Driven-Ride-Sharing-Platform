# 🚖 Scalable Event-Driven Ride-Sharing Platform  
### Real-Time Surge Pricing • Dispatch Matching • Driver Telemetry  
**Author: Corey Leath**

---

# 🏆 Badges

### 🟦 **Big Tech System Design Patterns**
![Event Driven](https://img.shields.io/badge/System%20Design-Event--Driven-blue)
![Microservices](https://img.shields.io/badge/Architecture-Microservices-green)
![Distributed Systems](https://img.shields.io/badge/Distributed%20Systems-Ready-orange)
![Real Time](https://img.shields.io/badge/Real--Time-Streaming-brightgreen)
![Surge Pricing](https://img.shields.io/badge/Uber--Style-Surge%20Pricing-red)

### 🟩 **Engineering Quality Badges**
![Quality L5](https://img.shields.io/badge/Engineering%20Quality-L5-success)
![System Design L6](https://img.shields.io/badge/System%20Design-L6-blueviolet)
![Cloud Native](https://img.shields.io/badge/Cloud--Native-Ready-lightgrey)
![Scalable](https://img.shields.io/badge/Horizontal--Scaling-Enabled-yellow)
![High Throughput](https://img.shields.io/badge/Throughput-High-orange)
![Low Latency](https://img.shields.io/badge/Latency-Low-critical)
![Testing Ready](https://img.shields.io/badge/CI%2FCD-Ready-informational)
![Validated](https://img.shields.io/badge/Pydantic-Validated-blue)
![AsyncIO](https://img.shields.io/badge/Concurrency-AsyncIO-success)

---

# 📘 Overview

This project is a **real-time, event-driven ride-sharing platform** modeled after the core architecture used by companies such as **Uber, Lyft, and DoorDash**.

It includes:

- Real-Time **Surge Pricing Engine**  
- **Dispatch Matching System** (driver–rider assignment)  
- **Driver Location Streaming**  
- **Trip Management Pipeline**  
- Fully asynchronous event-driven architecture  
- Modular microservices designed for horizontal scaling  

This project demonstrates **L5–L6 Big Tech engineering quality**, focusing on:

- Distributed systems  
- Concurrency  
- Streaming pipelines  
- Microservice decomposition  
- System design principles  

---

# 🚀 Technologies Used (Actual Repo Stack)

| Component | Technology |
|----------|------------|
| Language | Python |
| Web Framework | FastAPI |
| Concurrency | AsyncIO |
| Validation | Pydantic |
| Event Streaming | Custom Async EventBus |
| Architecture | Microservices + PUB/SUB |
| Logging | Python Logging |
| Utils | UUID generation, timestamps, zone mapping |

---

# 🧠 System Architecture

                     ┌──────────────────────┐
                     │  Driver Location     │
                     │       Service        │
                     └─────────┬────────────┘
                               │ emits location events
                               ▼
   ┌────────────────────────────────────────────────────┐
   │                    EVENT BUS                        │
   │   (Async PUB/SUB system powering real-time flow)   │
   └─────────────────────────┬──────────────────────────┘
                             │
            ┌────────────────┼─────────────────┐
            ▼                ▼                 ▼
  ┌────────────────┐  ┌───────────────┐  ┌────────────────┐
  │ Pricing Service │  │ Dispatch      │  │ Trip Mgmt      │
  │ (Surge Engine)  │  │ Service       │  │ Service        │
  └────────────────┘  └───────────────┘  └────────────────┘
            │                │                 │
            ▼                ▼                 ▼
      Real-Time API     Match Results       Trip Status
# 🔄 Real-Time Data Flow

Producer simulates supply/demand events

PricingConsumer computes surge multipliers

Surge updates pushed to internal cache

Dispatch Service consumes rider requests

Driver Location Service streams live positions

Matching engine assigns driver → rider

Trip Management Service handles lifecycle

yaml
Copy code

---

# 📦 Microservices Included

### ✔ Pricing Service
- Computes surge pricing  
- Exposes `/pricing/surge/*` API  
- Stream-based producer + consumer  

### ✔ Dispatch Service *(coming in next commits)*  
- Assigns drivers to riders  
- Computes ETAs  
- Emits MatchResultEvents  

### ✔ Driver Location Service *(coming in next commits)*  
- Streams live driver locations  
- Maintains zone-based availability  

### ✔ Trip Management Service *(coming in next commits)*  
- Creates trips  
- Completes trips  
- Sends PaymentEvents  

---

# ⚙️ Running the Pricing Service

```bash
uvicorn src.pricing-service.main:app --reload --port 8001

