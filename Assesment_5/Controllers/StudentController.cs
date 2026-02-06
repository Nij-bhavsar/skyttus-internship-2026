using Microsoft.AspNetCore.Mvc;
using MvcDemo.Models;

namespace MvcDemo.Controllers
{
    public class StudentController : Controller
    {
        public IActionResult Index()
        {
            var students = new List<Student>
            {
                new Student { Id = 1, Name = "Nij", Course = "ASP.NET Core", Field = "CSE"},
                new Student { Id = 2, Name = "Jil", Course = "Autocad", Field = "ME" },
                new Student { Id = 3, Name = "Jeet", Course = "Full Stack", Field = "CE" }
            };

            return View(students);
        }

        public IActionResult Details()
        {
            var student = new Student
            {
                Id = 1,
                Name = "Nij",
                Course = "ASP.NET Core MVC",
                Field = "CSE"
            };

            return View(student);
        }
    }
}
