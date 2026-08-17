# 🚢 FreightQuote AI

## Agentic AI for Maritime Freight Pricing & Route Optimization

**Infosys Springboard 7.0 --- Batch 1 \| Milestone 4**

FreightQuote AI is an AI-powered maritime freight intelligence platform
that combines freight pricing, route and weather analysis, carrier
evaluation, customs intelligence, document processing, multilingual
support, and Retrieval-Augmented Generation (RAG) in a unified Streamlit
application.

Milestone 4 focuses especially on **reducing hallucinations, improving
grounding, adding explainability, expanding port intelligence,
integrating live weather, improving translation reliability, and making
the complete system easier to demonstrate through Google Colab.**

------------------------------------------------------------------------

## 🎯 Project Objective

Maritime freight decisions often require information from several
independent sources: freight quotations, routes, ports, carriers,
customs regulations, weather conditions, shipping documents, and
operational guidelines.

FreightQuote AI brings these areas together into an intelligent platform
that can:

-   assist with maritime freight pricing and quotation analysis;
-   compare routes, ports, congestion, delay, weather and cost factors;
-   evaluate carrier performance and risk;
-   retrieve answers from a maritime knowledge base;
-   reduce LLM hallucinations through evidence-grounded RAG;
-   explain pricing and prediction results;
-   process freight/shipping documents;
-   support multilingual maritime information;
-   expose system and knowledge-base health information.

------------------------------------------------------------------------

## ⭐ Milestone 4 Highlights

Milestone 4 introduces or strengthens:

-   **Hybrid FAISS + BM25 retrieval**
-   **RAG grounding and hallucination reduction**
-   **Evidence/source panel**
-   **Grounding confidence badges**
-   **Expanded centralized port registry**
-   **Live Open-Meteo weather integration**
-   **Route comparison**
-   **Pricing explainability**
-   **Carrier scorecards**
-   **Translation terminology safeguards**
-   **Knowledge Base Manager**
-   **AI System Health and Network Health**
-   **Improved Streamlit UI**
-   **Google Colab-friendly deployment**

------------------------------------------------------------------------

## 🏗️ Architecture

``` text
                       ┌──────────────────────────┐
                       │      Streamlit UI        │
                       │         app.py           │
                       └────────────┬─────────────┘
                                    │
                       ┌────────────▼─────────────┐
                       │       backend.py         │
                       │ RAG • ML • LLM • Weather│
                       │ Translation • Validation │
                       └────────────┬─────────────┘
                                    │
             ┌──────────────────────┼─────────────────────┐
             │                      │                     │
      ┌──────▼──────┐       ┌──────▼──────┐      ┌──────▼──────┐
      │ FAISS + BM25│       │   SQLite    │      │ Live APIs / │
      │ RAG Indexes │       │  Database   │      │ Data Sources│
      └─────────────┘       └─────────────┘      └─────────────┘
```

`config_utils.py` contains shared configuration, database helpers,
authentication utilities, runtime paths, and the centralized port
registry in the simplified Milestone 4 architecture.

------------------------------------------------------------------------

# 🤖 AI Copilot

The AI Copilot provides a conversational interface for maritime freight
information.

Instead of allowing the language model to answer entirely from
pretrained knowledge, the system retrieves relevant information from the
connected knowledge base before producing an answer.

``` text
User Question
     ↓
Query Processing
     ↓
FAISS + BM25 Retrieval
     ↓
Relevant Evidence
     ↓
Grounding Validation
     ↓
LLM Response
     ↓
Answer + Evidence + Confidence
```

The Copilot is intended to handle questions involving ports, shipments,
freight terminology, quotations, carriers, customs information, maritime
documents, and operational knowledge available to the platform.

## Hallucination Reduction

A central Milestone 4 goal is to avoid confident unsupported answers.

The grounding layer can classify evidence approximately as:

-   🟢 **HIGH** --- strong supporting evidence;
-   🟡 **MEDIUM** --- useful but incomplete evidence;
-   🔴 **INSUFFICIENT** --- not enough verified context.

When evidence is insufficient, the intended behavior is to return a
controlled fallback such as:

> I don't have enough verified information in the connected database or
> knowledge base to answer this reliably.

------------------------------------------------------------------------

# 📚 Hybrid RAG: FAISS + BM25

FreightQuote AI uses Retrieval-Augmented Generation to connect the
Copilot with maritime reference documents.

### FAISS --- Dense Semantic Retrieval

FAISS searches document embeddings based on semantic similarity. It can
therefore retrieve a relevant passage even when the user's wording
differs from the document.

### BM25 --- Sparse Lexical Retrieval

BM25 focuses on exact and important terms. This is useful for domain
terminology such as:

-   TEU
-   BAF
-   HS Code
-   Bill of Lading
-   carrier names
-   port names
-   customs terminology

### Hybrid Retrieval

``` text
FAISS semantic score
        +
BM25 lexical score
        ↓
Normalization / weighting
        ↓
Hybrid ranking
        ↓
Best evidence chunks
```

The Milestone 4 design uses an approximate weighting of:

``` text
Hybrid Score = 0.60 × Dense Score + 0.40 × BM25 Score
```

Retrieved evidence can include the source document, page number where
available, chunk ID, retrieval score, and text snippet.

------------------------------------------------------------------------

# 📄 RAG Builder

`FreightQuote_M4_RAG_Builder.ipynb` prepares the knowledge base.

Typical workflow:

1.  Create Colab project and RAG directories.
2.  Add/download maritime reference documents.
3.  Extract PDF/text content.
4.  Split content into chunks.
5.  Attach document metadata.
6.  Generate embeddings.
7.  Build the FAISS vector index.
8.  Build/cache the BM25 index.
9.  Validate retrieval with test queries.
10. Report index/knowledge-base statistics.

The Milestone 4 approach prioritizes real maritime/trade references over
fabricated knowledge wherever available.

------------------------------------------------------------------------

# 💰 Agent 1 --- Freight Pricing & Explainability

The pricing component assists with freight quotation analysis.

Milestone 4 improves explainability so the user can understand why a
quotation is high or low instead of receiving only a final prediction.

Available factors can include:

-   base freight cost;
-   insurance;
-   customs-related fees;
-   fuel surcharge;
-   route conditions;
-   margin;
-   other available quote inputs.

``` text
Shipment Inputs
      ↓
Pricing / ML Logic
      ↓
Predicted Quote
      ↓
Cost Breakdown
      ↓
Explainability Panel
```

The **"Why is this quote expensive?"** view is intended to make pricing
results easier to justify and inspect.

------------------------------------------------------------------------

# 🗺️ Agent 2 --- Route & Weather Intelligence

The route component evaluates maritime routes using available port and
operational information.

Milestone 4 adds route comparison using factors such as:

-   distance;
-   congestion;
-   estimated delay;
-   weather;
-   risk;
-   cost indicators.

## Expanded Port Registry

A centralized port registry acts as a single source of truth for the
application.

The Milestone 4 design expands the platform to approximately **24
supported ports**, including additional Indian and international ports.

Port metadata can include:

-   coordinates;
-   country;
-   region;
-   vessel/network parameters;
-   dwell-time information;
-   congestion level;
-   risk parameters.

------------------------------------------------------------------------

# 🌦️ Live Weather

Weather information is retrieved using the **Open-Meteo API** based on
port coordinates.

Available values can include:

-   temperature;
-   wind speed;
-   weather code/condition;
-   calculated maritime risk;
-   retrieval timestamp.

The interface distinguishes live information from fallback/demo
information using labels such as:

``` text
🟢 LIVE API DATA
⚪ SYNTHETIC / DEMO DATA
```

This prevents demonstration values from being mistaken for real-time
operational information.

------------------------------------------------------------------------

# 🚚 Agent 3 --- Carrier Intelligence

The carrier component provides structured carrier evaluation.

Milestone 4 carrier scorecards can consider:

-   reliability;
-   punctuality;
-   cost efficiency;
-   operational risk;
-   compliance-related indicators.

The goal is not simply to output a carrier name, but also to communicate
the factors supporting the recommendation.

------------------------------------------------------------------------

# 📈 Dynamic Margin Predictor & Yield Optimizer

The broader platform contains margin and profitability analytics.

It can visualize information such as:

-   total quoted freight volume;
-   gross quoted revenue;
-   average freight margin;
-   total/net margin profit;
-   carrier-wise margin behavior;
-   base cost versus final quoted price;
-   freight quote ledger records.

This provides a business-oriented view of the effect of freight pricing
decisions.

------------------------------------------------------------------------

# 🛃 Customs, Tariff & Regulatory Compliance

The customs component supports analysis of regulatory and tariff-related
information.

It can work with:

-   HS codes;
-   cargo categories;
-   origin/destination countries;
-   duty rates;
-   clearance-risk values;
-   required documents;
-   tariff/advisory information.

Charts and tables can be used to compare duty rates and
customs-clearance risks across commodities.

------------------------------------------------------------------------

# 📑 Digital Bill of Lading & OCR

The document intelligence component is designed to process freight
documents such as Bills of Lading.

``` text
Document Upload
      ↓
OCR / Text Extraction
      ↓
Key Field Extraction
      ↓
Structured Metadata
      ↓
Verification / Analysis
```

Extracted fields can include:

-   document ID;
-   shipper;
-   consignee;
-   origin port;
-   destination port;
-   container information;
-   cargo;
-   HS code.

------------------------------------------------------------------------

# 🌐 Multilingual Maritime Translation

The platform includes multilingual maritime/SOP translation, with
NLLB-based translation support in the project design.

Milestone 4 improves reliability through terminology and value
preservation.

Protected/validated items can include:

-   BAF;
-   TEU;
-   HS Code;
-   port codes;
-   numbers;
-   currencies;
-   units.

Longer content can be processed in chunks, and validation checks help
ensure critical operational information is not unintentionally altered.

------------------------------------------------------------------------

# 📘 PDF SOP & Freight Document RAG Studio

The RAG Studio allows maritime documents to become searchable through
natural-language questions.

Suitable knowledge-base content includes:

-   maritime SOPs;
-   freight guidelines;
-   customs policies;
-   tariff references;
-   logistics documentation;
-   port-related documents.

The retrieved document passages are supplied as evidence to the AI
assistant.

------------------------------------------------------------------------

# 🌍 Global Ocean Freight Logistics Digital Twin

The wider FreightQuote AI platform includes a maritime digital-twin
simulation concept.

It allows network conditions and disruptions to be stress-tested
virtually.

Example parameters include:

-   bunker/fuel-price surge;
-   canal delay;
-   labor inflation;
-   foreign-exchange shift;
-   demurrage;
-   carbon tax;
-   freight-volume surge;
-   feeder-rate changes;
-   war-risk insurance;
-   Monte Carlo runs.

Possible outputs include:

-   simulated network volume;
-   average dwell delay;
-   congestion cost;
-   congested-port count;
-   congestion heatmaps;
-   corridor delay/cost analysis.

The emphasis is on connecting network simulation with freight pricing
and AI-assisted maritime decision support.

------------------------------------------------------------------------

# 🧾 AI Evidence Panel

A key Milestone 4 feature is transparency around RAG answers.

The Copilot can expose:

``` text
AI Answer
├── Grounding Confidence
├── Source Document
├── Page / Chunk
├── Retrieval Score
└── Evidence Snippet
```

This makes it easier to inspect the information supporting a generated
response.

------------------------------------------------------------------------

# 🧰 Knowledge Base Manager

The Knowledge Base Manager provides visibility into the RAG subsystem.

Depending on available metadata, it can display:

-   indexed document count;
-   chunk/vector statistics;
-   FAISS/BM25 status;
-   knowledge-base health;
-   rebuild/update controls.

------------------------------------------------------------------------

# 🩺 AI System & Network Health

The dashboard is designed to provide status information for major
components such as:

-   database;
-   vector/RAG index;
-   BM25 index;
-   AI/LLM subsystem;
-   weather integration;
-   knowledge base;
-   network/port conditions.

This is useful both operationally and during project demonstrations.

------------------------------------------------------------------------

# 🔐 Authentication & User Management

The platform includes authentication and user-management functionality,
including support for:

-   signup/login;
-   password handling;
-   JWT-based authentication;
-   user records;
-   administrative/role operations.

Secrets and API credentials should be stored through environment
variables, Colab Secrets, or Streamlit Secrets rather than committed to
the repository.

------------------------------------------------------------------------

# 🗃️ SQLite Database

FreightQuote AI uses SQLite for structured application data.

The architecture contains data areas for items such as:

-   users;
-   carriers;
-   quotes;
-   shipments;
-   merged/training data;
-   ML model information;
-   notifications;
-   chat history.

The exact populated records depend on the database used in the running
project.

------------------------------------------------------------------------

# 🧪 Machine Learning

The system includes ML-oriented functionality for freight-related
prediction/evaluation.

Milestone 4 aims to use stored training/model metrics where available
instead of relying only on hardcoded UI metrics.

The architecture supports pricing, delay/route, and
carrier/compliance-oriented evaluation, with trained model artifacts
stored under the `models/` directory where applicable.

------------------------------------------------------------------------

# 🖥️ Streamlit UI

Streamlit provides the main user interface.

Milestone 4 UI improvements emphasize:

-   consistent navigation;
-   metric cards;
-   analytics and charts;
-   route comparisons;
-   evidence panels;
-   explainability;
-   grounding badges;
-   live-data labels;
-   knowledge-base controls;
-   system-health information.

------------------------------------------------------------------------

# 📁 Simplified Runtime Structure

``` text
freightquote_m4/
│
├── app.py
│   └── Main Streamlit UI
│
├── backend.py
│   └── RAG, AI, ML, weather and translation logic
│
├── config_utils.py
│   └── Configuration, ports, DB and shared utilities
│
├── test_m4_features.py
│   └── Milestone 4 verification tests
│
├── train_ml.py
│   └── ML training/retraining pipeline
│
├── freightquote.db
│
├── faiss_index/
│   ├── index.faiss
│   ├── index.pkl
│   └── bm25_index.pkl
│
├── models/
│   └── Saved model artifacts
│
└── rag_documents/
    └── Maritime knowledge-base documents
```

The exact generated files may vary depending on which notebook cells
have been executed.

------------------------------------------------------------------------

# 📓 Google Colab Setup

Milestone 4 is organized around two notebooks for easier execution and
demonstration.

## 1. `FreightQuote_M4_RAG_Builder.ipynb`

Run this first when building or updating the knowledge base.

``` text
Documents
   ↓
Extraction
   ↓
Chunking
   ↓
Embeddings
   ↓
FAISS + BM25
   ↓
RAG Knowledge Base
```

## 2. `FreightQuote_M4_Streamlit.ipynb`

This prepares the runtime files/dependencies and launches the complete
application.

Main Streamlit command:

``` bash
streamlit run /content/freightquote_m4/app.py   --server.address 0.0.0.0   --server.port 8501   --server.headless true
```

Because Colab runs remotely, a tunnel such as LocalTunnel or ngrok can
expose port `8501` through a public HTTPS link.

------------------------------------------------------------------------

# 🚀 Recommended Demonstration Flow

1.  Open the dashboard and explain system/network health.
2.  Show the expanded port and network information.
3.  Demonstrate pricing and its explainability panel.
4.  Compare two routes and show weather/risk information.
5.  Show carrier scorecards and recommendation factors.
6.  Open AI Copilot and ask a maritime knowledge question.
7.  Show retrieved evidence and grounding confidence.
8.  Ask a question unsupported by the knowledge base to demonstrate
    hallucination control.
9.  Open the Knowledge Base Manager.
10. Demonstrate terminology-safe translation.
11. Explain how the separate RAG Builder produces FAISS + BM25 indexes.

------------------------------------------------------------------------

# 🛠️ Technology Stack

  Technology                           Role
  ------------------------------------ ----------------------------
  Python                               Main language
  Streamlit                            Web application/UI
  SQLite                               Structured data storage
  FAISS                                Dense semantic retrieval
  BM25 / rank_bm25                     Sparse lexical retrieval
  Sentence Transformers / Embeddings   Vector representation
  Qwen-based LLM integration           Generative AI/Copilot
  NLLB                                 Multilingual translation
  Open-Meteo                           Live weather
  Pandas / NumPy                       Data processing
  Scikit-learn                         Machine learning
  Plotly                               Interactive visualizations
  PyMuPDF                              PDF processing
  JWT / bcrypt                         Authentication utilities
  Google Colab                         Notebook execution
  LocalTunnel / ngrok                  Public Streamlit access

------------------------------------------------------------------------

# 🔍 Why Hybrid RAG?

FAISS and BM25 solve different retrieval problems.

``` text
FAISS
"What does the query mean?"
        +
BM25
"Which text contains the important exact terminology?"
        ↓
Hybrid Retrieval
        ↓
Better Evidence
        ↓
More Grounded Answer
```

This combination is particularly useful in maritime logistics because
both semantic meaning and exact terminology matter.

------------------------------------------------------------------------

# 🛡️ Reliability Principles

### Ground before generating

Retrieve relevant information before producing an answer.

### Show evidence

Allow the user to inspect the context supporting the response.

### Refuse unsupported answers

Prefer an insufficient-information response over confident fabrication.

### Distinguish live and demo data

Clearly identify live API information and fallback/demo values.

### Explain predictions

Expose the factors influencing AI/ML outputs wherever possible.

------------------------------------------------------------------------

# ⚠️ Prototype Scope

FreightQuote AI is an academic/internship prototype. AI responses,
predictions, digital-twin simulations, risk values, freight quotations,
translations, and recommendations should not be treated as production
maritime, customs, financial, or safety decisions without validation
against authoritative operational sources.

System behavior also depends on the data, models, documents, indexes,
network connectivity, and APIs available in the current runtime.

------------------------------------------------------------------------

# 🔮 Future Scope

Potential extensions include:

-   real shipping-line and freight-rate APIs;
-   AIS vessel tracking;
-   production port-congestion feeds;
-   larger verified maritime knowledge bases;
-   advanced neural rerankers;
-   stronger citation-level answer verification;
-   cloud vector databases;
-   graph-based maritime knowledge;
-   automated document ingestion;
-   richer digital-twin simulation;
-   continuous ML monitoring;
-   anomaly detection;
-   enterprise role-based access;
-   production cloud deployment.

------------------------------------------------------------------------

# 📌 Conclusion

FreightQuote AI demonstrates how **agentic AI, machine learning, RAG,
live data, document intelligence, and explainability** can be combined
for maritime freight decision support.

The main Milestone 4 improvement is that the language model is no longer
treated as an isolated chatbot. It is surrounded by retrieval, evidence,
grounding, validation, explainability, and controlled fallback
mechanisms.

``` text
Documents + Structured Data + Live Information
                     ↓
             AI / ML Intelligence
                     ↓
          Grounding & Validation
                     ↓
            Explainable Output
                     ↓
       Maritime Decision Support
```

------------------------------------------------------------------------

## 🎓 Project Information

**Internship:** Infosys Springboard 7.0 --- Batch 1\
**Milestone:** 4\
**Domain:** Agentic AI for Maritime Freight Pricing and Route
Optimization
