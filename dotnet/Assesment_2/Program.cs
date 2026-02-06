using System;
using System.Collections.Generic;

class Student
{
    // 1. Private fields (Encapsulation)
    private int studentId;
    private string name;
    private string department;
    private int year;
    private int marks;

    // 2. Constructor to initialize values
    public Student(int studentId, string name, string department, int year, int marks)
    {
        this.studentId = studentId;
        this.name = name;
        this.department = department;
        this.year = year;
        this.marks = marks;
    }

    // 3. Getters and Setters
    public int StudentId
    {
        get { return studentId; }
        set { studentId = value; }
    }

    public string Name
    {
        get { return name; }
        set { name = value; }
    }
    public string Department
    {
        get { return department; }
        set { department = value; }
    }
    public int Year
    {
        get { return year; }
        set { year = value; }
    }
    public int Marks
    {
        get { return marks; }
        set { marks = value; }
    }

    // Method to display student details
    public void Display()
    {
        Console.WriteLine($"{studentId} {name} {department} {year} {marks}");
    }
}
class Program
{
    static void Main()
    {
        // 4. Create multiple student objects
        List<Student> students = new List<Student>();

        students.Add(new Student(1, "AB", "IT", 2, 82));
        students.Add(new Student(2, "NM", "CE", 4, 91));
        students.Add(new Student(3, "RP", "ECS", 1, 68));
        students.Add(new Student(4, "MS", "EC", 3, 88));
        students.Add(new Student(5, "HP", "CSE", 2, 76));

        // 5. Display all student records
        Console.WriteLine("All Student Records:");
        foreach (var s in students)
        {
            s.Display();
        }

        // 6. Find students with marks > 75
        Console.WriteLine("\nStudents with marks > 75:");
        foreach (var s in students)
        {
            if (s.Marks > 75)
            {
                s.Display();
            }
        }

        // 7. Sort students by marks (Descending)
        for (int i = 0; i < students.Count - 1; i++)
        {
            for (int j = i + 1; j < students.Count; j++)
            {
                if (students[i].Marks < students[j].Marks)
                {
                    var temp = students[i];
                    students[i] = students[j];
                    students[j] = temp;
                }
            }
        }
        Console.WriteLine("\nStudents Sorted by Marks:");
        foreach (var s in students)
        {
            s.Display();
        }

        // 8. Display top 3 scorers
        Console.WriteLine("\nTop 3 Scorers:");
        for (int i = 0; i < 3 && i < students.Count; i++)
        {
            students[i].Display();
        }
    }
}