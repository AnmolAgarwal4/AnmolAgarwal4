import math, random
from pixfont import tw, px
T="#00D2BE"; SV="#cfd4d9"; BG="#07080a"; GR="#8b8b92"
SANS="font-family=\"'Helvetica Neue',Helvetica,Arial,sans-serif\""
W,H=1000,520
rnd=random.Random(11)
def ridge(base,A1,k1,p1,A2,k2,p2,n=250):
    pts=[]
    for i in range(n+1):
        t=i/n
        y=base-A1*(1-abs(math.sin(math.pi*k1*t+p1)))-A2*(1-abs(math.sin(math.pi*k2*t+p2)))
        pts.append((round(t*W,1),round(y,1)))
    return "M"+" L".join(f"{x} {y}" for x,y in pts)
def layer(base,A1,k1,p1,A2,k2,p2,fill,stroke,sop,sw,dur):
    d=ridge(base,A1,k1,p1,A2,k2,p2)
    shape=lambda dx:f'<path transform="translate({dx},0)" d="{d} L{W} 430 L0 430Z" fill="{fill}" stroke="{stroke}" stroke-opacity="{sop}" stroke-width="{sw}" stroke-linejoin="round"/>'
    return f'<g><animateTransform attributeName="transform" type="translate" from="0 0" to="-{W} 0" dur="{dur}s" repeatCount="indefinite"/>{shape(0)}{shape(W)}</g>'
def wheel(cx,cy,r):
    sp="".join(f'<line x1="0" y1="0" x2="{r*.5*math.cos(a*math.pi/3):.1f}" y2="{r*.5*math.sin(a*math.pi/3):.1f}" stroke="{SV}" stroke-width="2"/>' for a in range(6))
    return (f'<g transform="translate({cx},{cy})"><circle r="{r}" fill="#0e0e10" stroke="#2b2b2f" stroke-width="2"/>'
            f'<circle r="{r-5}" fill="none" stroke="{T}" stroke-width="1.2" opacity=".85"/>'
            f'<circle r="{r*.58:.1f}" fill="#16171a" stroke="#9aa1a8"/><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur=".28s" repeatCount="indefinite"/>{sp}'
            f'<rect x="{r*.4:.1f}" y="-2" width="5" height="4" fill="{T}"/><circle r="3" fill="{SV}"/></g></g>')
def car():
    c=f'<ellipse cx="0" cy="-3" rx="150" ry="5" fill="{T}" opacity=".55" filter="url(#bl)"/>'
    c+=f'<path d="M152 -19 L134 -24 L96 -27 L58 -31 L36 -33 L20 -39 L-6 -43 L-24 -53 L-44 -50 L-62 -42 L-112 -36 L-124 -31 L-122 -20 L-100 -15 L100 -15 L136 -15Z" fill="url(#sv)"/>'
    c+=f'<path d="M-98 -23 L-8 -31 L34 -30 L34 -24 L-98 -17Z" fill="{T}"/><rect x="-125" y="-15" width="262" height="3" fill="#18191b"/>'
    c+=f'<path d="M24 -39 C22 -57 -4 -57 -8 -45" fill="none" stroke="{SV}" stroke-width="2.6"/><path d="M24 -39 L44 -32" stroke="{SV}" stroke-width="2.6"/>'
    c+=f'<circle cx="8" cy="-45" r="5.5" fill="{T}"/><rect x="9" y="-47" width="5" height="3" fill="#0b0b0c"/>'
    c+=f'<rect x="-136" y="-64" width="30" height="4" fill="#1d1f22" stroke="{SV}" stroke-width=".6"/><rect x="-136" y="-58" width="28" height="3" fill="{T}"/><rect x="-138" y="-68" width="3" height="26" fill="{SV}"/><line x1="-118" y1="-60" x2="-116" y2="-34" stroke="#888" stroke-width="2"/>'
    c+=f'<line x1="146" y1="-19" x2="146" y2="-10" stroke="#888" stroke-width="2"/><rect x="128" y="-10" width="34" height="3" fill="#1d1f22"/><rect x="132" y="-13" width="28" height="2" fill="{T}"/><rect x="160" y="-17" width="3" height="12" fill="{SV}"/>'
    c+=wheel(-86,-28,28)+wheel(92,-25,25)
    for i in range(7):
        y=rnd.uniform(-14,-2); d=rnd.uniform(.25,.5); b=rnd.uniform(0,.5)
        c+=(f'<rect x="-128" y="{y:.1f}" width="{rnd.choice([3,4,5])}" height="2" fill="{rnd.choice([T,"#fff"])}"><animateTransform attributeName="transform" type="translate" values="0 0;-{rnd.randint(70,130)} {rnd.randint(2,12)}" dur="{d:.2f}s" begin="-{b:.2f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="1;0" dur="{d:.2f}s" begin="-{b:.2f}s" repeatCount="indefinite"/></rect>')
    return (f'<g transform="translate(430,410) scale(1.35)"><g><animateTransform attributeName="transform" type="translate" values="0 0;0 -.9;0 0;0 .5;0 0" dur=".3s" repeatCount="indefinite"/>{c}</g></g>')
def lights():
    b='<rect x="682" y="22" width="240" height="44" rx="10" fill="#0b0b0c" stroke="#fff" stroke-opacity=".18"/>'
    for i in range(5):
        on=(0.6+0.7*i)/9; off=5.4/9
        b+=(f'<circle cx="{714+i*48}" cy="44" r="11" fill="{T}" opacity=".12"><animate attributeName="opacity" values=".12;.12;1;1;.12;.12" keyTimes="0;{on:.4f};{on+.004:.4f};{off:.4f};{off+.004:.4f};1" dur="9s" repeatCount="indefinite"/></circle>')
    b+=f'<g opacity="0">{px("LIGHTS OUT",922-tw("LIGHTS OUT",2),78,2,T)}<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{5.4/9:.4f};{5.45/9:.4f};{7.2/9:.4f};{7.25/9:.4f};1" dur="9s" repeatCount="indefinite"/></g>'
    return b
def hud():
    b='<rect x="40" y="436" width="300" height="70" rx="12" fill="#0b0c0e"/><rect x="40" y="436" width="300" height="70" rx="12" fill="#fff" fill-opacity=".05" stroke="#fff" stroke-opacity=".18"/>'
    N=16; ramp=7.0; dur=8.0
    for k in range(N):
        v=round(318*(1-(1-(k+1)/N)**2)); g=min(8,1+k//2)
        t0=k*ramp/N/dur; t1=(k+1)*ramp/N/dur if k<N-1 else 1.0
        kt=f"0;{t0:.4f};{t1:.4f}" if k else f"0;{t1:.4f}"
        vals="hidden;visible;hidden" if k else "visible;hidden"
        if k==N-1: kt=f"0;{t0:.4f}"; vals="hidden;visible"
        b+=(f'<g visibility="hidden"><animate attributeName="visibility" calcMode="discrete" values="{vals}" keyTimes="{kt}" dur="{dur}s" repeatCount="indefinite"/>'
            f'<text x="58" y="486" {SANS} font-size="42" font-weight="200" fill="#fff">{v}</text><text x="298" y="486" {SANS} font-size="34" font-weight="300" fill="{T}" text-anchor="middle">{g}</text></g>')
    b+=px("KM/H",150,470,2,GR)+px("GEAR",278,452,2,GR)
    for i in range(15):
        t=(i+1)/15*ramp/dur
        b+=f'<rect x="{40+i*20}" y="420" width="16" height="5" rx="1" fill="{T}" opacity=".12"><animate attributeName="opacity" values=".12;.12;1;1" keyTimes="0;{t-.001:.4f};{t:.4f};1" dur="{dur}s" repeatCount="indefinite"/></rect>'
    # telemetry traces
    pts=[];x=0;hi=True
    while x<320:
        seg=rnd.randint(14,40); y=444 if hi else 486
        pts+= [(x,y),(x+seg,y)]; x+=seg; hi=not hi
    dd="M"+" L".join(f"{a} {b_}" for a,b_ in pts)
    b+='<rect x="640" y="436" width="320" height="70" rx="12" fill="#0b0c0e"/><rect x="640" y="436" width="320" height="70" rx="12" fill="#fff" fill-opacity=".05" stroke="#fff" stroke-opacity=".18"/><clipPath id="tc"><rect x="640" y="436" width="320" height="70"/></clipPath>'
    b+=f'<g clip-path="url(#tc)"><g><animateTransform attributeName="transform" type="translate" from="640 0" to="320 0" dur="4s" repeatCount="indefinite"/><path d="{dd}" fill="none" stroke="{T}" stroke-width="1.8"/><path transform="translate(320,0)" d="{dd}" fill="none" stroke="{T}" stroke-width="1.8"/></g></g>'
    b+=px("THROTTLE",650,442,1,GR)+f'<circle cx="940" cy="446" r="3" fill="{T}"><animate attributeName="opacity" values="1;.1;1" dur="1s" repeatCount="indefinite"/></circle>'
    return b
def hero():
    b=f'''<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#040506"/><stop offset=".7" stop-color="#0a1517"/><stop offset="1" stop-color="#0d2326"/></linearGradient>
<linearGradient id="sv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f6f8"/><stop offset="1" stop-color="#8f969d"/></linearGradient>
<radialGradient id="mn" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#b9c4c8"/></radialGradient>
<filter id="bl" x="-50%" y="-200%" width="200%" height="500%"><feGaussianBlur stdDeviation="8"/></filter></defs>
<clipPath id="cp"><rect width="{W}" height="{H}" rx="20"/></clipPath><clipPath id="rv"><rect x="40" y="70" width="0" height="110"><animate attributeName="width" from="0" to="700" dur="1.6s" begin=".3s" fill="freeze"/></rect></clipPath>
<g clip-path="url(#cp)"><rect width="{W}" height="{H}" fill="url(#sky)"/>'''
    for _ in range(45):
        x=rnd.randrange(0,1000,4); y=rnd.randrange(0,300,4); s=rnd.choice([2,2,3])
        b+=f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="#fff" opacity=".3"><animate attributeName="opacity" values=".1;.8;.1" dur="{rnd.randint(2,6)}s" begin="-{rnd.random()*3:.1f}s" repeatCount="indefinite"/></rect>'
    b+=f'<circle cx="800" cy="160" r="90" fill="{T}" opacity=".35" filter="url(#bl)"/><circle cx="800" cy="160" r="54" fill="url(#mn)"/><circle cx="800" cy="160" r="70" fill="none" stroke="{T}" stroke-opacity=".5"/><circle cx="800" cy="160" r="96" fill="none" stroke="#fff" stroke-opacity=".08"/>'
    b+=f'<ellipse cx="500" cy="345" rx="620" ry="50" fill="{T}" opacity=".16" filter="url(#bl)"/>'
    b+=layer(345,110,3,.4,40,8,1.2,"#0d1214",T,.3,1.2,70)
    b+=layer(378,92,4,1.1,34,11,.3,"#0a0d0f",SV,.3,1.2,34)
    b+=layer(404,70,6,.2,24,15,2.0,"#070809","#ffffff",.65,1.4,15)
    # road
    b+=f'<rect y="410" width="{W}" height="{H-410}" fill="#0b0c0e"/><rect y="410" width="{W}" height="1.5" fill="#fff" opacity=".25"/>'
    b+=f'<g><animateTransform attributeName="transform" type="translate" from="0 0" to="-48 0" dur=".3s" repeatCount="indefinite"/>'+"".join(f'<rect x="{i*24-48}" y="411" width="24" height="7" fill="{T if i%2 else "#fff"}" opacity=".85"/>' for i in range(46))+'</g>'
    b+=f'<path d="M0 520 H1100" stroke="#fff" stroke-opacity="0"/><path d="M0 512 H1100" stroke="#fff" stroke-opacity=".0"/>'
    b+=f'<path d="M0 424 H1100" stroke="#fff" stroke-opacity=".12"/>'
    b+=f'<ellipse cx="430" cy="413" rx="215" ry="7" fill="#000" opacity=".7"/>'
    # speed streaks
    for _ in range(16):
        y=rnd.randint(285,408); L=rnd.randint(60,190); d=rnd.uniform(.45,1.3); c=rnd.choice(["#fff",T,"#fff"])
        b+=f'<rect x="0" y="0" width="{L}" height="1.6" fill="{c}" opacity="{rnd.uniform(.12,.3):.2f}"><animateTransform attributeName="transform" type="translate" from="1100 {y}" to="-300 {y}" dur="{d:.2f}s" begin="-{rnd.random()*d:.2f}s" repeatCount="indefinite"/></rect>'
    b+=car()
    # center dashes in front
    b+=f'<path d="M0 478 H1100" stroke="#fff" stroke-opacity=".28" stroke-width="3" stroke-dasharray="46 46"><animate attributeName="stroke-dashoffset" from="0" to="-92" dur=".45s" repeatCount="indefinite"/></path>'
    b+=hud()+lights()
    # name
    b+=f'<g clip-path="url(#rv)"><text x="56" y="132" {SANS} font-size="58" font-weight="200" letter-spacing="7" fill="#fff">ANMOL AGARWAL</text></g>'
    b+=f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur=".7s" begin="1.7s" fill="freeze"/><rect x="58" y="146" width="56" height="3" fill="{T}"/>{px("AI / ML ENGINEER . FULL-STACK DEVELOPER",58,168,2,"#e4e7ea")}{px("RAG . LLMS . COMPUTER VISION . SYSTEMS IN C",58,188,2,GR)}</g>'
    b+=f'<circle cx="62" cy="46" r="4" fill="{T}"><animate attributeName="opacity" values="1;.15;1" dur="1.2s" repeatCount="indefinite"/></circle>'+px("LIVE TELEMETRY",76,41,2,"#fff")
    b+='</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{b}</svg>'
open("assets/banner.svg","w").write(hero())
