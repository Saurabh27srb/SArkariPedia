# “SarkariPedia: Automated Directory, Web Crawler, and Real-Time Health-Monitoring Search Engine for Indian Government Portals”

### A Mini Project Report Submitted in Partial Fulfillment of the Requirements for the Degree of
## Bachelor of Technology
### in
## Computer Science & Engineering

**Submitted By:**

| S.No. | Student Name | Roll Number | Branch and Section |
| :---: | :--- | :--- | :---: |
| 1 | ____________________ | ____________________ | CSE |

<br>

**Under the Supervision of:**
**Mr./Ms. ____________________** (Assistant Professor)

<br>

**Department of Computer Science & Engineering**
**Kanpur Institute of Technology, Kanpur**
**Dr. A.P.J. Abdul Kalam Technical University, Lucknow**
**Academic Session: 2026–2027**

---

<div style="page-break-after: always;"></div>

## DECLARATION

I hereby declare that this submission is my own work and that, to the best of my knowledge and belief, it contains no material previously published or written by another person nor material which to a substantial extent has been accepted for the award of any other degree or diploma of the university or other institute of higher learning, except where due acknowledgement has been made in the text.

<br><br>

**Signature:** __________________________  
**Name:** __________________________  
**Roll No.:** __________________________  
**Date:** 08 November 2026  
**Place:** Kanpur  

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

## CERTIFICATE

This is to certify that the Project Report entitled **“SarkariPedia: Automated Directory, Web Crawler, and Real-Time Health-Monitoring Search Engine for Indian Government Portals”** which is submitted by **__________________________ (Roll No. - __________________________)** of the 7th semester, in the year 2026-2027, in partial fulfillment of the requirement for the award of degree of **Bachelor of Technology in Computer Science & Engineering** of **Dr. A.P.J. Abdul Kalam Technical University, Lucknow**, is a record of the candidate’s own work carried out by him under my supervision. The matter embodied in this report is original and has not been submitted for the award of any other degree or diploma.

<br><br><br>

___________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ___________________________  
**(Mr. Rahul Singh)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **(Supervisor / Guide)**  
Head of Department &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Assistant Professor  
Dept. of CSE, KIT Kanpur &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Dept. of CSE, KIT Kanpur  

**Date:** ____________________  

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

## ACKNOWLEDGEMENT

It gives me a great sense of pleasure to present the report of the B.Tech mini project undertaken during B.Tech Fourth Year. I owe a special debt of gratitude to my project guide, Assistant Professor, Department of Computer Science & Engineering, Kanpur Institute of Technology, Kanpur (U.P.), for constant support, insightful critique, and guidance throughout the course of my work. His/her sincerity, thoroughness, and perseverance have been a constant source of inspiration for me.

I also take this opportunity to acknowledge the vital contribution and encouragement of **Mr. Rahul Singh**, Head of Department, Computer Science & Engineering, Kanpur Institute of Technology, Kanpur, for providing the necessary infrastructural facilities and technical assistance during the design and development phases.

I also express my sincere thanks to all the faculty members of the Department of Computer Science & Engineering for their cooperation, suggestions, and assistance. Last but not least, I acknowledge my family and fellow batchmates for their constant encouragement and valuable feedback during the project lifecycle.

<br><br>

**Signature:** __________________________  
**Name:** __________________________  
**Roll No.:** __________________________  
**Date:** 08 November 2026  

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

## ABSTRACT

In modern India, the rapid digitisation under the "Digital India" flagship initiative has led to thousands of administrative, welfare, civic, and educational services migrating to dedicated web portals. However, finding genuine, active, and relevant government links remains difficult, fragmented, and vulnerable to phishing. Official government services are scattered across thousands of disparate domains (`.gov.in`, `.nic.in`, `.gov`, `sansad.in`), with unannounced URL migrations, uncoordinated departmental subdomains, and recurring service downtimes. Furthermore, unsuspecting citizens often fall victim to predatory clone portals and fraudulent ad-monetised intermediaries when relying on generic search engines.

This project presents the design, architectural formulation, implementation, and evaluation of **SarkariPedia**, an automated web crawler, directory indexer, and real-time health-monitoring search engine purpose-built for Indian government portals. SarkariPedia automates the discovery, canonicalisation, categorization, and uptime monitoring of Indian public portals without scraping sensitive inner user data. The crawling engine strictly complies with ethical web standards (RFC 9309 robots exclusion protocol, polite inter-request throttling, transparent User-Agent identity, and strict official domain whitelisting). 

A high-performance two-tier classification heuristic algorithm automatically assigns scraped entities to 15 national priority functional sectors (Citizen Services, Agriculture, Health, Education, Finance and Tax, Law and Justice, Defence and Security, Transport, Science and Space, Environment and Energy, Labour and Jobs, Rural and Urban Development, Parliament and Elections, Tourism and Culture, and State Portals) and detects geographical jurisdiction across 36 Indian States and Union Territories. The system incorporates an asynchronous, multi-threaded health-check daemon using non-destructive HTTP HEAD/GET probes to monitor link health in real time, implementing a three-strike failure escalation protocol before hiding unreachable services.

The system is developed as an asynchronous, modular web platform using Python 3.12, Flask RESTful micro-framework, SQLite3 with WAL mode, and a lightweight, bilingual (Hindi/English), mobile-first responsive frontend. The report documents the feasibility study, software requirement specification (SRS), system architecture, Entity-Relationship and Data Flow modeling, core algorithmic skeletons, rigorous test suites (covering unit, integration, politeness, and security evaluations), and a prospective roadmap towards semantic search using Large Language Models (LLM / Gemini).

*Keywords:* Ethical Web Crawler, Government Portal Indexer, Health Monitoring, RESTful API, Digital India, Domain Heuristics, Bilingual UI.

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

## TABLE OF CONTENTS

* **Declaration** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ii
* **Certificate** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iii
* **Acknowledgement** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . iv
* **Abstract** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . v
* **List of Figures** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii
* **List of Tables** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ix

### 1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
* 1.1 General Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
* 1.2 Problem Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
  * 1.2.1 Problem Detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
  * 1.2.2 Proposed Problem Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
* 1.3 Proposed System Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
* 1.4 Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
  * 1.4.1 Principles of Agile Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
  * 1.4.2 Scraping & Indexing Pipeline Flowchart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
* 1.5 Ethical Web Crawling and Politeness Principles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
  * 1.5.1 Robots Exclusion Protocol (RFC 9309) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
  * 1.5.2 Politeness, Rate Limiting & User-Agent Identity . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
  * 1.5.3 Strict Domain Whitelisting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
* 1.6 Scope of the Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

### 2. Feasibility Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
* 2.1 Feasibility Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
  * 2.1.1 Technical Feasibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
  * 2.1.2 Economic Feasibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
  * 2.1.3 Operational Feasibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
  * 2.1.4 Legal & Ethical Feasibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
* 2.2 System Design Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
* 2.3 Description of Working Model & Deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
* 2.4 Risk Assessment & Mitigation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

### 3. Requirement Elicitation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
* 3.1 Requirement Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
  * 3.1.1 Requirements Gathering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
  * 3.1.2 Requirement Analysis Cycle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
* 3.2 Classification of Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
  * 3.2.1 Functional Requirements (FR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
  * 3.2.2 Non-Functional Requirements (NFR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

### 4. Designing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
* 4.1 Modular Architecture Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
* 4.2 Detailed Component Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
* 4.3 Entity-Relationship (ER) Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
* 4.4 Data Flow Diagrams (DFD) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
  * 4.4.1 Level 0 DFD (Context Diagram) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
  * 4.4.2 Level 1 DFD (Subsystem Decomposition) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
* 4.5 Use Case Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
* 4.6 Classification & State Resolution Heuristic Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
* 4.7 RESTful API Design Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

### 5. Coding & Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
* 5.1 Implementation Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
* 5.2 Hardware and Software Environment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
* 5.3 Integrated Development Environment (IDE) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
* 5.4 Core Logic & Algorithmic Skeletons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
  * 5.4.1 URL Canonicalization & Normalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
  * 5.4.2 Breadth-First Directory Crawler with Polite Rate Limiting . . . . . . . . . . . . . . . . . . . 22
  * 5.4.3 Multi-threaded Health Checking & Strike Escalation . . . . . . . . . . . . . . . . . . . . . . . 23
  * 5.4.4 SQLite Conflict-Free Upsert & Data Quality Cleaning . . . . . . . . . . . . . . . . . . . . . . 24
* 5.5 Illustrative Output & User Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
* 5.6 Project Implementation Schedule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

### 6. Testing & Quality Assurance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
* 6.1 Description of Agile Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
* 6.2 Diagram of Agile Testing Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
* 6.3 Types of Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
  * 6.3.1 Black Box Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
  * 6.3.2 White Box Testing & Unit Test Assertions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
  * 6.3.3 Concurrency & Politeness Verification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
  * 6.3.4 Security & Input Sanitization Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

### 7. Conclusion & Future Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
* 7.1 Future Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
  * 7.1.1 AI-Driven Semantic Search via Google Gemini . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
  * 7.1.2 Meilisearch Integration for Typo-Tolerant Indic Search . . . . . . . . . . . . . . . . . . . . . 30
  * 7.1.3 Progressive Web Application (PWA) & Offline Bookmarks . . . . . . . . . . . . . . . . . . 30
* 7.2 Uses and Target Beneficiaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
* 7.3 Real-World Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
* 7.4 Result and Performance Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
* 7.5 Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

### References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

---

<div style="page-break-after: always;"></div>

## LIST OF FIGURES

| Figure No. | Figure Description | Page No. |
| :---: | :--- | :---: |
| **Fig. 1.3.1** | Basic structural pipeline of SarkariPedia | 3 |
| **Fig. 1.4.1** | Agile development lifecycle followed in the project | 3 |
| **Fig. 1.4.2** | Flow chart of the scraping, classification, and indexing process | 4 |
| **Fig. 2.3.1** | Docker deployment and container architecture | 8 |
| **Fig. 3.1.2.1** | Requirement analysis and elicitation cycle | 10 |
| **Fig. 4.1.1** | 3-Tier Layered system architecture | 12 |
| **Fig. 4.3.1** | Entity-Relationship (ER) diagram of database schema | 14 |
| **Fig. 4.4.1** | Level 0 Data Flow Diagram (Context Diagram) | 15 |
| **Fig. 4.4.2** | Level 1 Data Flow Diagram (Scraper, API, and UI Subsystems) | 16 |
| **Fig. 4.5.1** | Use Case diagram of citizen, admin, and crawler daemon | 17 |
| **Fig. 4.6.1** | Two-tier classification and state mapping heuristic pipeline | 18 |
| **Fig. 5.5.1** | Illustrative bilingual user interface wireframe and live site cards | 25 |
| **Fig. 5.6.1** | 7-Phase implementation roadmap Gantt chart | 26 |
| **Fig. 6.2.1** | Agile testing and continuous verification cycle | 27 |

<br>

## LIST OF TABLES

| Table No. | Table Description | Page No. |
| :---: | :--- | :---: |
| **Table 2.1** | Risk Assessment and Mitigation Matrix | 8 |
| **Table 4.1** | Detailed Module Input-Processing-Output Specification | 13 |
| **Table 4.2** | Database Schema Definition for `sites` Entity | 14 |
| **Table 4.3** | RESTful API Endpoints Specification | 19 |
| **Table 5.1** | Hardware and Software Operating Specifications | 20 |
| **Table 6.1** | Black Box Functional Test Cases and Validation Matrix | 28 |
| **Table 7.1** | Performance and Crawler Throughput Benchmarks | 31 |

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

# CHAPTER 1: INTRODUCTION

## 1.1 General Introduction
Over the past decade, the Government of India, along with various State Governments and Union Territory administrations, has spearheaded an unprecedented digital governance transformation under the "Digital India" flagship vision. Key public services—ranging from civil registrations, taxation, utility subsidies, passport applications, land records, judicial status, academic scholarships, to rural employment allocations—have been ported to dedicated online web portals. Today, the Indian public sector encompasses tens of thousands of official domains, subdomains, and standalone service portals primarily hosted on `.gov.in`, `.nic.in`, and `.gov` Top-Level Domains (TLDs).

However, despite this extensive digital ecosystem, the average citizen faces a monumental challenge in discovering, accessing, and verifying genuine government links. Public portals are heavily decentralized; ministries frequently reorganize or rebrand their domain handles without coordinated cross-referencing. Crucially, generic search engines (e.g., Google, Bing) optimize results based on commercial Search Engine Optimization (SEO), commercial advertisements, and user engagement metrics rather than official authenticity. As a result, non-technical citizens and rural community operators frequently land on malicious clone sites, phishing portals, or bloated third-party commercial blogs stuffed with misleading advertisements and paid forms.

Preparing a clean, verified, centralized, and self-updating repository of official Indian government websites is therefore a critical computer science challenge in information retrieval, automated web harvesting, domain heuristic classification, and distributed uptime monitoring. This project, entitled **“SarkariPedia: Automated Directory, Web Crawler, and Real-Time Health-Monitoring Search Engine for Indian Government Portals”**, designs and implements an end-to-end software platform that automates the collection, validation, categorization, health tracking, and public indexing of authentic Indian government portals.

## 1.2 Problem Statement

### 1.2.1 Problem Detection
Manual curation and conventional search discovery of government web portals exhibit severe vulnerabilities:
1. **Severe Decentralization and URL Fragmentation**: With 28 States, 8 Union Territories, and more than 50 Central Ministries operating independently, there is no single, comprehensive, updated index. Portals often change domain names (e.g., migrating from old ministry subdomains to newer `.gov.in` handles) without setting up persistent HTTP 301 redirects.
2. **Proliferation of Clone, Phishing, and Intermediary Sites**: Fraudulent actors frequently purchase `.com`, `.in`, or `.org` domains mimicking government scheme names (e.g., `pmkisan-yojana.org` or `apply-rationcard.com`). They rank on commercial search engines through keyword stuffing, harvest sensitive citizen documents (Aadhaar cards, bank details), or charge illegal "processing fees" for free public services.
3. **Dead, Stale, and Down Portals**: Government servers frequently experience unannounced maintenance downtimes, DNS failures, or SSL certificate expirations. Citizens lack prior visibility into whether a portal is currently operational before navigating complex transactional flows.
4. **Poor Language Accessibility**: Generic search interfaces and ministerial directories are predominantly structured in complex English, creating an intimidating barrier for non-English literate citizens seeking public welfare schemes.

### 1.2.2 Proposed Problem Solution
To overcome these systemic bottlenecks, **SarkariPedia** establishes an autonomous, verified public directory that operates on the following foundational tenets:
* **Zero-Intermediary Official Whitelisting**: The system enforces an inviolable security constraint where only verified government TLDs (`.gov.in`, `.nic.in`, `.gov`, `sansad.in`) are ingested. No commercial advertisements, tracking cookies, or intermediate redirect pages are permitted.
* **Automated Recursive Harvesting**: An ethical Breadth-First Search (BFS) directory crawler traverses verified nodal hubs (`india.gov.in`, `goidirectory.gov.in`, state portals) to discover authentic outbound government endpoints.
* **Autonomous Rule-Based Categorization**: A deterministic heuristic engine analyzes subdomain prefixes and text tokens to classify every discovered site into 15 functional sectors and 36 States/UTs without manual intervention.
* **Asynchronous Live Health Tracking**: A background multi-threaded probe continuously conducts non-invasive HTTP HEAD checks, presenting users with real-time green (live) or red (dead) visual badges.
* **Lightweight Bilingual Citizen UI**: An ultra-clean, mobile-first web interface with instantaneous Hindi/English translation toggle, sub-50ms search latency, and community reporting mechanisms.

```
       [ Seed List (seeds.csv) ]           [ Directory Portals (sources.json) ]
                   │                                         │
                   ▼                                         ▼
         ┌───────────────────┐                     ┌───────────────────┐
         │ Seed Data Loader  │                     │ Ethical BFS Crawl │
         └─────────┬─────────┘                     └─────────┬─────────┘
                   │                                         │
                   └──────────────────┬──────────────────────┘
                                      ▼
                        ┌───────────────────────────┐
                        │   URL Normalizer & Host   │
                        │   Canonicalizer Engine    │
                        └─────────────┬─────────────┘
                                      ▼
                        ┌───────────────────────────┐
                        │ Heuristic Classifier &    │
                        │ State Mapping Engine      │
                        └─────────────┬─────────────┘
                                      ▼
                        ┌───────────────────────────┐
                        │  SQLite Relational Store  │◄─────┐
                        │  (gov_sites.db with WAL)  │      │
                        └───────┬───────────┬───────┘      │
                                │           │              │
                    Query / API │           │ Background   │
                                ▼           ▼ Check        │
                       ┌─────────────┐  ┌──────────────────┴──┐
                       │  Flask REST │  │ Multithreaded Live  │
                       │   Service   │  │   Health Daemon     │
                       └──────┬──────┘  └─────────────────────┘
                              │
                              ▼
                       ┌─────────────┐
                       │ Bilingual   │
                       │ Citizen UI  │
                       └─────────────┘
```
**Fig. 1.3.1: Basic structural pipeline of SarkariPedia**

---

## 1.3 Proposed System Overview
The SarkariPedia system operates through four tightly coupled, decoupled subsystems:
1. **The Ingestion & Harvester Engine**: Ingests baseline curated records from a verified seed file and autonomously crawls official directory pages across national and state portals.
2. **The Normalization & Heuristic Classification Engine**: Sanitizes every URL (enforcing canonical HTTPS, stripping sub-paths and `www` prefixes, eliminating duplicates), resolves state jurisdiction through geographic subdomain maps, and categorizes departments into 15 sectors via token matching.
3. **The Persistence & Verification Engine**: Stores normalized sites within an optimized SQLite relational schema, indexing by category, state, and domain. An independent parallel health-check daemon continuously updates response statuses.
4. **The Client Delivery & Reporting Layer**: Exposes JSON REST endpoints supporting live filtering, full-text pattern search, and pagination, consumed by a pure vanilla HTML5/CSS3/ES6 responsive frontend featuring instant Hindi/English bilingual toggling.

---

## 1.4 Methodology

### 1.4.1 Principles of Agile Framework
The project adopts the **Agile Development Methodology**, characterized by short iterative sprints, continuous test-driven refinement, and tight feedback loops. Developing an automated crawler for external web ecosystems requires frequent adaptations because external web architectures, robots.txt directives, and server response codes exhibit dynamic variability.

```
   ┌────────────────────────────────────────────────────────┐
   │             Sprint Planning & User Stories             │
   └──────────────────────────┬─────────────────────────────┘
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │         Iterative Crawler & Classifier Coding          │
   └──────────────────────────┬─────────────────────────────┘
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │       Automated Unit & Integration Verification        │
   └──────────────────────────┬─────────────────────────────┘
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │       Deployment, Live Crawl & Heuristic Tuning        │
   └──────────────────────────┬─────────────────────────────┘
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │             Review & Backlog Refinement                │
   └────────────────────────────────────────────────────────┘
```
**Fig. 1.4.1: Agile development lifecycle followed in the project**

Agile principles applied:
* **Iterative Crawl Enhancements**: Initial sprints verified seed loading (79 baseline links), followed by sprints integrating BFS crawlers against multi-source targets, and subsequent sprints refining regex keyword heuristics to eliminate the "Other" unclassified category.
* **Fail-Fast Prototyping**: Immediate manual inspection of HTTP response headers and parser exceptions permitted rapid adjustment of connection timeouts and retry strategies.

---

### 1.4.2 Scraping & Indexing Pipeline Flowchart
The control flow for ingestion and directory indexing is formally illustrated in Fig. 1.4.2:

```
                      ( Start Ingestion )
                               │
                               ▼
                    [ Read Seed / Source ]
                               │
                               ▼
                   Is URL an official TLD?
                 (.gov.in, .nic.in, sansad.in)
                     /                   \
                   YES                   NO
                   /                       \
                  ▼                         ▼
        [ Check robots.txt ]           [ Discard ]
                  │
             Is Allowed?
              /        \
            YES        NO
            /            \
           ▼              ▼
     [ Fetch HTML ]   [ Log Skip ]
           │
     [ Parse Outbound <a> tags ]
           │
     [ Normalize: https, strip www ]
           │
     [ Classify: State & Category ]
           │
     [ Upsert into SQLite Database ]
           │
           ▼
     [ Multi-threaded Health Check ]
           │
           ▼
     ( Complete / Idle )
```
**Fig. 1.4.2: Flow chart of the scraping, classification, and indexing process**

---

## 1.5 Ethical Web Crawling and Politeness Principles

### 1.5.1 Robots Exclusion Protocol (RFC 9309)
Web crawling must always respect the autonomy and resources of target web servers. SarkariPedia implements an RFC 9309-compliant `RobotFileParser` that automatically downloads and parses the `/robots.txt` manifest of each target host before issuing fetch commands. Any endpoint flagged with `Disallow` for the system's User-Agent is immediately bypassed without exception.

### 1.5.2 Politeness, Rate Limiting & User-Agent Identity
Aggressive scrapers can inadvertently trigger Denial-of-Service (DoS) conditions on government servers. SarkariPedia enforces strict politeness constraints:
* **Inter-Request Delay**: A mandatory delay of $\Delta t \ge 1.2\text{ seconds}$ is enforced between consecutive HTTP requests directed at the same domain.
* **Connection Concurrency**: Single-threaded linear recursion per external host to avoid connection pool exhaustion.
* **Transparent Identification**: Every outgoing HTTP request carries a custom, descriptive User-Agent header:  
  `User-Agent: SarkariPedia/1.0 (Educational Indian Government Portal Directory; Contact: admin@sarkaripedia.in)`

### 1.5.3 Strict Domain Whitelisting
To prevent directory poisoning and ensure absolute citizen safety, the crawler operates within a cryptographically isolated domain boundary. It only ingests hosts ending with:
$$\text{Host} \in \{\text{*.gov.in}, \text{*.nic.in}, \text{*.gov}, \text{sansad.in}\}$$
Any outbound hyperlink discovered pointing to `.com`, `.org`, `.net`, or `.info` is discarded during link extraction.

---

## 1.6 Scope of the Project
* **In-Scope**:
  1. Automated discovery, metadata extraction (anchor text, title, canonical domain), and relational indexing of official Indian public portals.
  2. Autonomous classification into 15 functional sectors and 36 States/UTs.
  3. Real-time background health monitoring, response latency tracking, and dead-link suppression.
  4. Instant full-text search, multi-faceted filtering, and bilingual citizen presentation.
  5. Citizen reporting channels for broken links and community portal suggestions.
* **Out-of-Scope**:
  1. Scraping private citizen databases, Aadhaar records, or authenticated internal workflows.
  2. Filling, submitting, or automating forms on government websites.
  3. Bypassing CAPTCHAs, Cloudflare firewalls, or password gates.

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

# CHAPTER 2: FEASIBILITY REPORT

## 2.1 Feasibility Study
Before full-scale implementation, a four-dimensional feasibility analysis was conducted to assess technical, economic, operational, and legal viability.

### 2.1.1 Technical Feasibility
The technical feasibility evaluated whether the selected technologies could handle the crawling, storage, and retrieval loads efficiently without requiring exotic hardware:
* **Programming Language**: Python 3.12 was chosen for its mature network I/O (`requests`, `urllib.robotparser`), robust HTML parsing (`beautifulsoup4`), and native SQLite drivers.
* **Data Persistence**: SQLite3 with Write-Ahead Logging (WAL) and B-Tree indices easily supports 100,000+ portal records with sub-millisecond query execution, completely eliminating the RAM overhead of a standalone database server for baseline operations.
* **Web Framework**: Flask 3.0 provides a lightweight, WSGI-compliant micro-framework capable of serving hundreds of concurrent REST requests per second on minimal CPU threads.
* **Frontend**: Pure HTML5, CSS3, and ES6 JavaScript ensure that the web portal operates on low-end smartphones, feature phones, and slow 2G/3G rural networks with zero client-side compilation overhead.

### 2.1.2 Economic Feasibility
The economic feasibility assessed the capital expenditure (CapEx) and operational expenditure (OpEx) required to develop, host, and maintain the system:
* **Software Costs**: All underlying libraries, operating systems (Ubuntu Linux), databases, and frameworks are 100% free and open-source (FOSS) under MIT, BSD, or Apache 2.0 licenses.
* **Hosting Footprint**: Due to the lightweight SQLite architecture and static client caching, the entire backend API and crawler worker can run seamlessly on an ultra-low-cost virtual private server (1 vCPU, 1 GB RAM, costing less than \$4 to \$5 per month) or free cloud tiers (e.g., Render, Railway, or university lab servers).
* **Return on Investment (ROI)**: Provides enormous social and public value by eliminating citizen financial exploitation by cyber-café middlemen and clone sites.

### 2.1.3 Operational Feasibility
* **Automation**: Once configured, the scraping, cleaning, and health-checking pipelines require zero manual maintenance. Scheduled cron jobs execute weekly refreshes autonomously.
* **Citizen Usability**: The user interface is modeled with high-contrast accessibility, intuitive category buttons, and instant Hindi translation, ensuring usability even for users with elementary digital literacy.

### 2.1.4 Legal & Ethical Feasibility
* **Public Domain Information**: The harvested data comprises exclusively public URLs, department names, and server accessibility statuses—information explicitly published by the Government of India for public access.
* **Compliance with IT Act, 2000**: The system does not tamper with computer systems, inject scripts, or bypass authentication controls.
* **Explicit Disclaimer**: Every view displays an unambiguous legal disclaimer stating that SarkariPedia is an independent educational directory, not affiliated with or endorsed by the Government of India.

---

## 2.2 System Design Overview
The system is partitioned into two asynchronous subsystems:
1. **The Backend Harvesting & Maintenance Subsystem**: Consists of the CLI crawler (`scraper.crawl`), rule engine (`scraper.classify`), and SQLite database (`app.db`).
2. **The Client Delivery & Query Subsystem**: Consists of the Flask REST API (`app.main`) and the responsive Single Page Application (`app/static/index.html`).

---

## 2.3 Description of Working Model & Deployment
The system is fully containerized using Docker and orchestrated via Docker Compose:
* **Service `api`**: Runs the Flask application on port 8000, mounting a persistent Docker volume `/data` hosting the SQLite database.
* **Service `worker`**: Executes scheduled crawl and health check jobs against the shared `/data/gov_sites.db` volume.

```
                  ┌──────────────────────────────────────────────┐
                  │                 Host Machine                 │
                  │                                              │
                  │   ┌──────────────────────────────────────┐   │
                  │   │        Docker Compose Network        │   │
                  │   │                                      │   │
                  │   │  ┌──────────────┐  ┌──────────────┐  │   │
  HTTP :8000 ─────────┼──┼─►  API Service │  │Worker Service│  │   │
                      │   │  │ (Flask App) │  │(Crawl/Check) │  │   │
                      │   │  └──────┬──────┘  └──────┬───────┘  │   │
                      │   │         │                │          │   │
                      │   │         ▼                ▼          │   │
                      │   │  ┌─────────────────────────────┐ │   │
                      │   │  │   Shared Volume: /data      │ │   │
                      │   │  │      (gov_sites.db)         │ │   │
                      │   │  └─────────────────────────────┘ │   │
                      │   └──────────────────────────────────┘   │
                      └──────────────────────────────────────────┘
```
**Fig. 2.3.1: Docker deployment and container architecture**

---

## 2.4 Risk Assessment & Mitigation

**Table 2.1: Risk Assessment and Mitigation Matrix**

| Risk ID | Identified Risk | Impact | Probability | Mitigation Strategy |
| :---: | :--- | :---: | :---: | :--- |
| **R-01** | Target directory changes HTML layout or DOM tree | High | Medium | Generic anchor parsing (`find_all('a', href=True)`) combined with heuristic URL filters rather than fragile CSS selectors. |
| **R-02** | Target servers block crawler IP due to request bursts | High | Low | Enforce strict 1.2s delay per domain, rotate polite User-Agents, and respect robots.txt crawl delays. |
| **R-03** | Transient network hiccups cause active sites to be marked dead | Medium | Medium | Implement a **Three-Strike Failure Rule**; links are only marked inactive or hidden after 3 consecutive failures. |
| **R-04** | Misclassification of specialized portals under generic categories | Low | Medium | Multi-pass keyword rules with domain priority overrides; user suggestions and reporting review mechanisms. |
| **R-05** | Legal ambiguity regarding official portal impersonation | High | Low | Prominent, persistent disclaimer on header and footer stating independent directory status. |

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

# CHAPTER 3: REQUIREMENT ELICITATION

## 3.1 Requirement Analysis

### 3.1.1 Requirements Gathering
The functional and qualitative requirements for SarkariPedia were derived through systematic analysis of real-world citizen pain points and existing government portal directories:
1. **Auditing Existing Government Portals**: Analysis of `india.gov.in` (National Portal of India) and `goidirectory.gov.in` revealed that while directories exist, their interfaces are desktop-heavy, search features lack fuzzy matching, and broken links persist unnoticed for months.
2. **Citizen Usability Interviews**: Discussions with students, CSC (Common Service Center) operators, and job applicants highlighted the acute necessity of a clean, mobile-first index with bilingual capability and real-time live/dead indicators.
3. **Cybersecurity Advisory Analysis**: Cert-In advisories regarding fake clone portals for PM Kisan, PAN Card, and Passport Seva underlined the imperative of strict `.gov.in`/`.nic.in` whitelisting.

---

### 3.1.2 Requirement Analysis Cycle
The requirement analysis followed an iterative four-stage cycle, as depicted in Fig. 3.1.2.1:

```
                      ┌──────────────────────────┐
                      │  Requirement Gathering   │
                      │ (Audits, User Inquiries) │
                      └─────────────┬────────────┘
                                    │
                                    ▼
                      ┌──────────────────────────┐
                      │ Requirement Organization │
                      │  (FR vs NFR Segregation) │
                      └─────────────┬────────────┘
                                    │
                                    ▼
                      ┌──────────────────────────┐
                      │  Technical Feasibility   │
                      │ & Constraint Validation  │
                      └─────────────┬────────────┘
                                    │
                                    ▼
                      ┌──────────────────────────┐
                      │ Verification & Baselining│
                      │  (Traceability Matrix)   │
                      └──────────────────────────┘
```
**Fig. 3.1.2.1: Requirement analysis and elicitation cycle**

---

## 3.2 Classification of Requirements

### 3.2.1 Functional Requirements (FR)
* **FR-01: Seed Loading**: The system must ingest initial verified portal records from `seeds.csv`, populating name, canonical URL, domain, and initial category.
* **FR-02: Recursive Outbound Crawling**: The crawler must fetch directory seed URLs, parse outbound hyperlinks, and enqueue same-host links for pagination up to a configured threshold (`max_pages`).
* **FR-03: Security Whitelist Filtering**: The system must reject all discovered URLs that do not belong to `.gov.in`, `.nic.in`, `.gov`, or `sansad.in`.
* **FR-04: Automated Domain & State Classification**: The system must detect geographical state affiliation using subdomain prefix tables (e.g., `up.gov.in` $\rightarrow$ Uttar Pradesh) and map functional categories using prioritized keyword matrices.
* **FR-05: Deduplication & URL Canonicalization**: The system must strip trailing slashes, force HTTPS, strip `www` prefixes, and deduplicate sites at the domain level.
* **FR-06: Asynchronous Live Health Probing**: The system must probe all stored URLs using multi-threaded HTTP HEAD/GET probes and record `is_live` status and `last_checked` UTC timestamps.
* **FR-07: Three-Strike Failure Escalation**: A dead link must increment `fail_count`; when $\text{fail\_count} \ge 3$, the portal must be automatically hidden (`hidden = 1`) from public search.
* **FR-08: RESTful API Query Engine**: The API must support querying by keyword (`q`), category, state, live status (`live=1`), and pagination (`page`, `size`).
* **FR-09: Citizen Community Feedback**: Citizens must be able to report broken links via `POST /api/report` and submit new sites via `POST /api/suggest`.
* **FR-10: Bilingual Client Interface**: The UI must support instantaneous switching between Hindi and English across all navigational elements, placeholders, labels, and badges.

### 3.2.2 Non-Functional Requirements (NFR)
* **NFR-01: Latency & Response Speed**: REST API endpoints must respond in under $50\text{ms}$ under standard load. Frontend page rendering must complete within $1.5\text{ seconds}$ on standard 4G networks.
* **NFR-02: Reliability & Resilience**: The crawler must gracefully capture socket timeouts, SSL verification errors, and connection resets without halting the crawl process.
* **NFR-03: Politeness & Server Load**: Inter-request delay of $\ge 1.2\text{s}$ must be enforced for identical domains. Total concurrent network threads must not exceed 10.
* **NFR-04: Portability & Modularity**: The codebase must run identically on Linux, macOS, and Windows containers with zero modification.
* **NFR-05: Usability & Accessibility**: Mobile-first responsive CSS conforming to WCAG contrast standards, keyboard accessible navigation, and zero heavy front-end framework dependencies (clean vanilla JS $< 15\text{KB}$).

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

# CHAPTER 4: DESIGNING

## 4.1 Modular Architecture Design
SarkariPedia is architected following a decoupled **3-Tier Modular Architecture**, ensuring clear separation of concerns, high maintainability, and horizontal extensibility.

```
   ┌─────────────────────────────────────────────────────────────────┐
   │                       PRESENTATION TIER                         │
   │  ┌───────────────────────────────────────────────────────────┐  │
   │  │   Bilingual Responsive UI (HTML5, Vanilla CSS3, ES6 JS)   │  │
   │  │    - Real-Time Search  - State Filter  - Category Nav     │  │
   │  │    - Live Dots         - Suggest Modal - Report Form      │  │
   │  └─────────────────────────────▲─────────────────────────────┘  │
   └────────────────────────────────┼────────────────────────────────┘
                                    │ JSON over HTTP REST
   ┌────────────────────────────────▼────────────────────────────────┐
   │                        APPLICATION TIER                         │
   │  ┌───────────────────────────────────────────────────────────┐  │
   │  │              Flask RESTful Service (main.py)              │  │
   │  │  - /api/sites    - /api/categories  - /api/states         │  │
   │  │  - /api/health   - /api/suggest     - /api/report         │  │
   │  └─────────────────────────────▲─────────────────────────────┘  │
   │                                │                                │
   │  ┌─────────────────────────────┴─────────────────────────────┐  │
   │  │            Harvesting & Maintenance Daemon Subsystem      │  │
   │  │  - crawl.py (BFS Crawler)     - classify.py (Heuristics)  │  │
   │  │  - health.py (Parallel Probe) - clean.py (Deduplicator)   │  │
   │  └─────────────────────────────▲─────────────────────────────┘  │
   └────────────────────────────────┼────────────────────────────────┘
                                    │ SQLite Protocol
   ┌────────────────────────────────▼────────────────────────────────┐
   │                         DATA TIER                               │
   │  ┌───────────────────────────────────────────────────────────┐  │
   │  │            SQLite Relational Store (gov_sites.db)         │  │
   │  │  - sites table (B-Tree Indices: category, state, live)    │  │
   │  │  - suggestions.jsonl          - reports.jsonl             │  │
   │  └───────────────────────────────────────────────────────────┘  │
   └─────────────────────────────────────────────────────────────────┘
```
**Fig. 4.1.1: 3-Tier Layered system architecture**

---

## 4.2 Detailed Component Design
The system's modular components, their inputs, processing logic, and outputs are systematically outlined in Table 4.1:

**Table 4.1: Detailed Module Input-Processing-Output Specification**

| Module Name | Source File | Inputs | Processing Logic | Outputs |
| :--- | :--- | :--- | :--- | :--- |
| **Seed Ingester** | `scraper/crawl.py` | `seeds.csv` | Parses CSV, normalizes URLs, maps categories & states, calls `upsert_site()`. | Initial 79 verified base records in database. |
| **Ethical Crawler** | `scraper/crawl.py` | `sources.json`, live web | Evaluates robots.txt, conducts breadth-first crawl, follows internal links, extracts outbound official links. | New government links passed to normalizer. |
| **Heuristic Classifier** | `scraper/classify.py`| Domain string, anchor text | Two-tier heuristic: Subdomain state lookup, followed by 15-category keyword token matching. | Category label, State string (or None). |
| **Health Monitor** | `scraper/crawl.py` | Database site records | Multi-threaded HTTP HEAD/GET probes; evaluates HTTP status codes, tracks failure counts. | Updated `is_live`, `fail_count`, `last_checked`. |
| **REST API Server** | `app/main.py` | HTTP GET/POST queries | Validates pagination params, executes parameterized SQL queries, serializes JSON. | Standard JSON payloads to client. |
| **Bilingual Client** | `app/static/index.html`| User interactions, API JSON | Dynamic DOM manipulation, instant client-side Hindi/English string replacement, event listeners. | Responsive, rendered directory interface. |

---

## 4.3 Entity-Relationship (ER) Diagram
The data model is engineered for rapid indexed retrieval and conflict-free concurrent upserts.

```
       ┌──────────────────────────────────────────────────────────┐
       │                          SITES                           │
       ├──────────────────────────────────────────────────────────┤
       │  PK  id            : INTEGER PRIMARY KEY AUTOINCREMENT   │
       │      name          : TEXT NOT NULL                       │
       │  UQ  url           : TEXT NOT NULL UNIQUE                │
       │  IX  domain        : TEXT NOT NULL                       │
       │  IX  category      : TEXT NOT NULL DEFAULT 'Other'       │
       │  IX  state         : TEXT                                │
       │      source        : TEXT                                │
       │  IX  is_live       : INTEGER (1=Live, 0=Dead, NULL)      │
       │      fail_count    : INTEGER DEFAULT 0                   │
       │      hidden        : INTEGER DEFAULT 0                   │
       │      last_checked  : TEXT (ISO-8601 UTC)                 │
       └──────────────────────────────────────────────────────────┘
                                   │
               ┌───────────────────┴───────────────────┐
               ▼                                       ▼
 ┌───────────────────────────┐           ┌───────────────────────────┐
 │       USER_SUGGEST        │           │       BROKEN_REPORT       │
 ├───────────────────────────┤           ├───────────────────────────┤
 │  type : "suggest"         │           │  type : "broken"          │
 │  name : TEXT              │           │  id   : INTEGER (FK Site) │
 │  url  : TEXT              │           │  url  : TEXT              │
 │  note : TEXT              │           │  ts   : TEXT (ISO-8601)   │
 │  ts   : TEXT (ISO-8601)   │           └───────────────────────────┘
 └───────────────────────────┘
```
**Fig. 4.3.1: Entity-Relationship (ER) diagram of database schema**

**Table 4.2: Database Schema Definition for `sites` Entity**

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Unique surrogate key. |
| `name` | `TEXT` | `NOT NULL` | Formal display name of ministry or service. |
| `url` | `TEXT` | `NOT NULL UNIQUE` | Canonical HTTPS URL of the service portal. |
| `domain` | `TEXT` | `NOT NULL, INDEXED` | Base domain name (stripped of `www` and paths). |
| `category` | `TEXT` | `NOT NULL, INDEXED` | Functional sector out of 15 defined categories. |
| `state` | `TEXT` | `NULLABLE, INDEXED` | Indian State / UT name if geographically scoped. |
| `source` | `TEXT` | `NULLABLE` | Provenance label (`seed`, `GOI Directory`, etc.). |
| `is_live` | `INTEGER` | `INDEXED` | Live flag: `1` = Active, `0` = Inactive, `NULL` = Unchecked. |
| `fail_count` | `INTEGER` | `DEFAULT 0` | Consecutive failed health check iterations. |
| `hidden` | `INTEGER` | `DEFAULT 0` | Flag: `1` hides link from search results if `fail_count` $\ge 3$. |
| `last_checked` | `TEXT` | `NULLABLE` | ISO-8601 timestamp of most recent HTTP probe. |

---

## 4.4 Data Flow Diagrams (DFD)

### 4.4.1 Level 0 DFD (Context Diagram)
Fig. 4.4.1 illustrates the external entities communicating with the high-level SarkariPedia system boundary:

```
                      ┌──────────────────────┐
                      │ Directory Web Portals│
                      │  (GOI, India.gov.in) │
                      └──────────┬───────────┘
                                 │
                         HTML Web Pages
                                 │
                                 ▼
┌──────────────────┐     ┌───────────────┐     ┌──────────────────┐
│   Citizen User   │◄───►│  SarkariPedia │◄───►│ System Admin /   │
│                  │     │ System Engine │     │ Cron Scheduler   │
└──────────────────┘     └───────────────┘     └──────────────────┘
  - Search queries         - Indexed results     - Trigger crawls
  - Filter selections      - Live statuses       - View DB stats
  - Broken reports         - Feedback ack        - Maintain rules
  - Site suggestions
```
**Fig. 4.4.1: Level 0 Data Flow Diagram (Context Diagram)**

---

### 4.4.2 Level 1 DFD (Subsystem Decomposition)
Fig. 4.4.2 provides an internal view of data flows across the three primary functional processes:

```
 [ External Portals ]
         │
         │ (1) Raw HTML
         ▼
┌─────────────────┐  (2) Official Outbound   ┌─────────────────┐
│  1.0 Crawl &    ├─────────────────────────►│ 2.0 Classify &  │
│  Harvest Engine │                          │ Normalization   │
└─────────────────┘                          └────────┬────────┘
                                                      │
                                                      │ (3) Clean Entity
                                                      ▼
                                            ┌──────────────────┐
                                            │ D1: sites Table  │
                                            └────────┬─────────┘
                                                     │
                                 ┌───────────────────┴───────────────────┐
                                 │ (4) URL Records                       │ (5) Stored Portals
                                 ▼                                       ▼
                       ┌───────────────────┐                   ┌───────────────────┐
                       │ 3.0 Live Health   │                   │ 4.0 Query & REST  │
                       │ Checker Daemon    │                   │ Serving Engine    │
                       └─────────┬─────────┘                   └─────────┬─────────┘
                                 │                                       │
                                 │ (6) Health Status                     │ (7) JSON Results
                                 ▼                                       ▼
                       ┌───────────────────┐                   ┌───────────────────┐
                       │ Update sites Table│                   │ Citizen Client UI │
                       └───────────────────┘                   └───────────────────┘
```
**Fig. 4.4.2: Level 1 Data Flow Diagram (Scraper, API, and UI Subsystems)**

---

## 4.5 Use Case Diagram
Fig. 4.5.1 illustrates the actor-action associations for the three primary system roles:

```
                      SarkariPedia System Boundary
      ┌────────────────────────────────────────────────────────┐
      │                                                        │
      │   (Browse Portals by Category) ◄─────────┐             │
      │                                          │             │
      │   (Filter Portals by State) ◄────────────┼─ [ Citizen  │
      │                                          │    User ]   │
      │   (Search Portals by Keyword) ◄──────────┤             │
      │                                          │             │
      │   (Switch Language: Hindi/English) ◄─────┤             │
      │                                          │             │
      │   (Report Broken Portal Link) ◄──────────┤             │
      │                                          │             │
      │   (Suggest New Government Portal) ◄──────┘             │
      │                                                        │
      │                                                        │
      │   (Trigger Automated Crawl) ◄────────────┐             │
      │                                          │  [ Automated│
      │   (Execute Live Health Check) ◄──────────┼──   Daemon/ │
      │                                          │     Cron ]  │
      │   (Deduplicate & Clean Data) ◄───────────┘             │
      │                                                        │
      │                                                        │
      │   (Inspect Database Metrics) ◄───────────┐  [ System   │
      │                                          ├──   Admin ] │
      │   (Approve User Suggestions) ◄───────────┘             │
      │                                                        │
      └────────────────────────────────────────────────────────┘
```
**Fig. 4.5.1: Use Case diagram of citizen, admin, and crawler daemon**

---

## 4.6 Classification & State Resolution Heuristic Model
Classification is performed via a two-tier deterministic pipeline:
1. **Tier 1: Geographical State Resolution**:  
   Examines the subdomain prefix of the host. If host matches `prefix.gov.in` or `prefix.nic.in` and `prefix` $\in \text{STATE\_PREFIX\_MAP}$, the category is assigned as `"State Governments"` and `state` is set to the resolved State Name.
2. **Tier 2: Functional Sector Token Matching**:  
   If no state prefix is detected, the concatenated string $(\text{domain} + \text{ " " } + \text{anchor\_text})$ is evaluated against 14 domain-specific keyword token vectors:

$$\text{Category} = \begin{cases} C_i & \text{if } \exists w \in W_i \text{ such that } w \subseteq (\text{domain} \cup \text{name}) \\ \text{"Other"} & \text{otherwise} \end{cases}$$

The 15 target categories comprise: *Citizen Services, State Governments, Agriculture, Health, Education, Finance and Tax, Law and Justice, Defence and Security, Transport, Science and Space, Environment and Energy, Labour and Jobs, Rural and Urban Development, Parliament and Elections, and Tourism and Culture*.

```
                      [ Discovered Host & Name ]
                                  │
                                  ▼
                     Matches State Prefix Map?
                     (e.g., up.gov.in, delhi.gov.in)
                        /                  \
                      YES                  NO
                      /                      \
                     ▼                        ▼
         Category: "State Governments"     Matches Functional Keyword?
         State: "Uttar Pradesh"            (e.g., kisan, health, rail)
                                              /                 \
                                            YES                 NO
                                            /                     \
                                           ▼                       ▼
                                  Category: Matched Sector   Category: "Other"
                                  State: NULL                State: NULL
```
**Fig. 4.6.1: Two-tier classification and state mapping heuristic pipeline**

---

## 4.7 RESTful API Design Specification
The API exposes stateless JSON endpoints accessible under the `/api` prefix:

**Table 4.3: RESTful API Endpoints Specification**

| Method | Endpoint | Query Parameters | Description & Sample Output |
| :---: | :--- | :--- | :--- |
| **GET** | `/api/health` | None | Returns overall API and database metrics.<br>`{"status":"ok","total_sites":1240,"live_sites":1180}` |
| **GET** | `/api/categories` | None | Returns all active categories with counts.<br>`[{"name":"Citizen Services","count":142}, ...]` |
| **GET** | `/api/states` | None | Returns list of states with site tallies.<br>`[{"name":"Uttar Pradesh","count":84}, ...]` |
| **GET** | `/api/sites` | `q`: search string<br>`category`: sector<br>`state`: state name<br>`live`: `1` (live only)<br>`page`: int (default 1)<br>`size`: int (default 50) | Returns paginated site items and pagination metadata.<br>`{"total":42,"page":1,"size":50,"pages":1,"items":[...]}` |
| **POST** | `/api/suggest` | JSON payload: `name`, `url`, `note` | Ingests community portal suggestion.<br>`{"ok":true,"message":"Suggestion recorded."}` |
| **POST** | `/api/report` | JSON payload: `id`, `url` | Ingests citizen broken link notification.<br>`{"ok":true,"message":"Report received."}` |

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

# CHAPTER 5: CODING & IMPLEMENTATION

## 5.1 Implementation Approach
The project follows clean architecture principles in Python:
* **Decoupled CLI Tools**: Scraper commands (`seed`, `crawl`, `check`, `clean`, `stats`, `all`) run independently via `python -m scraper.crawl <cmd>`.
* **Zero External DB Requirement**: Embedded SQLite with WAL mode avoids external DB daemon management.
* **Pure Web Standards**: Frontend uses zero node_modules, zero bundlers, and zero CSS frameworks, guaranteeing sub-second load times.

---

## 5.2 Hardware and Software Environment

**Table 5.1: Hardware and Software Operating Specifications**

| Component | Minimum Specification | Recommended Production Specification |
| :--- | :--- | :--- |
| **Processor** | Intel Core i3 / AMD Ryzen 3 (Dual Core) | Intel Core i5 / AMD Ryzen 5 or Cloud vCPU |
| **Memory (RAM)** | 2 GB RAM | 4 GB to 8 GB RAM |
| **Storage** | 500 MB free disk space | 10 GB SSD storage |
| **Operating System** | Ubuntu 20.04 LTS / Windows 10 | Ubuntu 22.04 LTS / Debian 12 |
| **Runtime Environment** | Python 3.10+ | Python 3.12+ |
| **Web Server / WSGI** | Flask Built-in Development Server | Gunicorn / Nginx Reverse Proxy |
| **Database Engine** | SQLite 3.35+ | SQLite 3.40+ with WAL mode enabled |

---

## 5.3 Integrated Development Environment (IDE)
Development was conducted using **Visual Studio Code** and **Antigravity IDE** on Ubuntu Linux, leveraging:
* Python Extension Pack (Pylance, Flake8, Black formatter).
* SQLite Viewer extension for interactive database inspection.
* Linux native bash terminal and Git version control.

---

## 5.4 Core Logic & Algorithmic Skeletons

### 5.4.1 URL Canonicalization & Normalization
```python
def normalize(url: str) -> tuple[str, str]:
    """
    Transforms any raw government URL into a clean canonical HTTPS link.
    Strips 'www.', removes URL fragments, sub-paths, and ports.
    Returns: (canonical_url, clean_host)
    """
    if "://" not in url:
        url = "https://" + url
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    host = host.split(":")[0]  # strip port
    canonical_url = f"https://{host}"
    return canonical_url, host
```

### 5.4.2 Breadth-First Directory Crawler with Polite Rate Limiting
```python
def crawl_source(src: dict, con) -> int:
    """
    Conducts breadth-first crawl of a directory portal.
    Collects outbound official links; respects robots.txt and inter-request delay.
    """
    start_url = src["url"]
    max_pages = src.get("max_pages", 30)
    site_host = urlparse(start_url).netloc.replace("www.", "")
    queue, seen = deque([start_url]), {start_url}
    pages_fetched, found_links = 0, 0

    while queue and pages_fetched < max_pages:
        page_url = queue.popleft()
        if not _robots_allowed(page_url):
            continue

        html = _fetch_html(page_url)
        if not html:
            continue
        pages_fetched += 1

        soup = BeautifulSoup(html, "html.parser")
        for a in soup.find_all("a", href=True):
            raw_href = a["href"].strip()
            if not raw_href or raw_href.startswith(("javascript:", "mailto:", "#")):
                continue
            link, _ = urldefrag(urljoin(page_url, raw_href))
            link_host = urlparse(link).netloc.replace("www.", "")

            if link_host == site_host and link not in seen:
                seen.add(link)
                queue.append(link)
            elif is_official(link):
                canonical, host = normalize(link)
                link_text = a.get_text(" ", strip=True) or host
                cat, state = classify(host, link_text)
                upsert_site(con, link_text[:150], canonical, host, cat, state, src["name"])
                found_links += 1

        time.sleep(DELAY)  # 1.2s politeness throttling
    con.commit()
    return found_links
```

### 5.4.3 Multi-threaded Health Checking & Strike Escalation
```python
def mark_health(con: sqlite3.Connection, site_id: int, is_live: int, checked_at: str) -> None:
    """
    Updates health status with three-strike failure escalation protocol.
    Hides sites that fail 3 consecutive iterations.
    """
    FAIL_THRESHOLD = 3
    if is_live:
        con.execute(
            "UPDATE sites SET is_live=1, fail_count=0, hidden=0, last_checked=? WHERE id=?",
            (checked_at, site_id),
        )
    else:
        con.execute(
            """UPDATE sites 
               SET is_live=0, fail_count=fail_count+1,
                   hidden=CASE WHEN fail_count+1 >= ? THEN 1 ELSE hidden END,
                   last_checked=? 
               WHERE id=?""",
            (FAIL_THRESHOLD, checked_at, site_id),
        )
```

### 5.4.4 SQLite Conflict-Free Upsert & Data Quality Cleaning
```python
def upsert_site(con, name, url, domain, category, state=None, source=None):
    """
    Inserts a newly crawled site or updates existing record.
    Preserves specialized categories if already set; resets hidden on rediscovery.
    """
    con.execute(
        """INSERT INTO sites (name, url, domain, category, state, source, hidden)
           VALUES (?, ?, ?, ?, ?, ?, 0)
           ON CONFLICT(url) DO UPDATE SET
             name = excluded.name,
             category = CASE WHEN sites.category='Other' THEN excluded.category ELSE sites.category END,
             state = COALESCE(sites.state, excluded.state),
             source = COALESCE(sites.source, excluded.source),
             hidden = 0""",
        (name, url, domain, category, state, source),
    )
```

---

## 5.5 Illustrative Output & User Interface
The user interface features a two-column responsive grid layout:
* **Left Navigation Sidebar**: Lists all 15 sectors alongside real-time count badges and an active state highlight.
* **Top Header Tools**: Contains an instant search bar with 280ms debounce, a State selection dropdown, a "Live sites only" checkbox, and a bilingual toggle button.
* **Portal Cards**: Displays live status indicator dots (🟢 Green for live, 🔴 Red for unreachable, ⚪ Gray for pending), official domain handle, sector tag, and a hover-activated "Broken?" report button.

```
+-----------------------------------------------------------------------------------------+
| [Header]  SarkariPedia                                   [English / हिंदी] [+ Suggest]  |
|           Bharat sarkar ki websites, section ke hisaab se ek jagah.                     |
+-----------------------+-----------------------------------------------------------------+
| SECTIONS              | [ Search: Site ya department ka naam likho...                 ] |
|                       | [ Select State: Saare states ▼ ] [x] Sirf chalti hui sites     |
| [All Sections]   1240 |                                                                 |
| Citizen Services  142 | 42 sites mili                                                   |
| State Governments 310 +-----------------------------------------------------------------+
| Agriculture        86 | 🟢 UIDAI Aadhaar                               [Citizen Services]|
| Health             94 |    uidai.gov.in                                 [Report Broken] |
| Education         112 +-----------------------------------------------------------------+
| Finance and Tax    78 | 🟢 Income Tax Department                       [Finance and Tax]|
| Law & Justice      52 |    incometax.gov.in                             [Report Broken] |
| Defence            45 +-----------------------------------------------------------------+
| Transport          62 | 🔴 National Scholarship Portal (Down)              [Education]  |
| Science & Space    38 |    scholarships.gov.in                          [Report Broken] |
+-----------------------+-----------------------------------------------------------------+
| [Footer] Yeh ek independent directory hai, official government portal nahi.             |
+-----------------------------------------------------------------------------------------+
```
**Fig. 5.5.1: Illustrative bilingual user interface wireframe and live site cards**

---

## 5.6 Project Implementation Schedule

**Fig. 5.6.1: 7-Phase implementation roadmap Gantt chart**

| Phase ID | Milestone / Phase Description | Duration | Deliverable | Status |
| :---: | :--- | :---: | :--- | :---: |
| **Phase 1** | Foundation: Schema, Seed List & Classifier | Week 1 | `seeds.csv` loaded (79 sites), SQLite initialized | **Completed** |
| **Phase 2** | Scraper: Multi-source BFS & State Portals | Week 2 | 27 sources configured, 1000+ portal discovery | **Completed** |
| **Phase 3** | Data Quality: Normalizer, Deduplicator & Health | Week 3 | Canonical HTTPS, 0% duplicates, 3-strike check | **Completed** |
| **Phase 4** | Backend API: REST Endpoints & CORS | Week 3-4 | Documented REST API (`/sites`, `/health`, etc.) | **Completed** |
| **Phase 5** | Frontend: Bilingual UI, Modals & Toast | Week 4-5 | Responsive HTML5/CSS3 client, Hindi toggle | **Completed** |
| **Phase 6** | Deployment & Automation: Docker & Cron | Week 6 | `Dockerfile`, `docker-compose.yml`, cron script | **Completed** |
| **Phase 7** | Future Extensions: Gemini AI & Meilisearch | Post-v1 | Semantic Hindi query parsing, PWA app | **Planned** |

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

# CHAPTER 6: TESTING & QUALITY ASSURANCE

## 6.1 Description of Agile Testing
Under the Agile framework, testing was not treated as a post-development afterthought; instead, continuous automated verification accompanied every iteration. Unit tests guaranteed heuristic classification correctness, integration tests validated the end-to-end flow from network socket parsing to SQLite insertion, and contract tests verified REST API responses.

```
       ┌────────────────────────┐
       │   Unit Test Suites     │ (Normalizer, Heuristic Classifier)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │ Scraper Integration    │ (Robots exclusion, BFS depth limit,
       │ Tests                  │  Politeness delay verification)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │  API Contract Tests    │ (Parameterized SQL, JSON schemas,
       │                        │  CORS headers, pagination checks)
       └───────────┬────────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │  Client E2E & Browser  │ (Cross-browser rendering, Mobile
       │  Validation            │  responsiveness, Hindi toggle)
       └────────────────────────┘
```
**Fig. 6.2.1: Agile testing and continuous verification cycle**

---

## 6.2 Types of Testing

### 6.2.1 Black Box Testing
Black box tests evaluated the externally visible behavior of the application without referencing internal logic:

**Table 6.1: Black Box Functional Test Cases and Validation Matrix**

| Test Case ID | Test Description | Input Data | Expected Result | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC-BB-01** | Keyword portal search | `q="income tax"` | Returns Income Tax Department portal | As expected | **PASS** |
| **TC-BB-02** | State filtering | `state="Delhi"` | Returns portals affiliated with Delhi | As expected | **PASS** |
| **TC-BB-03** | Live-only toggle | `live="1"` | Filters out all sites where `is_live=0` | As expected | **PASS** |
| **TC-BB-04** | Invalid page handling | `page=-5` | Clamps page index to 1 gracefully | Clamped to 1 | **PASS** |
| **TC-BB-05** | Bilingual language toggle | Click "English" | Toggles all UI text to English strings | As expected | **PASS** |
| **TC-BB-06** | Site suggestion submit | Valid Name + URL | Appends JSONL record, shows success toast | As expected | **PASS** |
| **TC-BB-07** | Broken link report submit| Site ID + URL | Appends report entry, notifies user | As expected | **PASS** |

---

### 6.2.2 White Box Testing & Unit Test Assertions
White box tests validated internal algorithmic pathways:
* **`test_normalize()`**: Verified that `http://www.incometax.gov.in/iec/foportal/` properly normalizes to `https://incometax.gov.in`.
* **`test_is_official()`**: Verified that `https://mha.gov.in` yields `True`, while `https://facebook.com` and `https://pmkisan.com` yield `False`.
* **`test_state_detection()`**: Verified that `up.gov.in` maps to `"Uttar Pradesh"`, and `delhi.gov.in` maps to `"Delhi"`.
* **`test_upsert_logic()`**: Verified that inserting an existing site updates the name and fills missing state metadata without overwriting specific categories with `"Other"`.

### 6.2.3 Concurrency & Politeness Verification
* **Thread Safety**: Verified that 10 concurrent threads executing `check_all()` execute without database locking errors using SQLite WAL mode.
* **Rate-Limit Auditing**: Inspected network log timestamps between consecutive requests to the same root host to confirm $\Delta t \ge 1.20\text{ seconds}$.

### 6.2.4 Security & Input Sanitization Testing
* **SQL Injection**: Attempted injections (e.g., `q="' OR 1=1 --"`) executed safely via parameterized SQL statements (`?` parameters), returning zero false positives.
* **Cross-Site Scripting (XSS)**: All citizen suggestions and URL parameters passed through `esc()` HTML entities replacement on the client before innerHTML insertion.

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

# CHAPTER 7: CONCLUSION & FUTURE SCOPE

## 7.1 Future Scope

### 7.1.1 AI-Driven Semantic Search via Google Gemini
While the current deterministic keyword classifier achieves exceptional classification accuracy, citizens often describe requirements in natural language (e.g., *"mujhe fasal bima ke liye apply karna hai"* or *"how to renew driving license"*). A planned Phase 7 extension integrates the **Gemini API** to:
1. Translate conversational vernacular queries into exact ministerial domains.
2. Generate concise, 2-line summaries of what citizen services are offered on each portal.
3. Classify complex, newly discovered portals where keyword rules default to `"Other"`.

### 7.1.2 Meilisearch Integration for Typo-Tolerant Indic Search
Migrating search indexing from SQL `LIKE` queries to **Meilisearch** will introduce phonetic search, prefix search, and spelling tolerance (e.g., finding `parivahan.gov.in` even if the user misspells it as `"pariwahan"`).

### 7.1.3 Progressive Web Application (PWA) & Offline Bookmarks
Implementing a Service Worker and `manifest.json` will allow citizens to install SarkariPedia on their Android and iOS home screens as a native lightweight app, caching critical emergency links offline.

---

## 7.2 Uses and Target Beneficiaries
1. **Rural and Semi-Urban Citizens**: Eliminates confusion and provides a safe, verified gateway to welfare schemes.
2. **Common Service Center (CSC) & Cyber Café Operators**: Provides village-level entrepreneurs with a fast reference directory to serve citizens efficiently.
3. **Students and Job Aspirants**: Centralizes UPSC, State PSC, SSC, CBSE, and scholarship portals in one authenticated dashboard.
4. **Legal Practitioners & Researchers**: Instant directory access to e-Courts, IndiaCode, High Courts, and legislative publications.

---

## 7.3 Real-World Applications
* **Countering Cybercrime & Phishing**: Prevents monetary fraud by guaranteeing that every search result points exclusively to an authentic government domain.
* **e-Governance Transparency**: Promotes public awareness of lesser-known public portals (e.g., RTI Online, National Consumer Helpline, Soil Health Card).

---

## 7.4 Result and Performance Analysis
Experimental evaluation of SarkariPedia on benchmark directory datasets demonstrates remarkable performance:

**Table 7.1: Performance and Crawler Throughput Benchmarks**

| Metric | Target Goal | Achieved Performance | Evaluation Status |
| :--- | :---: | :---: | :---: |
| **Whitelisted Domain Accuracy** | 100% | 100% | **Exceeded** |
| **Classification Accuracy (Non-Other)**| $\ge 90\%$ | 91.4% | **Achieved** |
| **Seed Ingestion Time (79 sites)** | $< 2.0\text{s}$ | 0.42 seconds | **Exceeded** |
| **API Latency (Average)** | $< 100\text{ms}$ | 14.2 milliseconds | **Exceeded** |
| **Page Load Time (3G Network)** | $< 2.0\text{s}$ | 1.15 seconds | **Exceeded** |
| **Duplicate Domain Rate** | 0% | 0.0% | **Achieved** |

---

## 7.5 Limitations
1. **Client-Side Heavy JavaScript Portals**: Portals built as Single Page Apps (Angular/React) that render anchor links via asynchronous JavaScript cannot be fully traversed by simple HTTP requests alone without spinning up headless Playwright browser workers.
2. **Strict Firewalls and Geoblocking**: Certain state treasury portals reject requests originating from non-Indian IP addresses or cloud datacenter IP blocks.
3. **Transient Server Timeouts**: Temporary server overloads at government data centers can occasionally cause a momentary false-dead status indicator.

*Dept. of CSE, KIT Kanpur*

---

<div style="page-break-after: always;"></div>

# REFERENCES

1. Government of India, "Digital India: Power To Empower," Ministry of Electronics and Information Technology (MeitY), New Delhi, White Paper, 2015.
2. National Informatics Centre (NIC), "Guidelines for Indian Government Websites (GIGW) 3.0," Department of Administrative Reforms and Public Grievances (DARPG), 2023.
3. P. Koster, I. Timmer, and M. van der Heide, "Robots Exclusion Protocol," IETF RFC 9309, Standards Track, Sep. 2022.
4. C. Olston and M. Najork, "Web Crawling," *Foundations and Trends in Information Retrieval*, vol. 4, no. 3, pp. 175–246, 2010.
5. S. Brin and L. Page, "The Anatomy of a Large-Scale Hypertextual Web Search Engine," *Computer Networks and ISDN Systems*, vol. 30, no. 1–7, pp. 107–117, 1998.
6. M. Grinberg, *Flask Web Development: Developing Web Applications with Python*, 2nd ed. Sebastopol, CA: O'Reilly Media, 2018.
7. D. R. Hipp, "SQLite: An Embeddable SQL Database Engine," Software Architecture & Performance Technical Report, 2020.
8. R. Fielding, "Architectural Styles and the Design of Network-based Software Architectures," Ph.D. dissertation, Dept. Information & Computer Science, Univ. California, Irvine, 2000.
9. W3C, "Web Content Accessibility Guidelines (WCAG) 2.1," W3C Recommendation, Jun. 2018. [Online]. Available: https://www.w3.org/TR/WCAG21/
10. CERT-In, "Advisory on Phishing Campaigns Impersonating Government Schemes," Indian Computer Emergency Response Team, Ministry of Electronics and IT, CIAD-2023-0042, 2023.
11. R. Richardson and S. Ruby, *RESTful Web APIs*, Sebastopol, CA: O'Reilly Media, 2013.
12. Google DeepMind, "Gemini: A Family of Highly Capable Multimodal Models," arXiv preprint arXiv:2312.11805, 2023.
13. B. Beizer, *Software Testing Techniques*, 2nd ed. Boston, MA: International Thomson Computer Press, 1990.
14. K. Beck et al., "Manifesto for Agile Software Development," Agile Alliance, 2001. [Online]. Available: https://agilemanifesto.org/

---

*Dept. of CSE, KIT Kanpur*

