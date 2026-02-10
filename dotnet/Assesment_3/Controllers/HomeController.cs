using Microsoft.AspNetCore.Mvc;

namespace Assesment_3.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
