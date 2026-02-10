using Microsoft.AspNetCore.Mvc;
using Assesment_6.Models;
using Assesment_6.ViewModels;

namespace Assesment_6.Controllers
{
    public class StudentController : Controller
    {
        static List<Student> students = new();
        static int id = 1;

        // READ
        public IActionResult Index()
        {
            return View(students);
        }

        // CREATE - GET
        public IActionResult Create()
        {
            return View();
        }

        // CREATE - POST
        [HttpPost]
        public IActionResult Create(StudentViewModel model)
        {
            if (ModelState.IsValid)
            {
                students.Add(new Student
                {
                    Id = id++,
                    Name = model.Name,
                    Email = model.Email,
                    Age = model.Age
                });
                return RedirectToAction("Index");
            }
            return View(model);
        }

        // EDIT - GET
        public IActionResult Edit(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            return View(student);
        }

        // EDIT - POST
        [HttpPost]
        public IActionResult Edit(Student student)
        {
            if (ModelState.IsValid)
            {
                var s = students.First(x => x.Id == student.Id);
                s.Name = student.Name;
                s.Email = student.Email;
                s.Age = student.Age;
                return RedirectToAction("Index");
            }
            return View(student);
        }

        // DELETE
        public IActionResult Delete(int id)
        {
            var student = students.First(x => x.Id == id);
            students.Remove(student);
            return RedirectToAction("Index");
        }
    }
}
