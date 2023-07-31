import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")


def preprocess_text(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    return words


def count_keywords(text, keywords):
    # Preprocess the text and keywords
    processed_text = preprocess_text(text)
    processed_keywords = preprocess_text(keywords)

    # Count the occurrences of keywords in the text
    keyword_count = sum(1 for word in processed_text if word in processed_keywords)

    return keyword_count


def find_best_candidate(job_description, candidate_resumes):
    best_candidate = None
    best_score = -1

    for candidate_name, resume in candidate_resumes.items():
        score = count_keywords(resume, job_description)
        if score > best_score:
            best_candidate = candidate_name
            best_score = score

    return best_candidate


if __name__ == "__main__":
    # Job description
    job_description = input("Enter the job description: ")

    # Candidate resumes
    candidate_resumes = {
        "John Doe": "Full-stack developer experienced in Python, Django, JavaScript, and React.",
        "Jane Smith": "Java developer with expertise in Spring Boot and Hibernate.",
        "Bob Johnson": "Front-end developer skilled in HTML, CSS, and JavaScript.",
        "Alice Brown": "Python developer with a focus on data analysis and machine learning.",
        "Michael Lee": "Backend developer experienced in Java and Spring Framework.",
        "Sophia Wilson": "Software engineer with experience in C++ and Linux system programming.",
        "Oliver Martinez": "Web developer proficient in PHP, Laravel, and MySQL.",
        "Emma Taylor": "Mobile app developer with expertise in Android and Kotlin.",
        "William Clark": "Game developer skilled in Unity and C#.",
        "Ava Rodriguez": "Embedded systems developer experienced in C and RTOS.",
        "James Evans": "DevOps engineer with expertise in Docker and Kubernetes.",
        "Emily Hernandez": "Database administrator experienced in SQL and MongoDB.",
        "Ethan Moore": "UI/UX designer with a focus on user-centered design principles.",
        "Madison Garcia": "Quality assurance engineer skilled in automated testing using Selenium.",
        "Olivia Martinez": "Software architect with extensive experience in system design and scalability.",
        "Noah Robinson": "Blockchain developer with expertise in Ethereum and Solidity.",
        "Isabella Stewart": "Cloud engineer experienced in AWS services and serverless architecture.",
        "Liam Murphy": "AR/VR developer with proficiency in Unity and Unreal Engine.",
        "Mia Reed": "Big data engineer skilled in Hadoop and Spark.",
        "Elijah Brooks": "Security analyst experienced in ethical hacking and vulnerability assessments.",
    }

    roles_input = input("Enter the roles you want applicants for (comma-separated): ")
    roles = [role.strip() for role in roles_input.split(",")]

    filtered_candidates = {name: resume for name, resume in candidate_resumes.items() if
                           any(role.lower() in resume.lower() for role in roles)}

    if not filtered_candidates:
        print("No suitable candidates found.")
    else:
        best_candidate = find_best_candidate(job_description, filtered_candidates)
        print("Best Candidate:", best_candidate)
