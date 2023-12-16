# pylint: disable-all
data = {
    "contact": {
        "name": "Daniela Pistol",
        "mail": "danapistol@flask.com",
        "phone": "+33123456789",
        "location": {
            "address": "2 rue Paradis",
            "postal_code": "75010",
            "city": "Paris",
            "country": "FR",
            "region": "France",
        },
    },
    "languages": [
        {"language": "Romanian", "fluency": "Native Language"},
        {"language": "French", "fluency": "Professional Proficiency"},
        {"language": "English", "fluency": "Professional Proficiency"},
        {"language": "Spanish", "fluency": "Elementary notions"},
    ],
    "experience": [
        {
            "company": "Sewan",
            "position": "Software Engineer",
            "start_date": "2020-10-20",
            "end_date": "",
            "summary": "Integrate Microsoft CSP services (Cloud Solution Provider) in Sewan's information system (SaaS)",
            "contributions": [
                "Implement RESTful APIs using Python, FastAPI in a micro-services architecture, participating in both technical and functional design processes.",
                "Code maintenance, debugging to identify technical issues, bug resolution, refactoring code and integration of performance solutions (caching, multi-threading, algorithm optimization)",
                "Participating in front-end development, ensuring the integration of user interfaces with backend components, using mostly PHP and JavaScript.",
                "Data modeling, data querying using PostgreSQL, SqlAlchemy",
                "Participate in migrating the application from a traditional server-based architecture to serverless technologies based on AWS (Lambda, SQS/SNS, Step Functions) and Terragrunt to define and provision the infrastructure",
                "Unit and integration testing, peer validation processes",
                "Working in a scrum environment, respect of scrum values and delivery deadlines, continuos deployment, CI/CD pipeline creation",
            ],
        },
        {
            "company": "SGSS",
            "position": "Data engineer intern",
            "start_date": "2020-02-20",
            "end_date": "2020-08-20",
            "summary": "Established a relational database for the storage of Request for Proposals (RFPs) information, implementing data analysis techniques to derive key performance indicators (KPIs)",
            "contributions": [
                "Managed the cleaning, organization, synthesis, and efficient modeling of data for storing responses to RFPs into a relational database.",
                "Development of Python scripts for automating data loading and extraction processes. and creation of a NodeJS application to streamline data entry into the database, serving as a user interface for the database information",
            ],
        },
    ],
    "education": [
        {
            "institution": "Télécom Paris - Institut Polytechnique de Paris, France",
            "area": "Data Engineering & AI & Data Science",
            "start_date": "2019-09-01",
            "end_date": "2020-09-01",
        },
        {
            "institution": "Paris-Saclay University, France",
            "area": "Computer Science",
            "start_date": "2015-09-01",
            "end_date": "2019-06-01",
        },
        {
            "institution": "Vasile Alecsandri National College, Romania",
            "area": "Mathematics and Computer Science",
            "start_date": "2011-09-01",
            "end_date": "2015-06-01",
        },
    ],
    "technical_skills": [
        {"name": "Programming Languages", "keywords": ["Python", "Go", "JAVA", "C"]},
        {
            "name": "Web development",
            "keywords": ["FastAPI", "HTML", "CSS", "JavaScript", "PHP"],
        },
        {
            "name": "Databases",
            "keywords": ["PostgreSQL", "MySQL", "SQLAlchemy", "Redis", "MongoDB"],
        },
        {
            "name": "Logging and Analytics",
            "keywords": ["ELK Stack (Elasticsearch, Logstash, Kibana)"],
        },
        {
            "name": "Cloud Computing",
            "keywords": [
                "Amazon Web Services (AWS)",
                "Lambdas",
                "SNS",
                "SQS",
                "Step Functions",
            ],
        },
        {
            "name": "Others",
            "keywords": [
                "Docker",
                "GitLab",
                "Unit/Integration Testing",
                "ML algorithms",
                "RabbitMQ",
                "Collaboration Tools (Jira, Confluence)",
            ],
        },
    ],
    "interests": [
        "photography",
        "travelling and discovering new cultures",
        "logical tests",
    ],
}
