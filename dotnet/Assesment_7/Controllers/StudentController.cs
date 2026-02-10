using Microsoft.AspNetCore.Mvc;
using Assesment_7.Data;
using System.Linq;

namespace Assesment_7.Controllers
{
    public class StudentController : Controller
    {
        private readonly ApplicationDbContext _context;

        public StudentController(ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            var students = _context.Students.ToList();
            return View(students);
        }
    }
}
