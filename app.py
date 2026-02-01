from flask import Flask, render_template_string

app = Flask(__name__)

# PREMIUM UI/UX TEMPLATE
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Siddhanta Lamsal | Full Stack Developer</title>
    <!-- Premium Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
    <!-- Icons -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    
    <style>
        :root {
            --bg-dark: #0a0a0a;
            --bg-card: rgba(255, 255, 255, 0.05);
            --primary: #00f2ff; /* Cyan Neon */
            --secondary: #7000ff; /* Purple Neon */
            --text-main: #ffffff;
            --text-muted: #a1a1aa;
            --glass-border: 1px solid rgba(255, 255, 255, 0.1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: 'Outfit', sans-serif;
            overflow-x: hidden;
        }

        /* --- BACKGROUND ANIMATION --- */
        #bg-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: radial-gradient(circle at center, #1a1a1a 0%, #000000 100%);
        }

        /* --- NAVIGATION (Glass Effect) --- */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
            backdrop-filter: blur(15px);
            background: rgba(10, 10, 10, 0.7);
            border-bottom: var(--glass-border);
        }

        .logo {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(to right, #fff, var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            cursor: pointer;
        }

        .nav-links {
            display: flex;
            gap: 30px;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-muted);
            font-size: 0.95rem;
            transition: 0.3s;
            position: relative;
        }

        .nav-links a:hover {
            color: var(--primary);
            text-shadow: 0 0 10px rgba(0, 242, 255, 0.5);
        }

        .btn-hire {
            padding: 10px 25px;
            background: transparent;
            border: 1px solid var(--primary);
            color: var(--primary);
            border-radius: 50px;
            text-decoration: none;
            transition: 0.4s;
            font-weight: 600;
        }

        .btn-hire:hover {
            background: var(--primary);
            color: #000;
            box-shadow: 0 0 20px rgba(0, 242, 255, 0.4);
        }

        /* --- HERO SECTION --- */
        .hero {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 0 20px;
            position: relative;
        }

        .hero h2 {
            color: var(--primary);
            font-size: 1.2rem;
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-bottom: 20px;
            animation: fadeInDown 1s ease;
        }

        .hero h1 {
            font-size: 5rem;
            line-height: 1.1;
            margin-bottom: 30px;
            font-family: 'Space Grotesk', sans-serif;
            background: linear-gradient(135deg, #ffffff 0%, #a5a5a5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: fadeInUp 1s ease 0.2s backwards;
        }

        .hero p {
            max-width: 600px;
            color: var(--text-muted);
            font-size: 1.2rem;
            margin-bottom: 40px;
            line-height: 1.8;
            animation: fadeInUp 1s ease 0.4s backwards;
        }

        .hero-btns {
            display: flex;
            gap: 20px;
            animation: fadeInUp 1s ease 0.6s backwards;
        }

        .btn-main {
            padding: 16px 40px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border-radius: 50px;
            color: white;
            text-decoration: none;
            font-weight: 700;
            transition: 0.3s;
            border: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .btn-main:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(112, 0, 255, 0.3);
        }

        /* --- SKILLS GRID --- */
        .section {
            padding: 100px 10%;
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 60px;
            font-family: 'Space Grotesk', sans-serif;
            text-align: center;
        }

        .section-title span {
            color: var(--primary);
        }

        .skills-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 30px;
        }

        .skill-card {
            background: var(--bg-card);
            border: var(--glass-border);
            padding: 40px 20px;
            border-radius: 20px;
            text-align: center;
            transition: 0.4s;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }

        .skill-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
            transform: rotate(45deg);
            transition: 0.6s;
            opacity: 0;
        }

        .skill-card:hover::before {
            opacity: 1;
        }

        .skill-card:hover {
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: 0 0 25px rgba(0, 242, 255, 0.1);
        }

        .skill-card i {
            font-size: 3rem;
            margin-bottom: 20px;
            color: #fff;
        }

        .skill-card h3 {
            font-size: 1.3rem;
            color: #fff;
            margin-bottom: 10px;
        }

        .skill-list {
            color: var(--text-muted);
            font-size: 0.9rem;
            line-height: 1.6;
        }

        /* --- CONTACT SECTION --- */
        .contact-section {
            text-align: center;
            padding: 100px 20px;
            background: linear-gradient(180deg, transparent 0%, rgba(0, 242, 255, 0.05) 100%);
        }

        .glass-box {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.03);
            padding: 60px;
            border-radius: 30px;
            border: var(--glass-border);
            backdrop-filter: blur(20px);
        }

        /* --- FOOTER --- */
        footer {
            padding: 30px;
            text-align: center;
            border-top: var(--glass-border);
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        /* Animations */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Mobile Responsive */
        @media (max-width: 768px) {
            .hero h1 { font-size: 3rem; }
            .nav-links { display: none; }
            .section { padding: 60px 5%; }
        }
    </style>
</head>
<body>

    <!-- Background Animation Canvas -->
    <canvas id="bg-canvas"></canvas>

    <!-- Navigation -->
    <nav>
        <div class="logo">Siddhanta Lamsal</div>
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#skills">Tech Stack</a>
            <a href="#contact">Contact</a>
        </div>
        <a href="https://wa.me/9779769312535" target="_blank" class="btn-hire">Let's Talk</a>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <h2>Full Stack Developer</h2>
        <h1>Code. Create. <br> Innovate.</h1>
        <p>Expert in Python, Java, Node.js & Modern Web Technologies. 
           Building scalable applications from Database to UI.</p>
        
        <div class="hero-btns">
            <a href="https://wa.me/9779769312535" class="btn-main">
                <i class="fab fa-whatsapp"></i> Start Project
            </a>
            <a href="#skills" class="btn-hire" style="color:white; border-color:white;">View Skills</a>
        </div>
    </section>

    <!-- Skills Section -->
    <section class="section" id="skills">
        <h2 class="section-title">My <span>Technical Arsenal</span></h2>
        
        <div class="skills-container">
            
            <!-- Frontend Card -->
            <div class="skill-card">
                <i class="fab fa-html5" style="color: #E34F26;"></i>
                <h3>Web Frontend</h3>
                <div class="skill-list">
                    HTML5 • CSS3 <br>
                    JavaScript • TypeScript <br>
                    XML
                </div>
            </div>

            <!-- Backend Card -->
            <div class="skill-card">
                <i class="fab fa-node-js" style="color: #68A063;"></i>
                <h3>Backend & API</h3>
                <div class="skill-list">
                    Node.js • Python <br>
                    Express • REST APIs
                </div>
            </div>

            <!-- Mobile & Core -->
            <div class="skill-card">
                <i class="fab fa-android" style="color: #3DDC84;"></i>
                <h3>App Development</h3>
                <div class="skill-list">
                    Java • Kotlin <br>
                    Android SDK
                </div>
            </div>

            <!-- Database Card -->
            <div class="skill-card">
                <i class="fas fa-database" style="color: #00f2ff;"></i>
                <h3>Databases</h3>
                <div class="skill-list">
                    MySQL • SQLite <br>
                    MongoDB • Firebase
                </div>
            </div>

        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section" id="contact">
        <div class="glass-box">
            <h2 style="font-size: 2.5rem; margin-bottom: 20px; font-family: 'Space Grotesk';">Ready to Collaborate?</h2>
            <p style="color: #a1a1aa; margin-bottom: 40px;">
                Proficient in the full software lifecycle. Let's build your next big idea using top-tier tech like Java, Python, and Node.js.
            </p>
            <a href="https://wa.me/9779769312535" class="btn-main" style="display: inline-flex; width: auto;">
                <i class="fab fa-whatsapp"></i> Chat on WhatsApp
            </a>
        </div>
    </section>

    <footer>
        <p>&copy; 2024 Siddhanta Lamsal. Powered by Python & Coffee.</p>
    </footer>

    <script>
        // --- PARTICLE ANIMATION LOGIC ---
        const canvas = document.getElementById('bg-canvas');
        const ctx = canvas.getContext('2d');
        
        let width, height;
        let particles = [];

        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }
        
        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.5;
                this.vy = (Math.random() - 0.5) * 0.5;
                this.size = Math.random() * 2;
                this.color = Math.random() > 0.5 ? '#00f2ff' : '#7000ff';
            }
            
            update() {
                this.x += this.vx;
                this.y += this.vy;
                
                if(this.x < 0 || this.x > width) this.vx *= -1;
                if(this.y < 0 || this.y > height) this.vy *= -1;
            }
            
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.globalAlpha = 0.6;
                ctx.fill();
            }
        }

        function init() {
            particles = [];
            for(let i=0; i<80; i++) particles.push(new Particle());
        }

        function animate() {
            ctx.clearRect(0, 0, width, height);
            particles.forEach(p => { p.update(); p.draw(); });
            
            particles.forEach((p1, i) => {
                for(let j=i+1; j<particles.length; j++) {
                    const p2 = particles[j];
                    const dx = p1.x - p2.x;
                    const dy = p1.y - p2.y;
                    const dist = Math.sqrt(dx*dx + dy*dy);
                    if(dist < 100) {
                        ctx.beginPath();
                        ctx.strokeStyle = `rgba(100, 100, 255, ${1 - dist/100})`;
                        ctx.lineWidth = 0.5;
                        ctx.moveTo(p1.x, p1.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.stroke();
                    }
                }
            });
            requestAnimationFrame(animate);
        }

        window.addEventListener('resize', () => { resize(); init(); });
        resize();
        init();
        animate();

        // --- SCROLL REVEAL ---
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    entry.target.style.opacity = 1;
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        });

        document.querySelectorAll('.skill-card').forEach(card => {
            card.style.opacity = 0;
            card.style.transform = 'translateY(50px)';
            card.style.transition = 'all 0.6s ease-out';
            observer.observe(card);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# Vercel requires app to be exposed, but this block is for local testing
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
