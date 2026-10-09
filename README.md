<div align="center">

<img src="assets/banner.svg" width="100%" alt="Anmol Agarwal — AI/ML Engineer + Full-Stack Dev"/>

<a href="https://github.com/AnmolAgarwal4">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=A78BFA&center=true&vCenter=true&width=700&lines=Hybrid+retrieval+in+C+%E2%80%94+0.17+ms+median+latency;First-author+preprint+%C2%B7+cs.IR;Shipping+RAG%2C+CV+%26+full-stack+products;Grokked.in+%C2%B7+1%2C571+DSA+problems+%2B+AI+tutor" alt="Typing SVG"/>
</a>

<br/><br/>

<a href="https://anmolagarwal4.github.io/"><img src="https://img.shields.io/badge/PORTFOLIO-6D28D9?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"/></a>
<a href="https://linkedin.com/in/anmol325/"><img src="https://img.shields.io/badge/LINKEDIN-7C3AED?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:anmolagarwal325@gmail.com"><img src="https://img.shields.io/badge/EMAIL-22D3EE?style=for-the-badge&logo=gmail&logoColor=0a0714" alt="Email"/></a>
<a href="https://lurox.netlify.app"><img src="https://img.shields.io/badge/LUROX_DEMO-F472B6?style=for-the-badge&logo=netlify&logoColor=0a0714" alt="Lurox demo"/></a>

<img src="https://komarev.com/ghpvc/?username=AnmolAgarwal4&color=7C3AED&style=flat-square&label=PROFILE+VIEWS" alt="Profile Views"/>
<img src="https://img.shields.io/github/followers/AnmolAgarwal4?style=flat-square&color=22D3EE&labelColor=0a0714&label=FOLLOWERS" alt="Followers"/>
<img src="https://img.shields.io/github/stars/AnmolAgarwal4?style=flat-square&color=F472B6&labelColor=0a0714&label=STARS" alt="Stars"/>

</div>

<br/>

<img src="assets/h-about.svg" width="100%" alt="About"/>

I build and ship **AI systems end-to-end** — from model training and retrieval to REST APIs and cloud deployment — and I care more about things that run in production than things that live in notebooks. B.Tech CSE (Hons.) student, class of 2028.

<img src="assets/m-overall.svg" width="100%" alt="Key metrics"/>

- 🔎 &nbsp;**First-author preprint (cs.IR, in submission)** — *Lurox*, a hybrid RAG system with a custom BM25 index written in C
- 🧠 &nbsp;CV/ML systems at **~88% attribute-detection accuracy on 10,000+ images**, sub-2s latency
- 🌐 &nbsp;Shipped **Grokked.in** and a **production website for a defence-tech/UAV startup** (freelance, 2026)
- 🏢 &nbsp;**Software Engineering Intern @ IBM** — Flask, SQL, REST APIs, role-based access control
- 🚀 &nbsp;Product-engineering mindset: scale, latency, and the person on the other end

> **Open to:** AI/ML & Software Engineering internships · research collaboration · open source

<br/>

<img src="assets/h-stack.svg" width="100%" alt="Tech Stack"/>

<div align="center">

<img src="https://skillicons.dev/icons?i=python,java,c,cpp,js,ts,html,css&theme=dark" alt="Languages"/><br/>
<img src="https://skillicons.dev/icons?i=react,nextjs,nodejs,flask,fastapi,wordpress&theme=dark" alt="Frameworks"/><br/>
<img src="https://skillicons.dev/icons?i=postgres,mysql,sqlite,pytorch,opencv&theme=dark" alt="Data and AI"/><br/>
<img src="https://skillicons.dev/icons?i=aws,docker,git,github,linux,netlify&theme=dark" alt="Cloud and tooling"/>

</div>

<br/>

<img src="assets/h-skills.svg" width="100%" alt="AI / ML Skills"/>

| Domain | What I've built with it |
|:--|:--|
| **RAG / LLMs** | Hybrid BM25 + dense retrieval, α-tunable fusion, grounded Llama-3.3-70B generation with zero factual contradictions across evaluated queries — no fine-tuning |
| **Information Retrieval** | Custom BM25 inverted index in C · 0.17 ms median latency · ~59× faster than dense-only · 65,899-posting index |
| **Computer Vision** | OpenCV + GAN pipeline · ~88% attribute-detection accuracy · 10,000+ images |
| **Machine Learning** | scikit-learn classifiers · ~82% accuracy on 1,000+ records · Pandas · Streamlit dashboards |
| **Deep Learning** | PyTorch · sentence-transformers · MiniLM 384-dim embeddings |
| **Deployment** | AWS (EC2, Lambda, S3, API Gateway, IAM, CloudWatch) · Docker · Hugging Face Spaces · Netlify |

<br/>

<img src="assets/h-research.svg" width="100%" alt="Research"/>

### 📄 Lurox: A Sub-millisecond Hybrid Retrieval System with Grounded LLM Generation
*First-author preprint (cs.IR), in submission · Jan 2026 – Present*

<img src="assets/m-lurox.svg" width="100%" alt="Lurox metrics"/>

Built end-to-end from first principles — **~1,500 LOC with zero external IR libraries**: a custom BM25 inverted index in C, dense MiniLM retrieval, α-tunable fusion, and grounded Llama-3.3-70B generation.

- **Finding:** retrieval diversity peaks at **α = 0.2–0.3**, an objective distinct from accuracy-optimal tuning — validated with paired bootstrap testing (n = 10,000, p < 0.0001)
- **Grounding:** prompt-level grounding produced zero factual contradictions across evaluated queries, no fine-tuning
- **Stack:** `C` `Python` `FastAPI` `PyTorch` `sentence-transformers` `Llama-3.3-70B`

[**Live demo ↗**](https://lurox.netlify.app) &nbsp;·&nbsp; [**Source ↗**](https://github.com/AnmolAgarwal4/Lurox)

<br/>

<img src="assets/h-projects.svg" width="100%" alt="Projects"/>

<details open>
<summary><b>📚 &nbsp;Grokked.in — DSA platform with an LLM-powered AI tutor</b> &nbsp;<sub>Nov 2025 – Present</sub></summary>

<br/>

| | |
|:--|:--|
| **Stack** | Next.js · React · Node.js · PostgreSQL · REST APIs · LLM |
| **Scale** | **1,571 DSA problems** across **4 languages** |
| **Architecture** | REST APIs + PostgreSQL progress tracking for reliable, scalable user progress management |
| **Link** | [grokked.in ↗](https://grokked.in) |

</details>

<details>
<summary><b>👗 &nbsp;Snap2Style — CV + GAN outfit recommender</b> &nbsp;<sub>Aug – Sep 2025</sub></summary>

<br/>

| | |
|:--|:--|
| **Stack** | Python · OpenCV · PyTorch · GAN |
| **Scale** | **10,000+ images** |
| **Performance** | **~88% attribute-detection accuracy** · **sub-2s** end-to-end latency |
| **Source** | [GitHub ↗](https://github.com/AnmolAgarwal4) |

</details>

<details>
<summary><b>🧠 &nbsp;NeuroTrace — cognitive data intelligence platform</b> &nbsp;<sub>Oct – Dec 2025</sub></summary>

<br/>

| | |
|:--|:--|
| **Stack** | Python · scikit-learn · Streamlit · Pandas |
| **Scale** | **1,000+ records** |
| **Performance** | **~82% accuracy** |
| **Impact** | Dashboards cut manual analysis time by **~50%** for non-technical analysts |
| **Source** | [GitHub ↗](https://github.com/AnmolAgarwal4) |

</details>

<details>
<summary><b>🏥 &nbsp;Hospital Management System</b> &nbsp;<sub>IBM · Jun – Aug 2025</sub></summary>

<br/>

| | |
|:--|:--|
| **Stack** | Python · Flask · SQL · REST APIs |
| **Scale** | Workflows across **500+ patient records** |
| **Performance** | Query optimization + automated scheduling cut admin handling time by **40%** |
| **Security** | Role-based access control |
| **Impact** | Usable by non-technical clinical staff with **zero training** |
| **Source** | [GitHub ↗](https://github.com/AnmolAgarwal4) |

</details>

<br/>

<img src="assets/h-experience.svg" width="100%" alt="Experience"/>

### 🛠️ Freelance Web Developer &nbsp;·&nbsp; Self-employed
`May – Aug 2026` · `Remote`

- Shipped a **production website for a defence-tech/UAV startup** — 6 UAV platforms, 240+ structured specification fields
- Architected a **reusable product system**: one shared template + URL-parameter routing replaces hand-coded product pages
- Built custom **SVG/CSS radar animations** and an **accessible product modal** (focus trapping, ESC-to-close, ARIA roles, dynamic `mailto` enquiries) across 3 responsive breakpoints

`WordPress` `Elementor` `Vanilla JS` `SVG/CSS` `Accessibility`

### 🏢 Software Engineering Intern &nbsp;·&nbsp; IBM
`Jun – Aug 2025` · `Remote`

- Implemented a full-stack **Hospital Management System** (Python/Flask, SQL, REST APIs, RBAC) across **500+ patient records**
- Optimized APIs and SQL workflows — **40% less** administrative handling time
- Coordinated requirements with technical and clinical stakeholders

`Python` `Flask` `SQL` `REST APIs` `RBAC`

<br/>

<img src="assets/h-achievements.svg" width="100%" alt="Achievements"/>

| | |
|:--|:--|
| 📄 **First-author preprint** | *Lurox* (cs.IR) — in submission |
| ☁️ **AWS Skill Builder Bootcamp (UPES)** | **Top 10 of 1,000+** participants (top 1%) |
| 🏆 **Hackathon finalist** | **Top 6 of 62** teams (top 10%) at a university-level hackathon |
| 📖 **IELTS** | Overall **Band 7.0** (C1) |

<br/>

<img src="assets/h-certs.svg" width="100%" alt="Certifications"/>

<div align="center">

<img src="https://img.shields.io/badge/AWS-Cloud_Security-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/AWS-Cloud_Architecture-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Google-Python-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
<img src="https://img.shields.io/badge/Google-UX_Design-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
<img src="https://img.shields.io/badge/Walmart_Forage-SWE_Simulation-0071CE?style=for-the-badge&logo=walmart&logoColor=white"/>

</div>

<br/>

<img src="assets/h-coding.svg" width="100%" alt="Coding profiles"/>

<div align="center">

<a href="https://leetcode.com/u/Anmol325/"><img src="https://leetcard.jacoblin.cool/Anmol325?theme=dark&font=Fira%20Code&ext=heatmap&border=0&bg=0a0714&ring=A78BFA&fire=22D3EE&radius=20" alt="LeetCode Stats" width="520"/></a>

</div>

<br/>

<img src="assets/h-stats.svg" width="100%" alt="GitHub stats"/>

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=AnmolAgarwal4&show_icons=true&hide_border=true&bg_color=0a0714&title_color=22D3EE&icon_color=A78BFA&text_color=E5E7EB&ring_color=F472B6&border_radius=20" height="170" alt="GitHub Stats"/>
<img src="https://streak-stats.demolab.com?user=AnmolAgarwal4&hide_border=true&background=0a0714&ring=22D3EE&fire=F472B6&currStreakLabel=22D3EE&sideLabels=E5E7EB&dates=9CA3AF&currStreakNum=ffffff&sideNums=ffffff&stroke=7C3AED&border_radius=20" height="170" alt="GitHub Streak"/>
<br/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=AnmolAgarwal4&layout=compact&hide_border=true&bg_color=0a0714&title_color=22D3EE&text_color=E5E7EB&langs_count=8&border_radius=20" height="180" alt="Top Languages"/>
<br/>
<img src="https://github-readme-activity-graph.vercel.app/graph?username=AnmolAgarwal4&bg_color=0a0714&color=A78BFA&line=22D3EE&point=ffffff&area=true&hide_border=true&radius=20" width="100%" alt="Activity Graph"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AnmolAgarwal4/AnmolAgarwal4/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AnmolAgarwal4/AnmolAgarwal4/output/github-contribution-grid-snake.svg"/>
  <img alt="Contribution Snake" src="https://raw.githubusercontent.com/AnmolAgarwal4/AnmolAgarwal4/output/github-contribution-grid-snake.svg"/>
</picture>

</div>

<br/>

<img src="assets/h-focus.svg" width="100%" alt="Current focus"/>

```yaml
anmol_agarwal:
  building:  [ "Lurox — preprint (cs.IR), in submission", "Grokked.in — DSA platform + AI tutor" ]
  learning:  [ distributed_systems, advanced_rag, mlops ]
  exploring: [ llm_fine_tuning, vector_databases, system_design ]
  open_to:   [ ai_ml_internships, swe_roles, research, open_source ]
```

<br/>

<img src="assets/h-connect.svg" width="100%" alt="Connect"/>

<div align="center">

<a href="mailto:anmolagarwal325@gmail.com"><img src="https://img.shields.io/badge/GMAIL-6D28D9?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://linkedin.com/in/anmol325/"><img src="https://img.shields.io/badge/LINKEDIN-7C3AED?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://github.com/AnmolAgarwal4"><img src="https://img.shields.io/badge/GITHUB-22D3EE?style=for-the-badge&logo=github&logoColor=0a0714"/></a>
<a href="https://anmolagarwal4.github.io/"><img src="https://img.shields.io/badge/PORTFOLIO-F472B6?style=for-the-badge&logo=googlechrome&logoColor=0a0714"/></a>

<br/><br/>

<img src="assets/footer.svg" width="100%" alt="Build systems that ship"/>

</div>
