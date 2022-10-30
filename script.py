from course_progress import CourseProgress

times = [
    ['23:12', '21:32', '09:24', '20:27', '08:13', '12:35'],
    ['29:41'],
    ['11:44','29:56','01:46'],
    ['05:26','09:06','02:38','10:38','04:28'],
    ['01:30','04:07','02:15','04:53'],
    ['07:29','07:48','08:55'],
    ['02:51','15:47','05:04']
]

my_course = CourseProgress(times)

section = 5
subsection = 4
print(my_course.get_completion_perc(section,subsection))