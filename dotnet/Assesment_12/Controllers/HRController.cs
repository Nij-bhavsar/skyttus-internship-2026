using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace Assesment_12.Controllers
{
    [Authorize(Policy = "HRDepartmentOnly")]
    [ApiController]
    [Route("api/[controller]")]
    public class HRController : ControllerBase
    {
        [HttpGet]
        public IActionResult Get()
        {
            return Ok("HR Department Access Granted");
        }
    }
}