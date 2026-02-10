using Assesment_8.Data;
using Assesment_8.Models;
using Assesment_8.Repositories.Interfaces;

namespace Assesment_8.Repositories.Implementations
{
    public class StudentRepository : IStudentRepository
    {
        private readonly ApplicationDbContext _context;

        public StudentRepository(ApplicationDbContext context)
        {
            _context = context;
        }

        public IEnumerable<Student> GetAll()
        {
            return _context.Students.ToList(); // LINQ
        }

        public Student GetById(int id)
        {
            return _context.Students.FirstOrDefault(s => s.Id == id); // LINQ
        }

        public void Add(Student student)
        {
            _context.Students.Add(student);
        }

        public void Update(Student student)
        {
            _context.Students.Update(student);
        }

        public void Delete(int id)
        {
            var student = _context.Students.Find(id);
            if (student != null)
                _context.Students.Remove(student);
        }

        public void Save()
        {
            _context.SaveChanges();
        }
    }
}
