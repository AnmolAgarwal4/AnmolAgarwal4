import random, math
from pixfont import F, tw, px
RED="#00D2BE"; BG="#0b0b0c"; GR="#8b8b92"; DK="#2a2a2e"
SANS="font-family=\"'Helvetica Neue',Helvetica,Arial,sans-serif\""
def ridge(x0,x1,n,fn,seed,amp):
    r=random.Random(seed); pts=[]
    for i in range(n+1):
        t=i/n; x=x0+(x1-x0)*t
        pts.append((round(x,1),round(fn(t)+r.uniform(-amp,amp),1)))
    return pts
def d_of(pts): return "M"+" L".join(f"{x} {y}" for x,y in pts)
def plen(pts): return sum(math.hypot(pts[i+1][0]-pts[i][0],pts[i+1][1]-pts[i][1]) for i in range(len(pts)-1))
def car(d,dur,s=1.0):
    return (f'<g transform="scale({s})"><g><path d="M-9 -2.5 L5 -2.5 L11 0 L5 2.5 L-9 2.5 Z" fill="{RED}"/><rect x="-11" y="-3.5" width="3" height="7" fill="#fff"/>'
            f'<animateMotion dur="{dur}s" repeatCount="indefinite" rotate="auto" path="{d}"/></g></g>') if s==1.0 else ""
def mover(d,dur,r=5):
    return (f'<g><circle r="{r*2.4}" fill="{RED}" opacity=".18"/><circle r="{r}" fill="{RED}"/><circle r="{r*.4}" fill="#fff"/>'
            f'<animateMotion dur="{dur}s" repeatCount="indefinite" path="{d}"/></g>')
def trail(d,L,dur,ln=80,w=3):
    return (f'<path d="{d}" fill="none" stroke="{RED}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="{ln} {L+ln:.0f}">'
            f'<animate attributeName="stroke-dashoffset" values="{ln};{ln-L:.0f}" dur="{dur}s" repeatCount="indefinite"/></path>')
def svg(w,h,body,r=14,bg=BG):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><clipPath id="c"><rect width="{w}" height="{h}" rx="{r}"/></clipPath>'
            f'<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="{bg}"/>{body}</g></svg>')
def eq(x0,x1,base,maxh,n,seed,col="#fff",op=.16,red_every=0,w=5):
    r=random.Random(seed); o=""; step=(x1-x0)/(n-1)
    for i in range(n):
        x=x0+i*step; hs=[r.randint(6,maxh) for _ in range(3)]; hs.append(hs[0])
        c=RED if red_every and i%red_every==red_every-1 else col; o_=1 if c==RED else op
        dur=r.uniform(.9,2.2)
        o+=(f'<rect x="{x:.1f}" y="{base-hs[0]}" width="{w}" height="{hs[0]}" fill="{c}" opacity="{o_}">'
            f'<animate attributeName="height" values="{";".join(map(str,hs))}" dur="{dur:.2f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="y" values="{";".join(str(base-h) for h in hs)}" dur="{dur:.2f}s" repeatCount="indefinite"/></rect>')
    return o
def txt(s,x,y,size,fill="#fff",wt=300,ls=0,anchor="start",extra=""):
    return f'<text x="{x}" y="{y}" {SANS} font-size="{size}" font-weight="{wt}" letter-spacing="{ls}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'

def shiftlights(x0,x1,y,n=21,h=4):
    step=(x1-x0)/n; o=""
    for i in range(n):
        o+=(f'<rect x="{x0+i*step:.1f}" y="{y}" width="{step-5:.1f}" height="{h}" rx="1" fill="{RED}" opacity=".12">'
            f'<animate attributeName="opacity" values=".12;1;1;.12;.12" keyTimes="0;.{min(i*4+5,60):02d};.8;.9;1" dur="3.6s" repeatCount="indefinite"/></rect>')
    return o
# ---------------- BANNER
def banner():
    w,h=1000,420; b=""
    sx,sy=800,150
    for rr,o in [(120,.07),(160,.05),(200,.035),(240,.025)]: b+=f'<circle cx="{sx}" cy="{sy}" r="{rr}" fill="none" stroke="#fff" stroke-opacity="{o*2}"/>'
    b+=f'<circle cx="{sx}" cy="{sy}" r="62" fill="{RED}"/>'
    back=ridge(0,1000,26,lambda t:285-165*math.sin(t*2.7)**2+14*math.sin(t*23),1,12)
    mid=ridge(0,1000,22,lambda t:310-150*t**1.1-34*math.sin(t*8.5),2,12)
    front=ridge(0,1000,26,lambda t:332-185*(t**1.25)+18*math.sin(t*13)*(1-t*.5),3,12)
    for pts,fill,stk in [(back,"#121214","#26262a"),(mid,"#0e0e10","#34343a")]:
        b+=f'<path d="{d_of(pts)} L1000 345 L0 345Z" fill="{fill}" stroke="{stk}" stroke-width="1.2" stroke-linejoin="round"/>'
    b+=f'<path d="{d_of(front)} L1000 345 L0 345Z" fill="{BG}" stroke="none"/>'
    b+=f'<path d="{d_of(front)}" fill="none" stroke="#fff" stroke-opacity=".9" stroke-width="1.6" stroke-linejoin="round"/>'
    L=plen(front); dur=9
    b+=trail(d_of(front),L,dur,110,3)+mover(d_of(front),dur,5)
    b+=f'<rect x="0" y="345" width="1000" height="1" fill="#fff" opacity=".12"/>'
    b+=eq(40,960,408,52,56,5,"#fff",.17,7,5)
    b+=shiftlights(56,944,14)
    # text
    b+=txt("ANMOL AGARWAL",56,124,54,"#fff",200,6)
    b+=f'<rect x="58" y="142" width="56" height="3" fill="{RED}"/>'
    b+=px("AI / ML ENGINEER . FULL-STACK DEVELOPER",58,166,2,"#cfcfd4")
    b+=px("RAG . LLMS . COMPUTER VISION . SYSTEMS IN C",58,186,2,GR)
    # HUD
    b+=f'<circle cx="62" cy="46" r="4" fill="{RED}"><animate attributeName="opacity" values="1;.15;1" dur="1.2s" repeatCount="indefinite"/></circle>'
    b+=px("LIVE TELEMETRY",76,41,2,"#fff")
    t="26.91N 75.79E . JAIPUR"; b+=px(t,944-tw(t,2),41,2,GR)
    b+=px("EVERY MILLISECOND COUNTS",944-tw("EVERY MILLISECOND COUNTS",2),322,2,RED)
    return svg(w,h,b,r=18)

# ---------------- SECTION HEADER
def header(idx,title,seed):
    w,h=900,64
    pts=ridge(380,872,16,lambda t:44-22*t+8*math.sin(t*9),seed,7)
    d=d_of(pts); L=plen(pts); dur=5+seed%3
    b=f'<rect x="24" y="19" width="4" height="26" fill="{RED}"/>'
    b+=px(f"LAP {idx:02d}",40,16,2,GR)
    b+=txt(title,40,46,21,"#fff",600,5)
    b+=f'<path d="{d}" fill="none" stroke="#fff" stroke-opacity=".22" stroke-width="1.2" stroke-linejoin="round"/>'
    b+=trail(d,L,dur,60,2)+mover(d,dur,3.5)
    b+=f'<rect x="0" y="{h-1}" width="{w}" height="1" fill="#fff" opacity=".1"/>'
    return svg(w,h,b,r=12)

# ---------------- METRICS
def metrics(items,seed):
    w,h=900,150; n=len(items); cw=w/n; b=""
    for i,(num,lab) in enumerate(items):
        cx=cw*i+cw/2
        if i: b+=f'<rect x="{cw*i:.0f}" y="28" width="1" height="{h-56}" fill="#fff" opacity=".1"/>'
        b+=txt(num,cx,78,44,"#fff",200,0,"middle")
        b+=px(lab,int(cx-tw(lab,2)/2),94,2,GR)
        b+=eq(cx-34,cx+34,128,16,9,seed+i,RED,.9,0,4)
    return svg(w,h,b,r=14)

# ---------------- JOURNEY (career as an elevation profile)
def journey():
    w,h=900,290
    keys=[("JUN 25","IBM INTERN"),("OCT 25","NEUROTRACE"),("NOV 25","GROKKED.IN"),("JAN 26","LUROX"),("MAY 26","UAV SITE"),("NOW","PREPRINT")]
    xs=[70+i*152 for i in range(6)]; ys=[205,184,168,132,104,70]
    r=random.Random(4); pts=[(xs[0],ys[0])]
    for i in range(5):
        for k in (1,2,3):
            t=k/4; x=xs[i]+(xs[i+1]-xs[i])*t; y=ys[i]+(ys[i+1]-ys[i])*t+r.uniform(-9,9)
            pts.append((round(x,1),round(y,1)))
        pts.append((xs[i+1],ys[i+1]))
    d=d_of(pts); L=plen(pts); dur=11
    b=f'<defs><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{RED}" stop-opacity=".28"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></linearGradient></defs>'
    for gy in (60,110,160,210): b+=f'<rect x="30" y="{gy}" width="840" height="1" fill="#fff" opacity=".05"/>'
    b+=f'<path d="{d} L{xs[-1]} 232 L{xs[0]} 232Z" fill="url(#ar)"/>'
    b+=f'<path d="{d}" fill="none" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/>'
    b+=trail(d,L,dur,120,3)+mover(d,dur,5)
    b+=f'<rect x="30" y="232" width="840" height="1" fill="#fff" opacity=".25"/>'
    for i,(x,y) in enumerate(zip(xs,ys)):
        last=i==5
        b+=f'<rect x="{x}" y="{y}" width="1" height="{232-y}" fill="#fff" opacity=".18"/>'
        b+=f'<circle cx="{x}" cy="{y}" r="5" fill="{BG}" stroke="{RED if last else "#fff"}" stroke-width="2"/>'
        if last: b+=f'<circle cx="{x}" cy="{y}" r="5" fill="none" stroke="{RED}"><animate attributeName="r" values="5;16" dur="1.8s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0" dur="1.8s" repeatCount="indefinite"/></circle>'
        d_,t_=keys[i]
        b+=px(d_,int(x-tw(d_,2)/2),246,2,RED if last else GR)+px(t_,int(x-tw(t_,2)/2),266,2,"#fff")
    b+=px("ELEVATION = SCOPE + SHIPPED WORK",30,24,2,GR)
    b+=px("THE CIRCUIT SO FAR",870-tw("THE CIRCUIT SO FAR",2),24,2,RED)
    return svg(w,h,b,r=14)

# ---------------- OFF THE CLOCK
def offclock():
    w,h=900,210; b=""; cw=300
    for i in (1,2): b+=f'<rect x="{cw*i}" y="28" width="1" height="{h-56}" fill="#fff" opacity=".1"/>'
    # 1 circuit
    loop="M70 88 C62 52 118 40 150 58 S212 96 192 120 S96 132 70 88 Z"
    b+=f'<path d="{loop}" fill="none" stroke="#fff" stroke-opacity=".8" stroke-width="2" stroke-linejoin="round" transform="translate(10,-4)"/>'
    b+=f'<g transform="translate(10,-4)">{mover(loop,4.5,4)}</g>'
    # 2 sound
    b+=eq(cw+100,cw+200,124,70,13,11,"#fff",.85,4,5)
    # 3 summits
    m=[(cw*2+60,128),(cw*2+110,72),(cw*2+136,96),(cw*2+176,52),(cw*2+240,128)]
    b+=f'<path d="{d_of(m)}" fill="none" stroke="#fff" stroke-opacity=".85" stroke-width="2" stroke-linejoin="round"/>'
    b+=f'<circle cx="{cw*2+176}" cy="40" r="4" fill="{RED}"/>'
    b+=f'<path d="M{cw*2+60} 128 L{cw*2+240} 128" stroke="{RED}" stroke-width="2" stroke-dasharray="4 8"><animate attributeName="stroke-dashoffset" values="0;-24" dur="1.4s" repeatCount="indefinite"/></path>'
    for i,(t,c) in enumerate([("SPEED","MERCEDES-AMG F1 FAN"),("SOUND","MUSIC WHILE I BUILD"),("SUMMITS","MOUNTAINS AND TRAVEL")]):
        cx=cw*i+cw/2
        b+=txt(t,cx,164,15,"#fff",600,5,"middle")+px(c,int(cx-tw(c,2)/2),176,2,GR)
    return svg(w,h,b,r=14)

# ---------------- FOOTER
def footer():
    w,h=900,170; b=""
    for row,y in enumerate((0,h-24)):
        b+=f'<g><animateTransform attributeName="transform" type="translate" values="0 0;{24 if row==0 else -24} 0" dur="1.6s" repeatCount="indefinite"/>'
        for r_ in range(2):
            for c_ in range(-2,40):
                if (r_+c_)%2==0: b+=f'<rect x="{c_*12}" y="{y+r_*12}" width="12" height="12" fill="#fff" opacity=".9"/>'
        b+='</g>'
    b+=shiftlights(30,870,0,28,3)
    b+=txt("PRECISION. SPEED. ITERATION.",450,92,30,"#fff",200,6,"middle")
    b+=f'<rect x="425" y="106" width="50" height="3" fill="{RED}"/>'
    s="EVERY LAP COUNTS . NEVER GIVE UP"; b+=px(s,int(450-tw(s,2)/2),124,2,GR)
    return svg(w,h,b,r=14)

open("assets/banner.svg","w").write(banner())
open("assets/footer.svg","w").write(footer())
open("assets/journey.svg","w").write(journey())
open("assets/offclock.svg","w").write(offclock())
secs=["about","stack","skills","research","projects","experience","achievements","certs","coding","stats","offclock","focus","connect"]
titles=["ABOUT","TECH STACK","AI / ML SKILLS","RESEARCH","PROJECTS","EXPERIENCE","ACHIEVEMENTS","CERTIFICATIONS","CODING","GITHUB STATS","OFF THE CLOCK","CURRENT FOCUS","CONNECT"]
for i,(f,t) in enumerate(zip(secs,titles),1): open(f"assets/h-{f}.svg","w").write(header(i,t,i))
open("assets/m-lurox.svg","w").write(metrics([("0.17 ms","BM25 LATENCY"),("59×","VS DENSE-ONLY"),("p&lt;0.0001","BOOTSTRAP N=10K"),("α 0.2–0.3","OPTIMAL ALPHA")],20))
open("assets/m-overall.svg","w").write(metrics([("~88%","CV ACCURACY"),("~82%","ML ACCURACY"),("40%","ADMIN TIME CUT"),("1,571","DSA PROBLEMS")],40))
