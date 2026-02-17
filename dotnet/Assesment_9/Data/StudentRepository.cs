using Assesment_9.Models;

namespace Assesment_9.Data
{
    public class StudentRepository
    {
        private static List<Student> students = new List<Student>()
        {
            new Student { Id = 1, Name = "Nij", Course = "DotNet", Age = 21 },
            new Student { Id = 2, Name = "Jil", Course = "React", Age = 22 }
        };

        public List<Student> GetAll() => students;

        public Student GetById(int id)
        {
            return students.FirstOrDefault(x => x.Id == id);
        }

        public void Add(Student student)
        {
            students.Add(student);
        }

        public void Update(Student student)
        {
            var existing = GetById(student.Id);
            if (existing != null)
            {
                existing.Name = student.Name;
                existing.Course = student.Course;
                existing.Age = student.Age;
            }
        }

        public void Delete(int id)
        {
            var student = GetById(id);
            if (student != null)
                students.Remove(student);
        }
    }
}
