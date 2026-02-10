using System;
using System.Collections.Generic;

class StudentDetails
{
    public int student_id;
    public string name;
    public string department;
    public int marks;
}

class Program
{
    static void Main()
    {
        List<StudentDetails> students = new List<StudentDetails>();
        // -------- ADD STUDENT DATA -------
        Console.Write("Enter number of students: ");
        int n = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < n; i++)
        {
            Console.WriteLine($"\nEnter details for Student {i + 1}");

            StudentDetails s = new StudentDetails();

            Console.Write("Student ID: ");
            s.student_id = Convert.ToInt32(Console.ReadLine());

            Console.Write("Name: ");
            s.name = Console.ReadLine();

            Console.Write("Department: ");
            s.department = Console.ReadLine();

            Console.Write("Marks: ");
            s.marks = Convert.ToInt32(Console.ReadLine());

            students.Add(s);
        }
        // ----->>>> MENU DRIVEN DISPLAY  <<<<<------
        int choice;
        do
        {
            Console.WriteLine("\n--->>>>> Student Menu <<<<<---");
            Console.WriteLine("1). Display all student records");
            Console.WriteLine("2). Display name and department");
            Console.WriteLine("3). Display students with marks > 75");
            Console.WriteLine("4). Display students from specific department");
            Console.WriteLine("5). Sort students by marks (Descending)");
            Console.WriteLine("6). Display top scorer");
            Console.WriteLine("0). Exit");

            Console.Write("Enter your choice: ");
            choice = Convert.ToInt32(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    Console.WriteLine("\nAll Student Records are shown below:");
                    foreach (var s in students)
                    {
                        Console.WriteLine($"{s.student_id} {s.name} {s.department} {s.marks}");
                    }
                    break;
                case 2:
                    Console.WriteLine("\nName and Department:");
                    foreach (var s in students)
                    {
                        Console.WriteLine($"{s.name} - {s.department}");
                    }
                    break;
                case 3:
                    Console.WriteLine("\nStudents with marks > 75:");
                    foreach (var s in students)
                    {
                        if (s.marks > 75)
                        {
                            Console.WriteLine($"{s.name} {s.marks}");
                        }
                    }
                    break;
                case 4:
                    Console.Write("\nEnter the department: ");
                    string dept = Console.ReadLine();

                    Console.WriteLine($"Students from {dept} department:");
                    foreach (var s in students)
                    {
                        if (s.department == dept)
                        {
                            Console.WriteLine($"{s.name} {s.marks}");
                        }
                    }
                    break;
                case 5:
                    Console.WriteLine("\nStudents sorted by their marks (Descending):");
                    for (int i = 0; i < students.Count - 1; i++)
                    {
                        for (int j = i + 1; j < students.Count; j++)
                        {
                            if (students[i].marks < students[j].marks)
                            {
                                var temp = students[i];
                                students[i] = students[j];
                                students[j] = temp;
                            }
                        }
                    }
                    foreach (var s in students)
                    {
                        Console.WriteLine($"{s.name} {s.marks}");
                    }
                    break;

                case 6:
                    StudentDetails topper = students[0];
                    foreach (var s in students)
                    {
                        if (s.marks > topper.marks)
                        {
                            topper = s;
                        }
                    }
                    Console.WriteLine("\nThe Top Scorer is:");
                    Console.WriteLine($"{topper.name} - {topper.marks}");
                    break;
                case 0:
                    Console.WriteLine("Exiting program...>>>>>");
                    break;
                default:
                    Console.WriteLine("Invalid choice!!!!");
                    break;
            }
        } while (choice != 0);
    }
}