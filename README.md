<!-- ====================== HEADER ====================== -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,50:7C3AED,100:6D28D9&height=200&section=header&text=Anmol%20Agarwal&fontSize=58&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=AI%20%2F%20ML%20Engineer%20%C2%B7%20Full-Stack%20Developer&descAlignY=58&descSize=18&descAlignX=50" width="100%"/>

<a href="https://github.com/AnmolAgarwal4">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=A78BFA&center=true&vCenter=true&width=620&lines=AI+%2F+ML+Engineer;Retrieval-Augmented+Generation+%26+LLMs;Computer+Vision+%26+Deep+Learning;Full-Stack+%2B+Product+Engineering" alt="Typing SVG"/>
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

## &nbsp; About

B.Tech CSE (Hons.) student at **JECRC University, Jaipur** (2024–2028). I build and ship **AI systems end-to-end** — from model training and retrieval to REST APIs and cloud deployment — with a focus on things that run in production rather than staying in notebooks.

- 🔎 &nbsp;First-author **preprint (cs.IR, in submission)**: *Lurox*, a hybrid RAG system with a **custom BM25 index in C** — **0.17 ms median latency, ~59× faster than dense-only retrieval**
- 🧠 &nbsp;Built CV/ML systems reaching **~88% attribute-detection accuracy on 10,000+ images** with **sub-2s latency**
- 🌐 &nbsp;Shipped **Grokked.in** (1,571 DSA problems + LLM AI tutor) and a **production site for a defence-tech/UAV startup** as a freelancer
- 🏢 &nbsp;**Software Engineering Intern at IBM** (Flask, SQL, REST APIs, RBAC)
- 🚀 &nbsp;Product-engineering mindset — I care about scale, latency, and the user on the other end

**Open To:** AI/ML & Software Engineering Internships &nbsp;·&nbsp; Research Collaboration &nbsp;·&nbsp; Open-Source

---

## &nbsp; Tech Stack

<div align="center">

**Languages**

<img src="https://skillicons.dev/icons?i=python,java,c,cpp,js,ts,html,css" alt="Languages"/>

**Frontend**

<img src="https://skillicons.dev/icons?i=react,nextjs,html,css,js,wordpress" alt="Frontend"/>

**Backend &amp; Databases**

<img src="https://skillicons.dev/icons?i=nodejs,flask,fastapi,postgres,mysql,sqlite" alt="Backend"/>

**AI / ML**

<img src="https://skillicons.dev/icons?i=pytorch,opencv" alt="AI and ML"/>

**Cloud, DevOps &amp; Tooling**

<img src="https://skillicons.dev/icons?i=aws,docker,git,github,linux,netlify" alt="Cloud and Tooling"/>

</div>

---

## &nbsp; AI / ML Expertise

| Domain | Details |
|:--|:--|
| **RAG / LLMs** | Hybrid BM25 + dense retrieval, α-tunable fusion, grounded Llama-3.3-70B generation (zero factual contradictions across evaluated queries, no fine-tuning) |
| **Information Retrieval** | Custom BM25 inverted index in C, 0.17 ms median latency, ~59× faster than dense-only, 65,899-posting index |
| **Computer Vision** | OpenCV + GAN pipeline, ~88% attribute-detection accuracy on 10,000+ images |
| **Machine Learning** | scikit-learn classification, ~82% accuracy on 1,000+ records, Pandas, Streamlit dashboards |
| **Deep Learning** | PyTorch, sentence-transformers, MiniLM 384-dim embeddings |
| **Deployment** | AWS (EC2, Lambda, S3, API Gateway, IAM, CloudWatch), Docker, Hugging Face Spaces, Netlify |

---

## &nbsp; Research

<details open>
<summary><b>📄 &nbsp;Lurox: A Sub-millisecond Hybrid Retrieval System with Grounded LLM Generation</b></summary>

<br/>

*First-author preprint (cs.IR), in submission · Jan 2026 – Present*

| | |
|:--|:--|
| **Stack** | C · Python · FastAPI · PyTorch · sentence-transformers · Llama-3.3-70B |
| **Build** | End-to-end hybrid RAG from first principles — ~1,500 LOC, **zero external IR libraries** |
| **Architecture** | Custom BM25 inverted index in C → dense MiniLM retrieval → α-tunable fusion → grounded Llama-3.3-70B generation |
| **Performance** | **0.17 ms** median BM25 latency, **~59× faster** than dense-only retrieval, 65,899-posting index |
| **Finding** | Retrieval diversity peaks at **α = 0.2–0.3**, an objective distinct from accuracy-optimal tuning — validated with paired bootstrap testing (n = 10,000, **p < 0.0001**) |
| **Grounding** | Prompt-level grounding gave **zero factual contradictions** across evaluated queries, without fine-tuning |
| **Links** | [Live Demo ↗](https://lurox.netlify.app) · [Source ↗](https://github.com/AnmolAgarwal4/Lurox) |

</details>

---

## &nbsp; Featured Projects

<details open>
<summary><b>📚 &nbsp;Grokked.in — DSA Learning Platform with AI Tutor</b></summary>

<br/>

A scalable web platform for practicing data structures and algorithms, with an LLM-powered tutor. *Nov 2025 – Present*

| | |
|:--|:--|
| **Stack** | Next.js · React · Node.js · PostgreSQL · REST APIs · LLM |
| **Scale** | **1,571 DSA problems** across **4 languages** |
| **Architecture** | REST APIs + PostgreSQL-based progress tracking for reliable user progress management |
| **Link** | [grokked.in ↗](https://grokked.in) |

</details>

<details>
<summary><b>👗 &nbsp;Snap2Style — CV + GAN Outfit Recommender</b></summary>

<br/>

A computer-vision and GAN-based pipeline that reads clothing attributes from a photo and recommends outfits. *Aug – Sep 2025*

| | |
|:--|:--|
| **Stack** | Python · OpenCV · PyTorch · GAN |
| **Scale** | **10,000+ images** |
| **Performance** | **~88% attribute-detection accuracy** · **sub-2s** end-to-end latency |
| **Repository** | [Source ↗](https://github.com/AnmolAgarwal4) |

</details>

<details>
<summary><b>🧠 &nbsp;NeuroTrace — Cognitive Data Intelligence Platform</b></summary>

<br/>

Supervised ML models plus interactive dashboards for exploring cognitive datasets. *Oct – Dec 2025*

| | |
|:--|:--|
| **Stack** | Python · scikit-learn · Streamlit · Pandas |
| **Scale** | **1,000+ records** |
| **Performance** | **~82% accuracy** |
| **Impact** | Dashboards cut manual analysis time by **~50%** for non-technical analysts |
| **Repository** | [Source ↗](https://github.com/AnmolAgarwal4) |

</details>

<details>
<summary><b>🏥 &nbsp;Hospital Management System (IBM)</b></summary>

<br/>

Full-stack hospital platform with role-based access, built during the IBM internship.

| | |
|:--|:--|
| **Stack** | Python · Flask · SQL · REST APIs |
| **Scale** | Workflows across **500+ patient records** |
| **Performance** | Query optimization + automated scheduling cut administrative handling time by **40%** |
| **Security** | Role-based access control |
| **Impact** | Usable by non-technical clinical staff with **zero training** |
| **Repository** | [Source ↗](https://github.com/AnmolAgarwal4) |

</details>

---

## &nbsp; Experience

### &nbsp;Freelance Web Developer &nbsp;·&nbsp; Self-employed
`May 2026 – Aug 2026` &nbsp;·&nbsp; `Remote`

- Developed and deployed a **production website for a defence-tech/UAV startup**: 6 UAV platforms, 240+ structured specification fields
- Architected a **reusable product system** — one shared template with URL-parameter routing replaces hand-coded product pages
- Built custom **SVG/CSS radar animations** and an **accessible product modal** (focus trapping, ESC-to-close, ARIA roles, dynamic `mailto` enquiries) across 3 responsive breakpoints

`WordPress` &nbsp; `Elementor` &nbsp; `Vanilla JavaScript` &nbsp; `SVG/CSS` &nbsp; `Accessibility`

<br/>

### &nbsp;Software Engineering Intern &nbsp;·&nbsp; IBM
`June 2025 – August 2025` &nbsp;·&nbsp; `Remote`

- Implemented a full-stack **Hospital Management System** (Python/Flask, SQL, REST APIs, RBAC) across **500+ patient records**
- Optimized APIs and SQL workflows, reducing administrative handling time by **40%**
- Coordinated requirements with technical and clinical stakeholders; shipped a system non-technical staff could use with zero training

`Python` &nbsp; `Flask` &nbsp; `SQL` &nbsp; `REST APIs` &nbsp; `RBAC`

---

## &nbsp; Education

**JECRC University, Jaipur** — B.Tech. in Computer Science Engineering (Hons.) · `Sep 2024 – May 2028`

---

## &nbsp; Achievements

<div align="center">

| Recognition | Details |
|:--|:--|
| 📄 **First-Author Preprint** | *Lurox* (cs.IR) — in submission |
| ☁️ **AWS Skill Builder Bootcamp (UPES)** | **Top 10 of 1,000+** participants (**Top 1%**) |
| 🏆 **Hackathon Finalist** | **Top 6 of 62** teams (**Top 10%**) at a university-level hackathon |
| 📖 **IELTS** | Overall **Band 7.0** (C1) |

</div>

---

## &nbsp; Certifications

**Amazon Web Services (AWS)**

<img src="https://img.shields.io/badge/Cloud_Security-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Cloud_Architecture-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Skill_Builder_Modules-FF9900?style=flat-square&logo=amazonaws&logoColor=white"/>

**Google**

<img src="https://img.shields.io/badge/Python-4285F4?style=flat-square&logo=google&logoColor=white"/>
<img src="https://img.shields.io/badge/UX_Design-4285F4?style=flat-square&logo=google&logoColor=white"/>

**Walmart USA (Forage)**

<img src="https://img.shields.io/badge/Software_Engineering_Job_Simulation-0071CE?style=flat-square&logo=walmart&logoColor=white"/>

---

## &nbsp; Coding Profiles

<div align="center">

<a href="https://leetcode.com/u/Anmol325/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/></a>

<br/><br/>

<img src="https://leetcard.jacoblin.cool/Anmol325?theme=dark&font=Fira%20Code&ext=heatmap&border=0&bg=0D1117&ring=A78BFA&fire=7C3AED&radius=12" alt="LeetCode Stats" width="500"/>

</div>

---

## &nbsp; GitHub Analytics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=AnmolAgarwal4&show_icons=true&hide_border=true&bg_color=0D1117&title_color=A78BFA&icon_color=7C3AED&text_color=C9D1D9&ring_color=A78BFA" height="170" alt="GitHub Stats"/>
<img src="https://streak-stats.demolab.com?user=AnmolAgarwal4&hide_border=true&background=0D1117&ring=7C3AED&fire=A78BFA&currStreakLabel=A78BFA&sideLabels=C9D1D9&dates=8B949E&currStreakNum=ffffff&sideNums=ffffff&stroke=A78BFA" height="170" alt="GitHub Streak"/>

<br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=AnmolAgarwal4&layout=compact&hide_border=true&bg_color=0D1117&title_color=A78BFA&text_color=C9D1D9&langs_count=8" height="180" alt="Top Languages"/>

</div>

---

## &nbsp; GitHub Trophies

<div align="center">

<img src="https://github-profile-trophy.vercel.app/?username=AnmolAgarwal4&theme=algolia&no-frame=true&no-bg=true&margin-w=4&column=7" alt="GitHub Trophies"/>

</div>

---

## &nbsp; Contribution Activity

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=AnmolAgarwal4&bg_color=0D1117&color=A78BFA&line=7C3AED&point=ffffff&area=true&hide_border=true" alt="Activity Graph" width="100%"/>

</div>

---

## &nbsp; Contribution Snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnmolAgarwal4/AnmolAgarwal4/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AnmolAgarwal4/AnmolAgarwal4/output/github-contribution-grid-snake.svg"/>
  <img alt="Contribution Snake" src="https://raw.githubusercontent.com/AnmolAgarwal4/AnmolAgarwal4/output/github-contribution-grid-snake.svg"/>
</picture>

</div>

---

## &nbsp; Current Focus

```yaml
Anmol_Agarwal:
  Building:   [ "Lurox — preprint (cs.IR) in submission", "Grokked.in — DSA platform + AI tutor" ]
  Learning:   [ Distributed Systems, Advanced RAG, MLOps ]
  Exploring:  [ LLM Fine-Tuning, Vector Databases, System Design ]
  Open_To:    [ AI/ML Internships, SWE Roles, Research & Open-Source Collaboration ]
```

---

## &nbsp; Connect

<div align="center">

<a href="mailto:anmolagarwal325@gmail.com"><img src="https://img.shields.io/badge/Gmail-4F46E5?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://linkedin.com/in/anmol325/"><img src="https://img.shields.io/badge/LinkedIn-7C3AED?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://github.com/AnmolAgarwal4"><img src="https://img.shields.io/badge/GitHub-181825?style=for-the-badge&logo=github&logoColor=A78BFA"/></a>
<a href="https://anmolagarwal4.github.io/"><img src="https://img.shields.io/badge/Portfolio-6D28D9?style=for-the-badge&logo=googlechrome&logoColor=white"/></a>

</div>

---

<div align="center">

<i>"Build systems that ship — accuracy in the model, latency in the pipeline, and the user always in mind."</i>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6D28D9,50:7C3AED,100:4F46E5&height=120&section=footer" width="100%"/>

</div>
