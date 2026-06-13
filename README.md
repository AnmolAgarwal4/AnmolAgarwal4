<!-- ====================== HEADER ====================== -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,50:7C3AED,100:6D28D9&height=200&section=header&text=Anmol%20Agarwal&fontSize=58&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=AI%20%2F%20ML%20Engineer%20%C2%B7%20Full-Stack%20Developer&descAlignY=58&descSize=18&descAlignX=50" width="100%"/>

<a href="https://github.com/AnmolAgarwal4">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=A78BFA&center=true&vCenter=true&width=620&lines=AI+%2F+ML+Engineer;Computer+Vision+%26+Deep+Learning;Retrieval-Augmented+Generation+%26+LLMs;Full-Stack+%2B+Product+Engineering" alt="Typing SVG"/>
</a>

<br/>


<img src="https://img.shields.io/badge/Jaipur,_India-4F46E5?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Location"/>

<br/><br/>

<a href="https://anmolagarwal4.github.io/"><img src="https://img.shields.io/badge/Portfolio-6D28D9?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"/></a>
<a href="https://linkedin.com/in/anmol325/"><img src="https://img.shields.io/badge/LinkedIn-7C3AED?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:anmolagarwal325@gmail.com"><img src="https://img.shields.io/badge/Email-4F46E5?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
<a href="https://github.com/AnmolAgarwal4"><img src="https://img.shields.io/badge/GitHub-181825?style=for-the-badge&logo=github&logoColor=A78BFA" alt="GitHub"/></a>

<br/><br/>

<img src="https://komarev.com/ghpvc/?username=AnmolAgarwal4&color=7C3AED&style=for-the-badge&label=PROFILE+VIEWS" alt="Profile Views"/>
<img src="https://img.shields.io/github/followers/AnmolAgarwal4?style=for-the-badge&color=6D28D9&labelColor=4F46E5&logo=github&label=FOLLOWERS" alt="Followers"/>
<img src="https://img.shields.io/github/stars/AnmolAgarwal4?style=for-the-badge&color=A78BFA&labelColor=4F46E5&logo=github&label=STARS" alt="Stars"/>

</div>

---

<!-- ====================== ABOUT ====================== -->
## &nbsp; About

I build and ship **AI systems end-to-end** — from model training and feature extraction to cloud deployment. My work spans **computer vision, machine learning, and retrieval-augmented generation**, with a focus on shipping things that actually run in production rather than staying in notebooks.

- 🧠 &nbsp;Deployed CV/ML systems reaching **~88% accuracy on 10,000+ image datasets** with **sub-2s inference latency**
- 🔎 &nbsp;Built a hybrid RAG search engine with a **custom BM25 index in C** — *110× faster* than brute force; findings submitted as an **ArXiv preprint (cs.IR)**
- ⚙️ &nbsp;Comfortable across the **full pipeline**: data → modeling → REST APIs → AWS deployment
- 🎓 &nbsp;B.Tech CSE · backed by an **IBM internship**
- 🚀 &nbsp;Product-engineering mindset — I care about scale, latency, and the user on the other end

**Open To:** AI/ML Internships &nbsp;·&nbsp; Software Engineering Roles &nbsp;·&nbsp; Open-Source Collaboration

---

<!-- ====================== TECH STACK ====================== -->
## &nbsp; Tech Stack

<div align="center">

**Languages**

<img src="https://skillicons.dev/icons?i=python,c,js,mysql,html,css" alt="Languages"/>

**Frontend**

<img src="https://skillicons.dev/icons?i=react,html,css,js" alt="Frontend"/>

**Backend &amp; Databases**

<img src="https://skillicons.dev/icons?i=flask,fastapi,mysql,sqlite,pytorch" alt="Backend"/>

**Cloud, DevOps &amp; Tooling**

<img src="https://skillicons.dev/icons?i=aws,docker,git,github,linux,arduino" alt="Cloud and Tooling"/>

</div>

---

<!-- ====================== AI / ML EXPERTISE ====================== -->
## &nbsp; AI / ML Expertise

| Domain | Proficiency | Details |
|:--|:--|:--|
| **Computer Vision** | Advanced | Attribute extraction, OpenCV pipelines, ~88% accuracy on 10K+ images |
| **Machine Learning** | Advanced | Classification & anomaly detection, scikit-learn, ~82% accuracy |
| **RAG / LLMs** | Proficient | Hybrid sparse+dense retrieval, Llama-3.3-70B, zero-hallucination RAG |
| **Information Retrieval** | Proficient | Custom BM25 in C (djb2 hashing), 110× speedup, ArXiv preprint (cs.IR) |
| **Deep Learning** | Proficient | PyTorch, sentence-transformers, MiniLM 384-dim embeddings |
| **MLOps / Deployment** | Working | AWS EC2 / Lambda / S3, Docker, HuggingFace Spaces, CI |

---

<!-- ====================== FEATURED PROJECTS ====================== -->
## &nbsp; Featured Projects

<details open>
<summary><b>🔍 &nbsp;Lurox — Hybrid Retrieval-Augmented Search Engine</b></summary>

<br/>

A four-layer hybrid search engine combining a hand-built sparse index with dense semantic retrieval and grounded LLM generation — engineered for speed and zero hallucination, deployed entirely on free-tier infrastructure.

| | |
|:--|:--|
| **Stack** | C · Python · FastAPI · PyTorch · Llama-3.3-70B |
| **Scale** | 10,087-document corpus · 132-query alpha-sweep experiment |
| **Performance** | Custom BM25 inverted index in C — **0.17ms median latency, 110× faster** than brute force |
| **Architecture** | Sparse BM25 → MiniLM semantic search (384-dim) → hybrid fusion → Llama-3.3-70B RAG |
| **Impact** | Identified **α = 0.2–0.3** as diversity-optimal fusion weight — submitted as **ArXiv preprint (cs.IR)** |
| **Repository** | [Live Demo ↗](https://lurox.netlify.app) · [Source ↗](https://github.com/AnmolAgarwal4) |

Deployed end-to-end at **$0 cost** — HuggingFace Spaces backend, Netlify frontend. The C-based index uses djb2 hashing to keep query latency in the microsecond range while the semantic layer maintains relevance.

</details>

<details>
<summary><b>👗 &nbsp;Snap2Style — AI-Powered Outfit Recommendation Platform</b></summary>

<br/>

An end-to-end computer-vision system that reads clothing attributes from a user photo and generates personalized outfit recommendations.

| | |
|:--|:--|
| **Stack** | Python · OpenCV · Streamlit |
| **Scale** | Trained & validated on **10,000+ fashion images** (DeepFashion / Kaggle) |
| **Performance** | **~88% attribute-detection accuracy** · **<2s inference latency** |
| **Architecture** | Modular pipeline: preprocessing → feature extraction → recommendation engine |
| **Impact** | Designed for easy scaling to wardrobe tracking & trend-aware suggestions |
| **Repository** | [Source ↗](https://github.com/AnmolAgarwal4) |

The modular design means new capabilities slot in without re-architecting the core inference path.

</details>

<details>
<summary><b>🧠 &nbsp;NeuroTrace — Cognitive Data Intelligence Platform</b></summary>

<br/>

A data-analytics platform that processes neural/cognitive datasets to surface behavioral patterns and anomalies through interactive dashboards.

| | |
|:--|:--|
| **Stack** | Python · Machine Learning · Streamlit |
| **Scale** | Trained on **1,000+ records** |
| **Performance** | **~82% classification accuracy** |
| **Architecture** | Dynamic filtering + visualization pipelines for real-time insight generation |
| **Impact** | Interactive dashboards cut manual analysis time by **~50%** |
| **Repository** | [Source ↗](https://github.com/AnmolAgarwal4) |

Built for exploratory analysis — analysts can filter and visualize patterns without writing code.

</details>

<details>
<summary><b>💡 &nbsp;Intelligent High-Beam Automation System</b></summary>

<br/>

A hybrid software–hardware prototype that adaptively switches vehicle high-beams based on real-time traffic density and ambient light.

| | |
|:--|:--|
| **Stack** | Python (simulation) · Arduino / C (embedded) · I2C / SPI |
| **Scale** | Live prototype with distance + light sensor integration |
| **Performance** | **~90% switching accuracy** in controlled tests |
| **Architecture** | Sensor fusion → adaptive beam-switching logic → monitoring dashboard |
| **Impact** | Lightweight dashboard for sensor data & system state improved debugging/tuning |
| **Repository** | [Source ↗](https://github.com/AnmolAgarwal4) |

Bridges embedded control and software simulation, with stable performance observed during live deployment.

</details>

<details>
<summary><b>🏥 &nbsp;Hospital Management System</b></summary>

<br/>

A full-stack hospital management platform with role-based access for patients, doctors, and administrators — built during the IBM internship.

| | |
|:--|:--|
| **Stack** | Python · Flask · SQL · HTML · CSS · JavaScript |
| **Scale** | SQL workflows across **500+ records** (patients, appointments, scheduling) |
| **Performance** | Reduced record-handling time by **~40%** |
| **Security** | Secure APIs + **role-based access control** |
| **Impact** | Responsive frontend reduced manual administrative effort |
| **Repository** | [Source ↗](https://github.com/AnmolAgarwal4) |

End-to-end ownership from secure API design through database workflows to a responsive UI.

</details>

---

<!-- ====================== EXPERIENCE ====================== -->
## &nbsp; Experience

### &nbsp;AI/ML Intern &nbsp;·&nbsp; IBM
`June 2025 – August 2025` &nbsp;·&nbsp; `Remote`

Worked across the full software pipeline, shipping a production-style full-stack platform with secure APIs and a relational data layer.

- Built a full-stack **Hospital Management System** with role-based access control
- Designed **SQL-driven workflows** managing 500+ records, cutting handling time ~40%
- Developed a responsive frontend improving usability and reducing manual effort

`Python` &nbsp; `Flask` &nbsp; `SQL` &nbsp; `REST APIs` &nbsp; `Full-Stack`

<br/>

### &nbsp;Volunteer &nbsp;·&nbsp; Time Bank of India
`May 2022` &nbsp;·&nbsp; `On-Site`

Contributed to community-driven initiatives, coordinating on-site with the team.

`Collaboration` &nbsp; `Community` &nbsp; `Coordination`

---

<!-- ====================== ACHIEVEMENTS ====================== -->
## &nbsp; Achievements

<div align="center">

| Recognition | Details |
|:--|:--|
| 🎬 **Netflix ML/AI Internship Screening (2026)** | Invited to complete screening from a global applicant pool of **3,000+** |
| 🏆 **Hackathon Finalist** | Ranked **Top 6 of 62** competing teams (**Top 10%**) at a university hackathon |
| ☁️ **AWS Skill Builder Bootcamp (UPES)** | **Top 10 of 1,000+** participants (**Top 1%**) |
| 📖 **IELTS Academic** | **Band 7** |

</div>

---

<!-- ====================== CERTIFICATIONS ====================== -->
## &nbsp; Certifications

**Amazon Web Services (AWS)**

<img src="https://img.shields.io/badge/Cloud_Security_Foundations-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Cloud_Architecture-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Introduction_to_Cloud_(I_%26_II)-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Skill_Builder_Modules-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>

**Google**

<img src="https://img.shields.io/badge/Crash_Course_on_Python-4285F4?style=flat-square&logo=google&logoColor=white"/>
<img src="https://img.shields.io/badge/Foundations_of_UX_Design-4285F4?style=flat-square&logo=google&logoColor=white"/>

**Walmart USA (Forage)**

<img src="https://img.shields.io/badge/Advanced_Software_Engineering_Job_Simulation-0071CE?style=flat-square&logo=walmart&logoColor=white"/>

**University of Michigan · Coursera**

<img src="https://img.shields.io/badge/Leading_Teams-7C3AED?style=flat-square&logo=coursera&logoColor=white"/>
<img src="https://img.shields.io/badge/Learning_How_to_Learn-7C3AED?style=flat-square&logo=coursera&logoColor=white"/>

---

<!-- ====================== CODING PROFILES ====================== -->
## &nbsp; Coding Profiles

<div align="center">

<a href="https://leetcode.com/u/Anmol325/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/></a>

<br/><br/>

<img src="https://leetcard.jacoblin.cool/Anmol325?theme=dark&font=Fira%20Code&ext=heatmap&border=0&bg=0D1117&ring=A78BFA&fire=7C3AED&radius=12" alt="LeetCode Stats" width="500"/>

</div>

---

<!-- ====================== GITHUB ANALYTICS ====================== -->
## &nbsp; GitHub Analytics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=AnmolAgarwal4&show_icons=true&hide_border=true&bg_color=0D1117&title_color=A78BFA&icon_color=7C3AED&text_color=C9D1D9&ring_color=A78BFA" height="170" alt="GitHub Stats"/>
<img src="https://streak-stats.demolab.com?user=AnmolAgarwal4&hide_border=true&background=0D1117&ring=7C3AED&fire=A78BFA&currStreakLabel=A78BFA&sideLabels=C9D1D9&dates=8B949E&currStreakNum=ffffff&sideNums=ffffff&stroke=A78BFA" height="170" alt="GitHub Streak"/>

<br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=AnmolAgarwal4&layout=compact&hide_border=true&bg_color=0D1117&title_color=A78BFA&text_color=C9D1D9&langs_count=8" height="180" alt="Top Languages"/>

</div>

---

<!-- ====================== TROPHIES ====================== -->
## &nbsp; GitHub Trophies

<div align="center">

<img src="https://github-profile-trophy.vercel.app/?username=AnmolAgarwal4&theme=algolia&no-frame=true&no-bg=true&margin-w=4&column=7" alt="GitHub Trophies"/>

</div>

---

<!-- ====================== CONTRIBUTION ACTIVITY ====================== -->
## &nbsp; Contribution Activity

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=AnmolAgarwal4&bg_color=0D1117&color=A78BFA&line=7C3AED&point=ffffff&area=true&hide_border=true" alt="Activity Graph" width="100%"/>

</div>

---

<!-- ====================== CONTRIBUTION SNAKE ====================== -->
## &nbsp; Contribution Snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnmolAgarwal4/AnmolAgarwal4/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AnmolAgarwal4/AnmolAgarwal4/output/github-contribution-grid-snake.svg"/>
  <img alt="Contribution Snake" src="https://raw.githubusercontent.com/AnmolAgarwal4/AnmolAgarwal4/output/github-contribution-grid-snake.svg"/>
</picture>

</div>

---

<!-- ====================== CURRENT FOCUS ====================== -->
## &nbsp; Current Focus

```yaml
Anmol_Agarwal:
  Learning:   [ Distributed Systems, Advanced RAG, MLOps ]
  Building:   "Lurox — Hybrid Retrieval-Augmented Search Engine"
  Exploring:  [ LLM Fine-Tuning, Vector Databases, System Design ]
  Open_To:    [ AI/ML Internships, SWE Roles, Open-Source Collaboration ]
```

---

<!-- ====================== CONNECT ====================== -->
## &nbsp; Connect

<div align="center">

<a href="mailto:anmolagarwal325@gmail.com"><img src="https://img.shields.io/badge/Gmail-4F46E5?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://linkedin.com/in/anmol325/"><img src="https://img.shields.io/badge/LinkedIn-7C3AED?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://github.com/AnmolAgarwal4"><img src="https://img.shields.io/badge/GitHub-181825?style=for-the-badge&logo=github&logoColor=A78BFA"/></a>
<a href="https://anmolagarwal4.github.io/"><img src="https://img.shields.io/badge/Portfolio-6D28D9?style=for-the-badge&logo=googlechrome&logoColor=white"/></a>

</div>

---

<!-- ====================== FOOTER ====================== -->
<div align="center">

<i>"Build systems that ship — accuracy in the model, latency in the pipeline, and the user always in mind."</i>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6D28D9,50:7C3AED,100:4F46E5&height=120&section=footer" width="100%"/>

</div>
