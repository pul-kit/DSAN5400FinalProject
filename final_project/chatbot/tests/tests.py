from chatbot.search_engine.tf_idf_searcher import SearchEngine
searcher = SearchEngine()


def test_onecanvas():
    output = searcher.search("What is Canvas?")
    assert output[0] == "Instructor Getting Started Resources Below are some general questions and answers about Canvas, the Teacher role, and links to resources to help you be comfortable with Canvas. Visit the Instructor Guides to learn more. What is Canvas? Canvas is a Learning Management System. To learn more about Canvas terminology and definitions, visit How does Canvas define the terms used to describe its features and functions?\xa0 Because Canvas is a web-based system, it doesn’t need to be installed on your computer. However, you’ll want to make sure that your computer and web browser meet the basic requirements to run Canvas.\xa0 What is the Instructor/Teacher role? In Canvas, the Teacher role is used to enroll users responsible for course creation, instruction, and management. Teachers are also referred to as instructors in Canvas. In general, users with the Teacher role have permissions that allow them to moderate a course, view course data, and direct daily course communications. However, these permissions may vary among institutions. Canvas for Elementary Canvas for Elementary is a Canvas setting that displays a simplified interface and experience designed for young learners. Your institution may have this enabled for your course(s). Course Structure Resources Additional Resources Flowcharts For a visual representation of how to get started with Canvas as an instructor, view the Getting Started with Canvas as an Instructor Flowchart. For a visual representation of what students can view and access course content, view the Student Course Visibility and Participation Flowchart. Videos To watch a short video series on setting up a new Canvas course, view Set up your Canvas course in 30 minutes or less. Canvas Guides The Canvas Instructor Guide has over 600 articles that each answer a question that relates to using the Canvas interface as an instructor. Each article also includes Next and Previous links so you can easily navigate to related content. Before you can do anything in Canvas, you'll need an account and the URL for your institution's Canvas website. View the articles below for help with setting up your account, logging in, and managing your user settings. Theres a very simple way to log in to the Canvas Teacher app. In the web version of Canvas, if you click the Account link in the Global Navigation menu, you'll see a QR for Mobile Login link. After opening the Canvas Teacher app on your mobile device, scan that code. You will be instantly logged-in, without having to worry about connecting to your school and retyping your information. Canvas has four main areas: Canvas Dashboard, sidebar, Global Navigation menu, and course interface. The articles below show you how to navigate Canvas and use a few of the tools that link across all your courses. Canvas provides several tools that allow you to create a course and add content for your students. View the articles below for information on setting up your Canvas course. Each course includes various features where you can share course content, hold discussions, assign coursework, grade student submissions, and much more. View the articles below for some of the basics of Canvas courses. Learn more about Canvas features in the Canvas Basics Guide. Visit the Canvas Teacher Android Guide or the Canvas Teacher iOS Guide to learn more.\xa0 Canvas also has a free mobile app available for iOS and Android that is specifically tailored to instructors. View information about the Teacher app below. Resource documents offer visualizations of information as well as deep dives into various feature or data areas in Canvas. Below are commonly accessed resource documents.\xa0", "How do I log in to Canvas as an instructor? You can access Canvas through an institution-specific Canvas URL, your school's website, a course invitation email, or the Canvas Teacher iOS app or Canvas Teacher Android app.  You must have an account to log in to Canvas. View troubleshooting steps if you are unable to log in to Canvas. Notes: You can access Canvas through an institution-specific Canvas URL. Canvas URLs use one of the following structures: [your institution's name].instructure.com or canvas.[your institution's name].edu.  You can also locate your institution's Canvas URL using the Canvas Teacher iOS app or Canvas Teacher Android app. Some institution's may also allow access to Canvas via an institution-specific authentication system which redirects to Canvas, such as a school portal or website. Note: Canvas Network and Free-For-Teacher accounts do not follow an institution-specific URL structure. Canvas Network accounts can be accessed at learn.canvas.net. Free-For-Teachers accounts can be accessed at canvas.instructure.com. After locating your institution's Canvas URL, you can log in to your Canvas account. To log in, enter your credentials (or login information) which may display as your email address, username, or login ID [1] and password [2]. Then click the Login link [3]. If needed and depending on your institution's settings, you may be able to reset your password by clicking the Forgot Password link [4]. Note: The Login page may display differently depending on your instititution or if you are logging in via the Canvas Teacher app.  Alternatively, you can navigate to your institution's Canvas instance and log in to the Canvas Teacher app by scanning your Canvas profile QR code from Canvas web.  View QR log in steps for the Canvas Teacher app using an Android or iOS device."
    output = searcher.get_top_docid("What is Canvas?")
    assert output == 24


def test_twocanvas():
    output = searcher.search("What should i do to create an assignment?")
    # print(output[0])
    assert output[0] == "How do I create an assignment? You can create assignments on the Assignments page. You can create an assignment shell, which is a placeholder for an assignment within an assignment group, or you can create an entire assignment with all the assignment details. In Course Navigation, click the Assignments link. If you want to create an assignment placeholder with a title and a date, you can create an assignment shell in an assignment group.  Assignment groups house the different types of assignments you may want to keep in your course, such as assignments, discussions, quizzes, surveys, etc [1]. If you create assignment groups in your course, students can filter their assignments page by assignment type to view the same groups. Learn how to add an assignment group. To create an assignment shell, locate an assignment group and click the Add Assignment button [2]. Assignment shells only include fields for the assignment type, name, due date (optional), and points. You can add assignment details at any time by editing the assignment.  If you want to create an assignment with all assignment details at the same time, click the Add Assignment button.  Assignment details include fields for the assignment type, name, description, points, assignment group (if desired), grade display, and submission type, and due dates. You can also specify if the assignment is a group assignment or requires peer reviews in the assignment details lesson.  When you add details to an assignment, you can also assign the assignment to all students, course sections, course groups, or individual students as part of the Canvas differentiated assignments feature. "
    output = searcher.get_top_docid("What should i do to create an assignment?")
    assert output == 74 

def test_turnitin():
    output = searcher.search("If a student has plagiarized. What should I do?")
    output = (output[0])
    output = (output[0:44])
    assert output  == "How do I know if my student has plagiarized?"
    output = searcher.get_top_docid("If a student has plagiarized. What should I do?")
    assert output == 14


def test_zoom():
    output = searcher.search("why is my virtual background not working?")
    assert output[0:58] == "Why can’t I get virtual background to work on my computer?"
    output = searcher.get_top_docid("why is my virtual background not working?")
    assert output == 792
