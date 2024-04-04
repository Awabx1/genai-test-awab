1. Summarizer Task
Used PDF libraries to load doc. Using 10k tokens in a chunk. Using chucks in Map Reduce which is a technique in langchain. Apparently its better than stuffing and easier to implement than refining. It will give me small summaries of small chunks which I can then combine

Summaries are generated like:
    Summary #0
    Summary #1...



2. Prompt Engineering Task

For this task, I chose gpt-4 model for higher accuracy, a temp of 1.0 to make it factual and no limit on the number of output tokens. My approach here was defining a prompt template that I had tested on Playground first. The prompt works perfectly. Next was the task of automating it. Since the link I was given was empty, I generated some dummy data using chatGPT and added it in a JSON format 'student.json'. By iterating through the json document in my code, I extracted and changed the prompt placeholders with the required field. The outputs were consistent and thorough. 


The outputs generated using the students.json file is:


    Study plan for  Mia Thompson
    1. Mia Thompson is a second-year student majoring in Computer Science. Her current studies include subjects such as Programming Fundamentals, Data Structures, Computer Networks, and Discrete Mathematics. She is a visual learner who also benefits from hands-on experience. She has two primary academic goals: enhancing her programming skills and mastering data structures and algorithms. In addition to her studies, she participates in a Coding Club and is a member of the Basketball Team.

    2. Yes, her participation in the Coding Club definitely aligns with her field of study and will help enhance her programming skills. Even though the basketball team does not directly relate to her studies, it is excellent for her overall wellbeing, mental health, and team building skills.

    3. Study plan: Mia should aim to study for 4-5 hours each day. She could allocate 2 hours for Programming Fundamentals and Data Structures, considering her objective to improve in these areas. Computer Networks and Discrete Mathematics can be allocated an hour each. After studies, she can spend time on extracurricular activities. About 1 to 2 hours for the Coding Club twice a week and Basketball practices and matches can be done three times a week.

    4. Mia can improve by continually practicing her programming skills outside school hours. Online platforms provide an excellent opportunity for this. She can consider pair programming to improve her teamwork skills. Furthermore, she can leverage the Coding Club to explore real-life applications and even start a small project with her peers. Time-management will be crucial for her, balancing studies, and extracurricular activities. Doing physical exercise and activities like basketball will help her keep herself mentally agile and physically fit.

    Study plan for  Alex Johnson
    1. Alex Johnson, a third year Mechanical Engineering student, is a dedicated and active scholar with unique learning preferences for Kinesthetic and Auditory styles. Notably, Alex is juggling between his extracurricular activities - the Robotics Team and volunteering at Engineering Workshops, and his aim to design a functional prototype for a sustainable energy solution. Besides this, he aims to maintain a GPA of 3.5.

    2. His extracurricular activities align perfectly with his field of Mechanical Engineering. Both the Robotics team and volunteering at Engineering Workshops can serve as practical platforms which will enhance Alex's hands-on experience and complement his academic learning. 

    3. For Alex to manage his time effectively, he should devote at least 3 hours daily to his studies, which can be broken into 1.5 hours revise and 1.5 hours for hands-on practice to reinforce concepts he learns from the lectures. Alongside, he should devote about 8-10 hours per week to his extracurricular activities. Consistent contribution in these activities can aid him to understand his studies better and equally help in his project to design a sustainable energy solution.

    4. Alex can improve by not only getting involved in the hands-on aspects of his extracurricular activities but also taking up leadership roles. This will help him improve his technical as well as soft skills, which are essential for his career development. Furthermore, he should consider attending seminars and workshops on sustainable energy solutions to acquire better insights for his project. Lastly, seeking guidance from his professors or a tutor for academics can help him maintain his desired GPA.

    Study plan for  Sara Kim
    1. Sara Kim is a fourth year psychology student who is mainly pursuing subjects such as Cognitive Psychology, Social Psychology, Statistics, and Research Methods. Sara has an auditory and reading/writing type of learning style. Her objectives are to complete a thesis on cognitive biases and to secure an internship in a clinical setting.

    2. One of Sara's extracurricular activities is the Psychology Student Association, which directly aligns with her field of study as it can provide her a platform to gain practical experience and valuable connections. Her participation in the Yoga Club, while not directly related to her study, can aid in managing stress and achieving a well-rounded college experience.

    3. Sara should ideally reserve 3-4 hours daily concentrating on her academic work. Time can be balanced across her subjects dedicating: 2 hours for Cognitive and Social Psychology and 1-2 hours for Statistics and Research Methods, depending on the extensive work involved in the course. However, she should spend additional hours when working on her thesis. Sara should allot at least 3-4 hours per week for her extracurricular activities.

    4. Sara can improve by taking advantage of her preferred learning styles and incorporating more audio books and written exercises into her study routine. She can also seek out opportunities within her club activities that can serve her career interests, such as pursuing leadership roles or organizing relevant events. Sara should also actively seek for internship opportunities in clinical settings. Lastly, maintaining a balanced lifestyle with adequate time for relaxation and other activities will be beneficial for Sara's overall achievements.



    Study plan for  David Martinez
    1. David Martinez is a first-year student studying Business Administration. His subjects this year include Principles of Management, Accounting, Economics, and Marketing. David identifies his preferred learning styles as reading/writing and visual. The challenges he wishes to work on during the course of his studies are developing a business plan for a startup and understanding the basics of the stock market. Outside of his academic pursuits, he attends Business Insights Seminars and plays for the college basketball team.

    2. His choice of extracurricular activities both complement his academic interests well. The Business Insights Seminar aligns directly with David's field of study, offering real-world context and knowledge expansion around various facets of the business industry. Participation in the basketball team also hones important skills such as teamwork, strategy, and leadership, all of which are vital in his field of study.

    3. To better balance between academics and extracurricular activities, David can allot around 30 hours a week for study, breaking down as 6 hours of study for each subject. This  will cater to in-depth understanding and revision. He could then devote approximately 6-8 hours in a week for the Business Insights Seminar and dedicated sports practice, ensuring he reaps the benefits of these activities without compromising on his academic pursuits.

    4. To enhance his academic performance, David could try to incorporate more practical application of his theoretical knowledge. This could be achieved by case study discussions, virtual stock trading for understanding stock market functionalities, or even small-scale startup simulations. Additionally, considering his learning styles, David should make use of visual aids like charts, diagrams, and even educational videos whenever possible, besides reading textbooks and writing summaries or notes.


    Study plan for  Lily Anderson
    1. Lily Anderson is a second-year Environmental Science major, focusing on subjects like Ecology, Environmental Policy, GIS, and Organic Chemistry. She prefers a mix of visual and hands-on learning methods. A major goal is for her to participate in a significant environmental restoration project and achieve proficiency in GIS.

    2. Yes, Lily's extracurricular activities align well with her field. Being part of the Environmental Club will expose her to practical aspects of environmental science and policy. On the other hand, Photography Club can support her visual learning style and can be useful in documenting environmental changes and restoration processes.

    3. Lily’s study plan should include 25-30 hours a week for academics encompassing all her subjects with a focus on GIS to achieve proficiency. An additional 6-8 hours a week should be devoted to her extracurricular activities, balancing both clubs. Be sure to allocate extra time for assignment completion and exam preparations.

    4. For improvement, Lily can seek real-world applications of her studies. By pursuing internships with environmental organizations or joining research projects, she can gain hands-on experience and improve her understanding. Also, enrolling in advanced GIS workshops or online courses can fast track her proficiency. Additionally, considering her visual learning preference, Lily might benefit from educational documentaries or virtual seminars related to her field.


    Study plan for  Omar Hassan
    1. Omar Hassan is a third-year Biochemistry student currently pursuing subjects like Organic Chemistry, Molecular Biology, Biochemical Techniques, and Genetics. He is also involved in extracurricular activities such as Science Club and student tutoring. Towards his major, he has set personal objectives to publish research in an undergraduate science journal and to secure a research position.

    2. Omar's extracurricular activities, especially the Science Club and his role as a student tutor, align with his field of study and would likely contribute to his knowledge base in Biochemistry.

    3. Omar is advised to follow a rigorous study routine, dedicating 25-30 hours a week towards academics considering the level of his course. This could consist of 8-10 hours each for Organic Chemistry and Molecular Biology, 4-6 hours for Genetics, and 4-6 hours for Biochemical Techniques. For his extracurricular activities, he can devote about 5-6 hours each week. An additional 3-4 hours can be reserved for independent research towards meeting his personal objectives.

    4. Omar can improve by involving himself more into practical aspects of his preferred learning style. Working more with laboratory experiments and real-world analogies could help. He should also seek out mentors who can offer advice on his independent research efforts. As a tutor, he should try to use that opportunity to strengthen his own concepts as well, by teaching others. Considering his goal to publish research, Omar should start to interact with his professors or staff who regularly publish and can provide guidance.

