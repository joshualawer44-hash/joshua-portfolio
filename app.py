
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Joshua Opata | Portfolio</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: #07111f;
            color: white;
            line-height: 1.7;
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 22px 8%;
            background: #0c1b2d;
        }

        nav h2 {
            color: #00e5ff;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 20px;
        }

        .hero {
            min-height: 75vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 70px 10%;
        }

        .hero h1 {
            font-size: 52px;
            margin-bottom: 10px;
        }

        .hero h1 span {
            color: #00e5ff;
        }

        .hero h3 {
            color: #00e5ff;
            margin-bottom: 20px;
        }

        .hero p {
            max-width: 600px;
            color: #c3d0df;
        }

        .btn {
            display: inline-block;
            background: #00e5ff;
            color: #07111f;
            padding: 12px 25px;
            margin-top: 25px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: bold;
            width: fit-content;
        }

        section {
            padding: 65px 10%;
        }

        section h2 {
            color: #00e5ff;
            margin-bottom: 20px;
            font-size: 30px;
        }

        .card {
            background: #102238;
            padding: 25px;
            margin: 15px 0;
            border-radius: 10px;
            border: 1px solid #193650;
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .skills span {
            background: #102d43;
            padding: 12px 20px;
            border-radius: 6px;
            color: #00e5ff;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #0c1b2d;
            color: #9aafc3;
        }

        @media(max-width: 600px) {
            nav {
                flex-direction: column;
                gap: 12px;
            }

            nav a {
                margin: 5px;
            }

            .hero h1 {
                font-size: 36px;
            }
        }
    </style>
</head>

<body>

    <nav>
        <h2>JO.</h2>
        <div>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    <div class="hero">
        <h3>WELCOME TO MY PORTFOLIO</h3>
        <h1>I'm <span>Joshua Opata</span></h1>
        <h3>Aspiring Python Developer & Cybersecurity Enthusiast</h3>
        <p>
            I am passionate about technology, programming,
            cybersecurity and continuous learning.
            I am building my skills one project at a time.
        </p>
        <a href="#about" class="btn">Explore My Portfolio</a>
    </div>

    <section id="about">
        <h2>About Me</h2>
        <div class="card">
            <p>
                My name is Joshua Opata. I am an enthusiastic
                technology learner with an interest in Python
                programming, cybersecurity and ethical hacking.
                I enjoy exploring technology and developing
                practical skills through hands-on projects.
            </p>
        </div>
    </section>

    <section id="skills">
        <h2>My Skills & Learning Areas</h2>
        <div class="skills">
            <span>Python</span>
            <span>Cybersecurity</span>
            <span>Ethical Hacking</span>
            <span>Computer Networking</span>
            <span>Problem Solving</span>
            <span>Technology</span>
        </div>
    </section>

    <section id="projects">
        <h2>My Projects</h2>
        <div class="card">
            <h3>Personal Portfolio Website</h3>
            <p>
                A personal website built using Python and Flask
                to showcase my skills and learning journey.
            </p>
        </div>
        <div class="card">
            <h3>More Projects Coming Soon</h3>
            <p>
                I am continuously learning and working on
                new technology projects.
            </p>
        </div>
    </section>

    <section id="contact">
        <h2>Contact Me</h2>
        <div class="card">
            <p>Interested in connecting or collaborating?</p>
            <p>Email: Add your email address here.</p>
        </div>
    </section>

    <footer>
        <p>© 2026 Joshua Opata | Personal Portfolio</p>
    </footer>

</body>
</html>
    """)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
