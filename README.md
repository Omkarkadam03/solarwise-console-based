# ☀️ SolarWise — Intelligent ROI & Eligibility Decision Support System

> A Python-based console application for evaluating solar energy feasibility through eligibility verification, system sizing, financial analysis, environmental impact assessment, and multi-scenario comparison.

---

## 📌 Project Overview

**SolarWise** is an intelligent decision-support system developed to help users evaluate the technical, financial, and environmental feasibility of installing a solar photovoltaic (PV) system.

Traditional solar calculators generally provide only basic installation-cost or generation estimates. SolarWise goes a step further by combining:

- Eligibility verification
- Manual and automatic solar system sizing
- Residential subsidy calculation
- Commercial accelerated depreciation tax benefit
- 25-year financial simulation
- Solar panel degradation
- Electricity tariff escalation
- ROI and payback analysis
- Environmental impact estimation
- Session saving
- Multi-scenario comparison

The application is implemented as a **modular Python console application**, making the system easy to understand, maintain, modify, and extend.

---

## 🎯 Objectives

The primary objectives of SolarWise are:

1. To determine whether a user satisfies the basic eligibility requirements for solar installation analysis.
2. To provide both **Manual Mode** and **Auto-Sizer Mode** for determining the required solar capacity.
3. To calculate installation cost and applicable financial benefits.
4. To distinguish between residential and commercial financial models.
5. To simulate solar generation and financial savings over a **25-year period**.
6. To account for annual solar panel degradation and electricity tariff escalation.
7. To estimate the environmental benefits of solar energy adoption.
8. To allow users to save multiple simulation sessions.
9. To compare different solar configurations and support informed decision-making.

---

## ✨ Key Features

### 1. 🔐 Eligibility Gatekeeper

Before performing calculations, SolarWise verifies the basic eligibility conditions:

- Citizenship eligibility
- Roof ownership / roof rights

The financial analysis proceeds only when the required eligibility conditions are satisfied.

---

### 2. ⚡ Hybrid Solar Capacity Input

SolarWise provides two methods for determining system capacity.

#### Manual Mode

The user directly enters the required solar capacity in kilowatts.

Example:

```text
Enter Solar Capacity: 3 kW
````

#### Auto-Sizer Mode

The system calculates the required solar capacity based on:

* Monthly electricity bill
* Electricity tariff per unit

The calculation follows:

```text
Daily Units = (Monthly Bill / Tariff) / 30

Required kW = Daily Units / (5 × 0.8)
```

This allows users who do not know their required solar capacity to obtain an estimated system size from their electricity consumption.

---

### 3. 🏠 Residential Financial Model

For residential users, SolarWise applies the defined subsidy model:

```text
Subsidy = min(Capacity × ₹30,000, ₹78,000)
```

Therefore, the subsidy cannot exceed:

```text
₹78,000
```

The final net installation cost is:

```text
Net Cost = Total Cost − Subsidy
```

---

### 4. 🏢 Commercial Financial Model

For commercial users, the system uses an accelerated depreciation tax benefit instead of the residential subsidy.

The tax shield is calculated as:

```text
Tax Shield = Total Cost × 0.40 × 0.30
```

Where:

* `0.40` = 40% accelerated depreciation
* `0.30` = 30% assumed tax rate

The resulting net cost is:

```text
Net Cost = Total Cost − Tax Shield
```

Residential subsidy and commercial tax benefits are treated as separate sector-specific benefits.

---

## 💰 Financial Calculation Model

### Installation Cost

The base installation cost is:

```text
₹60,000 per kW
```

Therefore:

```text
Total Cost = Capacity × ₹60,000
```

For example:

```text
Capacity = 3 kW

Total Cost = 3 × 60,000
           = ₹1,80,000
```

---

## ☀️ Solar Generation Model

SolarWise estimates annual electricity generation using:

```text
Yearly Generation =
Capacity × 365 × 5 × 0.8
```

Where:

| Parameter             | Value |
| --------------------- | ----: |
| Days per year         |   365 |
| Average sun hours/day |     5 |
| System efficiency     |   80% |

For a 3 kW system:

```text
3 × 365 × 5 × 0.8
= 4,380 kWh/year
```

---

## 📈 25-Year Financial Simulation

SolarWise performs a long-term simulation over:

```text
25 Years
```

The simulation incorporates two major factors:

### Solar Panel Degradation

Solar generation decreases by:

```text
0.5% per year
```

The next year's generation is calculated as:

```text
Generationₙ = Generationₙ₋₁ × 0.995
```

For example:

```text
Year 1 = 4,380 kWh

Year 2 = 4,380 × 0.995
       = 4,358.1 kWh
```

---

### Electricity Tariff Escalation

The electricity tariff increases by:

```text
5% per year
```

The next year's tariff is therefore:

```text
Tariffₙ = Tariffₙ₋₁ × 1.05
```

This allows the model to account for increasing electricity costs over the lifetime of the system.

---

## 💵 Annual Savings

Annual electricity savings are estimated using:

```text
Annual Savings =
Annual Solar Generation × Electricity Tariff
```

As the simulation progresses:

* Solar generation gradually decreases because of degradation.
* Electricity tariff gradually increases because of tariff escalation.

The interaction of these two variables is incorporated into the 25-year projection.

---

## ⏱️ Payback Period

The system calculates the approximate payback period by tracking cumulative savings.

Conceptually:

```text
Cumulative Savings = Previous Cumulative Savings + Annual Savings
```

The payback period is reached when cumulative savings recover the effective initial investment:

```text
Cumulative Savings ≥ Net Cost
```

The corresponding year is reported as the estimated payback period.

---

## 🌱 Environmental Impact

SolarWise also evaluates the environmental benefits associated with solar electricity generation.

The system provides environmental indicators such as:

* CO₂ emissions avoided
* Equivalent trees
* Coal consumption avoided

These metrics help demonstrate the sustainability benefits of replacing conventional grid electricity with solar generation.

---

## 💾 Session Management

SolarWise supports multiple simulation sessions.

After completing one analysis, the user can choose to:

* Save the current session
* Run another simulation
* Compare saved sessions
* Exit the application

This allows users to evaluate different combinations of:

```text
Capacity
Sector
Tariff
Financial benefit
Savings
Payback period
Environmental impact
```

---

## 📊 Scenario Comparison

The comparison feature displays saved simulations in a structured `PrettyTable`.

Example:

```text
+---------+------+-------------+----------+----------+----------+--------+
| Sr. No. | kW   | Sector      | Net Cost | Savings  | Payback  | CO2    |
+---------+------+-------------+----------+----------+----------+--------+
|    1    |  3   | Residential | 102000   | 850000   |    3     | 45000  |
|    2    |  5   | Commercial  | 264000   | 1400000  |    4     | 72000  |
+---------+------+-------------+----------+----------+----------+--------+
```

This makes it easier for users to compare multiple scenarios before making a decision.

---

### Main Components

| File              | Responsibility                                           |
| ----------------- | -------------------------------------------------------- |
| `main.py`         | Controls application flow and user interaction           |
| `config.py`       | Stores project constants and assumptions                 |
| `finance.py`      | Handles financial calculations and 25-year simulation    |
| `session.py`      | Manages saved sessions and scenario comparison           |
| `calculations.py` | Performs supporting technical/environmental calculations |

> The exact file names may vary depending on the final project structure.

---

# 🛠️ Technology Stack

### Programming Language

**Python 3**

### Libraries

* **PrettyTable** — formatted console tables
* Python Standard Library — application logic and data processing

### Development Environment

The project can be executed using:

* Windows
* Linux
* macOS
* Any environment supporting Python 3

---

# 🔄 Application Workflow

The overall application flow can be summarized as:

```text
                    ┌──────────────────────┐
                    │       START          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Eligibility Check    │
                    │ Citizenship + Roof   │
                    │ Rights               │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Select Input Mode    │
                    │                      │
                    │ Manual / Auto-Sizer  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Select Sector        │
                    │ Residential /        │
                    │ Commercial           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Financial Analysis   │
                    │ Cost + Benefit       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ 25-Year Simulation   │
                    │ Degradation + Tariff │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Environmental        │
                    │ Impact Analysis      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Display Results      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Save Session?        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Run Another /        │
                    │ Compare / Exit       │
                    └──────────────────────┘
```

---

# 🧮 Core Constants

The current model uses the following assumptions:

| Parameter                         |       Value |
| --------------------------------- | ----------: |
| Solar installation cost           |  ₹60,000/kW |
| Average sun hours                 | 5 hours/day |
| System efficiency                 |         80% |
| Simulation period                 |    25 years |
| Annual degradation                |        0.5% |
| Annual tariff escalation          |          5% |
| Residential subsidy               |  ₹30,000/kW |
| Maximum residential subsidy       |     ₹78,000 |
| Commercial depreciation           |         40% |
| Assumed commercial tax rate       |         30% |
| Days used for monthly calculation |          30 |

Centralizing these values in `config.py` makes the application easier to maintain and modify.

---

# 🔍 Example Use Case

Consider a residential user who wants to evaluate a 3 kW solar installation.

### Step 1 — Installation Cost

```text
3 × ₹60,000 = ₹1,80,000
```

### Step 2 — Residential Subsidy

```text
min(3 × ₹30,000, ₹78,000)
= ₹78,000
```

### Step 3 — Net Cost

```text
₹1,80,000 − ₹78,000
= ₹1,02,000
```

### Step 4 — Annual Generation

```text
3 × 365 × 5 × 0.8
= 4,380 kWh/year
```

The system then uses this generation as the basis for the 25-year simulation while applying annual degradation and tariff escalation.

---

# 📊 Why SolarWise Is a Decision-Support System

SolarWise is designed beyond the functionality of a basic solar calculator.

A conventional calculator may answer:

> “How much will a solar system cost?”

SolarWise attempts to answer a broader question:

> “Which solar configuration is financially and environmentally suitable for my situation?”

The system achieves this by combining:

```text
Eligibility
     +
System Sizing
     +
Financial Benefits
     +
Long-Term Simulation
     +
Environmental Impact
     +
Scenario Comparison
     =
Decision Support
```

---

# 🚀 Future Scope

The current console application can be extended in several directions.

### 1. Web-Based Interface

The existing calculation engine can be integrated with a React or other web-based interface for a more accessible user experience.

### 2. Live Weather Data

Real-time weather and solar irradiance APIs could be integrated to replace fixed average sun-hour assumptions.

### 3. Location-Based Analysis

Latitude, longitude, local solar irradiation, and regional electricity tariffs could be incorporated for more location-specific predictions.

### 4. IoT Integration

Smart meters and IoT-enabled solar monitoring systems could provide actual generation and consumption data.

### 5. Advanced Predictive Models

Machine learning models could be incorporated to predict:

* Solar generation
* Electricity consumption
* Tariff trends
* Long-term financial returns

### 6. Database Integration

A database could replace in-memory session storage, allowing users to permanently store and retrieve previous analyses.

### 7. Policy Updates

Government subsidy and tax-benefit parameters can be updated through configuration or external policy data sources.

---

# 🔒 Limitations

The current system is an analytical prototype and uses predefined assumptions.

Some important limitations include:

* Solar generation is based on a fixed average of 5 sun-hours per day.
* Actual weather conditions are not directly used in the basic calculation.
* Electricity tariff escalation is modeled at a fixed 5% annually.
* Panel degradation is modeled at a fixed 0.5% annually.
* Installation cost is based on a fixed ₹60,000/kW assumption.
* Environmental conversion factors depend on predefined assumptions.
* Actual project economics may vary depending on location, installer, financing, electricity consumption patterns, and applicable government policies.

Therefore, the results should be considered **decision-support estimates rather than guaranteed financial returns**.

---

# 🎓 Academic Context

**Project Title:**
SolarWise: Intelligent ROI & Eligibility Decision Support System

**Domain:**
Predictive Analytics for Sustainable Development

**Application Area:**
Renewable Energy / Environmental Science / Data Science

**Implementation:**
Python Console Application

---

# 📄 License

This project is developed for academic and educational purposes.

You may modify and extend the project for learning, experimentation, and academic demonstrations.

---

# ⭐ Project Summary

**SolarWise** combines technical sizing, financial modeling, environmental analysis, and scenario comparison into a single Python-based decision-support system.

Its modular architecture allows the system to be extended from a console-based academic prototype into a larger renewable-energy analytics platform incorporating real-time data, IoT devices, predictive models, and web-based visualization.

---

## ☀️ SolarWise

**Analyze. Compare. Decide. Go Solar.**

```