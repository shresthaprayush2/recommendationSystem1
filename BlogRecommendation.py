
blogs = {
    1: "Beginner’s Guide to IT Careers",
    2: "How to Start Your IT Journey (Even If You’re a Beginner)",
    3: "Why Practical Skills Matter (And How to Build Them)",
    4: "Certifications vs. Experience: What Employers Really Want",
    5: "How to Afford IT Training Without Breaking the Bank",
    6: "Top Mistakes to Avoid When Starting Your IT Career",
    7: "A Day in the Life of an IT Professional",
    8: "The Ultimate Roadmap for Your First IT Job",
    9: "How to Make Time for Learning IT Skills (Even with a Busy Schedule)",
    10: "How to Impress Recruiters as a Fresh Graduate",
    11: "Youtube Learning VS Self Learning"
}
education =""
area =""
learning_method=""
challenge=""
preference=""
factor=""

questionOptions = {
    "education": {
        0:"Where are you in your education journey?",
        1: "High school graduate",
        2: "Pursuing a Bachelor’s degree",
        3: "Completed Bachelor’s degree",
        4: "Other (please specify)"
    },
    "area": {
        0: "What’s your area of study or interest?",
        1: "IT/Computer Science",
        2: "Engineering (non-IT)",
        3: "Business/Management",
        4: "Other (please specify)"
    },
    "learning_method": {
        0:"How are you currently learning IT skills?",
        1: "College/university courses",
        2: "Online platforms like YouTube or Udemy",
        3: "Personal projects and self-study",
        4: "I haven’t started yet (that’s okay!)"
    },
    "challenge": {
        0:"What’s the biggest challenge you face when learning IT skills?",
        1: "Lack of practical, hands-on training",
        2: "Courses feel too theoretical or outdated",
        3: "Not knowing where to start or what to focus on",
        4: "Staying motivated and consistent"
    },
    "worry": {
        0:"What worries you the most about starting your IT career?",
        1: "Not having enough real-world experience",
        2: "Not knowing what employers are looking for",
        3: "Competing with more skilled candidates",
        4: "Finding affordable training and opportunities"
    },
    "preference": {
        0:"What type of learning works best for you?",
        1: "Hands-on classes with a mentor",
        2: "Flexible online lessons",
        3: "A combination of in-person and online training",
        4: "Self-study with structured materials and clear goals"
    },
    "factor": {
        0:"What factors would make you choose an IT training program?",
        1: "Affordable pricing or scholarships",
        2: "Guaranteed internship or job placement",
        3: "Practical, project-based learning",
        4: "Success stories from people like me"
    }
}


def recommend_blogs(userResponse):
    for key, value in userResponse.items():
        globals()[key] = value
    recommendations = []
    #Map responses to blogs
    if education in ["High school graduate", "Other"]:
        recommendations.append(2)
    elif education in ["Pursuing a Bachelor’s degree", "Completed Bachelor’s degree"]:
        recommendations.append(4)

    if area in ["IT/Computer Science"]:
        recommendations.append(3)
    elif area in ["Engineering (non-IT)", "Business/Management"]:
        recommendations.append(1)
    elif area == "Other":
        recommendations.append(2)

    if learning_method in ["College/university courses"]:
        recommendations.append(6)
    elif learning_method in ["Online platforms like YouTube or Udemy", "Personal projects and self-study"]:
        recommendations.append(3)
    elif learning_method == "I haven’t started yet":
        recommendations.append(2)

    if challenge in ["Lack of practical, hands-on training", "Courses feel too theoretical or outdated"]:
        recommendations.append(3)
    elif challenge == "Not knowing where to start or what to focus on":
        recommendations.append(2)
    elif challenge == "Staying motivated and consistent":
        recommendations.append(9)

    if preference in ["Hands-on classes with a mentor", "Practical, project-based learning"]:
        recommendations.append(3)
    elif preference in ["Flexible online lessons", "Self-study with structured materials and clear goals"]:
        recommendations.append(2)
    elif preference == "A combination of in-person and online training":
        recommendations.append(7)

    if factor in ["Affordable pricing or scholarships"]:
        recommendations.append(5)
    elif factor in ["Guaranteed internship or job placement"]:
        recommendations.append(8)
    elif factor in ["Practical, project-based learning"]:
        recommendations.append(3)

    return list(set(recommendations))  # Remove duplicates


# Generate questions
def askQuestions(qustionOptions):
    answers = {
        "education": "",
        "area": "",
        "learning_method": "",
        "challenge": "",
        "worry": "",
        "preference": "",
        "factor": ""
    }

    print("Please Answer The Following Questions , Enter the option number for you answer ")
    for key,values in qustionOptions.items():
        print(values[0])
        for x in range(1,5):
            print(f'{x} : {values[x]}')
        userAnswer = int(input("> "))
        if(userAnswer<=0 and userAnswer>=4):
            print("Invalid Options")
            return
        answers[key] = values[userAnswer]

    return answers;

userResponse = askQuestions(questionOptions)
print(userResponse)


# Get recommendations
recommended_blogs = recommend_blogs(userResponse)
# Display recommended blogs
print("Recommended Blogs:")
for blog_id in recommended_blogs:
    print(f"- {blogs[blog_id]}")


