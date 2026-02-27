using Microsoft.AspNetCore.Mvc;

namespace Assesment_14.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class HealthController : ControllerBase
    {
        [HttpGet("status")]
        public IActionResult GetStatus()
        {
            return Ok(new
            {
                Service = "Assesment_14 Background Job",
                Status = "Running",
                Time = DateTime.Now
            });
        }
    }
}