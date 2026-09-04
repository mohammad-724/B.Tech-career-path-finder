from flask import Flask, render_template, abort

app = Flask(__name__)

BRANCHES = {
    "ECE": {
        "name": "Electronics & Communication Engineering",
        "short": "ECE",
        "icon": "◈",
        "description": "Explore careers spanning embedded systems, IoT, VLSI, wireless communication and software.",
        "careers": [
            {
                "slug": "embedded-systems-engineer",
                "title": "Embedded Systems Engineer",
                "tag": "Hardware + Software",
                "objective": "Design, develop and test embedded products by combining microcontrollers, electronics and software.",
                "skills": ["C", "C++", "Python", "Microcontrollers", "RTOS", "Communication Protocols"],
                "tools": ["Arduino IDE", "Keil", "VS Code", "STM32CubeIDE"],
                "roadmap": ["Master C and embedded C", "Learn microcontrollers", "Practice UART, SPI and I2C", "Learn RTOS fundamentals", "Build 3 practical projects"],
                "level": "Beginner → Advanced"
            },
            {
                "slug": "iot-engineer",
                "title": "IoT Engineer",
                "tag": "Connected Devices",
                "objective": "Build connected devices that sense, process and exchange data between physical systems and cloud platforms.",
                "skills": ["Python", "Embedded C", "Sensors", "MQTT", "Networking", "Cloud Basics"],
                "tools": ["ESP32", "Arduino", "Blynk", "Node-RED"],
                "roadmap": ["Learn sensors and microcontrollers", "Learn networking basics", "Build MQTT projects", "Connect devices to cloud", "Create a complete IoT system"],
                "level": "Beginner → Advanced"
            },
            {
                "slug": "pcb-design-engineer",
                "title": "PCB Design Engineer",
                "tag": "Electronics Hardware",
                "objective": "Design reliable printed circuit boards by converting electronic schematics into production-ready layouts.",
                "skills": ["Circuit Design", "Schematic Capture", "PCB Layout", "Signal Integrity", "Electronics"],
                "tools": ["KiCad", "Altium Designer", "Cadence", "EAGLE"],
                "roadmap": ["Revise circuit fundamentals", "Learn schematic design", "Learn PCB layout", "Practice DRC and BOM", "Design complete boards"],
                "level": "Beginner → Advanced"
            },
            {
                "slug": "vlsi-engineer",
                "title": "VLSI Engineer",
                "tag": "Semiconductor",
                "objective": "Design, verify and optimize digital hardware used in modern integrated circuits.",
                "skills": ["Digital Electronics", "Verilog", "RTL Design", "Computer Architecture", "Verification"],
                "tools": ["Vivado", "ModelSim", "Cadence", "Questa"],
                "roadmap": ["Master digital electronics", "Learn Verilog", "Practice RTL design", "Learn verification", "Build FPGA projects"],
                "level": "Intermediate → Advanced"
            },
            {
                "slug": "wireless-network-engineer",
                "title": "Wireless & Network Engineer",
                "tag": "Networking + RF",
                "objective": "Design, configure, test and troubleshoot communication networks and wireless systems.",
                "skills": ["Computer Networks", "Wi-Fi", "TCP/IP", "Wireless Communication", "Troubleshooting"],
                "tools": ["Wireshark", "Cisco Packet Tracer", "Linux", "Network Simulators"],
                "roadmap": ["Learn OSI and TCP/IP", "Understand Wi-Fi", "Practice subnetting", "Use packet analysis tools", "Build network labs"],
                "level": "Beginner → Advanced"
            }
        ]
    },

    "CSE": {
        "name": "Computer Science & Engineering",
        "short": "CSE",
        "icon": "</>",
        "description": "Explore software, web development, data, cloud and artificial intelligence careers.",
        "careers": [
            {
                "slug": "software-developer",
                "title": "Software Developer",
                "tag": "Software",
                "objective": "Design, develop, test and maintain software applications that solve real-world problems.",
                "skills": ["Python", "Java", "C++", "Data Structures", "SQL", "Git"],
                "tools": ["VS Code", "GitHub", "Docker", "Postman"],
                "roadmap": ["Choose a programming language", "Master data structures", "Learn Git", "Build projects", "Practice coding interviews"],
                "level": "Beginner → Advanced"
            },
            {
                "slug": "full-stack-developer",
                "title": "Full Stack Developer",
                "tag": "Web Development",
                "objective": "Build complete web applications by working across user interfaces, APIs, backend systems and databases.",
                "skills": ["HTML", "CSS", "JavaScript", "Python", "Flask", "SQL"],
                "tools": ["VS Code", "GitHub", "Flask", "Postman"],
                "roadmap": ["Learn HTML and CSS", "Learn JavaScript", "Build Flask APIs", "Learn SQL", "Deploy a full-stack project"],
                "level": "Beginner → Advanced"
            },
            {
                "slug": "data-analyst",
                "title": "Data Analyst",
                "tag": "Data + Business",
                "objective": "Transform raw data into useful insights, dashboards and recommendations that support decisions.",
                "skills": ["Python", "SQL", "Excel", "Statistics", "Data Visualization"],
                "tools": ["Power BI", "Pandas", "NumPy", "Excel"],
                "roadmap": ["Learn Excel", "Master SQL", "Learn Python data analysis", "Build dashboards", "Create a portfolio"],
                "level": "Beginner → Advanced"
            },
            {
                "slug": "ai-ml-engineer",
                "title": "AI / ML Engineer",
                "tag": "Artificial Intelligence",
                "objective": "Develop intelligent applications using machine learning, data and artificial intelligence techniques.",
                "skills": ["Python", "Machine Learning", "Statistics", "Data Processing", "Deep Learning"],
                "tools": ["Google Colab", "Scikit-learn", "TensorFlow", "Jupyter"],
                "roadmap": ["Learn Python", "Learn statistics", "Study ML algorithms", "Build ML projects", "Explore deep learning"],
                "level": "Intermediate → Advanced"
            },
            {
                "slug": "cloud-engineer",
                "title": "Cloud Engineer",
                "tag": "Cloud Computing",
                "objective": "Deploy, manage and optimize applications and infrastructure on modern cloud platforms.",
                "skills": ["Linux", "Networking", "Cloud Fundamentals", "Python", "DevOps Basics"],
                "tools": ["AWS", "Docker", "GitHub", "Linux"],
                "roadmap": ["Learn Linux", "Learn networking", "Study cloud fundamentals", "Practice deployment", "Build cloud projects"],
                "level": "Beginner → Advanced"
            }
        ]
    },

    "EEE": {
        "name": "Electrical & Electronics Engineering",
        "short": "EEE",
        "icon": "⚡",
        "description": "Explore power, automation, control, electrical design and industrial technology careers.",
        "careers": [
            {
                "slug": "automation-engineer",
                "title": "Automation Engineer",
                "tag": "Industrial Automation",
                "objective": "Develop automated industrial systems using PLCs, sensors, controllers and industrial communication.",
                "skills": ["PLC", "Control Systems", "Sensors", "Automation", "Industrial Communication"],
                "tools": ["TIA Portal", "Factory I/O", "MATLAB", "PLC Software"],
                "roadmap": ["Learn control basics", "Learn PLC programming", "Practice sensors", "Study industrial networks", "Build automation projects"],
                "level": "Beginner → Advanced"
            },
            {
                "slug": "electrical-design-engineer",
                "title": "Electrical Design Engineer",
                "tag": "Electrical Design",
                "objective": "Design electrical systems and components while meeting performance, safety and engineering requirements.",
                "skills": ["Electrical Circuits", "Electrical Machines", "AutoCAD", "Power Systems"],
                "tools": ["AutoCAD", "MATLAB", "ETAP"],
                "roadmap": ["Revise circuit theory", "Learn electrical CAD", "Study protection", "Practice design calculations", "Create design projects"],
                "level": "Beginner → Advanced"
            },
            {
                "slug": "control-systems-engineer",
                "title": "Control Systems Engineer",
                "tag": "Controls",
                "objective": "Analyze and develop control systems used in industrial machines, robotics and automated processes.",
                "skills": ["Control Systems", "MATLAB", "Sensors", "PLC", "Instrumentation"],
                "tools": ["MATLAB", "Simulink", "TIA Portal"],
                "roadmap": ["Learn control theory", "Practice MATLAB", "Study instrumentation", "Learn PLCs", "Build control projects"],
                "level": "Intermediate → Advanced"
            }
        ]
    },

    "MECH": {
        "name": "Mechanical Engineering",
        "short": "MECH",
        "icon": "⚙",
        "description": "Explore mechanical design, manufacturing, automation and robotics-oriented careers.",
        "careers": [
            {
                "slug": "mechanical-design-engineer",
                "title": "Mechanical Design Engineer",
                "tag": "CAD + Design",
                "objective": "Design and develop mechanical components and products using engineering principles and CAD tools.",
                "skills": ["CAD", "Engineering Drawing", "Materials", "Manufacturing", "3D Modelling"],
                "tools": ["AutoCAD", "SolidWorks", "CATIA"],
                "roadmap": ["Master engineering drawing", "Learn 2D CAD", "Learn 3D modelling", "Study GD&T", "Create a design portfolio"],
                "level": "Beginner → Advanced"
            },
            {
                "slug": "robotics-automation-engineer",
                "title": "Robotics & Automation Engineer",
                "tag": "Robotics",
                "objective": "Combine mechanical, electronic and software technologies to design automated robotic systems.",
                "skills": ["Robotics", "CAD", "Sensors", "Control Systems", "Programming"],
                "tools": ["ROS", "SolidWorks", "Arduino", "MATLAB"],
                "roadmap": ["Learn robotics basics", "Study sensors and actuators", "Learn CAD", "Practice robot programming", "Build an autonomous project"],
                "level": "Intermediate → Advanced"
            },
            {
                "slug": "manufacturing-engineer",
                "title": "Manufacturing Engineer",
                "tag": "Production",
                "objective": "Improve manufacturing processes, production efficiency, quality and reliability.",
                "skills": ["Manufacturing Processes", "Quality", "CAD", "Process Improvement"],
                "tools": ["AutoCAD", "SolidWorks", "Excel"],
                "roadmap": ["Understand manufacturing processes", "Learn quality methods", "Study CAD", "Practice process analysis", "Build a production case study"],
                "level": "Beginner → Advanced"
            }
        ]
    }
}


def get_branch(branch_code):
    return BRANCHES.get(branch_code.upper())


@app.route("/")
def home():
    return render_template("index.html", branches=BRANCHES)


@app.route("/branch/<branch_code>")
def branch_page(branch_code):
    branch = get_branch(branch_code)

    if not branch:
        abort(404)

    return render_template("branch.html", branch=branch)


@app.route("/branch/<branch_code>/careers")
def careers_page(branch_code):
    branch = get_branch(branch_code)

    if not branch:
        abort(404)

    return render_template("careers.html", branch=branch)


@app.route("/branch/<branch_code>/career/<career_slug>")
def career_page(branch_code, career_slug):
    branch = get_branch(branch_code)

    if not branch:
        abort(404)

    career = next(
        (item for item in branch["careers"] if item["slug"] == career_slug),
        None
    )

    if not career:
        abort(404)

    return render_template(
        "career.html",
        branch=branch,
        career=career
    )


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)