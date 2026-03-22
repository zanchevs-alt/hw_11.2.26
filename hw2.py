"""
שאלה 2 – גיבוי וניקוי רשימה
נתונה הרשימה:

grades = [85, 90, 78, 92, 88]
בצע את הפעולות הבאות:

1- צור עותק גיבוי של הרשימה
2- נקה את הרשימה המקורית
3- הדפס את שתי הרשימות כדי להוכיח שהעותק נשמר
4- חבר את הרשימה [100, 95] לרשימת הגיבוי בשתי דרכים שונות :

פעם אחת עם +
פעם אחת עם extend
יש להשתמש ב: copy, clear, extend
"""
grades = [85, 90, 78, 92, 88]
new_grades_list = grades.copy()
grades.clear()
print(new_grades_list)
print(grades)
_list = [85, 90, 78, 92, 88] + [95,100]
print(_list)
new_grades_list.extend([95,100])
print(new_grades_list)