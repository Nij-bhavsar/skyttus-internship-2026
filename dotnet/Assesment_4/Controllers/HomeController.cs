using Assesment_4.Services;
using Microsoft.AspNetCore.Mvc;

namespace Assesment_4.Controllers
{
    public class HomeController : Controller
    {
        private readonly IConfiguration _configuration;
        private readonly IMyService _myService;
        private readonly ILogger<HomeController> _logger;

        public HomeController(
            IConfiguration configuration,
            IMyService myService,
            ILogger<HomeController> logger)
        {
            _configuration = configuration;
            _myService = myService;
            _logger = logger;
        }

        public IActionResult Index()
        {
            // Read configuration values
            string appName = _configuration["AppSettings:ApplicationName"];
            string version = _configuration["AppSettings:Version"];

            // Log message
            _logger.LogInformation("Home Index page accessed");

            ViewBag.AppName = appName;
            ViewBag.Version = version;
            ViewBag.ServiceMessage = _myService.GetMessage();

            return View();
        }
    }
}
